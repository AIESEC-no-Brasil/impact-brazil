<template>
    <div id="apply">
        <a href="#" @click="preApply" class="shiny-btn" v-if="!applying">Apply</a>
        <Loading center v-if="applying"/>

        <SweetModal overlay-theme="dark"
                    modal-theme="light"
                    ref="question">
            <b-form @submit.prevent="applyGT" v-show="!applying">
                <b-form-group id="answer-group"
                              label="Why are you the best candidate for this opportunity?"
                              label-for="answer"
                              description="Up to 1000 characters.">
                    <b-form-textarea id="answer"
                                     required
                                     v-model="answer"
                                     rows="3"
                                     max-rows="8"/>
                </b-form-group>
                <div class="title" style="color: red" v-if="tooManyChars">
                    Please ensure your answer is less than 1000 characters.
                </div>

                <b-button type="submit" variant="success">Apply</b-button>
            </b-form>
            <Loading v-if="applying" dark center/>
        </SweetModal>
    </div>
</template>

<script>
	import axios from 'axios';
	import {config} from '../../config';
	import {SweetModal} from 'sweet-modal-vue';
	import bForm from 'bootstrap-vue/es/components/form/form';
	import bFormGroup from 'bootstrap-vue/es/components/form-group/form-group';
	import bFormTextarea from 'bootstrap-vue/es/components/form-textarea/form-textarea';
	import bButton from 'bootstrap-vue/es/components/button/button';
	import Loading from '../Loading.vue';

	export default {
		name:       "OpportunityPerformApplyButton",
		components: {
			SweetModal,
			bForm,
			bFormGroup,
			bFormTextarea,
			bButton,
			Loading
		},
		props:      {
			id:   Number,
			isGt: Boolean,
		},
		data()
		{
			return {
				applying:     false,
				tooManyChars: false,
				answer:       '',
			};
		},
		methods:    {
			async preApply()
			{
				if (this.isGt)
					this.$refs.question.open();
				else
					this.apply();
			},
			async applyGT()
			{
				if (this.answer === '' || this.answer.length >= 1000)
					this.tooManyChars = true;
				else
					this.apply();
			},
			async apply()
			{
				if (!this.$session.get('loggedIn'))
					this.$root.$emit('login');
				else
				{
					this.applying = true;
					let applyData;
					try
					{
						applyData = await axios.post(config.api + config.endpoints.apply, {
							api_key:    this.$session.get('accessToken'),
							opp_id:     this.id,
							gip_answer: this.answer,
						});
					}
					catch (err)
					{
						if (err.response)
						{
							if (err.response.status === 401)
							{
								// Access token expired, refresh the page for now
								// TODO: Better way to handle this in the future
								this.$root.$emit('logout');
							}
							else if (err.response.status === 403)
								this.$root.$emit('profile');
							else
								this.$root.$emit('error');
						}
						else
						{
							console.error(err);
							this.$root.$emit('error');
						}
						this.applying = false;
						return;
					}
					window.location.reload();
					return applyData;
				}
			}
		}
	};
</script>

<style lang="scss" scoped>
    @import "../../../node_modules/bootstrap/scss/functions";
    @import "../../../node_modules/bootstrap/scss/variables";
    @import "../../../node_modules/bootstrap/scss/mixins/breakpoints";
    @import "../../assets/colors";

    .shiny-btn
    {
        color: white;
        display: block;
        text-align: center;
        font-size: 36px;
        text-decoration: none;
        padding: 4px 12px;
        transition: transform 500ms cubic-bezier(0.68, -0.55, 0.265, 1.55), background-position 800ms cubic-bezier(0.68, -0.55, 0.265, 1.55), box-shadow 500ms linear;
        background: $ib-pink-dk url('data:image/svg+xml;utf8,<?xml version="1.0" encoding="utf-8"?><svg version="1.1" id="Livello_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"   width="1296px" height="768px" viewBox="0 0 1296 768" enable-background="new 0 0 1296 768" xml:space="preserve"><g><polygon fill="%23FF2355" points="766.6,1.2 -0.2,768 200.7,768 967.5,1.2   "/></g><g><polygon fill="%23FF2355" points="1094.8,1.2 328,768 528.9,768 1295.7,1.2   "/></g></svg>') no-repeat -200px center;
        background-size: contain;

        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.24);

        @include media-breakpoint-up(md)
        {
            font-size: 36px;
            margin: 32px 0;
        }
        @include media-breakpoint-down(sm)
        {
            font-size: 20px;
            margin: 14px 0;
        }
    }

    .shiny-btn:hover
    {
        transform: scale(1.1);
        background-position: -40px;
        box-shadow: 0 3px 6px rgba(0, 0, 0, 0.16), 0 3px 6px rgba(0, 0, 0, 0.23);
    }

    .shiny-btn:focus, .shiny-btn:active
    {
        transform: scale(1);
        background-position: 500px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.24);
    }
</style>