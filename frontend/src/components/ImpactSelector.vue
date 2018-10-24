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
	import axios from 'axios';
	import {config} from '../config.js';

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
                defaultText: {
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
						question:  "When do you want to visit Brazil?",
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
		async mounted()
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
				el.style.top = -9999;
				el.style.left = -9999;

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
				// Create a function to load data into {id, text} format
				async function loadData(vm, url, idKey, textKey, imageKey = false, imageW = 0)
				{
					let data;
					try
					{
						data = await axios.get(url);
					}
					catch (err)
					{
						console.error(err);
						vm.$root.$emit('error');
						return false;
					}
					let loadedData = [];
					let loadedDataWithImages = [];

					for (let k in data.data)
					{
						if (data.data.hasOwnProperty(k))
						{
							loadedData.push({id: data.data[k][idKey], text: data.data[k][textKey]});

							if (imageKey !== false)
							{
								// Load the image list
								loadedDataWithImages.push({
									id:   data.data[k][idKey],
									text: `<img src='${data.data[k][imageKey]}' style='width: ${imageW}px'> ${data.data[k][textKey]}`
								});

								// Preload the image in a hidden element
								let preload = new Image();
								preload.src = data.data[k][imageKey];
								vm.$refs['image-preloader'].appendChild(preload);
							}
						}
					}

					if (imageKey === false)
						return loadedData;
					else
						return {textOnly: loadedData, withImages: loadedDataWithImages};

				}

				// Load entities list
				let entityList = await loadData(this, config.api + config.endpoints.entities, 'id', 'name');
				if (entityList === false)
					return false;

				this.lists.entityList = entityList;

				// Generate months array
				let months         = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
				    monthsNextYear = [];

				// We want to circle the month so it starts from this month
				let now = new Date(), month = now.getMonth(), year = now.getFullYear();

				for (let i = 0; i < month; i++)
					monthsNextYear.push(months.shift() + " " + (year + 1));

				months = months.map(m => m + " " + year);
				months = [...months, ...monthsNextYear];


				for (let i = 1; i <= 12; i++)
					this.lists.months.push({id: ((i + month) % 12), text: months[i - 1]});

				// Load products etc.
				// For the sake of not adding a "load" between choosing your product and choosing the SDG/subproduct,
				// we load both SDGs and subproduct
				let loadList = ["products", "sdgs", "subproductsGT", "subproductsGE"];

				loadList.forEach(async (load) => {
					let {textOnly, withImages} = await loadData(this, config.api + config.endpoints[load], 'gis_id', (load === 'products' ? 'description' : 'name'), 'logo', 90);

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
    @import "../assets/colors";

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

        @media (max-aspect-ratio: 16/9)
        {
            height: 70vh;
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

        @media (max-aspect-ratio: 16/9)
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
                padding-top: 40vh;

                img
                {
                    display: none;
                }
            }
            .right
            {
                right: 5vw;
                padding-top: 40vh;
            }
        }

        .question-text
        {
            display: inline-block;
            margin-top: 20px;

            @media (max-aspect-ratio: 16/9)
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
            border-left: $border-left-width solid map_get($ib-colors-list-lt, $border-left);
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