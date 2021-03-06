<template>
    <div v-if="ready" id="options-menu">
        <div id="options">
            Filters:
            <div id="searchbox">
                <b-form-input size="sm"
                              placeholder="Search"
                              v-model="search"/>
            </div>
            <b-dropdown id="prog"
                        variant="transparent"

                        size="sm"
                        :text="selections.products">
                <b-dropdown-item @click="removeOption('product', 'All products')">All products</b-dropdown-item>
                <b-dropdown-item v-for="product in lists.products"
                                 :key="product.id"
                                 @click="changeOption('product', product.id)">
                    {{product.text}}
                </b-dropdown-item>
            </b-dropdown>
            <b-dropdown id="sdg"
                        ref="sdg"
                        variant="transparent"

                        size="sm"
                        :text="selections.sdgs"
                        v-if="$store.state.options.product===1">
                <b-dropdown-item @click="removeOption('sdg', 'All projects')">All projects</b-dropdown-item>
                <b-dropdown-item v-for="sdg in lists.sdgs"
                                 :key="sdg.id"
                                 @click="changeOption('sdg', sdg.id)">
                    {{sdg.text}}
                </b-dropdown-item>
            </b-dropdown>
            <b-dropdown id="subproductGT"
                        ref="subproductGT"
                        variant="transparent"

                        size="sm"
                        :text="selections.subproductsGT"
                        v-if="$store.state.options.product===2">
                <b-dropdown-item @click="removeOption('subproduct', 'All fields')">All fields</b-dropdown-item>
                <b-dropdown-item v-for="subproduct in lists.subproductsGT"
                                 :key="subproduct.id"
                                 @click="changeOption('subproduct', subproduct.id)">
                    {{subproduct.text}}
                </b-dropdown-item>
            </b-dropdown>
            <b-dropdown id="subproductGE"
                        ref="subproductGE"
                        variant="transparent"

                        size="sm"
                        :text="selections.subproductsGE"
                        v-if="$store.state.options.product===5">
                <b-dropdown-item @click="removeOption('subproduct', 'All fields')">All fields</b-dropdown-item>
                <b-dropdown-item v-for="subproduct in lists.subproductsGE"
                                 :key="subproduct.id"
                                 @click="changeOption('subproduct', subproduct.id)">
                    {{subproduct.text}}
                </b-dropdown-item>
            </b-dropdown>
            <span id="daterange" v-show="datepickerActive">
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

                        size="sm"
                        :text="selections.months">
                <b-dropdown-item @click="removeOption('month', 'Anytime')">Anytime</b-dropdown-item>
                <b-dropdown-item @click="chooseDateRange">Select a date range</b-dropdown-item>
                <b-dropdown-item v-for="month in lists.months"
                                 :key="month.id"
                                 @click="changeOption('month', month.id)">
                    {{month.text}}
                </b-dropdown-item>
            </b-dropdown>
            <b-dropdown id="lc"
                        ref="lc"
                        variant="transparent"

                        size="sm"
                        :text="selections.lcs">
                <b-dropdown-item @click="removeOption('lc', 'All offices')">All offices</b-dropdown-item>
                <b-dropdown-item v-for="lc in lists.lcs"
                                 :key="lc.id"
                                 @click="changeOption('lc', lc.id)">
                    {{lc.text}}
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
	import bFormInput from 'bootstrap-vue/es/components/form-input/form-input';

	import {monthList} from '../../functions/month-list';
	import {dataLoad} from '../../functions/data-loader';
	import Loading from '../Loading';
	import DatePicker from 'vue2-datepicker';
	import dateFormat from 'dateformat';

	export default {
		name:       "OpportunityOptions",
		props:      {
			reloading: Boolean
		},
		components: {
			bDropdown,
			bDropdownItem,
			bFormInput,
			Loading,
			DatePicker,
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
					lcs:           [],
				},
				selections: {
					months:        "Anytime",
					products:      "All products",
					sdgs:          "All projects",
					subproductsGT: "All fields",
					subproductsGE: "All fields",
					lcs:           "All offices",
				},
				search:     "",

				customDate:       false,
				ready:            false,
				datepickerActive: false,
				selectionList:    [
					{option: "month", list: "months", default: "Anytime"},
					{option: "product", list: "products", default: "All products"},
					{option: "subproduct", list: "subproductsGT", default: "All fields"},
					{option: "subproduct", list: "subproductsGE", default: "All fields"},
					{option: "sdg", list: "sdgs", default: "All projects"},
					{option: "lc", list: "lcs", default: "All offices"},
				],
				searchTimer:      null,
			};
		},
		computed:   {
			options()
			{
				return this.$store.state.options;
			},
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
				let listsArray = ["products", "sdgs", "subproductsGT", "subproductsGE", "lcs"];
				let loadOut = await dataLoad(this, listsArray);

				// Convert our "un-vetted" data to vetted data
				let getDataFromList = (data, idKey, textKey) => {
					let loadedData = [];

					for (let k in data)
						if (data.hasOwnProperty(k))
							loadedData.push({id: data[k][idKey], text: data[k][textKey]});

					return loadedData;
				};

				// First handle months
				let {months, month} = monthList();
				for (let i = 0; i < 12; i++)
					this.lists.months.push({id: ((i + month) % 12) + 1, text: months[i]});

				// Now handle dynamics
				for (let i in listsArray)
					this.lists[listsArray[i]] = getDataFromList(loadOut[listsArray[i]], 'gis_id', (listsArray[i] === 'lcs' ? 'reference_name' : 'name'));

				this.ready = true;
				this.setSelections();
			},
			setSelections()
			{
				if (!this.ready) return;
				let selectionList = this.selectionList;

				selectionList.forEach((selection) => {
					if (this.options[selection.option])
					{
						let searchResult = this.lists[selection.list].find(x => x.id === this.options[selection.option]);

						if (searchResult !== undefined)
							this.selections[selection.list] = searchResult.text;
						else
							this.selections[selection.list] = selection.default;
					}
					else
						this.selections[selection.list] = selection.default;
				});

				// Fix product
				switch (this.options.product)
				{
					case 1:
						this.selections.subproductsGT = "All fields";
						this.selections.subproductsGE = "All fields";
						break;

					case 2:
						this.selections.sdgs = "All projects";
						this.selections.subproductsGE = "All fields";
						break;

					case 5:
						this.selections.subproductsGT = "All fields";
						this.selections.sdgs = "All fields";
						break;

					default:
						this.selections.sdgs = "All projects";
						this.selections.subproductsGT = "All fields";
						this.selections.sdgs = "All fields";
						break;
				}

				// Special case for months - get it directly from the query string
				if (this.$route.query.month)
					this.selections['months'] = this.lists['months'].find(x => x.id === parseInt(this.$route.query.month)).text;
				else if (this.$route.query.start_date && this.$route.query.end_date)
					this.selections['months'] = `${this.$route.query.start_date} - ${this.$route.query.end_date}`;
				else
					this.selections['months'] = "Anytime";
			},
			changeOption(opt, val)
			{
				let queryString = Object.assign({}, this.$route.query);
				queryString[opt] = `${val}`;

				// Remove unnecessary items
				if (queryString.product && parseInt(queryString.product) === 1)
					delete queryString['subproduct'];
				else if (queryString.product && (parseInt(queryString.product) === 2 || parseInt(queryString.product) === 5))
					delete queryString['sdg'];

				// If we're chosing a month, no longer need to care about customRange
				if (opt === 'month')
				{
					this.customDate = false;

					delete queryString['start_date'];
					delete queryString['end_date'];
				}

				this.$router.push({path: '/opportunities', query: queryString});
				this.$store.commit('optquery', queryString);
				this.$emit('options-changed');

				// Track on Google
				this.$ga.event('Filters', 'filter_set', JSON.stringify(queryString), this.id);
			},
			removeOption(opt, text)
			{
				let selectionList = this.selectionList, currentSelection;
				try
				{
					currentSelection = selectionList.find(x => x.option === opt).list;
				}
				catch (err)
				{
					return;
				}
				let queryString = Object.assign({}, this.$route.query);
				delete queryString[opt];

				if (opt === 'month')
				{
					delete queryString['start_date'];
					delete queryString['end_date'];
				}
				if (opt === 'product')
				{
					delete queryString['sdg'];
					delete queryString['subproduct'];
				}
				this.selections[currentSelection] = text;

				this.$router.push({path: '/opportunities', query: queryString});
				this.$store.commit('optquery', queryString);
				this.$emit('options-changed');
			},
			searchHandler()
			{
				clearTimeout(this.searchTimer);
				this.searchTimer = setTimeout(this.changeSearch, 750);
			},
			changeSearch()
			{
				let queryString = Object.assign({}, this.$route.query);
				if (this.search.length > 0)
					queryString.q = this.search;
				else
					delete queryString.q;

				this.$router.push({path: '/opportunities', query: queryString});
				this.$store.commit('optquery', queryString);
				this.$emit('options-changed');
			},
			changeDate(evt)
			{
				let queryString = Object.assign({}, this.$route.query);
				delete queryString['month'];
				queryString['start_date'] = dateFormat(evt[0], "yyyy-mm-dd");
				queryString['end_date'] = dateFormat(evt[1], "yyyy-mm-dd");

				this.customDate = true;
				this.$router.push({path: '/opportunities', query: queryString});
				this.$emit('options-changed');
				this.$store.commit('optquery', queryString);
			},
			chooseDateRange()
			{
				this.customDate = true;
				this.datepickerActive = true;
				this.selections.months = "Custom range";
				document.querySelector("[name=date]").click();
			}
		},
		watch:      {
			options()
			{
				this.setSelections();
			},
			reloading(val)
			{
				if (val)
					this.setSelections();
			},
			search()
			{
				this.searchHandler();
			}
		},
		async created()
		{
			this.loadOptions();
			if (this.$route.query.product)
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

    #options
    {
        text-align: center;
    }

    #options /deep/
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

    #searchbox
    {
        display: inline-block;
        width: 120px;
        position: relative;
        top: 1px;
    }
</style>