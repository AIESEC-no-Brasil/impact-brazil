<template>
    <div class="product-logo">
        <a v-for="product in lc.products"
           :key="product.id"
           class="product-row"
           href="#"
           @click="goToOpportunity(product.gis_id, false, lc.gis_id)">
            <img :src="`${getLogoDirectory(0)}${product.logo}`">
        </a>
    </div>
</template>

<script>
	import bContainer from 'bootstrap-vue/es/components/layout/container';
	import bCol from 'bootstrap-vue/es/components/layout/col';
	import bRow from 'bootstrap-vue/es/components/layout/row';

	import {config} from '../../config';


	export default {
		name:       "CityProjects",
		props:      {
			lc: {}
		},
		components: {
			bContainer,
			bCol,
			bRow
		},
		methods:    {
			getLogoDirectory(product)
			{
				switch (product)
				{
					case 1:
						return config.logos.sdgs;

					case 2:
						return config.logos.subproductsGT;

					case 5:
						return config.logos.subproductsGE;

					default:
						return config.logosHD.products;
				}
			},
			getProjectsArray(product)
			{
				let retArray;
				switch (product)
				{
					case 1:
						retArray = JSON.parse(JSON.stringify(this.lc.projects));
						retArray.sort((a, b) => parseInt(a.sdg) - parseInt(b.sdg));
						return retArray;

					case 2:
					case 5:
						retArray = JSON.parse(JSON.stringify(this.lc.subproducts.filter(x => x.product === parseInt(product))));
						retArray.sort((a, b) => parseInt(a.gis_id) - parseInt(b.gis_id));
						return retArray;

					default:
						return [];
				}
			},
			goToOpportunity(product, project, lc)
			{
				this.$store.commit('queueOptReload');

				let query = {lc, product};
				if (project)
				{
					switch (product)
					{
						case 1:
							query.sdg = project;
							break;
						case 2:
						case 5:
							query.subproduct = project;
							break;
					}
				}
				this.$router.push({path: '/opportunities', query});
				return true;
			},
		}
	};
</script>

<style scoped>
    .product-logo img
    {
        max-width: 200px;
        width: 100%;
    }

    .product-row, .product-logo
    {
        margin: 10px;
    }
</style>