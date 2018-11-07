<template>
    <div class="cityinfo" v-if="cityId === 0">
        <div class="title">About this City</div>
        <div class="citydesc">Click on a city to get started.</div>
    </div>
    <div class="cityinfo" v-else-if="cityLoaded">
        <div class="title">About {{city.name}}</div>
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
        <!-- TODO: show the list of LCs here -->
        <div class="details" v-if="city.details">
            <b>More about {{city.name}}</b><br>
            <span v-html="markdown(city.details)"></span>
        </div>
    </div>
    <Loading dark center v-else/>
</template>

<script>
	import axios from 'axios';
	import {config} from '../../config';
	import Loading from '../Loading.vue';
	import MarkdownIt from 'markdown-it';

	export default {
		name:       "CityInfo",
		props:      {
			cityId: Number,
			cities: Array
		},
		data()
		{
			return {
				city:       {},
				cityLoaded: false,
			};
		},
		components: {
			Loading,
		},
		methods:    {
			async loadCity()
			{
				this.cityLoaded = false;

				let cityData;
				try
				{
					cityData = await axios.get(config.api + config.endpoints.city(this.cityId));
				}
				catch (err)
				{
					console.error(err);
					this.$root.$emit('error');
					return false;
				}
				this.city = cityData.data;
				this.cityLoaded = true;
			},
			markdown(text)
			{
				let md = new MarkdownIt();
				return md.render(text);
			},
			youtubeURL(url)
			{
				return config.youtubeURL(url);
			}
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

<style scoped>
    .title
    {
        font-size: 36px;
        font-family: PierSans, sans-serif;
    }

    .cityinfo
    {
        text-align: justify;
    }

    .details
    {
        margin-top: 20px;
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