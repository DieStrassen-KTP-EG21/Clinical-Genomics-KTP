import axios from "axios";
import store from "../store";
import router from "../router/index";
export default {
  namespaced: true,
  state: {
    status: "",
    token: localStorage.getItem("access-token") || "",
    resendtoken: localStorage.getItem("X-token") || "",
    User: {},
    msg:""
  },
  mutations: {
    auth_request(state) {
      state.status = "loading";
    },
    auth_success(state, { token, user }) {
      state.status = "success";
      state.token = token;
      state.User = user;
    },
    auth_error(state, err_msg) {
      state.status = err_msg;
    },
    logout(state) {
      state.status = "";
      state.token = "";
      state.User = {};
    }
  },
  actions: {
    get_user({ commit }, flag) {
      const token = localStorage.getItem("access-token");
      console.log(token);
      axios.defaults.headers.common["x-access-token"] = token;
      commit("auth_request");
      axios
        .get("https://genomicanalyzer.herokuapp.com/profile")
        .then((response) => {
          console.log(response);
          const user = response.data;
          console.log(user);
          commit("auth_success", { token, user });
          localStorage.setItem("type", user.EmployeeType);
          console.log(localStorage);
          if (flag) router.replace("/");
        })
        .catch((error) => {
          commit("auth_error", "user_err");
          localStorage.removeItem("access-token");
          console.log(error);
        });
    },
    login({ commit }, user) {
      console.log("hi iam in log in");
      console.log(user);
      commit("auth_request");
      axios
        .post("https://genomicanalyzer.herokuapp.com/login", {
          Password: user.Password,
          Name: user.Name
        })
        .then((response) => {
          console.log(response);
          const token = response.data.access_token;
          console.log(token);
          localStorage.setItem("access-token", token);
          axios.defaults.headers.common["access-token"] = token;
          store.dispatch("Authorization/get_user", true);
        })
        .catch((error) => {
          console.log(error);
          commit("auth_error", "not user by this email");
          localStorage.removeItem("access-token");
        });
    },
    logout({ commit }) {
      commit("logout");
        localStorage.removeItem("access-token");
        delete axios.defaults.headers.common["access-token"];
        console.log(localStorage);
        router.replace("/");
    }
  },
  getters: {
    Username: (state) => state.User.displayName,
    GetStatus: (state) => state.status,
    user: (state) => state.User,
    userid: (state) => state.User._id,
    usertype: (state) => state.User.EmployeeType,
  },
};
