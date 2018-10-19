import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';

Vue.use(Router);

export default new Router({
	mode:           'history',
	base:           process.env.BASE_URL,
	routes:         [
		{
			path:      '/',
			name:      'home',
			component: Home
		},
		{
			path:      '/opportunities',
			name:      'opportunities',
			component: () => import(/* webpackChunkName: "opportunities" */ './views/Opportunities.vue')
		}
		//{
		//	path:      '/about',
		//	name:      'about',
		//	// route level code-splitting
		//	// this generates a separate chunk (about.[hash].js) for this route
		//	// which is lazy-loaded when the route is visited.
		//	component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
		//}
	],
	scrollBehavior: (to, from, savedPosition) => {
		if (savedPosition)
			return savedPosition;
		else if (to.hash)
			return window.scrollTo({top: document.querySelector(to.hash).offsetTop, behavior: 'smooth'});
		else
			return window.scrollTo({top: 0, behavior: 'smooth'});
	}
});
