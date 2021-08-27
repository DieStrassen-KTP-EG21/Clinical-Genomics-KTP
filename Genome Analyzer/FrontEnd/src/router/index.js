import Vue from "vue";
import VueRouter from "vue-router";
import store from "../store";
import Home from "../views/Home.vue";
import Nurse from "../views/Nurse.vue";
import Login from "../views/Login.vue";
import Admin from "../views/Admin.vue";
import Doctor from "../views/Doctor.vue";
import AddStaff from "../views/AddStaff.vue";
import Report from "../views/Report.vue";
import Element from 'element-ui'

Vue.use(Element)

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
  {
    path: "/AddStaff",
    name: "AddStaff",
    component: AddStaff,
  },
  {
    path: "/Admin",
    name: "Admin",
    component: Admin,
  },
  {
    path: "/Doctor",
    name: "Doctor",
    component: Doctor,
  },
  {
    path: "/Report",
    name: "Report",
    component: Report,
  },
  
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
  store,
});


router.beforeEach((to, from, next) => {
  console.log(store.getters["Authorization/GetStatus"]);
  if (to.matched.some((record) => record.meta.isLogged)) {
    if (store.getters["Authorization/GetStatus"] == "success") {
      next("/");
      return;
    }
  } else {
    next();
  }
});


export default router;