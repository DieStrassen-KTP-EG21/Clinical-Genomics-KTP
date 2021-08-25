import Vue from "vue";
import Vuex from "vuex";
import Authorization from "../modules/Authorization";
import Staff from "../modules/Staff";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    Authorization,
    Staff
 
  },
});