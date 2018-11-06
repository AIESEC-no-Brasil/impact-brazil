<template>
    <div class="section">
        <div class="title">Our Projects</div>
        <div class="product"
             v-for="product in products"
             :key="product.id">
            <img :src="logoDirs.products + product.logo"
                 :title="product.name"
                 :alt="product.name"/>
            <div class="description">{{product.description}}</div>
            <div class="projects">
                <span v-for="project in getDataset(product.gis_id)">
                    <img :key="project.id"
                         :id="'proj' + project.gis_id"
                         :src="[null, logoDirs.sdgs, logoDirs.subproductsGT, null, null, logoDirs.subproductsGE][product.gis_id] + project.logo"
                         role="button"/>
                    <b-popover :target="'proj' + project.gis_id"
                               :title="project.name"
                               triggers="hover focus"
                               placement="bottom">
                        <div>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aspernatur at consequatur
                            eligendi error iure nemo sed soluta temporibus. Doloribus ea fugiat harum illum natus odit
                            provident quidem, reiciendis sed similique?
                        </div>
                        <div>Aliquid, aspernatur deleniti in nisi quae reprehenderit vero! A accusamus architecto
                            beatae, culpa, cum cupiditate dolore, doloremque enim est illum laudantium nam nisi odio
                            praesentium quod quos rem similique veritatis?
                        </div>
                        <a href="#">APPLY NOW &rarr;</a>
                    </b-popover>
                </span>
            </div>
        </div>
        <VideoModal ref="videomodal"/>
    </div>
</template>

<script>
	import VideoModal from '../components/VideoModal.vue';
	import bPopover from 'bootstrap-vue/es/components/popover/popover';
	import axios from 'axios';
	import {config} from '../config';

	export default {
		name:       "Projects",
		components: {
			VideoModal,
			bPopover
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
			}

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