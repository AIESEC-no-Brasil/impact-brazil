<template>
    <div class="section" id="opportunities">
        <div id="invite">Inviting <span>India</span> to Impact Brazil</div>
        <div id="ey-banner">
            <div></div>
        </div>
        <div id="options-menu">
            <div id="options-left">
                Showing <b>IT</b> opportunities for <b>Global Talent</b>
            </div>
            <div id="options-right">
                <b-dropdown id="timespan" variant="transparent" right size="sm" text="January 2019">
                    <b-dropdown-item>Global Volunteer</b-dropdown-item>
                    <b-dropdown-item>Global Talent</b-dropdown-item>
                    <b-dropdown-item>Global Entrepreneur</b-dropdown-item>
                </b-dropdown>
                <b-dropdown id="prog" variant="transparent" right size="sm" text="Global Talent">
                    <b-dropdown-item>Global Volunteer</b-dropdown-item>
                    <b-dropdown-item>Global Talent</b-dropdown-item>
                    <b-dropdown-item>Global Entrepreneur</b-dropdown-item>
                </b-dropdown>
                <b-dropdown id="subproductOrSdg" variant="transparent" right size="sm" text="IT">
                    <b-dropdown-item>Global Volunteer</b-dropdown-item>
                    <b-dropdown-item>Global Talent</b-dropdown-item>
                    <b-dropdown-item>Global Entrepreneur</b-dropdown-item>
                </b-dropdown>
            </div>
        </div>
        <div id="opportunities-list">
            <b-container fluid class="opportunity">
                <b-row>
                    <b-col cols="12" md="4" class="opportunity-image opportunity-card">
                        <div></div>
                    </b-col>
                    <b-col cols="12" md="8" class="opportunity-desc-col">
                        <b-container fluid class="ml-md-3 mt-3 mt-md-0 opportunity-desc opportunity-card">
                            <b-row>
                                <b-col cols="6">
                                    <div class="city">Florianópolis</div>
                                    <div class="title">Full Stack Developer</div>
                                    <div class="organization">Cedro Technologies</div>
                                </b-col>
                                <b-col cols="6" class="text-right">
                                    <div class="duration">Jan 15, 2019 &middot; 24 Weeks</div>
                                    <div class="apply">Apply &raquo;</div>
                                    <div class="host-title">Hosted by:</div>
                                    <div class="host-lc">AIESEC in Florianopolis</div>
                                </b-col>
                            </b-row>
                        </b-container>
                    </b-col>
                </b-row>
            </b-container>
        </div>
        <br><br><br><br>
        this is where oppportunities will occur
        Selection: {{potato.query}}
    </div>
</template>

<script>
	import bDropdown from 'bootstrap-vue/es/components/dropdown/dropdown';
	import bDropdownItem from 'bootstrap-vue/es/components/dropdown/dropdown-item';
	import bImg from 'bootstrap-vue/es/components/image/img';
	import bContainer from 'bootstrap-vue/es/components/layout/container';
	import bCol from 'bootstrap-vue/es/components/layout/col';
	import bRow from 'bootstrap-vue/es/components/layout/row';

	export default {
		name:       "Opportunities",
		components: {
			bDropdown,
			bDropdownItem,
			bImg,
			bContainer,
			bCol,
			bRow,
		},
		data()
		{
			return {
				potato: this.$route
			};
		}
	};
</script>

<style lang="scss" scoped>
    #invite
    {
        padding-top: 12px;
        text-align: center;

        span
        {
            font-size: 3em;
            padding: 0 4px;
            font-family: PierSansBold, sans-serif;
        }
    }

    #ey-banner
    {
        width: calc(100% + 48px);
        height: 300px;
        margin: 12px 0 24px -24px;
        padding: 0;

        cursor: pointer;

        background-attachment: fixed;
        background-position: center;
        background-repeat: no-repeat;
        background-size: cover;

        background-image: url('../assets/videothumbs/sample_ep.jpg');

        div
        {
            background-image: url('../assets/play-button.png');
            width: 150px;
            height: 150px;
            background-size: 100%;
            position: relative;
            top: 75px;
            margin: auto;
        }
    }

    #options-left
    {
        float: left;
    }

    #options-right
    {
        float: right;
    }

    #options-right /deep/
    {
        button
        {
            margin-left: 8px;
        }
    }

    #options-menu:after
    {
        content: "";
        clear: both;
        display: block;
    }

</style>

<style lang="scss">
    @import "~bootstrap/scss/functions";
    @import "~bootstrap/scss/variables";
    @import "~bootstrap/scss/mixins/breakpoints";
    @import "../assets/colors";

    #opportunities-list
    {
        margin-top: 24px;
    }

    .opportunity-card
    {
        border-radius: 4px;
        // box-shadow: offset-x offset-y blur spread color position
        box-shadow: 0 2px 6px 0 rgba(0, 0, 0, 0.3);

        @include media-breakpoint-down(md)

        {
            padding: 8px 15px;
        }
    }

    .opportunity-image
    {
        background: url('/static/videothumbs/sample_city.jpg') center;
        background-size: cover;
        height: 180px;
        max-height: 180px;
        cursor: pointer;

        div
        {
            background-image: url('../assets/play-button.png');
            width: 100px;
            height: 100px;
            background-size: 100%;
            position: relative;
            top: 50px;
            margin: auto;
        }
    }

    .opportunity-desc-col
    {
        @include media-breakpoint-down(md)
        {
            padding: 0;
        }
    }
    .opportunity-desc
    {
        @include media-breakpoint-up(md)
        {
            height: 180px;
            max-height: 180px;
        }

        .city
        {
            @include media-breakpoint-up(md)
            {
                font-size: 48px;
            }
            @include media-breakpoint-down(md)
            {
                font-size: 20px;
            }
            font-family: PierSansBold, sans-serif;
        }

        .title
        {
            @include media-breakpoint-up(md)
            {
                margin-top: 16px;
                line-height: 40px;
                font-size: 32px;
            }
            @include media-breakpoint-down(md)
            {
                font-size: 16px;
            }
            font-family: PierSans, sans-serif;
        }

        .organization
        {
            @include media-breakpoint-up(md)
            {
                font-size: 28px;
            }
            @include media-breakpoint-down(md)
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
                font-size: 12px;
            }
        }
        .apply
        {
            background-color: $ib-green-dk;
            color: #fff;
            display: inline-block;
            padding: 4px 12px;
            border-radius: 4px;
            transition: background-color 0.2s;
            cursor: pointer;

            @include media-breakpoint-up(md)
            {
                font-size: 48px;
            }
            @include media-breakpoint-down(md)
            {
                font-size: 20px;
            }
        }

        .apply:hover
        {
            background-color: $ib-green-lt;
        }

        .host-title
        {
            color: #686868;

            @include media-breakpoint-up(md)
            {
                font-size: 16px;
            }
            @include media-breakpoint-down(md)
            {
                display: none;
            }
        }
        .host-lc
        {
            color: #686868;

            @include media-breakpoint-up(md)
            {
                font-size: 20px;
            }
            @include media-breakpoint-down(md)
            {
                font-size: 12px;
            }
        }
    }
</style>