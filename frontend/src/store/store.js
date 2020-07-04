import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

const store = new Vuex.Store({
    state: {
        allSongRecommendations: null,
    },
    getters: {
        getAllSongRecommendations(state) {
            return state.allSongRecommendations;
        }
    },
    mutations: {
        setAllSongRecommendations(state, payload) {
            state.allSongRecommendations = payload;
        }
    },
    actions: {
        changeAllSongRecommendations({ commit }, payload) {
            commit("setAllSongRecommendations", payload);
        }
    }
});

export default store;