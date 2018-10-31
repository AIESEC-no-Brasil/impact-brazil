<template>
    <div>
        <div id="cover-opportunity" :style="backgroundStyle">
            <div id="cover-overlay">
                <div class="title">{{opportunity.title}}</div>
                <div class="location"><i class="material-icons">location_on</i> {{opportunity.location}}</div>
                <OpportunityApplyButton v-if="daysLeft >= 0"/>
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
	import OpportunityApplyButton from "../Opportunities/OpportunityApplyButton.vue";

	export default {
		name:       "OpportunityCover",
		components: {
			OpportunityApplyButton
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

    #cover-overlay
    {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.75);
        z-index: 100;
        padding-top: 120px;
        text-align: center;
        color: #fff;

        .title
        {
            font-family: PierSansBold, sans-serif;
            font-size: 34px;
            margin-bottom: 8px;
        }

        .location
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
    }
</style>