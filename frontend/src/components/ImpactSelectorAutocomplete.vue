<template>
    <div id="autocomplete-component">
        <div class="autocomplete-input-container" v-if="optlistReady">
            <input title="question"
                   type="text"
                   autocomplete="disabled"
                   :class="error ? 'error-bounce' : ''"
                   :placeholder="caption"
                   v-model="search"
                   @focus="focusText($event)"
                   @keydown="selectOption($event)"
                   ref="ibox"
                   tabindex="0"
            />
            <transition name="autocomplete-items">
                <div class="autocomplete-items"
                     v-if="dropdownVisible">
                    <div v-for="(opt, index) in optlistFiltered"
                         :class="index === selection ? 'autocomplete-active' : ''"
                         :key="index"
                         @click="confirmOption(opt.id)">
                        <strong>{{ opt.text.substr(0, search.length) }}</strong><span
                            v-html="opt.text.substr(search.length)"></span>
                    </div>
                </div>
            </transition>
        </div>
        <div v-else>
            <Loading />
        </div>
    </div>
</template>

<script>
	import Vue from "vue";
    import Loading from "./Loading.vue";

	export default {
		name:     "ImpactSelectorAutocomplete",
        components: {
			Loading
        },
		props:    {
			caption:  String,
			options:  Array,
			defaults: Array,
			error:    Boolean
		},
		data()
		{
			return {
				selection:       -1,
				selectedID:      -1,
				dropdownVisible: false,
				search:          "",
			};
		},
		computed: {
			optlistFiltered()
			{
				return this.search.length === 0 ? this.defaults : this.options.filter(opt => this.search.length === 0 || opt.text.substr(0, this.search.length).toLowerCase() === this.search.toLowerCase());
			},
			optlistReady()
			{
				return typeof this.options !== "undefined" && this.options.length > 0;
			}
		},
		methods:  {
			selectOption(e)
			{
				switch (e.which)
				{
					case 40: // Down
						if (++this.selection >= this.optlistFiltered.length)
							this.selection = 0;
						e.preventDefault();
						break;

					case 38: // Up
						if (--this.selection < 0)
							this.selection = this.optlistFiltered.length - 1;
						e.preventDefault();
						break;

					case 13: // Enter
						if (this.selectedID > -1)
							this.$emit('got-answer');
						else if (this.selection > -1)
						{
							let selectedOption = this.optlistFiltered[this.selection];
							this.confirmOption(selectedOption.id);
						}
						e.preventDefault();
						break;

					default:
						// Check if we only have one option
						// Since optlistFiltered is updated only _after_ we type, this needs to happen after a tick
						Vue.nextTick(() => {
							if (this.optlistFiltered.length === 1)
								this.selection = 0;
							else
								this.selection = -1;
						});

						this.dropdownVisible = true;
						this.selectedID = -1;

						break;
				}
			},
			confirmOption(id)
			{
				// We want to make sure we don't get the data from 'defaults' since those might include images etc.
				let correctedOption = this.options.find(option => option.id === id);

				this.selectedID = correctedOption.id;
				this.search = correctedOption.text;
				this.$refs.ibox.focus();
				this.dropdownVisible = false;
			},
			focusText(e)
			{
				this.dropdownVisible = true;
				e.target.select();
			}
		}
	};
</script>

<style scoped>
    .autocomplete
    {
        /*the container must be positioned relative:*/
        position: relative;
        display: inline-block;
    }

    input
    {
        border: 1px solid transparent;
        background-color: #f1f1f1;
        padding: 12px;
        font-size: 2em;
        font-family: 'Pier Sans', sans-serif;
        position: relative;

    }

    input[type=text]
    {
        background-color: #f1f1f1;
        width: 90%;
    }

    .autocomplete-items
    {
        position: absolute;
        border: 1px solid #d4d4d4;
        border-bottom: none;
        border-top: none;
        z-index: 99;
        /*position the autocomplete items to be the same width as the container:*/
        bottom: 100%;
        /*top: 40%;*/
        left: 0;
        right: 0;
        max-height: 70vh;
        overflow-y: auto;
    }

    .autocomplete-items div
    {
        transition: all 0.3s;
        padding: 10px;
        cursor: pointer;
        background-color: #fff;
        border-bottom: 1px solid #d4d4d4;
        /*font-size: 2em;*/
        font-family: 'Pier Sans', sans-serif;
    }

    .autocomplete-items div:hover
    {
        /*when hovering an item:*/
        background-color: #e9e9e9;
    }

    .autocomplete-items::-webkit-scrollbar
    {
        width: 4px;
        background-color: #f5f5f5;
    }

    .autocomplete-items::-webkit-scrollbar-track
    {
        border-radius: 10px;
        background: rgba(0, 0, 0, 0.1);
        border: 1px solid #ccc;
    }

    .autocomplete-items::-webkit-scrollbar-thumb
    {
        border-radius: 10px;
        background: linear-gradient(to left, #fff, #e4e4e4);
        border: 1px solid #aaa;
    }

    .autocomplete-items::-webkit-scrollbar-thumb:hover
    {
        background: #fff;
    }

    .autocomplete-items::-webkit-scrollbar-thumb:active
    {
        background: linear-gradient(to left, #22add4, #1e98ba);
    }

    .autocomplete-input-container
    {
        position: relative;
    }

    .autocomplete-active
    {
        /*when navigating through the items using the arrow keys:*/
        background-color: DodgerBlue !important;
        color: #ffffff;
    }

    .autocomplete-items-enter, .autocomplete-items-leave-to
    {
        max-height: 0;
    }

    .autocomplete-items-enter-active, .autocomplete-items-leave-active
    {
        transition: max-height 0.5s;
        overflow-y: hidden;
    }

    .error-bounce
    {
        position: relative;
        animation-name: bouncelr;
        animation-duration: 0.2s;
        animation-iteration-count: infinite;
        animation-timing-function: linear;
    }

    @keyframes bouncelr
    {
        0%
        {
            left: 0;
        }
        33%
        {
            left: -8px;
        }
        67%
        {
            left: 8px;
        }
        100%
        {
            left: 0;
        }
    }
</style>