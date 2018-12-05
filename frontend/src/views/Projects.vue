<template>
    <div class="section">
        <div class="title">Projects</div>

        <b-container fluid v-if="!loading">
            <b-row>
                <b-col cols="12"
                       md="4"
                       class="product"
                       v-for="product in lists.products"
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
                             v-if="project.name !== 'Other'"
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
                                    <a @click="goToOpportunity(product.gis_id, product.gis_id === 1 ? (1100+project.sdg) : project.gis_id)"
                                       :style="buttonBackground(product.color)"
                                       class="orange-button">
                                        Apply &raquo;
                                    </a>
                                </b-col>
                            </b-row>
                        </b-container>
                    </div>
                </b-col>
            </b-row>
        </b-container>
        <Loading v-else fullscreen center dark/>
        <VideoModal ref="videomodal"/>
    </div>
</template>

<script>
	import VideoModal from '../components/VideoModal.vue';
	import Loading from '../components/Loading.vue';

	import bContainer from 'bootstrap-vue/es/components/layout/container';
	import bCol from 'bootstrap-vue/es/components/layout/col';
	import bRow from 'bootstrap-vue/es/components/layout/row';

	import MarkdownIt from 'markdown-it';
	import axios from 'axios';
	import {config} from '../config';
	import {dataLoad} from '../functions/data-loader';

	export default {
		name:       "Projects",
		components: {
			VideoModal,
			Loading,
			bContainer,
			bCol,
			bRow,
		},
		data()
		{
			return {
				lists:    {
					products:      [],
					projects:      [],
					subproductsGT: [],
					subproductsGE: [],
				},
				logoDirs: config.logosHD,
				loading:  true,
			};
		},
		async created()
		{
			this.setTitle("Projects");
			this.loadProjects();
		},
		methods:    {
			async loadProjects()
			{
				let lists = ["products", "projects", "subproductsGT", "subproductsGE"];
				let loadOut = await dataLoad(this, lists);

				lists.forEach(list => {
					if (loadOut.hasOwnProperty(list))
						this.lists[list] = loadOut[list];
				});

				this.loading = false;
			},
			getDataset(product)
			{
				switch (product)
				{
					case 1:
						return this.lists.projects.filter(project => !project.hidden);

					case 2:
						return this.lists.subproductsGT;

					case 5:
						return this.lists.subproductsGE;
				}
			},
			goToOpportunity(product, project)
			{
				this.$store.commit('queueOptReload');

				let query = {product};
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
				this.$router.push({path: '/opportunities', query});
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
					backgroundImage: `url('${config.videos.projectThumbDir}${img ? img : config.videos.defaultProjectThumb}')`
				};
			},
			showVideo(url = false)
			{
				this.$refs.videomodal.showVideo(url);
			},
			buttonBackground(color)
			{
				return {
					backgroundColor: color
				};
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
            max-width: 200px;
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
            margin-bottom: 20px;

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
        }
    }

    .no-padding
    {
        padding: 0;
    }
</style>