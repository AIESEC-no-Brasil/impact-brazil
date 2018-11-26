import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
	state:     {
		// This is accessed by a bunch of components, so it's easier to just store it here
		showingQuestions: false,
		showingDropdown:  false,
		
		// We store these in $store because we don't want the opportunity page to ever reload
		options:         {},
		optquery:        {},
		optReloadQueued: {invite: false, list: false},
		
		// This is the global page loading variable, run before each router change
		pageLoading: false,
		
		// Since we need these on almost every page, it's better to put them in the store
		lists: {
			entities:      [],
			products:      [],
			sdgs:          [],
			subproductsGT: [],
			subproductsGE: [],
			lcs:           [],
		},
	},
	getters:   {
		showingQuestions: state => state.showingQuestions,
		getList:          state => list => state.lists[list],
	},
	mutations: {
		showingQuestions: (state, sQ) => state.showingQuestions = sQ,
		showingDropdown:  (state, sD) => state.showingDropdown = sD,
		options:          (state, options) => state.options = options,
		optquery:         (state, optquery) => state.optquery = optquery,
		queueOptReload:   state => state.optReloadQueued = {invite: true, list: true},
		inviteLoaded:     state => state.optReloadQueued.invite = false,
		listLoaded:       state => state.optReloadQueued.list = false,
		pageLoading:      state => state.pageLoading = true,
		pageLoaded:       state => state.pageLoading = false,
		setList:          (state, payload) => state.lists[payload.list] = payload.arr,
	}
});