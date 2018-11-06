<template>
    <div class="section" id="opportunities">
        <OpportunityInvite v-if="!$store.state.noVisa"
                           @show-video="showVideo"/>
        <OpportunityList :no-visa="$store.state.noVisa"
                         :i-am-from-brazil="$store.state.iAmFromBrazil"
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
		methods:    {
			showVideo(url = false)
			{
				this.$refs.videomodal.showVideo(url);
			},
		},
	};
</script>

<style scoped>

</style>

