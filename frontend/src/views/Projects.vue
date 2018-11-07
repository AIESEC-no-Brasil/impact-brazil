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
                    <div class="product-header">
                        <img :src="logoDirs.products + product.logo"
                             :title="product.name"
                             :alt="product.name"/>
                        <div class="description">{{product.description}}</div>
                    </div>
                    <div class="project" v-for="project in getDataset(product.gis_id)" :key="project.id">
                        <div class="project-title">{{project.name}}</div>
                        <div class="project-image"
                             :style="videoThumb(project.thumbnail)"
                             @click="showVideo(project.video_link)">
                            <div></div>
                        </div>
                        <b-container fluid>
                            <b-row>
                                <b-col cols="12" md="8" class="no-padding">
                                    <div class="project-desc">
                                        {{project.description}}
                                    </div>
                                </b-col>
                                <b-col cols="12" md="4" class="no-padding text-right">
                                    <router-link to="/" class="project-apply">
                                        Apply &raquo;
                                    </router-link>
                                </b-col>
                            </b-row>
                        </b-container>
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
				if (typeof text !== "string") return;
				let md = new MarkdownIt();
				return md.render(text);
			},
			videoThumb(img)
			{
				return {
					backgroundImage: `url('${config.videos.projectThumbDir}${img === null ? config.videos.defaultProjectThumb : img}')`
				};
			},
			showVideo(url = false)
			{
				this.$refs.videomodal.showVideo(url);
			},
		}
	};
</script>

<style lang="scss" scoped>
    @import "../assets/colors";

    .title
    {
        text-align: center;
        margin: 10px 0;
        font-size: 36px;
        font-family: PierSansBold, sans-serif;
    }

    .product
    {
        .product-header
        {
            text-align: center;
        }
        img
        {
            max-width: 300px;
            margin: 0 30px;
        }

        .description
        {
            font-family: PierSans, sans-serif;
            font-size: 20px;
            margin-bottom: 20px;
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

        .project
        {

            .project-image
            {
                background-position: center;
                background-size: cover;
                width: 100%;
                height: 200px;
                cursor: pointer;

                div
                {
                    background-image: url('../assets/play-button.png');
                    width: 100px;
                    height: 100px;
                    background-size: 100%;
                    position: relative;
                    top: 50px;
                    margin: auto;
                }
            }
            .project-title
            {
                font-size: 24px;
                font-family: PierSansBold, sans-serif;
            }
            .project-desc
            {
                margin: 4px 4px 0 0;
            }
            .project-apply
            {
                margin: 4px 0;
                padding: 8px 16px;

                background-color: $ib-orange-dk;
                display: inline-block;
                font-family: PierSansBold, sans-serif;
                color: #fff;
                font-size: 24px;
                text-decoration: none;
                transition: background-color 0.3s;
            }
            .project-apply:hover
            {
                background-color: $ib-orange-lt;
            }
        }
    }

    .no-padding
    {
        padding: 0;
    }
</style>