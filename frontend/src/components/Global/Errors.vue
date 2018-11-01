<template>
    <div id="errors">
        <SweetModal title="Oops!"
                    icon="error"
                    hide-close-button
                    blocking
                    overlay-theme="dark"
                    modal-theme="light"
                    ref="reloaderror">
            We were unable to load this page. Check your internet connection and try again.

            <button class="retry"
                    @click="reloadPage()">
                Try Again
            </button>
        </SweetModal>
        <SweetModal title="Oops!"
                    icon="error"
                    hide-close-button
                    blocking
                    overlay-theme="dark"
                    modal-theme="light"
                    ref="fatalerror">
            {{fatalError}}
            <br>
            <button class="retry"
                    @click="goHome()">
                Ok
            </button>
        </SweetModal>
    </div>
</template>

<script>
	import {SweetModal} from 'sweet-modal-vue';

	export default {
		name:       "Errors",
		components: {
			SweetModal,
		},
		data()
		{
			return {
				fatalError: "Something went wrong while loading this page.",
			};
		},
		methods:    {
			reloadPage()
			{
				window.location.reload();
			},
			goHome()
			{
				window.location = "/";
			}
		},
		created()
		{
			this.$root.$on('error', () => {
				setTimeout(() => {
					this.$refs.reloaderror.open();
				}, 1000);
			});
			this.$root.$on('fatal', (text) => {
				setTimeout(() => {
					if (typeof text !== undefined)
						this.fatalError = text;

					this.$refs.fatalerror.open();
				}, 1000);
			});

		}
	};
</script>

<style scoped>
    .retry
    {
        border: 1px solid #f44336;
        padding: 8px;
        font-family: PierSans, sans-serif;
        margin-top: 20px;
        font-size: 18px;
        background: transparent;
        color: #f44336;
        cursor: pointer;
        transition: all 0.3s;
    }

    .retry:hover
    {
        border: 1px solid #000;
        color: #000;
    }
</style>