<template>
    <SweetModal modal-theme="dark"
                overlay-theme="dark"
                ref="sweetmodal"
                id="video-modal"
                width="90%"
                :enable-mobile-fullscreen="false"
                @close="stopPlayingVideo">
        <iframe width="100%"
                height="100%"
                frameborder="0"
                allow="autoplay; encrypted-media"
                allowfullscreen
                ref="youtube"
                id="youtube">
        </iframe>
    </SweetModal>
</template>

<script>
	import {SweetModal} from 'sweet-modal-vue';
	import {config} from '../config';

	export default {
		name:       "VideoModal",
		components: {

			SweetModal,
		},
		methods:    {
			showVideo(url = false)
			{
				if (url !== false)
				{
					let setSrc;
					if (url !== "")
						setSrc = config.youtubeURL(url);
					else
						setSrc = config.defaultVideoURL;

					if (this.$refs.youtube.src !== setSrc)
						this.$refs.youtube.src = setSrc;
				}

				setTimeout(() => {
					this.$refs.sweetmodal.open();
				}, 400);

				// Track this event on Google
                this.$ga.event('Video', 'play', url);
			},
			stopPlayingVideo()
			{
				this.$refs.youtube.contentWindow.postMessage('{"event":"command","func":"stopVideo","args":""}', '*');
			}
		}
	};
</script>

<style scoped>
    #youtube
    {
        width: 100%;
        height: calc(70vw * 0.5625);
    }
</style>