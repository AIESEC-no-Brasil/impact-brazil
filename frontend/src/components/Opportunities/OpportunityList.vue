<!--suppress XmlDuplicatedId -->
<template>
    <div id="opportunity-list-root">
        <OpportunityOptions v-if="!$store.state.noVisa"
                            @options-changed="optionsChanged"/>

        <div v-if="missingOpts && !iAmFromBrazil && !$store.state.noVisa" id="no-opps-available">
            <i class="material-icons">settings</i><br>
            To get started, please select a product or a city from the top right.<br class="nobreak">
            You can keep customizing the filters to suit your needs better.<br class="doublebreak">
            Not sure what product is best for you?
            <router-link to="/about">Read more about our products</router-link>
        </div>

        <div v-else-if="iAmFromBrazil" id="no-opps-available">
            <i class="material-icons">location_on</i><br>
            Hello! This website is meant for internationals who are searching for opportunities in Brazil.<br
                class="nobreak">
            If you are a Brazilian and you want to find opportunities internationally, please visit <a
                href="https://aiesec.org.br">our national website</a>.
        </div>

        <div v-else-if="$store.state.noVisa" id="no-opps-available">
            <i class="material-icons">location_off</i><br>
            Sorry, due to Visa regulations, we do not have any opportunities to show you right now.<br class="nobreak">
            Please
            <router-link to="/contact">get in touch</router-link>
            if you would like to know more.
        </div>

        <div v-else-if="oppList.length > 0 && !noOpps" id="opportunities-list">
            <OpportunityCard v-for="opp in oppList"
                             :ref="opp.id"
                             :opp="opp"
                             :key="opp.id"
                             @show-video="showVideo"/>
        </div>
        <div v-else-if="noOpps" id="no-opps-available">
            <i class="material-icons">visibility_off</i><br>
            Sorry, we couldn't find any opportunities for you.<br class="nobreak">
            Try changing the filters on the top right so we can search again!
        </div>
        <div v-else id="oplist-loading">
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
		data()
		{
			return {
				oppList:     [],
				noOpps:      false,
				missingOpts: false,
			};
		},
		computed:   {
			iAmFromBrazil()
			{
				return this.$session.get('entity') === config.gisBrazilID;
			}
		},
		methods:    {
			showVideo(url)
			{
				this.$emit('show-video', url);
			},
			optionsChanged()
			{
				this.oppList = [];
				this.noOpps = false;
				this.loadOpps();
			},
			async loadOpps()
			{
				// Reset
				this.missingOpts = false;

				// Configure the options
				let options = {};
				if (this.$route.query.product)
					options.product = this.$route.query.product;

				if (this.$route.query.start_date && this.$route.query.end_date)
				{
					options.start_date = this.$route.query.start_date;
					options.end_date = this.$route.query.end_date;
				}
				else if (this.$route.query.month)
				{
					let startDate = new Date(
						new Date().getFullYear()
						+ (parseInt(this.$route.query.month) < ((new Date()).getMonth() + 1) ? 1 : 0),
						parseInt(this.$route.query.month) - 1,
						1);
					options.start_date = dateFormat(startDate, 'yyyy-mm-dd');

					let endDate = startDate;
					endDate.setMonth(startDate.getMonth() + config.defaultMonthOffset);
					options.end_date = dateFormat(endDate, 'yyyy-mm-dd');
				}

				if (this.$route.query.sdg)
					options.sdg = this.$route.query.sdg;
				else if (this.$route.query.subproduct)
					options.subproduct = this.$route.query.subproduct;

				if (this.$route.query.lc)
					options.lc = this.$route.query.lc;

				if (this.$route.query.q)
					options.q = this.$route.query.q;

				// Convert objects to proper datatype
				for (let k in options)
				{
					if (k.indexOf("date") === -1 && k !== "q")
						options[k] = parseInt(options[k]);
				}
				// Remove all NaNs
				for (let k in options)
				{
					if (isNaN(options[k]))
						delete options[k];
				}
				this.$store.commit('options', options);

				// Check if all required parameters are set
				if (!options.product && !options.lc)
				{
					//console.error("All required parameters not set");
					this.missingOpts = true;
					return false;
				}

				// Now that we're 100% sure, let's set this up
				let query = queryString.stringify(options);

				let opps;
				try
				{
					opps = await axios.get(config.api + config.endpoints.opportunities + '?' + query);
				}
				catch (err)
				{
					console.error(err);
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
					.trim()
					.replace(/^\[(.*)]( - )?/, '')
					.replace(` at ${opp.organization_name}`, '')
					.replace(` in ${opp.lc.reference_name}`, '')
					.replace(' in Brazil', '');

					opp.title =
						opp.title.toUpperCase() === opp.title ?
							opp.title
							.split(' ')
							.map(i => i !== "" ? (i[0].toUpperCase()
								+ i.substring(1).toLowerCase()) : "")
							.join(' ')
							: opp.title;

					opp.start_date = dateFormat(opp.start_date, "mmm d, yyyy");
				});
				this.oppList = opps.data;

				// Store the querystring too
				this.$store.commit('optquery', this.$route.query);

				// We don't need to reload any more
				this.$store.commit('listLoaded');
			}
		},
		async created()
		{
			this.loadOpps();
		},
		async activated()
		{
			if (this.$store.state.optReloadQueued.list)
			{
				this.oppList = [];
				this.noOpps = false;
				this.loadOpps();
			}
		}
	};
</script>

<style scoped>
    #opportunities-list
    {
        margin-top: 24px;
    }

    #oplist-loading
    {
        margin-top: 24px;
        margin-bottom: 60vh;
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

    @media only screen and (max-width: 767.98px)
    {
        br.nobreak
        {
            display: none;
        }

        br.doublebreak
        {
            line-height: 40px;
        }
    }
</style>