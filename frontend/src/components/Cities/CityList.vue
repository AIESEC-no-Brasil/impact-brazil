<template>
    <div v-if="regions">
        <div class="section">
            <ul style='margin-left: 20px;'>
                <li v-for="region in sortRegions(regions)" :key="region.id">
                    <b class='region-name'>{{region.name}}</b>
                    <ul>
                        <li v-for="city in region.city_set" :key="city.id">
                            <a href="#"
                               @click='$emit("city-clicked", city.id)'
                               @mouseover="$emit('city-hovered', city.id)"
                               @mouseout="$emit('city-unhovered')">
                                {{city.name}}
                            </a>
                        </li>
                    </ul>
                    <br>
                    <div v-if='region.order === sectionBreak'></div>
                </li>
            </ul>
        </div>
    </div>
    <Loading small dark v-else/>
</template>

<script>
	import bContainer from 'bootstrap-vue/es/components/layout/container';
	import bCol from 'bootstrap-vue/es/components/layout/col';
	import bRow from 'bootstrap-vue/es/components/layout/row';
	import Loading from '../Loading.vue';

	export default {
		name:       "CityList",
		props:      {
			regions: Array,
		},
		components: {
			Loading,
			bContainer,
			bCol,
			bRow,
		},
		computed:   {
			sectionBreak()
			{
				if (this.regions)
                    return parseInt(this.regions.length / 2);
			}
		},
		methods:    {
			sortRegions(regions)
			{
				let regions_copy = JSON.parse(JSON.stringify(regions));
				regions_copy.sort((a, b) => a.order - b.order);
				return regions_copy;
			}
		}
	};
</script>

<style scoped>
    .section
    {
        -webkit-columns: 2;
        -moz-columns: 2;
        columns: 2;
        width: 100%;
    }

    .section *
    {
        margin: 0;
    }

    .section div
    {
        -webkit-column-break-inside: avoid;
        page-break-inside: avoid;
        break-inside: avoid;
    }
</style>