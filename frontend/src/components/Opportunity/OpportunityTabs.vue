<template>
    <div id="nav-opportunity">
        <!--<img src="../assets/logonav.png" title="Impact Brazil"/>-->
        <img v-if="opportunity"
             :src="'/static/images/products/'+opportunity.programme.short_name_display.toLowerCase()+'-logo-hd.png'"><br>
        <nav>
            <ul>
                <li class="">
                    <a @click="changeTab('overview')"
                       role="button"
                       :class="tab === 'overview' ? 'active-tab' : ''">
                        Overview
                    </a>
                </li>
                <li>
                    <a @click="changeTab('role')"
                       role="button"
                       :class="tab === 'role' ? 'active-tab' : ''">
                        Role
                    </a>
                </li>
                <li>
                    <a @click="changeTab('prerequisites')"
                       role="button"
                       :class="tab === 'prerequisites' ? 'active-tab' : ''">
                        Prerequisites
                    </a>
                </li>
                <li>
                    <a @click="changeTab('logistics')"
                       role="button"
                       :class="tab === 'logistics' ? 'active-tab' : ''">
                        Logistics
                    </a>
                </li>
                <li>
                    <a @click="changeTab('visa')"
                       role="button"
                       :class="tab === 'visa' ? 'active-tab' : ''">
                        Visa
                    </a>
                </li>
            </ul>
        </nav>
    </div>
</template>

<script>
	export default {
		name:    "OpportunityNav",
		props:   {
			opportunity: Object,
			tab:         {
				type:    String,
				default: 'overview'
			}
		},
		methods: {
			changeTab(tab)
			{
				this.$emit('change-tab', tab);
			}
		}
	};
</script>

<style lang="scss" scoped>
    @import "../../../node_modules/bootstrap/scss/functions";
    @import "../../../node_modules/bootstrap/scss/variables";
    @import "../../../node_modules/bootstrap/scss/mixins/breakpoints";
    @import "../../assets/_colors";

    #nav-opportunity
    {
        $border-color: #e4e4e4;
        @include media-breakpoint-down(sm)
        {
            border-bottom: 1px solid $border-color;
        }
        @include media-breakpoint-up(md)
        {
            border-right: 1px solid $border-color;
            padding-right: 16px;
        }
        width: 100%;
        height: 100%;
        transition: background-color 0.5s;
        font-family: PierSansLight, sans-serif;

        img
        {
            width: 99%;
            @include media-breakpoint-down(sm)
            {
                display: none;
            }
        }

        nav
        {
        }
        nav ul li
        {
            @include media-breakpoint-down(sm)
            {
                display: inline-block;
            }
            list-style-type: none;
        }

        a
        {
            font-size: 14px;
            display: block;
            text-decoration: none;

            @include media-breakpoint-down(sm)
            {
                padding: 4px 10px;
                margin: 2px 8px;
            }
            @include media-breakpoint-up(md)
            {
                padding: 10px 10px;
                margin: 8px 0;
            }
            color: #353535;
            border-radius: 4px;
            transition: all 0.3s;
            cursor: pointer;
        }

        a:hover
        {
            box-shadow: inset 0 0 0 1px #353535;
        }

        a.active-tab:hover
        {
            box-shadow: none !important;
        }

        a.active-tab
        {
            background-color: $ib-blue-dk;
            color: #fff;
        }
    }
</style>