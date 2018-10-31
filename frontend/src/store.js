import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
	state:     {
		noVisa:          false,
		iAmFromBrazil:   false,
		options:         {},
		optquery:        {},
		optReloadQueued: {invite: false, list: false},
	},
	getters:   {},
	mutations: {
		noVisa:         (state, noVisa) => state.noVisa = noVisa,
		brazilian:      (state, brazilian) => state.iAmFromBrazil = brazilian,
		options:        (state, options) => state.options = options,
		optquery:       (state, optquery) => state.optquery = optquery,
		queueOptReload: state => state.optReloadQueued = {invite: true, list: true},
		inviteLoaded:   state => state.optReloadQueued.invite = false,
		listLoaded:     state => state.optReloadQueued.list = false,
	}
});