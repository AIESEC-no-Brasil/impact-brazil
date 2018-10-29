<!--suppress XmlDuplicatedId -->
<template>
    <div id="opportunity-list-root">
        <OpportunityOptions v-if="!noVisa"
                            @options-changed="optionsChanged"/>
        <div v-if="iAmFromBrazil" id="no-opps-available">
            <i class="material-icons">location_on</i><br>
            Hello! This website is meant for internationals who are searching for opportunities in Brazil.<br>
            If you are a Brazilian and you want to find opportunities internationally, please visit <a
                href="https://aiesec.org.br">our national website</a>.
        </div>
        <div v-else-if="noVisa" id="no-opps-available">
            <i class="material-icons">location_off</i><br>
            Sorry, due to Visa regulations, we do not have any opportunities to show you right now.<br>
            Please
            <router-link to="/contact">get in touch</router-link>
            if you would like to know more.
        </div>
        <div v-else-if="oppList.length > 0 && !noOpps" id="opportunities-list">
            <OpportunityCard v-for="opp in oppList"
                             :ref="opp.id"
                             :opp="opp"
                             @show-video="showVideo"/>
        </div>
        <div v-else-if="noOpps" id="no-opps-available">
            <i class="material-icons">visibility_off</i><br>
            Sorry, we couldn't find any opportunities for you.<br>
            Try changing the filters on the top right so we can search again!
        </div>
        <div v-else id="opportunities-list">
            <Loading center dark/>
        </div>
    </div>
</template>

<script>
	import OpportunityOptions from './OpportunityOptions.vue';
	import OpportunityCard from './OpportunityCard.vue';
	import Loading from '../Loading';
	import axios from 'axios';
	import dateFormat from 'dateformat';
	import queryString from 'query-string';
	import {config} from '../../config';

	export default {
		name:       "OpportunityList",
		components: {
			OpportunityOptions,
			OpportunityCard,
			Loading,
		},
		props:      {
			noVisa:        Boolean,
			iAmFromBrazil: Boolean
		},
		data()
		{
			return {
				oppList: [],
				noOpps:  false,
				options: {}
			};
		},
		methods:    {
			showVideo(url)
			{
				this.$emit('show-video', url);
			},
			optionsChanged(options)
			{

			},
			async loadOpps()
			{
				// Configure the options
				let {entity, product} = this.$route.query;
				let options = {entity, product};

				if (this.$route.query.start_date && this.$route.query.end_date)
				{
					options.start_date = this.$route.query.start_date;
					options.end_date = this.$route.query.end_date;
				}
				else if (this.$route.query.month)
				{
					let thisDate = new Date();
					options.start_date = thisDate.getFullYear() + "-" + ("0" + this.$route.query.month).substr(-2) + "-01";
				}

				if (this.$route.query.sdg)
					options.sdg = this.$route.query.sdg;
				else if (this.$route.query.subproduct)
					options.subproduct = this.$route.query.subproduct;

				// Convert objects to proper datatype
				for (let k in options)
				{
					if (k.indexOf("date") > -1)
						options[k] = new Date(options[k]);
					else
						options[k] = parseInt(options[k]);
				}

				// Check if all required parameters are set
				if (!(options.entity && options.product)
					|| !(options.month || (options.start_date && options.end_date))
					|| !(options.sdg || options.subproduct)
					|| ((options.product === 5 || options.product === 2) && !options.subproduct)
					|| (options.product === 1 && !options.sdg))
				{
					console.error("All required parameters not set");
					this.$root.$emit('fatal');
					return false;
				}
				this.options = options;

				// Now that we're 100% sure, let's set this up
				let query = queryString.stringify(options);
				console.log(query);
				try
				{
					let opps = await axios.get(config.api + config.endpoints.opportunities + '?' + query);
				}
				catch (err)
				{
					console.log(err);
					this.$root.$emit('error');
					return;
				}

				// Do we have any opps fitting the criteria?
				if (opps.data.length === 0)
				{
					this.noOpps = true;
					return;
				}

				// "Prettify" the opps
				// Ensure we remove extra details like [Venture Brazil] from the title
				// Change all caps title to title case
				// Remove "at [company name]" from the end of titles;
				// Make the dates look nice
				opps.data.forEach((opp) => {
					opp.title = opp.title
					.replace(/^\[(.*)]( - )?/, '')
					.replace(` at ${opp.organization_name}`, '');

					opp.title =
						opp.title.toUpperCase() === opp.title ?
							opp.title
							.split(' ')
							.map(i => i[0].toUpperCase()
								+ i.substring(1).toLowerCase())
							.join(' ')
							: opp.title;

					opp.start_date = dateFormat(opp.start_date, "mmm d, yyyy");
				});
				this.oppList = opps.data;
			}
		},
		async mounted()
		{
			this.loadOpps();
		}
	};
</script>

<style scoped>
    #opportunities-list
    {
        margin-top: 24px;
    }

    #no-opps-available
    {
        text-align: center;
        margin-top: 36px;
    }

    .material-icons
    {
        font-size: 96px;
    }
</style>