<template>
    <transition name="impact-selector">
        <div id="impact-selector"
             :class="['bg-ib--'+questionColors[currentQ], 'border-left--'+questionColors[currentQ]]">
            <div class="left">
                <ImpactSelectorButton dir="left"
                                      :qno="currentQ"
                                      :accent="questionColors[currentQ]"
                                      @click.native="prevQuestion"/>
            </div>
            <div class="center">
                <transition-group name="question-transition"
                                  @before-enter="hideQuestionBeforeEnter">
                    <div class="questions"
                         v-for="question in questionList"
                         v-show="question.condition"
                         :key="question.id">
                        <div class="question-text">
                            {{question.question}}
                        </div>
                        <div class="answer-space">
                            <ImpactSelectorAutocomplete @got-answer="nextQuestion"
                                                        :caption="question.caption"
                                                        :options="question.options"
                                                        :defaults="question.defaults"
                                                        :ref="question.id"
                                                        :text="defaultText[question.id]"
                                                        :error="error"/>
                        </div>
                    </div>
                </transition-group>
            </div>
            <div class="right">
                <ImpactSelectorButton dir="right"
                                      ref="rbutton"
                                      :accent="questionColors[currentQ]"
                                      @click.native="nextQuestion"/>
            </div>
            <div v-show="false" class="image-preloader" ref="image-preloader"></div>
        </div>
    </transition>
</template>

<script>
	import ImpactSelectorAutocomplete from './ImpactSelectorAutocomplete.vue';
	import ImpactSelectorButton from './ImpactSelectorButton.vue';
	import {config} from '../../config.js';
	import {monthList} from '../../functions/month-list';
	import {dataLoad} from '../../functions/data-loader';

	export default {
		name:       "ImpactSelector",
		components: {
			ImpactSelectorAutocomplete,
			ImpactSelectorButton,
		},
		data()
		{
			return {
				currentQ:       0,
				lists:          {
					entityList:              [],
					months:                  [],
					productsWithImages:      [],
					products:                [],
					sdgsWithImages:          [],
					sdgs:                    [],
					subproductsGTWithImages: [],
					subproductsGEWithImages: [],
					subproductsGT:           [],
					subproductsGE:           [],
				},
				answers:        {
					entity:          -1,
					month:           -1,
					product:         -1,
					subproduct:      -1,
					sdg:             -1,
					subproductOrSdg: ""
				},
				defaultText:    {
					q0: "",
				},
				error:          false,
				questionColors: ["blue", "pink", "orange", "purple"]
			};
		},
		computed:   {
			questionList()
			{
				return [
					{
						id:        'q0',
						condition: this.currentQ === 0,
						question:  "Where are you from?",
						caption:   "Choose country or territory",
						options:   this.lists.entityList,
						defaults:  this.lists.entityList
					},
					{
						id:        'q1',
						condition: this.currentQ === 1,
						question:  "From when are you available to visit Brazil?",
						caption:   "Choose month",
						options:   this.lists.months,
						defaults:  this.lists.months
					},
					{
						id:        'q2',
						condition: this.currentQ === 2,
						question:  "What are you looking for?",
						caption:   "Choose product",
						options:   this.lists.products,
						defaults:  this.lists.productsWithImages
					},
					{
						id:        'q3subproductGE',
						condition: this.currentQ === 3 && this.answers.product === 5,
						question:  "What field do you want to work in?",
						caption:   "Choose field",
						options:   this.lists.subproductsGE,
						defaults:  this.lists.subproductsGEWithImages
					},
					{
						id:        'q3subproductGT',
						condition: this.currentQ === 3 && this.answers.product === 2,
						question:  "What field do you want to work in?",
						caption:   "Choose field",
						options:   this.lists.subproductsGT,
						defaults:  this.lists.subproductsGTWithImages
					},
					{
						id:        'q3sdg',
						condition: this.currentQ === 3 && this.answers.product === 1,
						question:  "What kind of project are you looking for?",
						caption:   "Choose project type",
						options:   this.lists.sdgs,
						defaults:  this.lists.sdgsWithImages
					},
				];
			}
		},
		async created()
		{
			await this.loadLists();
		},
		methods:    {
			prevQuestion()
			{
				this.currentQ = Math.max(--this.currentQ, 0);
			},
			nextQuestion()
			{
				// This one's not as simple as prevQuestion!
				// First, check our ref:
				let ref;

				if (this.currentQ < 3)
					ref = this.$refs[`q${this.currentQ}`];
				else if (this.currentQ === 3)
				{
					if (this.answers.subproductOrSdg === 'sdg')
						ref = this.$refs['q3sdg'];
					else
						ref = this.$refs['q3subproduct' + (this.answers.product === 2 ? "GT" : "GE")];
				}

				// Get the search
				let selectedID = ref[0].selectedID;

				if (selectedID === -1)
				{
					this.error = true;
					setTimeout(() => {
						this.error = false;
					}, 500);
				}
				else
				{
					switch (this.currentQ)
					{
						case 0:
							this.answers.entity = selectedID;
							break;

						case 1:
							this.answers.month = selectedID;
							break;

						case 2:
							this.answers.product = selectedID;
							this.answers.subproductOrSdg = selectedID === 1 ? 'sdg' : 'subproduct';
							break;

						case 3:
							this.answers.subproductOrSdg === 'sdg' ? this.answers.sdg = selectedID : this.answers.subproduct = selectedID;
							break;
					}

					if (this.currentQ === 3)
						this.$emit('got-answers', this.answers);
					else
						this.currentQ = Math.min(++this.currentQ, 3);
				}
			},
			hideQuestionBeforeEnter(el)
			{
				// Small hack to make sure that when we hit "prevQuestion", the list doesn't displace the current question as it's fading out
				el.style.position = 'absolute';
				el.style.top = "-9999px";
				el.style.left = "-9999px";

				function showElem(elem)
				{
					elem.style.position = '';
					elem.style.top = 0;
					elem.style.left = 0;
				}

				setTimeout(showElem, 501, el);
			},
			reloadPage()
			{
				window.location.reload();
			},
			async loadLists()
			{
				let imageLists = ["products", "sdgs", "subproductsGT", "subproductsGE"];
				let listsArray = ["entities", ...imageLists];
				let loadOut = await dataLoad(this, listsArray);

				// Convert our "un-vetted" data to vetted data
				let getDataFromList = (data, idKey, textKey, imageKey = false, imageW = 0, imageDir = "/static/images/") => {
					let loadedData = [];
					let loadedDataWithImages = [];

					for (let k in data)
					{
						if (data.hasOwnProperty(k))
						{
							loadedData.push({id: data[k][idKey], text: data[k][textKey]});

							if (imageKey !== false)
							{
								// Load the image list
								loadedDataWithImages.push({
									id:   data[k][idKey],
									text: `<img src='${imageDir}${data[k][imageKey]}' style='width: ${imageW}px'> ${data[k][textKey]}`
								});

								// Preload the image in a hidden element
								let preload = new Image();
								preload.src = data[k][imageKey];
								if (this.$refs['image-preloader'] !== undefined)
									this.$refs['image-preloader'].appendChild(preload);
							}
						}
					}

					if (imageKey === false)
						return loadedData;
					else
						return {textOnly: loadedData, withImages: loadedDataWithImages};
				};

				// Load entities list
				this.lists.entityList = getDataFromList(loadOut['entities'], 'id', 'name');

				// Generate months array
				let {months, month} = monthList();
				for (let i = 0; i < 12; i++)
					this.lists.months.push({id: ((i + month) % 12) + 1, text: months[i]});

				// Load products & projects
				imageLists.forEach(load => {
					let {textOnly, withImages} = getDataFromList(loadOut[load], 'gis_id', (load === 'products' ? 'description' : 'name'), 'logo', 60, config.logos[load]);

					if (textOnly === false || withImages === false)
						return false;

					this.lists[load] = textOnly;
					this.lists[load + 'WithImages'] = withImages;
				});
			}
		}
	};
</script>

<style lang="scss" scoped>
    @import "../../../node_modules/bootstrap/scss/functions";
    @import "../../../node_modules/bootstrap/scss/variables";
    @import "../../../node_modules/bootstrap/scss/mixins/breakpoints";
    @import "../../assets/colors";

    $border-left-width: 20px;

    #impact-selector
    {
        height: 30vh;
        /*background-color: #3be33d;*/
        transition: background-color 0.5s, border-left 0.5s;
        position: absolute;
        bottom: 0;
        width: 100%;
        z-index: 5;
        box-shadow: 0 -4px 12px 4px rgba(0, 0, 0, 0.8);
        /*padding-top: 20px;*/

        @include media-breakpoint-down(sm)
        {
            height: 100vh;
            padding-top: 20px;
        }

        #ib-logo-questions
        {
            text-align: center;

            img
            {
                padding-right: 30px;
                padding-top: 10px;
                padding-left: 10px;
                border-right: 2px solid #fff;
                max-width: 190px;
            }
        }
        .left, .right
        {
            padding-top: 50px;
        }
        .left, .right, .center
        {
            position: absolute;
        }
        .left
        {
            left: 4vw;
            width: 10vw;
        }
        .center
        {
            left: 18vw;
            width: 60vw;
            padding-top: 20px;
        }
        .right
        {
            right: 5vw;
        }

        @include media-breakpoint-down(sm)
        {
            // We redo the positionining on mobile
            .center
            {
                left: 5vw;
                width: 90vw;
                padding-top: 5px;
            }
            .left
            {
                left: 5vw;
                bottom: 20vh;

                img
                {
                    display: none;
                }
            }
            .right
            {
                right: 5vw;
                bottom: 20vh;
            }
        }

        .question-text
        {
            display: inline-block;
            margin-top: 20px;

            @include media-breakpoint-down(sm)
            {
                margin-top: 30px;
            }
            font-size: 2em;
            font-family: PierSansLight, sans-serif;
            color: #fff;
        }
        .answer-space
        {
            margin-top: 10px;
        }
    }

    $border-left-list: blue yellow green purple pink orange;
    @each $border-left in $border-left-list
    {
        .border-left--#{$border-left}
        {
            @include media-breakpoint-up(md)
            {
                border-left: $border-left-width solid map_get($ib-colors-list-lt, $border-left);
            }
        }

    }

    .question-transition-enter, .question-transition-leave-to
    {
        opacity: 0;
    }

    .question-transition-enter-active, .question-transition-leave-active
    {
        transition: opacity 0.5s;
    }

    .question-transition-enter-active
    {
        transition-delay: 0.5s;
    }

    .impact-selector-enter-to
    {
        transform: translateY(0);
    }

    .impact-selector-enter-active, .impact-selector-leave-active
    {
        transition: transform 0.5s !important; // this has to override the background-color transition
    }

    .impact-selector-enter, .impact-selector-leave-to
    {
        transform: translateY(100%);
    }

</style>