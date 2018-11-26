<template>
    <div class="section" id="opportunities">
        <OpportunityInvite @show-video="showVideo"/>
        <OpportunityList @show-video="showVideo"/>
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

