<template>
    <div id="header">
        <!-- We v-show these because if we v-if these, the video stops playing in the background -->
        <div class="overlay"
             id="lower-overlay"
             v-show="!showingQuestions"></div>
        <div class="overlay"
             id="higher-overlay"
             v-show="showingQuestions"
             @mousedown="hideQuestions"></div>
        <VideoBg :sources="['../static/background.webm']"
                 img="/static/background.jpg">
            <div class="text-center" id="logo">
                <img src="../../assets/logo4.png">
            </div>
            <div id="buttons">
                <ImpactWelcomeButton id="button-visit"
                                     @click.native="showQuestions">
                    Visit<br><b>Brazil</b>
                </ImpactWelcomeButton>
            </div>
            <!-- We v-show this so that the API can load while the page is loading -->
            <ImpactSelector v-show="showingQuestions"
                            @got-answers="setAnswers"/>
        </VideoBg>
    </div>
</template>

<script>
	import ImpactWelcomeButton from './ImpactWelcomeButton.vue';
	import ImpactSelector from './ImpactSelector.vue';
	import VideoBg from './VideoBackground.vue';

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
				showingQuestions: false
			};
		},
		methods:    {
			setAnswers(answers)
			{
				this.hideQuestions();

				// Entity is not part of answers, so let's put that in a session varaible
                this.$session.set('entity', answers.entity);
                delete answers.entity;

                // Figure out which one of the unnecessary answers we need to delete
				if (answers.subproductOrSdg === 'sdg')
					delete answers.subproduct;
				else
					delete answers.sdg;
				delete answers.subproductOrSdg;

				this.$store.commit('queueOptReload');
				this.$store.commit('noVisa', false);
				this.$store.commit('options', {});
				this.$store.commit('optquery', {});
				this.$router.push({path: '/opportunities', query: answers});
			},
			showQuestions()
			{
				this.showingQuestions = true;
				this.$store.commit('showingQuestions', true);
			},
			hideQuestions()
			{
				this.showingQuestions = false;
				this.$store.commit('showingQuestions', false);
			}
		},
	};
</script>

<style lang="scss" scoped>
    @import "../../../node_modules/bootstrap/scss/functions";
    @import "../../../node_modules/bootstrap/scss/variables";
    @import "../../../node_modules/bootstrap/scss/mixins/breakpoints";
    @import '../../assets/colors';

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
            height: 100%;
        }

        @include media-breakpoint-down(sm)
        {
            height: 45vh;
        }

    }

    #buttons
    {
        position: absolute;
        bottom: 5%;
        left: 50%;
        transform: translateX(-50%);
        border-spacing: 10px;

        @include media-breakpoint-down(sm)
        {
            bottom: 20%;
        }
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