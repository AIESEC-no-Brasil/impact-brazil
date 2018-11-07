<template>
    <div class="section">
        <div class="title">Projects</div>

        <b-container fluid>
            <b-row>
                <b-col cols="12"
                       md="4"
                       class="product"
                       v-for="product in products"
                       :key="product.id">
                    <img :src="logoDirs.products + product.logo"
                         :title="product.name"
                         :alt="product.name"/>
                    <div class="description">{{product.description}}</div>
                    <div class="detail">
                        {{markdown(product.detail)}}
                    </div>
                </b-col>
            </b-row>
        </b-container>

        <VideoModal ref="videomodal"/>

        <!--<div class="projects">
                        <span v-for="project in getDataset(product.gis_id)">
                            <img :key="project.id"
                                 :id="'proj' + project.gis_id"
                                 :src="[null, logoDirs.sdgs, logoDirs.subproductsGT, null, null, logoDirs.subproductsGE][product.gis_id] + project.logo"
                                 role="button"/>

                                <div>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aspernatur at consequatur
                                    eligendi error iure nemo sed soluta temporibus. Doloribus ea fugiat harum illum natus odit
                                    provident quidem, reiciendis sed similique?
                                </div>
                                <div>Aliquid, aspernatur deleniti in nisi quae reprehenderit vero! A accusamus architecto
                                    beatae, culpa, cum cupiditate dolore, doloremque enim est illum laudantium nam nisi odio
                                    praesentium quod quos rem similique veritatis?
                                </div>
                                <a href="#">APPLY NOW &rarr;</a>

                        </span>
                    </div>-->
    </div>
</template>

<script>
	import VideoModal from '../components/VideoModal.vue';

	import bContainer from 'bootstrap-vue/es/components/layout/container';
	import bCol from 'bootstrap-vue/es/components/layout/col';
	import bRow from 'bootstrap-vue/es/components/layout/row';

	import MarkdownIt from 'markdown-it';
	import axios from 'axios';
	import {config} from '../config';

	export default {
		name:       "Projects",
		components: {
			VideoModal,
			bContainer,
			bCol,
			bRow,
			Nl2br,
		},
		data()
		{
			return {
				products:      [],
				sdgs:          [],
				subproductsGT: [],
				subproductsGE: [],
				logoDirs:      config.logosHD,
			};
		},
		async mounted()
		{
			this.loadProjects();
		},
		methods:    {
			async loadProjects()
			{
				let productsData, sdgsData, subproductsGTData, subproductsGEData;
				try
				{
					[productsData, sdgsData, subproductsGTData, subproductsGEData] = await Promise.all([
						axios.get(config.api + config.endpoints.products),
						axios.get(config.api + config.endpoints.sdgs),
						axios.get(config.api + config.endpoints.subproductsGT),
						axios.get(config.api + config.endpoints.subproductsGE)
					]);
					[this.products, this.sdgs, this.subproductsGT, this.subproductsGE] = [productsData.data, sdgsData.data, subproductsGTData.data, subproductsGEData.data];
				}
				catch (err)
				{
					console.error(err);
					this.$root.$emit('error');
					return false;
				}
			},
			getDataset(product)
			{
				switch (product)
				{
					case 1:
						return this.sdgs;

					case 2:
						return this.subproductsGT;

					case 3:
						return this.subproductsGE;
				}
			},
			markdown(text)
			{
				let md = new MarkdownIt();
				return md.render(text);
			},
		}
	};
</script>

<style lang="scss" scoped>
    .title
    {
        text-align: center;
        margin: 10px 0;
        font-size: 36px;
        font-family: PierSansBold, sans-serif;
    }

    .product
    {
        text-align: center;
        img
        {
            max-width: 300px;
            margin: 0 30px;
        }

        .description
        {
            font-family: PierSans, sans-serif;
            font-size: 20px;
        }

        .projects
        {
            width: 90vw;
            max-width: 1000px;
            margin: 20px auto;

            img
            {
                width: 150px;
                margin: 10px;
                cursor: pointer;
            }
        }
    }
</style>