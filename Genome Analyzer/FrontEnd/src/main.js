import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import "normalize.css";
import Vuelidate from "vuelidate";
import axios from "axios";
import ElementUI from 'element-ui';

Vue.use(ElementUI)

Vue.config.productionTip = false;
Vue.use(Vuelidate);
Vue.prototype.$http = axios;
var vm = new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");

global.vm = vm;
