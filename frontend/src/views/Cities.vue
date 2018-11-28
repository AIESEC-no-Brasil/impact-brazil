<template>
    <div class="section">
        <div class="title">Cities</div>
        <b-container fluid>
            <b-row>
                <b-col cols="12" lg="6" md="7">
                    <CityMap :cities="cities"
                             :hovered="hovered"
                             @city-clicked="loadCity"/>
                </b-col>
                <b-col cols="12" lg="6" md="5">
                    <CityInfo :cities="cities"
                              :city-id="city"
                              @city-hovered="hoverCity"
                              @city-unhovered="hovered = 0"
                              @city-clicked="loadCity"
                              @city-cleared="city=0"/>
                </b-col>
            </b-row>
        </b-container>
    </div>
</template>

<script>
	import CityMap from '../components/Cities/CityMap.vue';
	import CityInfo from '../components/Cities/CityInfo.vue';
	import bContainer from 'bootstrap-vue/es/components/layout/container';
	import bCol from 'bootstrap-vue/es/components/layout/col';
	import bRow from 'bootstrap-vue/es/components/layout/row';

	import axios from 'axios';
	import {config} from '../config';

	export default {
		name:       "Cities",
		components: {
			CityMap,
			CityInfo,
			bContainer,
			bCol,
			bRow,
		},
		data()
		{
			return {
				cities: [],
				city:   0,
                hovered: 0,
			};
		},
		methods:    {
			async loadCities()
			{
				let cityData;
				try
				{
					cityData = await axios.get(config.api + config.endpoints.regions);
				}
				catch (err)
				{
					console.error(err);
					this.$root.$emit('error');
					return false;
				}
				this.cities = cityData.data;
			},
            hoverCity(id)
            {
            	this.hovered = id;
            },
			async loadCity(cityID)
			{
				this.city = cityID;
			}
		},
		async created()
		{
            this.setTitle("Cities");
			this.loadCities();
		}
	};
</script>

<style scoped>
    .title
    {
        text-align: center;
        margin: 10px 0;
        font-size: 36px;
        font-family: PierSansBold, sans-serif;
    }
</style>