import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import VueSession from 'vue-session';

Vue.use(VueSession, {persist: true});

// configure router here, since we need both $store and $router
router.beforeEach((to, from, next) => {
	store.commit('pageLoading');
	next();
});

router.afterEach(() => {
	store.commit('pageLoaded');
});


Vue.config.productionTip = false;

new Vue({
	router,
	store,
	render: h => h(App)
}).$mount('#app');
