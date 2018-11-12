<template>
    <div id="opportunity" v-if="opportunity.title">
        <OpportunityCover :opportunity="opportunity"/>
        <b-container>
            <b-row>
                <b-col cols="12" md="3">
                    <OpportunityNav :opportunity="opportunity"
                                    :extra="extra"
                                    :tab="tab"
                                    @change-tab="changeTab"/>
                </b-col>
                <b-col cols="12" md="9">
                    <OpportunityDetails v-if="opportunity.title"
                                        :opportunity="opportunity"
                                        :extra="extra"
                                        :tab="tab"/>
                </b-col>
            </b-row>
        </b-container>
    </div>
    <div id="loading" v-else>
        <div id="fake-navbar"></div>
        <Loading fullscreen dark center/>
    </div>
</template>

<script>
	import OpportunityCover from '../components/Opportunity/OpportunityCover.vue';
	import OpportunityNav from '../components/Opportunity/OpportunityTabs.vue';
	import OpportunityDetails from '../components/Opportunity/OpportunityDetails.vue';
	import Loading from '../components/Loading.vue';
	import bContainer from 'bootstrap-vue/es/components/layout/container';
	import bCol from 'bootstrap-vue/es/components/layout/col';
	import bRow from 'bootstrap-vue/es/components/layout/row';
	import axios from 'axios';
	import {config} from '../config';
	import {gqlGetOpportunity} from '../functions/get-opportunity';

	export default {
		name:       "Opportunity",
		components: {
			OpportunityCover,
			OpportunityNav,
			OpportunityDetails,
			Loading,
			bCol,
			bRow,
			bContainer,
		},
		data()
		{
			return {
				opportunity:     {},
				extra:           {},
				tab:             'overview',
				subproductOrSdg: 'sdg',
			};
		},
		async created()
		{
			this.setTitle("Opportunity");

			// Do we have an Opp ID?
			if (isNaN(parseInt(this.$route.params.id)))
			{
				console.error('Invalid ID was specified');
				this.$root.$emit('fatal', "The opportunity link is invalid. Please check your link and try again.");
				return;
			}
			// Run a GQL query on the API
			let oppData;
			try
			{
				let requestURL = this.$session.get('loggedIn')
					? config.gisTokenAPI(this.$session.get('accessToken'))
					: config.gisPublicAPI;

				oppData = await axios.post(requestURL, {
					query:     gqlGetOpportunity,
					variables: {
						id:        parseInt(this.$route.params.id),
						cdn_links: true
					}
				});
			}
			catch (err)
			{
				if (err.response && err.response.status === 404)
				{
					this.$root.$emit('fatal', 'This opportunity does not exist.');
					return;
				}
				console.error(err);
				this.$root.$emit('error');
				return;
			}
			this.opportunity = oppData.data.data.getOpportunity;

			this.setTitle(this.opportunity.title.length > 23 ? this.opportunity.title.substr(0, 20) + "..." : this.opportunity.title);

			// Find out if we need to find more details about subproduct or SDG?
			let extraDataProj, extraDataLC;
			try
			{
				if (parseInt(this.opportunity.programme.id) === 1)
					extraDataProj = axios.get(config.api + config.endpoints.sdg(this.opportunity.sdg_info.sdg_target.goal_index));
				else
					extraDataProj = axios.get(config.api + config.endpoints.subproduct(this.opportunity.sub_product.id));

				extraDataLC = axios.get(config.api + config.endpoints.lc(this.opportunity.home_lc.id));
				[extraDataProj, extraDataLC] = await Promise.all([extraDataProj, extraDataLC]);
			}
			catch (err)
			{
				// Let's not kill the whole thing in case we add a new SDG/subproduct or something
				console.error(err);
				//this.$root.$emit('error');
				this.extra = {project: {name: "Unknown"}, lc: {id: 0, city: {id: 0, name: "Unknown"}}};
				return;
			}
			this.$set(this.extra, 'project', extraDataProj.data);
			this.$set(this.extra, 'lc', extraDataLC.data);
		},
		methods:    {
			changeTab(tab)
			{
				this.tab = tab;
			},
		}

	};
</script>

<style lang="scss" scoped>
    /*@import "../../node_modules/bootstrap/scss/functions";*/
    /*@import "../../node_modules/bootstrap/scss/variables";*/
    /*@import "../../node_modules/bootstrap/scss/mixins/breakpoints";*/
    @import "../assets/colors";

    #opportunity
    {
        font-family: PierSansLight, sans-serif;
    }

    #fake-navbar
    {
        background-color: $ib-blue-dk;
        height: 38px;
    }
</style>