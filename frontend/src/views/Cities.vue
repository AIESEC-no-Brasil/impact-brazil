<template>
    <div class="section">
        <div class="title">Cities</div>
        <b-container>
            <b-row>
                <b-col cols="12" lg="6" md="7">
                    <Map :cities="cities"
                         @city-clicked="loadCity"/>
                </b-col>
                <b-col cols="12" lg="6" md="5">
                    <CityInfo :cities="cities"
                              :city-id="city"/>
                </b-col>
            </b-row>
        </b-container>
    </div>
</template>

<script>
	import Map from '../components/Cities/Map.vue';
	import CityInfo from '../components/Cities/CityInfo.vue';
	import bContainer from 'bootstrap-vue/es/components/layout/container';
	import bCol from 'bootstrap-vue/es/components/layout/col';
	import bRow from 'bootstrap-vue/es/components/layout/row';

	import axios from 'axios';
	import {config} from '../config';

	export default {
		name:       "Cities",
		components: {
			Map,
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
			};
		},
		methods:    {
			async loadCities()
			{
				let cityData;
				try
				{
					cityData = await axios.get(config.api + config.endpoints.cities);
				}
				catch (err)
				{
					console.error(err);
					this.$root.$emit('error');
					return false;
				}
				this.cities = cityData.data;
			},
			async loadCity(cityID)
			{
				this.city = cityID;
			}
		},
		async mounted()
		{
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