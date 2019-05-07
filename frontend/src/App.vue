<template>
    <div id="app">
        <Navigation/>
        <transition name="fade">
            <keep-alive include="Opportunities">
                <router-view v-if="!$store.state.pageLoading"/>
                <Loading v-else fullscreen center dark/>
            </keep-alive>
        </transition>
        <Footer v-if="!$store.state.showingQuestions"/>

        <User/>
        <Errors/>

        <div id='content-snackbar'>
          <div id="snackbar">
            This website uses cookies to ensure you get the best experience in our website.
            <a href="./static/cookies_policy.pdf" target="_blank"><u>Learn more</u></a>
            <button type="button" class="btn btn-default btn-transparent" v-on:click="hideSnackBar">Ok!</button>
          </div>
        </div>
    </div>
</template>

<script>
	import Navigation from './components/Global/Navigation.vue';
	import Errors from './components/Global/Errors.vue';
	import User from './components/Global/User.vue';
	import Footer from './components/Global/Footer.vue';
	import Loading from './components/Loading.vue';

	import 'bootstrap/dist/css/bootstrap.css';
	import 'bootstrap-vue/dist/bootstrap-vue.css';

	export default {
		name:       "app",
		components: {
			Navigation,
			Errors,
			Footer,
			User,
			Loading,
		},
        methods: {
          hideSnackBar: function (event) {
            var x = document.getElementById("snackbar");
            x.className = "";
            localStorage.acceptedCookiesPolicy = true;
          },
          showSnackBar: function(event) {
            var x = document.getElementById("snackbar");
            x.className = "show";
          }
        },
        mounted(){
          if(!localStorage.acceptedCookiesPolicy){
            this.showSnackBar();
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
        font-display: swap;
    }

    @font-face
    {
        font-family: PierSansLight;
        src: local('Pier Sans Light'), url('./assets/PierSans-Light.otf');
        font-display: swap;
    }

    @font-face
    {
        font-family: PierSansBold;
        src: local('Pier Sans Bold'), url('./assets/PierSans-Bold.otf');
        font-display: swap;
    }

    *
    {
        margin: 0;
        padding: 0;
    }

    b
    {
        font-family: PierSansBold, sans-serif;
        padding: 0 4px 0 0;
    }

    body, html
    {
        margin: 0;
        padding: 0;
    }

    body
    {
        background-color: #f5f5f5;
        position: relative;
        height: 100%;
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

    .orange-button
    {
        margin: 4px 0;
        padding: 8px 16px;

        cursor: pointer;
        background-color: $ib-orange-dk;
        display: inline-block;
        font-family: PierSansBold, sans-serif;
        color: #fff !important;
        font-size: 24px;
        text-decoration: none;
        transition: background-color 0.3s;
    }

    .orange-button:hover
    {
        color: #fff;
        text-decoration: none;
        background-color: $ib-orange-lt;
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

    #content-snackbar {
    width: 100%;
    position: fixed;
    bottom: 0;
    left: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 99999;

    #snackbar {
        visibility: hidden;
        /* Hidden by default. Visible on click */
        min-width: 250px;
        /* Set a default minimum width */
        margin: auto;
        background-color: #333;
        /* Black background color */
        color: #fff;
        /* White text color */
        text-align: center;
        /* Centered text */
        border-radius: 0.25rem;
        /* Rounded borders */
        padding: 5px 15px;
        /* Padding */
        position: relative;
        /* Sit on top of the screen */
        display: flex;
        align-items: center;

        /* Add a z-index if needed */
        &.show {
            visibility: visible;
            /* Show the snackbar */
            /* Add animation: Take 0.5 seconds to fade in and out the snackbar. 
      However, delay the fade out process for 2.5 seconds */
            -webkit-animation: fadein 0.5s, fadeout 0.5s 2.5s;
            animation: fadein 0.5s, fadeout 0.5s 2.5s;
        }

        button {
            margin-left: 20px;
            padding: 5px 15px;
            font-size: 12px;
            line-height: 15px;
        }

        a {
            margin-left: 10px;
        }
    }
}


/* Animations to fade the snackbar in and out */
@-webkit-keyframes fadein {
    from {
        bottom: 0;
        opacity: 0;
    }

    to {

        opacity: 1;
    }
}

@keyframes fadein {
    from {
        bottom: 0;
        opacity: 0;
    }

    to {
        opacity: 1;
    }
}

@-webkit-keyframes fadeout {
    from {
        opacity: 1;
    }

    to {
        bottom: 0;
        opacity: 0;
    }
}

@keyframes fadeout {
    from {
        opacity: 1;
    }

    to {
        bottom: 0;
        opacity: 0;
    }
}

@media screen and (max-width: 991px) {
    #content-snackbar {
        #snackbar {
            display: block;
            padding: 10px;

            button {
                margin-top: 10px;
            }
        }
    }
}

.btn-transparent {
  background-color: #333;
  color: white;
  border: 1px solid #fff;
}

.btn-transparent:hover {
  background-color: rgba(255, 255, 255, 0.9);
  color: black;
}

</style>
