<template>
    <div class="section">
        <CityInfo :city-name="cityName"
                  show-details
                  change-title/>
    </div>
</template>

<script>
	import CityInfo from '../components/Cities/CityInfo.vue';

	export default {
		name:       "City",
		components: {
			CityInfo
		},
		computed:   {
			cityName()
			{
				return this.$route.params.name.toLowerCase();
			}
		},
		created()
		{
			this.setTitle("City");
		}
	};
</script>

<style scoped>

    @media screen and (min-width: 768px)
    {
        .section
        {
            width: 70%;
            margin: auto;
        }
    }
</style>