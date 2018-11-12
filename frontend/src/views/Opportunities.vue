<template>
    <div class="section" id="opportunities">
        <OpportunityInvite :no-visa="noVisa"
                           @show-video="showVideo"/>
        <OpportunityList :no-visa="noVisa"
                         @show-video="showVideo"/>
        <VideoModal ref="videomodal"/>
    </div>
</template>

<script>
	import OpportunityInvite from '../components/Opportunities/OpportunityInvite.vue';
	import OpportunityList from '../components/Opportunities/OpportunityList.vue';
	import VideoModal from '../components/VideoModal.vue';
	import {config} from '../config';

	export default {
		name:       "Opportunities",
		components: {
			OpportunityInvite,
			OpportunityList,
			VideoModal,
		},
		data()
		{
			return {
				defaultVideoURL: config.defaultVideoURL
			};
		},
		computed:   {
			noVisa()
			{
				return this.$store.state.noVisa;
			}
		},
		methods:    {
			showVideo(url = false)
			{
				this.$refs.videomodal.showVideo(url);
			},
		},
        activated()
        {
            this.setTitle("Opportunities");
        }
	};
</script>

<style scoped>

</style>

