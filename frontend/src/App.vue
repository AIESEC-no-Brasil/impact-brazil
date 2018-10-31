<template>
    <div id="app">
        <div id="nav"
             :class="isTopOfPage ? 'no-background' : ''">
            <img src="./assets/logonav.png" title="Impact Brazil"/>

            <nav>
                <ul>
                    <li>
                        <router-link to="/" exact>Home</router-link>
                    </li>
                    <li>
                        <router-link :to="opportunityLink">Opportunities</router-link>
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
                </ul>
            </nav>
        </div>

        <transition name="fade">
            <keep-alive include="Opportunities">
                <router-view/>
            </keep-alive>
        </transition>
        <div id="footer" style="text-align: center;"><br><br>
            This website is &copy; AIESEC in Brazil. Don't do shady stuff.
        </div>
        <SweetModal title="Oops!"
                    icon="error"
                    hide-close-button
                    blocking
                    overlay-theme="dark"
                    modal-theme="light"
                    ref="reloaderror">
            We were unable to load this page. Check your internet connection and try again.

            <button class="retry"
                    @click="reloadPage()">
                Try Again
            </button>
        </SweetModal>
        <SweetModal title="Oops!"
                    icon="error"
                    hide-close-button
                    blocking
                    overlay-theme="dark"
                    modal-theme="light"
                    ref="fatalerror">
            {{fatalError}}
            <br>
            <button class="retry"
                    @click="goHome()">
                Ok
            </button>
        </SweetModal>
    </div>
</template>

<script>
	import {SweetModal} from 'sweet-modal-vue';
	import 'bootstrap/dist/css/bootstrap.css';
	import 'bootstrap-vue/dist/bootstrap-vue.css';
	import queryString from 'query-string';

	export default {
		name:       "app",
		components: {
			SweetModal,
		},
		data()
		{
			return {
				isTopOfPage:     true,
				opportunityOpts: {},
				fatalError:      "Something went wrong while loading this page.",
			};
		},
		computed:   {
			opportunityLink()
			{
				return "/opportunities?" + queryString.stringify(this.$store.state.optquery);
			}
		},
		methods:    {
			reloadPage()
			{
				window.location.reload();
			},
			goHome()
			{
				window.location = "/";
			},
			handleMenubarVisibility()
			{
				this.isTopOfPage = (this.$route.name === "home" || this.$route.name === "opportunity") && window.scrollY === 0;
			}
		},
		created()
		{
			this.$root.$on('error', () => {
				setTimeout(() => {
					this.$refs.reloaderror.open();
				}, 1000);
			});
			this.$root.$on('fatal', (text) => {
				setTimeout(() => {
					if (typeof text !== undefined)
						this.fatalError = text;

					this.$refs.fatalerror.open();
				}, 1000);
			});
			window.addEventListener('scroll', this.handleMenubarVisibility);

		},
		destroyed()
		{
			window.removeEventListener('scroll', this.handleMenubarVisibility);
		},
		watch:      {
			$route(to, from)
			{
				this.handleMenubarVisibility();
			}
		}
	};
</script>

<style lang="scss">
    @import "./assets/_colors";

    @font-face
    {
        font-family: PierSans;
        src: local('Pier Sans Regular'), url('./assets/PierSans-Regular.otf');
    }

    @font-face
    {
        font-family: PierSansLight;
        src: local('Pier Sans Light'), url('./assets/PierSans-Light.otf');
    }

    @font-face
    {
        font-family: PierSansBold;
        src: local('Pier Sans Bold'), url('./assets/PierSans-Bold.otf');
    }

    *
    {
        margin: 0;
        padding: 0;
    }

    b
    {
        font-family: PierSansBold, sans-serif;
        padding: 0 4px;
    }

    body, html
    {
        margin: 0;
        padding: 0;
    }

    body
    {
        background-color: #f5f5f5;
    }

    html
    {
        // The "questions" modal prevents scrolling, but we don't want the scrollbar to disappear
        overflow-y: scroll;
    }

    .section
    {
        padding: 44px 24px;
        font-family: PierSansLight, sans-serif;
        color: #353535;
    }

    .fade-enter-active, .fade-leave-active
    {
        transition: opacity .2s;
    }

    .fade-leave-active
    {
        /*transition-delay: 1s;*/
    }

    .fade-enter, .fade-leave-to
    {
        opacity: 0;
    }

    .retry
    {
        border: 1px solid #f44336;
        padding: 8px;
        font-family: PierSans, sans-serif;
        margin-top: 20px;
        font-size: 18px;
        background: transparent;
        color: #f44336;
        cursor: pointer;
        transition: all 0.3s;
    }

    .retry:hover
    {
        border: 1px solid #000;
        color: #000;
    }

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

            @media (max-aspect-ratio: 16/9)
            {
                display: none;
            }
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
