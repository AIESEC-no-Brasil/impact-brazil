<template>
    <b-container fluid class="opportunity">
        <b-row>
            <b-col cols="12" md="4" class="opportunity-image opportunity-card"
                   @mousedown="showVideo(opp.lc.city.video_link)"
                   :style="oppVideoThumb">
                <div></div>
            </b-col>
            <b-col cols="12" md="8" class="opportunity-desc-col">
                <b-container fluid class="ml-md-3 opportunity-desc opportunity-card">
                    <b-row>
                        <b-col cols="12" md="8">
                            <div class="city">{{opp.lc.city.name}}</div>
                            <div class="title text-truncate" :title="opp.title">{{opp.title}}</div>
                            <div class="organization text-truncate" :title="opp.organization_name">
                                {{opp.organization_name}}
                            </div>
                            <div class="duration">
                                {{opp.start_date}}
                                &middot; {{opp.duration}} Weeks
                                <span v-if="opp.standards_delivery">
                                    &middot;
                                    <i class="material-icons star star-full"
                                       v-for="rating in opp.standards_delivery.rating"
                                       :key="rating">star</i>
                                    <i class="material-icons star star-empty"
                                       v-for="rating in 5-opp.standards_delivery.rating"
                                       :key="rating">star_border</i>
                                    from {{opp.standards_delivery.responses}} responses
                                </span>
                            </div>
                        </b-col>
                        <b-col cols="12" md="4">
                            <b-row no-gutters>
                                <b-col cols="12" class="order-2 order-md-0">
                                    <OpportunityApplyButton :id="opp.gis_id"
                                                            :response-time="opp.response_time"/>
                                </b-col>
                                <b-col cols="0" md="12" class="order-0 order-md-1">
                                    <div class="host-title">Hosted by:</div>
                                </b-col>
                                <b-col cols="12" md="12" class="order-1 order-md-2">
                                    <div class="host-lc text-truncate" :title="'AIESEC in ' +opp.lc.reference_name">
                                        AIESEC in {{opp.lc.reference_name}}
                                    </div>
                                </b-col>
                            </b-row>
                        </b-col>
                    </b-row>
                </b-container>
            </b-col>
        </b-row>
    </b-container>
</template>

<script>
	import OpportunityApplyButton from './OpportunityApplyButton';
	import bContainer from 'bootstrap-vue/es/components/layout/container';
	import bCol from 'bootstrap-vue/es/components/layout/col';
	import bRow from 'bootstrap-vue/es/components/layout/row';
	import {config} from '../../config';

	export default {
		name:       "OpportunityCard",
		components: {
			bCol,
			bRow,
			bContainer,
			OpportunityApplyButton,
		},
		props:      {
			opp: Object,
		},
		data()
		{
			return {
				oppVideoThumb: {
					backgroundImage: "url('" + config.videos.lcThumbDir + (this.opp.lc.city.thumbnail === "" ? config.videos.defaultLCThumb : this.opp.lc.city.thumbnail) + "')",
				}
			};
		},
		methods:    {
			showVideo(url)
			{
				this.$emit('show-video', url);
			}
		},
	};
</script>

<style lang="scss" scoped>
    @import "../../../node_modules/bootstrap/scss/functions";
    @import "../../../node_modules/bootstrap/scss/variables";
    @import "../../../node_modules/bootstrap/scss/mixins/breakpoints";
    @import "../../assets/colors";

    $box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.2);

    .opportunity
    {
        @include media-breakpoint-down(sm)
        {
            box-shadow: $box-shadow;
            border-radius: 4px;
        }
        margin-bottom: 32px;

    }

    .opportunity-card
    {
        // box-shadow: offset-x offset-y blur spread color position

        @include media-breakpoint-up(md)
        {
            border-radius: 4px;
            box-shadow: $box-shadow;
        }

        @include media-breakpoint-down(sm)
        {
            padding: 8px 15px;
        }

    }

    .opportunity-image
    {
        background-position: center;
        background-size: cover;
        height: 180px;
        max-height: 180px;
        cursor: pointer;

        div
        {
            background-image: url('../../assets/play-button.png');
            width: 100px;
            height: 100px;
            background-size: 100%;
            position: relative;
            top: 50px;
            margin: auto;
        }

        @include media-breakpoint-down(sm)
        {
            border-top-left-radius: 4px;
            border-top-right-radius: 4px;
        }
    }

    .opportunity-desc-col
    {
        @include media-breakpoint-down(sm)
        {
            padding: 0;
        }
    }

    .opportunity-desc
    {
        background-color: #fff;

        @include media-breakpoint-up(md)
        {
            height: 180px;
            max-height: 180px;
        }

        @include media-breakpoint-down(sm)
        {
            border-bottom-left-radius: 4px;
            border-bottom-right-radius: 4px;
        }

        .city
        {
            @include media-breakpoint-up(md)
            {
                font-size: 36px;
            }
            @include media-breakpoint-down(sm)
            {
                font-size: 20px;
            }
            font-family: PierSansBold, sans-serif;
        }

        .title
        {
            @include media-breakpoint-up(md)
            {
                margin-top: 10px;
                line-height: 30px;
                font-size: 24px;
            }
            @include media-breakpoint-down(sm)
            {
                font-size: 16px;
            }
            font-family: PierSans, sans-serif;
            white-space: nowrap;
        }

        .organization
        {
            @include media-breakpoint-up(md)
            {
                font-size: 24px;
            }
            @include media-breakpoint-down(sm)
            {
                font-size: 14px;
            }
            color: #686868;
            font-family: PierSansLight, sans-serif;
        }

        .duration
        {

            @include media-breakpoint-up(md)
            {
                margin-top: 12px;
                font-size: 20px;
            }
            @include media-breakpoint-down(md)
            {
                margin-top: 8px;
                font-size: 12px;
            }
        }

        .host-title
        {
            color: #686868;

            @include media-breakpoint-up(md)
            {
                font-size: 16px;
                text-align: right;
                line-height: 12px;
            }
            @include media-breakpoint-down(sm)
            {
                display: none;
                font-size: 12px;
            }
        }
        .host-lc
        {
            color: #686868;

            @include media-breakpoint-up(md)
            {
                font-size: 20px;
                text-align: right;
            }
            @include media-breakpoint-down(sm)
            {
                font-size: 12px;
            }
        }

        .star
        {
            vertical-align: middle;
            position: relative;
            top: -2px;
            letter-spacing: -4px;
        }

        .star-full
        {
            color: $ib-orange-dk;
        }
        .star-empty
        {
            color: #686868;
        }
    }
</style>