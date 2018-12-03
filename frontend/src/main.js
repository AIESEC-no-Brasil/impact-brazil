import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import VueSession from 'vue-session';
import {config} from "./config";
import vClickOutside from 'v-click-outside';
import VueAnalytics from 'vue-analytics';

Vue.use(VueSession, {persist: true});
Vue.use(vClickOutside);

Vue.use(VueAnalytics, {
	id: 'UA-130274379-1',
	router
});

// configure router here, since we need both $store and $router
router.beforeEach((to, from, next) => {
	store.commit('pageLoading');
	store.commit('cityPage', false);
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

//// "click outside" directive
//Vue.directive('click-outside', {
//	bind(el, binding, vnode)
//	{
//		this.event = event => vnode.$emit(binding.expression, event);
//		el.addEventListener('click', this.stopProp);
//		document.body.addEventListener('click', this.event);
//	},
//	unbind(el)
//	{
//		el.removeEventListener('click', this.stopProp);
//		document.body.removeEventListener('click', this.event);
//	},
//
//	stopProp(event)
//	{
//		event.stopPropagation();
//	}
//});

new Vue({
	router,
	store,
	render: h => h(App)
}).$mount('#app');
