<template>
    <b-container fluid>
        <b-row v-for="product in lc.products"
               :key="product.id"
               class="product-row">
            <b-col cols="12" md="2" class="text-center product-logo">
                <a href="#" @click="goToOpportunity(product.gis_id, false, lc.gis_id)">
                    <img :src="`${getLogoDirectory(0)}${product.logo}`">
                </a>
            </b-col>
            <b-col cols="12" md="10" class="project-logos">
                <a href="#"
                   @click="goToOpportunity(product.gis_id, project.gis_id, lc.gis_id)"
                   v-for="project in getProjectsArray(product.gis_id)"
                   :key="project.id">
                    <img :alt="project.name"
                         :title="project.name"
                         :src="`${getLogoDirectory(product.gis_id)}${project.logo}`"/>
                </a>
            </b-col>
        </b-row>
    </b-container>
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
						retArray = JSON.parse(JSON.stringify(this.lc.sdgs));
						retArray.sort((a, b) => parseInt(a.gis_id) - parseInt(b.gis_id));
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
        margin-bottom: 10px;
    }
</style>