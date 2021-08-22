import Vue from "vue";
import VueRouter from "vue-router";
import store from "../store";
import Home from "../views/Home.vue";
import Nurse from "../views/Nurse.vue";
import Login from "../views/Login.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/Nurse",
    name: "Nurse",
    component: Nurse,
  },
  {
    path: "/Login",
    name: "Login",
    component: Login,
  },
  
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
  store,
});


export default router;