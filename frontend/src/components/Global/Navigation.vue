<template>
    <div id="nav"
         :class="isTopOfPage ? 'no-background' : ''">
        <img src="../../assets/logonav.png" title="Impact Brazil"/>

        <nav :class="hidden ? 'collapsed' : 'open'">
            <ul>
                <li class="mobile-only">
                    <a class="close-button" @click="hidden = true">
                        <i class="material-icons">close</i>
                    </a>
                </li>
                <li>
                    <router-link to="/" exact>Home</router-link>
                </li>
                <li>
                    <router-link :to="opportunityLink">Opportunities</router-link>
                </li>
                <li>
                    <router-link to="/projects">Projects</router-link>
                </li>
                <li>
                    <router-link to="/cities">Cities</router-link>
                </li>
                <li>
                    <router-link to="/about">About</router-link>
                </li>
                <li>
                    <router-link to="/contact">Contact</router-link>
                </li>
                <li>
                    <a @click="showLoginBox" v-if="!loggedIn">Login</a>
                    <a @click="logout" v-else>Logout</a>
                </li>
            </ul>
        </nav>
        <a @click="hidden = false" class="mobile-only open-button">
            <i class="material-icons">menu</i>
        </a>
    </div>
</template>

<script>
	import queryString from 'query-string';

	export default {
		name:     "Navigation",
		data()
		{
			return {
				isTopOfPage: true,
				hidden:      true,
			};
		},
		computed: {
			opportunityLink()
			{
				return "/opportunities?" + queryString.stringify(this.$store.state.optquery);
			},
			loggedIn()
			{
				return typeof this.$session.get('loggedIn') === "undefined" ? false : this.$session.get('loggedIn');
			}
		},
		methods:  {
			handleMenubarVisibility()
			{
				this.isTopOfPage = (this.$route.name === "home" || this.$route.name === "opportunity") && window.scrollY === 0;
			},
			showLoginBox()
			{
				this.$root.$emit('login');
			},
			logout()
			{
                this.$session.set('loggedIn', false);
                this.$session.set('accessToken', "");
                window.location.reload();
			}
		},
		created()
		{
			window.addEventListener('scroll', this.handleMenubarVisibility);
		},
		destroyed()
		{
			window.removeEventListener('scroll', this.handleMenubarVisibility);
		},
		watch:    {
			$route(to, from)
			{
				this.handleMenubarVisibility();
			}
		}
	};
</script>

<style lang="scss" scoped>
    @import "../../../node_modules/bootstrap/scss/functions";
    @import "../../../node_modules/bootstrap/scss/variables";
    @import "../../../node_modules/bootstrap/scss/mixins/breakpoints";
    @import "../../assets/_colors";

    #nav
    {
        height: 38px;
        max-height: 50px;
        position: fixed;
        width: 100%;
        z-index: 1000;
        background-color: $ib-blue-dk;
        transition: background-color 0.5s;
        font-family: PierSansLight, sans-serif;

        img
        {
            margin: 8px 0 0 16px;
            height: 24px;
            float: left;
        }

        nav
        {
            float: right;
            margin-right: 8px;
        }
        nav ul li
        {
            display: inline-block;
            list-style-type: none;
        }

        a
        {
            font-size: 14px;
            display: block;
            text-decoration: none;
            padding: 5px 10px;
            margin: 4px 2px;
            color: #fff;
            border-radius: 4px;
            transition: all 0.3s;
            cursor: pointer;
        }

        a:hover
        {
            box-shadow: inset 0 0 0 1px #fff;
        }

        a.router-link-active
        {
            background-color: #fff;
            color: $ib-blue-dk;
        }
    }

    @include media-breakpoint-down(sm)
    {
        nav.collapsed
        {
            right: -233px;
        }
        nav
        {
            position: fixed;
            right: 0;
            width: 232px;
            height: 100%;
            padding: 0 16px;
            margin-right: 0 !important;
            background-color: $ib-blue-dk;
            transition: right ease-in-out 0.5s;
        }
        nav ul li
        {
            display: block !important;
        }
        a
        {
            font-size: 16px !important;
            margin: 16px 2px !important;
        }

    }

    .open-button
    {
        float: right;
        padding: 2px !important;
        margin: 6px 10px !important;
    }

    .close-button
    {
        text-align: right;
    }

    .mobile-only
    {
        @include media-breakpoint-up(md)
        {
            display: none !important;
        }
    }

    .mobile-only:hover, .mobile-only a:hover
    {
        box-shadow: none !important;
    }

    .no-background
    {
        background-color: transparent !important;

        a
        {
            color: #fff !important;
            background-color: transparent !important;
        }
    }
</style>