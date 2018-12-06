<template>
    <Loading dark fullscreen center/>
</template>

<script>
	import axios from 'axios';
	import {config} from '../config';
	import Loading from '../components/Loading.vue';

	export default {
		name:       "CityRedirect",
		components: {
			Loading,
		},
		async created()
		{
			let error404 = () => {
				this.$router.push('/404');
				return false;
			};


			let operation;

			try
			{
				operation = this.$route.path.toString().substr(1).split("-")[0].toLowerCase();
			}
			catch (err)
			{
				return error404();
			}

			let operations = ["search", "impact", "gv", "gt", "ge"];
			let cityName;

			if (operations.indexOf(operation) === -1)
			{
				operation = "search";
				cityName = this.$route.path.toString().substr(1);
			}
			else
			{
				if (!this.$route.params.name)
					return error404();

				cityName = this.$route.params.name.toLowerCase();
			}
			console.log(operation, cityName);

			let lcID, lcName;
			try
			{
				let cityData = await axios.get(config.api + config.endpoints.city(cityName));

				// If we're at a city with >1 LC, 404 outta here
				if (!cityData.data.lc_set || cityData.data.lc_set.length > 1)
					return error404();

				lcID = cityData.data.lc_set[0].gis_id;
				lcName = cityData.data.lc_set[0].reference_name;
			}
			catch (err)
			{
				// If the name was not found, maybe they're referring to the LC name (eg. USP)
				if (err.response && err.response.status === 404)
				{
					try
					{
						let lcData = await axios.get(config.api + config.endpoints.lcByName(cityName));
						lcID = lcData.data.gis_id;
						lcName = lcData.data.reference_name;
					}
					catch (err)
					{
						if (err.response && err.response.status === 404)
							return error404();

						console.error(err);
						this.$root.$emit('error');
						return false;
					}
				}
			}

			let destination;
			switch (operation)
			{
				case "search":
					destination = "/searchtool/?filter=" + encodeURIComponent(lcName);
					break;

				case "impact":
					destination = "/opportunities/?lc=" + lcID;
					break;

				case "gv":
					destination = "/opportunities/?product=1&lc=" + lcID;
					break;

				case "gt":
					destination = "/opportunities/?product=2&lc=" + lcID;
					break;

				case "ge":
					destination = "/opportunities/?product=5&lc=" + lcID;
					break;

				default:
					return error404();
			}
			this.$router.push(destination);
		}
	};
</script>

<style scoped>

</style>