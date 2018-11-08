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
		},
		{
			path:      '/opportunity/:id',
			name:      'opportunity',
			component: () => import(/* webpackChunkName: "opportunities" */ './views/Opportunity.vue')
		},
		{
			path:      '/about',
			name:      'about',
			component: () => import('./views/About.vue')
		},
		{
			path:      '/projects',
			name:      'projects',
			component: () => import('./views/Projects.vue')
		},
		{
			path:      '/cities',
			name:      'cities',
			component: () => import('./views/Cities.vue'),
		},
		{
			path:      '/contact',
			name:      'contact',
			component: () => import('./views/Contact.vue')
		},
		{
			path:      '/404',
			name:      '404',
			component: () => import('./views/Error404.vue')
		},
		{
			path:     '*',
			redirect: '/404'
		},
	],
	scrollBehavior: (to, from, savedPosition) => {
		if (savedPosition)
			return savedPosition;
		else if (to.hash)
			return window.scrollTo({top: document.querySelector(to.hash).offsetTop, behavior: 'smooth'});
		//else
		//	return window.scrollTo({top: 0, behavior: 'smooth'});
	}
});
