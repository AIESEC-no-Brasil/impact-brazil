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
                                        :project="project"
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
	import {dataLoad} from '../functions/data-loader';
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
				project:         {},
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
				if (this.$session.get('loggedIn'))
				{
					let requestURL = config.gisTokenAPI(this.$session.get('accessToken'));

					oppData = await axios.post(requestURL, {
						query:     gqlGetOpportunity,
						variables: {
							id:        parseInt(this.$route.params.id),
							cdn_links: true
						}
					});
					this.opportunity = oppData.data.data.getOpportunity;
				}
				else
				{
					oppData = await axios.get(config.api + config.endpoints.opportunity(this.$route.params.id));
					this.opportunity = oppData.data;
				}
				// Now we run the cache update function, which will basically check if the opportunity was updated
				// on GIS and update the cache on the server. We do it this way because getting data from GIS is slow,
				// (usually) compared to IB. But GIS stopped providing updated_at, and we don't want to clear the
				// cache unless absolutely necessary.
				if (this.opportunity.from_cache)
				{
					// Run this asynchronously, otherwise our project and city requests get blocked
					axios.get(config.api + config.endpoints.oppCacheUpdate(this.$route.params.id)).then((oppData) => {
						if (oppData.data.cache_status === "CACHE_UPDATED")
							this.opportunity = oppData.data;
					});
					// We don't care if there's an error, means GIS is down or something, that's where the cache saves us
				}
			}
			catch (err)
			{
				if (err.response)
				{
					if (err.response.status === 404)
					{
						this.$root.$emit('fatal', 'This opportunity does not exist.');
						return;
					}
					else if (err.response.status === 401 && this.$session.get('loggedIn'))
					{
						this.$root.$emit('logout');
						return;
					}
				}
				console.error(err);
				this.$root.$emit('error');
				return;
			}
			//this.opportunity = oppData.data.data.getOpportunity;
			//this.opportunity = oppData.data;

			this.setTitle(this.opportunity.title.length > 23 ? this.opportunity.title.substr(0, 20) + "..." : this.opportunity.title);

			// Find out if we need to find more details about subproduct or SDG?
			let extraDataField, extraDataLC;
			try
			{
				if (parseInt(this.opportunity.programme.id) === 1)
					extraDataField = axios.get(config.api + config.endpoints.sdg(this.opportunity.sdg_info.sdg_target.goal_index));
				else
					extraDataField = axios.get(config.api + config.endpoints.subproduct(this.opportunity.sub_product.id));

				extraDataLC = axios.get(config.api + config.endpoints.lc(this.opportunity.home_lc.id));
				[extraDataField, extraDataLC] = await Promise.all([extraDataField, extraDataLC]);
			}
			catch (err)
			{
				// Let's not kill the whole thing in case we add a new SDG/subproduct or something
				console.error(err);
				//this.$root.$emit('error');
				this.extra = {project: {name: "Unknown"}, lc: {id: 0, city: {id: 0, name: "Unknown"}}};
				return;
			}
			this.$set(this.extra, 'field', extraDataField.data);
			this.$set(this.extra, 'lc', extraDataLC.data);

			// We also need to figure out the project
			let loadOut = await dataLoad(this, ["projects"]);
			let projectList = loadOut['projects'];

			// Try to match the "project" title
			//let projectMatch = this.opportunity.title.match(/\[(.*)]/);
			//if (projectMatch !== null)
			//{
			//	projectMatch = projectMatch[0];
			//
			//	let project = projectList.find(project => project.name.localeCompare(projectMatch, 'en', {sensitivity: 'base'}));
			//
			//	if (project !== undefined)
			//		this.project = project;
			//	else
			//		this.project = {name: "Unknown", description: ""};
			//}
			//else
			//	this.project = {name: "Unknown", description: ""};

			// The above method is too "advanced", we are smarter than following the national format:
			// we search for the project name ANYWHERE in the title.
			let project = projectList.find(project => this.opportunity.title.toLowerCase().indexOf(project.name.toLowerCase()) > -1);

			if (project !== undefined)
				this.project = project;
			else
				this.project = {name: "Unknown", description: ""};
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