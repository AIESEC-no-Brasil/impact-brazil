<template>
    <div id="app">
        <Navigation/>
        <transition name="fade">
            <keep-alive include="Opportunities">
                <router-view v-if="!$store.state.pageLoading"/>
                <div class="fullscreen-loading" v-else>
                    <Loading center dark/>
                </div>
            </keep-alive>
        </transition>
        <Footer v-if="!$store.state.showingQuestions"/>

        <User/>
        <Errors/>
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

    .fullscreen-loading
    {
        margin: 40vh 0 40vh 0;
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
</style>
