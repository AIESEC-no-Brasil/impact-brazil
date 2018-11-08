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
                                    <a @click="goToOpportunity(product.gis_id, project.gis_id)"
                                       class="project-apply">
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
					sdgs:          [],
					subproductsGT: [],
					subproductsGE: [],
				},
				logoDirs: config.logosHD,
				loading:  true,
			};
		},
		async mounted()
		{
			this.loadProjects();
		},
		methods:    {
			async loadProjects()
			{
				let lists = ["products", "sdgs", "subproductsGT", "subproductsGE"];
				for (let i in lists)
				{
					let list = lists[i];
					let storedList = this.$store.getters.getList(list);
					if (storedList.length > 0)
						this.lists[list] = storedList;
					else
					{
						let fetchedList;
						try
						{
							fetchedList = await axios.get(config.api + config.endpoints[list]);
						}
						catch (err)
						{
							console.error(err);
							this.$root.$emit('error');
							return false;
						}
						this.lists[list] = fetchedList.data;
						this.$store.commit('setList', {list, arr: fetchedList.data});
					}
				}
				this.loading = false;
			},
			getDataset(product)
			{
				switch (product)
				{
					case 1:
						return this.lists.sdgs;

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
				this.$router.push({path: 'opportunities', query});
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
            .project-apply
            {
                margin: 4px 0;
                padding: 8px 16px;

                cursor: pointer;
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