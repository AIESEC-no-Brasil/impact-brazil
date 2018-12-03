<template>
    <div>
        <div id="cover-opportunity" :style="backgroundStyle">
            <div id="cover-back-button"
                 @click="goBack">
                <i class="material-icons">arrow_back</i>
            </div>
            <div id="cover-overlay">
                <div class="title text-truncate">{{opportunity.title}}</div>
                <div class="location"><i class="material-icons">location_on</i> {{opportunity.location}}</div>
                <div class="social"><OpportunityShare :opportunity="opportunity"/></div>

                <OpportunityPerformApplyButton
                        :id="parseInt(opportunity.id)"
                        :is-gt="parseInt(opportunity.programme.id) > 1"
                        v-if="daysLeft >= 0 && !opportunity.applied_to"/>
                <div class="location" v-else-if="opportunity.applied_to">
                    You have applied to this opportunity.<br>
                    You can check the status of your applications by clicking your name on the top right.
                </div>
                <div class="deadline"><i class="material-icons">alarm</i>
                    {{daysLeft > 0 ? `${daysLeft} day${daysLeft !== 1 ? 's' : ''} left to apply`
                    : daysLeft === 0 ? `Last day to apply`
                    : `This opportunity is not accepting applications since ${new
                    Date(opportunity.applications_close_date).toDateString()}`}}
                </div>
            </div>
        </div>
    </div>
</template>

<script>
	import OpportunityPerformApplyButton from "./OpportunityPerformApplyButton.vue";
	import OpportunityShare from './OpportunityShare.vue';

	export default {
		name:       "OpportunityCover",
		components: {
			OpportunityPerformApplyButton,
			OpportunityShare,
		},
		props:      {
			opportunity: Object
		},
		computed:   {
			backgroundStyle()
			{
				if (this.opportunity.cover_photo)
					return {
						backgroundImage: "url('" + this.opportunity.cover_photo + "')"
					};
				return {};
			},
			daysLeft()
			{
				if (this.opportunity.applications_close_date)
				{
					let ddl = new Date(this.opportunity.applications_close_date), now = new Date();
					//let diff = new Date(ddl - now);
					//return Math.max(0, diff.getDate());
					return Math.floor((ddl - now) / 86400000);
				}
				return 0;
			}
		},
		methods:    {
			goBack()
			{
				window.history.back();
			}
		}
	};
</script>

<style lang="scss" scoped>
    #cover-opportunity
    {
        width: 100%;
        height: 400px;
        background-position: center;
        background-size: cover;
        margin-bottom: 24px;
        position: relative;
    }

    #cover-back-button
    {
        position: absolute;
        top: 50px;
        left: 10px;
        color: #fff;
        z-index: 200;
        i
        {
            font-size: 48px;
        }
        cursor: pointer;
    }

    #cover-overlay
    {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.75);
        z-index: 100;
        padding-top: 100px;
        text-align: center;
        color: #fff;

        .title
        {
            font-family: PierSansBold, sans-serif;
            font-size: 34px;
            margin-bottom: 8px;
        }

        .social
        {
            margin-bottom: 32px;
        }
        .deadline
        {
            font-size: 14px;
        }

        i
        {
            vertical-align: middle;
            position: relative;
            top: -2px;
        }
    }

    #cover-overlay /deep/
    {
        a.shiny-btn
        {
            width: 200px;
            border-radius: 4px;
            margin: 0 auto 16px auto;
        }

        .sweet-modal
        {
            color: #000;
        }
    }
</style>