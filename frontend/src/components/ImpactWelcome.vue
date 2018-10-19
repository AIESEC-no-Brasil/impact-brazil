<template>
    <div id="header"
         :class="showingQuestions ? 'no-scroll' : ''">
        <!-- We v-show these because if we v-if these, the video stops playing in the background -->
        <div class="overlay"
             id="lower-overlay"
             v-show="!showingQuestions"></div>
        <div class="overlay"
             id="higher-overlay"
             v-show="showingQuestions"></div>
        <VideoBg :sources="['../static/background.webm']">
            <div class="text-center" id="logo">
                <img src="../assets/logo4.png">
            </div>
            <div id="buttons"
                 @click="showingQuestions = true">
                <ImpactWelcomeButton id="button-visit">
                    Visit<br><b>Brazil</b>
                </ImpactWelcomeButton>
            </div>
        </VideoBg>
        <!-- We v-show this so that the API can load while the page is loading -->
        <ImpactSelector v-show="showingQuestions"
                        @got-answers="setAnswers"/>
    </div>
</template>

<script>
	import ImpactWelcomeButton from '@/components/ImpactWelcomeButton.vue';
	import ImpactSelector from '@/components/ImpactSelector.vue';
	import VideoBg from '@/components/VideoBackground.vue';

	export default {
		name:       "ImpactWelcome",
		components: {
			ImpactWelcomeButton,
			ImpactSelector,
			VideoBg
		},
		data()
		{
			return {
				showingQuestions: false,
				answers:          {}
			};
		},
		methods:    {
			setAnswers(answers)
			{
				this.showingQuestions = false;
				this.answers = answers;
			}
		}
	};
</script>

<style lang="scss" scoped>
    @import '../assets/colors';

    /*#header
    {
        height: 100vh;
        overflow: hidden;
    }

    #header video
    {
        position: fixed;
        top: 0;
        left: 0;

        @media (min-aspect-ratio: 16/9)
        {
            width: 100%;
            height: 100%;
        }

        @media (max-aspect-ratio: 16/9)
        {
            width: 100%;
            height: 100%;
        }

        z-index: -9000;
        overflow: hidden;
    }*/

    .stop-scrolling
    {
        height: 100%;
        overflow: hidden;
    }

    .VideoBg video
    {
        z-index: -9000;
    }

    .overlay
    {
        width: 100%;
        height: 100vh;
        position: absolute;
        left: 0;
        top: 0;
    }

    #lower-overlay
    {
        z-index: -8000;
        background-color: rgba(41, 39, 34, 0.55);
    }

    #higher-overlay
    {
        z-index: 1;
        background-color: rgba(0, 0, 0, 0.85);
    }

    #logo
    {
        position: absolute;
        top: 5vh;
        left: 50%;
        height: 65vh;
        transform: translateX(-50%);

        img
        {
            display: block;
            min-height: 256px;
            height: 100%;
        }

    }

    #buttons
    {
        position: absolute;
        bottom: 5%;
        left: 50%;
        transform: translateX(-50%);
        border-spacing: 10px;
    }

    #button-visit
    {
        background-color: $ib-blue-dk;
        line-height: 0.85;
        padding: 20px 60px;
    }

    #button-visit:hover
    {
        background-color: $ib-blue-lt;
    }

    #button-learn
    {
        background-color: $ib-green-dk;
        line-height: 1.2;
    }

    #button-learn:hover
    {
        background-color: $ib-green-lt;
    }
</style>