<template>
    <div id="opportunity" v-if="opportunity.title">
        <OpportunityCover :opportunity="opportunity"/>
        <b-container>
            <b-row>
                <b-col cols="12" md="3">
                    <OpportunityNav :opportunity="opportunity"
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
        <Loading dark center></Loading>
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
		async mounted()
		{
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
				oppData = await axios.post(config.gisPublicAPI, {
					query:     gqlGetOpportunity,
					variables: {
						id:        parseInt(this.$route.params.id),
						cdn_links: true
					}
				});
			}
			catch (err)
			{
				if (err.response.status === 404)
				{
					this.$root.$emit('fatal', 'This opportunity does not exist.');
					return;
				}
				console.error(err);
				this.$root.$emit('error');
				return;
			}
			this.opportunity = oppData.data.data.getOpportunity;

			// Find out if we need to find more details about subproduct or SDG?
			let extraData;
			try
			{
				if (parseInt(this.opportunity.programme.id) === 1)
					extraData = await axios.get(config.api + config.endpoints.sdg(this.opportunity.sdg_info.sdg_target.goal_index));
				else
					extraData = await axios.get(config.api + config.endpoints.subproduct(this.opportunity.sub_product.id));

			}
			catch (err)
			{
				// Let's not kill the whole thing in case we add a new SDG/subproduct or something
				console.error(err);
				//this.$root.$emit('error');
				this.extra = {name: "Unknown"};
				return;
			}
			this.extra = extraData.data;
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