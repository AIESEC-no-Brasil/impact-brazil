<template>
    <div v-if="ready" id="options-menu">
        <div id="options-left">
            Showing <b>{{subproductOrSdg}}</b> opportunities for <b>{{this.selections.products === "Choose product" ?
            "Brazil" : this.selections.products}}</b>
        </div>
        <div id="options-right">
            <span id="daterange">
                <DatePicker range
                            range-separator="-"
                            width="0"
                            lang="en"
                            ref="daterange"
                            @change="changeDate"/>
            </span>
            <b-dropdown id="month"
                        ref="month"
                        variant="transparent"
                        right
                        size="sm"
                        :text="selections.months">
                <b-dropdown-item @click="chooseDateRange">Select a date range</b-dropdown-item>
                <b-dropdown-item v-for="month in lists.months"
                                 @click="changeOption('month', month.id)">
                    {{month.text}}
                </b-dropdown-item>
            </b-dropdown>
            <b-dropdown id="prog"
                        variant="transparent"
                        right
                        size="sm"
                        :text="selections.products">
                <b-dropdown-item v-for="product in lists.products"
                                 @click="changeOption('product', product.id)">
                    {{product.text}}
                </b-dropdown-item>
            </b-dropdown>
            <b-dropdown id="sdg"
                        ref="sdg"
                        variant="transparent"
                        right
                        size="sm"
                        :text="selections.sdgs"
                        v-if="product===1">
                <b-dropdown-item v-for="sdg in lists.sdgs"
                                 @click="changeOption('sdg', sdg.id)">
                    {{sdg.text}}
                </b-dropdown-item>
            </b-dropdown>
            <b-dropdown id="subproductGT"
                        ref="subproductGT"
                        variant="transparent"
                        right
                        size="sm"
                        :text="selections.subproductsGT"
                        v-if="product===2">
                <b-dropdown-item v-for="subproduct in lists.subproductsGT"
                                 @click="changeOption('subproduct', subproduct.id)">
                    {{subproduct.text}}
                </b-dropdown-item>
            </b-dropdown>
            <b-dropdown id="subproductGE"
                        ref="subproductGE"
                        variant="transparent"
                        right
                        size="sm"
                        :text="selections.subproductsGE"
                        v-if="product===5">
                <b-dropdown-item v-for="subproduct in lists.subproductsGE"
                                 @click="changeOption('subproduct', subproduct.id)">
                    {{subproduct.text}}
                </b-dropdown-item>
            </b-dropdown>
        </div>
    </div>
    <div v-else id="loading">
        <Loading dark center small/>
    </div>
</template>

<script>
	import bDropdown from 'bootstrap-vue/es/components/dropdown/dropdown';
	import bDropdownItem from 'bootstrap-vue/es/components/dropdown/dropdown-item';
	import axios from 'axios';
	import {config} from '../../config';
	import {monthList} from '../../functions/month-list';
	import Loading from '../Loading';
	import DatePicker from 'vue2-datepicker';
	import dateFormat from 'dateformat';

	export default {
		name:       "OpportunityOptions",
		components: {
			bDropdown,
			bDropdownItem,
			Loading,
			DatePicker,
		},
		props:      {
			options: Object,
		},
		data()
		{
			return {
				lists:      {
					months:        [],
					products:      [],
					sdgs:          [],
					subproductsGT: [],
					subproductsGE: [],
				},
				selections: {
					months:        "Choose month",
					products:      "Choose product",
					sdgs:          "Choose project",
					subproductsGT: "Choose field",
					subproductsGE: "Choose field"
				},
				product:    0,
				customDate: false,
				ready:      false,
			};
		},
		computed:   {
			subproductOrSdg()
			{
				let retText = this.options.product === 1 ? this.selections.sdgs
					: this.options.product === 2 ? this.selections.subproductsGT
						: this.options.product === 5 ? this.selections.subproductsGE
							: "";

				return (retText === "Choose field" || retText === "Choose project") ? "" : retText;
			}
		},
		methods:    {
			async loadOptions()
			{
				async function loadData(vm, url, idKey, textKey)
				{
					let data;
					try
					{
						data = await axios.get(url);
					}
					catch (err)
					{
						console.error(err);
						vm.$root.$emit('error');
						return false;
					}
					let loadedData = [];

					for (let k in data.data)
					{
						if (data.data.hasOwnProperty(k))
						{
							loadedData.push({id: data.data[k][idKey], text: data.data[k][textKey]});

						}
					}

					return loadedData;
				}

				// First handle months
				let {months, month} = monthList();
				for (let i = 0; i < 12; i++)
					this.lists.months.push({id: ((i + month) % 12) + 1, text: months[i]});

				// Now handle dynamics
				let loadList = ["products", "sdgs", "subproductsGT", "subproductsGE"];

				let promiseArray = [];
				for (let i in loadList)
					promiseArray.push(loadData(this, config.api + config.endpoints[loadList[i]], 'gis_id', 'name'));

				let [products, sdgs, subproductsGT, subproductsGE] = await Promise.all(promiseArray);
				this.lists = {...this.lists, products, sdgs, subproductsGT, subproductsGE};
				this.ready = true;

				this.setSelections();
			},
			setSelections()
			{
				if (!this.ready) return;
				let selectionList = [
					{option: "product", list: "products"},
					{option: "subproduct", list: "subproductsGT"},
					{option: "subproduct", list: "subproductsGE"},
					{option: "sdg", list: "sdgs"}
				];

				selectionList.forEach((selection) => {
					if (this.options[selection.option])
					{
						let searchResult = this.lists[selection.list].find(x => x.id === this.options[selection.option]);

						if (searchResult !== undefined)
							this.selections[selection.list] = searchResult.text;
					}
				});

				// Special case for products
				if (this.product > 0)
					this.selections['products'] = this.lists['products'].find(x => x.id === this.product).text;

				// Special case for months - get it directly from the query string
				if (this.$route.query.month)
					this.selections['months'] = this.lists['months'].find(x => x.id === parseInt(this.$route.query.month)).text;
				else if (this.$route.query.start_date && this.$route.query.end_date)
					this.selections['months'] = `${this.$route.query.start_date} - ${this.$route.query.end_date}`;
				else
					this.selections['months'] = "Select month";
			},
			changeOption(opt, val)
			{
				// Did we change the product? Then we need to choose the SDG/subproduct
				if (opt === 'product')
				{
					this.product = val;
					this.setSelections();

					this.$nextTick(() => {
						switch (this.product)
						{
							case 1:
								this.$refs.sdg.show();
								break;

							case 2:
								this.$refs.subproductGT.show();
								break;

							case 5:
								this.$refs.subproductGE.show();
								break;
						}
					});

					return;
				}

				// Handle it
				let queryString = Object.assign({}, this.$route.query);
				queryString[opt] = `${val}`;
				queryString['product'] = `${this.product}`;

				// Remove unnecessary items
				if (this.product === 1)
					delete queryString['subproduct'];
				else if (this.product === 2 || this.product === 5)
					delete queryString['sdg'];

				// If we're chosing a month, no longer need to care about customRange
				if (opt === 'month')
				{
					this.customDate = false;

					delete queryString['start_date'];
					delete queryString['end_date'];
				}

				this.$router.push({path: 'opportunities', query: queryString});
				this.$emit('options-changed');
				this.$root.$emit('options-changed', queryString);
			},
			changeDate(evt)
			{
				let queryString = Object.assign({}, this.$route.query);
				delete queryString['month'];
				queryString['start_date'] = dateFormat(evt[0], "yyyy-mm-dd");
				queryString['end_date'] = dateFormat(evt[1], "yyyy-mm-dd");

				this.customDate = true;
				this.$router.push({path: 'opportunities', query: queryString});
				this.$emit('options-changed');
				this.$root.$emit('options-changed', queryString);
			},
			chooseDateRange()
			{
				this.customDate = true;
				this.selections.months = "Custom range";
				document.querySelector("[name=date]").click();
			}
		},
		watch:      {
			options(newOpts, oldOpts)
			{
				this.product = this.options.product;
				this.setSelections();
			}
		},
		async mounted()
		{
			this.loadOptions();
			if (this.$route.query.entity || this.$route.query.product)
				this.$root.$emit('options-changed', this.$route.query);
		}
	};
</script>

<style lang="scss" scoped>
    #options-left
    {
        float: left;
    }

    #options-right
    {
        float: right;
    }

    #options-right /deep/
    {
        button
        {
            margin-left: 8px;
            margin-bottom: 2px;
        }
    }

    #options-menu:after
    {
        content: "";
        clear: both;
        display: block;
    }

    #daterange /deep/
    {
        input
        {
            display: none;
        }
    }
</style>