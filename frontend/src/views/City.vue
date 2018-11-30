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
				if (this.$route.params.name)
                    return this.$route.params.name.toLowerCase();
				else
					return this.$route.path.toString().substr(1);
			}
		},
		created()
		{
			this.setTitle("City");
		},
        mounted()
        {
            this.$store.commit('cityPage', true);
        },
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