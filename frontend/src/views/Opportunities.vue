<template>
    <div class="section" id="opportunities">
        <OpportunityInvite v-if="!noVisa"
                           @no-visa="noVisa = true"
                           @i-am-from-brazil="iAmFromBrazil = true"
                           @show-video="showVideo"/>
        <OpportunityList :no-visa="noVisa"
                         :i-am-from-brazil="iAmFromBrazil"
                         @show-video="showVideo"/>
        <SweetModal modal-theme="dark"
                    overlay-theme="dark"
                    ref="videoModal"
                    id="video-modal"
                    width="90%"
                    :enable-mobile-fullscreen="false"
                    @close="stopPlayingVideo">
            <iframe width="100%"
                    height="100%"
                    :src="defaultVideoURI"
                    frameborder="0"
                    allow="autoplay; encrypted-media"
                    allowfullscreen
                    ref="youtube"
                    id="youtube">
            </iframe>
        </SweetModal>
    </div>
</template>

<script>
	import OpportunityInvite from '../components/Opportunities/OpportunityInvite.vue';
	import OpportunityList from '../components/Opportunities/OpportunityList.vue';
	import {SweetModal} from 'sweet-modal-vue';
	import {config} from '../config';

	export default {
		name:       "Opportunities",
		components: {
			OpportunityInvite,
			OpportunityList,
			SweetModal,
		},
		data()
		{
			return {
				noVisa:          false,
				iAmFromBrazil:   false,
				defaultVideoURI: config.defaultVideoURI
			};
		},
		methods:    {
			showVideo(url = false)
			{
				if (url !== false)
				{
					let setSrc;
					if (url !== "")
						setSrc = `https://www.youtube.com/embed/${url}?enablejsapi=1`;
					else
						setSrc = this.defaultVideoURI;

					if (this.$refs.youtube.src !== setSrc)
						this.$refs.youtube.src = setSrc;
				}

				setTimeout(() => {
					this.$refs.videoModal.open();
				}, 400);
			},
			stopPlayingVideo()
			{
				this.$refs.youtube.contentWindow.postMessage('{"event":"command","func":"stopVideo","args":""}', '*');
			}
		},
	};
</script>

<style scoped>
    #youtube
    {
        width: 100%;
        height: calc(80vw * 0.5625);
    }
</style>

