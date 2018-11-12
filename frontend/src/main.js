import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import VueSession from 'vue-session';
import {config} from "./config";

Vue.use(VueSession, {persist: true});

// configure router here, since we need both $store and $router
router.beforeEach((to, from, next) => {
	store.commit('pageLoading');
	next();
});

router.afterEach(() => {
	store.commit('pageLoaded');
});

// "set title" mixin
Vue.mixin({
	methods: {
		setTitle(title = false)
		{
			document.title = title ? (title + " · " + config.websiteName) : config.websiteName;
		}
	}
});
Vue.config.productionTip = false;

new Vue({
	router,
	store,
	render: h => h(App)
}).$mount('#app');
