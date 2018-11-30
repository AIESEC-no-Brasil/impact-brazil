import Vue from 'vue';
import App from './App.vue';
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
			component: () => import(/* webpackChunkName: "city" */ './views/Cities.vue'),
		},
		{
			path:      '/contact',
			name:      'contact',
			component: () => import('./views/Contact.vue')
		},
		{
			path:      '/searchtool/:prod',
			name:      'searchtool',
			component: () => import(/* webpackChunkName: "opportunities" */ './views/Searchtool.vue'),
		},
		{
			path:     '/gv',
			redirect: '/searchtool/1'
		},
		{
			path:     '/gv',
			redirect: '/searchtool/2'
		},
		{
			path:     '/gv',
			redirect: '/searchtool/5'
		},
		{
			path:      '/404',
			name:      '404',
			component: () => import('./views/Error404.vue')
		},
		{
			path:      '*',
			name:      'city',
			component: () => import(/* webpackChunkName: "city" */ './views/City.vue'),
		},
	],
	scrollBehavior: (to, from, savedPosition) => {
		if (savedPosition)
		{
			return new Promise(resolve => {
				setTimeout(() => {
					resolve(savedPosition);
				}, 250);
			});
		}
		else if (to.hash)
		{
			return {
				selector: to.hash
			};
		}
		else
		{
			return {x: 0, y: 0};
		}
	}
});
