<template>
    <div class="cityinfo" v-if="cityId === 0">
        <!--<div class="title">Cities</div>-->
        <div class="citydesc">Click on a city to get started.</div>
        <CityList @city-clicked="id => $emit('city-clicked', id)"
                  @city-hovered="id => $emit('city-hovered', id)"
                  @city-unhovered="$emit('city-unhovered')"
                  :regions="cities"/>
    </div>
    <div class="cityinfo" v-else-if="cityLoaded">
        <div class="title">
            <a href="#" @click="$emit('city-cleared')">
                <i class="material-icons"
                   style="font-size: 48px; vertical-align: middle; position: relative; top: -4px"
                   v-if="cities">arrow_back</i>
            </a>
            <span v-if="isLC">About {{lc.reference_name}}, {{city.name}}</span>
            <span v-else>About {{city.name}}</span>
        </div>
        <div class="video" v-if="city.video_link">
            <iframe frameborder="0"
                    allow="encrypted-media"
                    allowfullscreen
                    ref="youtube"
                    id="youtube"
                    :src="youtubeURL(city.video_link)">
            </iframe>
        </div>
        <div class="citydesc">{{city.short_desc}}</div>
        <div class="details" v-if="city.lc_set.length > 1 && !isLC">
            <b>AIESEC Offices in {{city.name}}</b><br>
            <div v-for="lc in city.lc_set" :key="lc.gis_id">
                <a v-if="lc.unaccented_name" :href="`/${lc.unaccented_name}`">{{lc.reference_name}}</a>
                <router-link v-else :to="`/opportunities?lc=${lc.gis_id}`">
                    {{lc.reference_name}}
                </router-link>
            </div>
        </div>
        <div class="details" v-else>
            The AIESEC Office in {{city.name}} is
            <strong v-if="!isLC">{{city.lc_set[0].reference_name}}</strong><strong v-else>{{cityRefName}}</strong>.
        </div>
        <div v-if="(city.lc_set.length === 1 || isLC) && showDetails">
            <div class="details" v-if="this.lc.reference_name">
                <b>Products running in {{cityRefName}}</b>
                <CityProjects :lc="lc"/>
            </div>
            <Loading small dark center v-else/>
        </div>

        <router-link class="orange-button"
                     :to='`/${city.name_unaccented.toLowerCase().replace(/\s/g, "-")}`'
                     v-if="!showDetails">
            Learn More about {{city.name}} &raquo;
        </router-link>

        <div class="details" v-if="city.details && showDetails">
            <b>More about {{city.name}}</b><br>
            <span v-html="markdown(city.details)"></span>

            <div v-if="city.lc_set.length <= 1 || isLC">
                <router-link class="orange-button"
                             :to="isLC ? `/opportunities?lc=${this.lc.id}` : `/opportunities?lc=${city.lc_set[0].gis_id}`"
                             @click.native="$store.commit('queueOptReload')">
                    Apply for Opportunities in {{cityRefName}} &raquo;
                </router-link>
            </div>
            <div v-else>
                <b>Apply for Opportunities in...</b><br>
                <div v-for="lc in city.lc_set" :key="lc.gis_id">
                    <router-link :to="`/opportunities?lc=${lc.gis_id}`"
                                 @click.native="$store.commit('queueOptReload')">
                        {{lc.reference_name}}
                    </router-link>
                </div>
            </div>
        </div>
    </div>
    <Loading :fullscreen="showDetails" dark center v-else/>
</template>

<script>
	import CityProjects from './CityProjects.vue';
	import CityList from './CityList.vue';

	import axios from 'axios';
	import {config} from '../../config';
	import Loading from '../Loading.vue';
	import MarkdownIt from 'markdown-it';

	export default {
		name:       "CityInfo",
		props:      {
			cityId:      Number,
			cities:      Array,
			showDetails: Boolean,
			changeTitle: Boolean,
			cityName:    String,
		},
		data()
		{
			return {
				city:        {},
				lc:          {},
				cityRefName: "",
				isLC:        false,
				cityLoaded:  false,
			};
		},
		components: {
			CityProjects,
			CityList,
			Loading,
		},
		methods:    {
			async loadCity()
			{
				this.cityLoaded = false;

				let cityData, cityName, lcData;

				let loadCityById = async id => {
					let cityData;
					try
					{
						cityData = await axios.get(config.api + config.endpoints.city(id));
					}
					catch (err)
					{
						if (err.response && err.response.status === 404)
						{
							this.$root.$emit('fatal', 'This city does not exist.');
							return false;
						}

						console.error(err);
						this.$root.$emit('error');
						return false;
					}
					return cityData;
				};
				// First get city data
				// By ID
				if (!this.cityName)
				{
					cityData = await loadCityById(this.cityId);
                    this.cityRefName = cityData.data.name;
				}
				// By Name
				else
				{
					cityName = this.cityName.toLowerCase();
					try
					{
						cityData = await axios.get(config.api + config.endpoints.city(cityName));
						this.cityRefName = cityData.data.name;
					}
					catch (err)
					{
						// If the name was not found, maybe they're referring to the LC name (eg. USP)
						if (err.response && err.response.status === 404)
						{
							try
							{
								lcData = await axios.get(config.api + config.endpoints.lcByName(cityName));
							}
							catch (err)
							{
								if (err.response && err.response.status === 404)
								{
									// They've probably come here from typing ib.org/something, so give them a 404 page
									this.$router.push("/404");
									return false;
								}

								console.error(err);
								this.$root.$emit('error');
								return false;
							}
							this.isLC = true;
							this.lc = lcData.data;

							this.cityRefName = this.lc.reference_name;
							cityData = await loadCityById(this.lc.city.id);
						}
					}
				}
				this.city = cityData.data;

				if (this.changeTitle)
					this.setTitle(this.city.name);

				this.cityLoaded = true;

				// Now we have to get LC Data so we know eg. what products it runs
				// We only do this if there's =1 LC, lazy solution for now but only SP runs >1 LC
				// so for now it's okay, maybe in the future we'll have to react this
				if (this.city.lc_set.length === 1 && !this.isLC)
				{
					try
					{
						let lcID = parseInt(this.city.lc_set[0].gis_id);
						lcData = await axios.get(config.api + config.endpoints.lc(lcID));
					}
					catch (err)
					{
						console.error(err);
						this.$root.$emit('error');
						return false;
					}
					this.lc = lcData.data;
				}
			},
			markdown(text)
			{
				let md = new MarkdownIt();
				return md.render(text);
			},
			youtubeURL(url)
			{
				return config.youtubeURL(url);
			},
		},
		created()
		{
			if (this.cityId || this.cityName)
				this.loadCity();
		},
		watch:      {
			cityId(val)
			{
				if (val > 0)
					this.loadCity();
			}
		}
	};
</script>

<style lang="scss" scoped>
    @import "../../../node_modules/bootstrap/scss/functions";
    @import "../../../node_modules/bootstrap/scss/variables";
    @import "../../../node_modules/bootstrap/scss/mixins/breakpoints";
    @import "../../assets/colors";

    .title
    {
        font-size: 36px;
        font-family: PierSans, sans-serif;
        @include media-breakpoint-down(sm)
        {
            font-size: 24px;

            i
            {
                display: block;
            }
        }
    }

    .cityinfo
    {
        text-align: justify;
    }

    .details
    {
        margin-top: 20px;
        margin-bottom: 20px;
    }

    .details b
    {
        font-size: 20px;
    }

    .video
    {
        position: relative;
        width: 100%;
        height: 0;
        padding-bottom: 56%; /* The height of the item will now be 56% of the width. */
        margin-bottom: 16px;
    }

    /* Adjust the iframe so it's rendered in the outer-width and outer-height of it's parent */
    .video iframe
    {
        position: absolute;
        width: 100%;
        height: 100%;
        left: 0;
        top: 0;
    }
</style>