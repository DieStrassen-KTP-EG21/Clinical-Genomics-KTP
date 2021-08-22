import axios from "axios";
import store from "../store";
import router from "../router/index";
export default {
  namespaced: true,
  state: {
    status: "",
    token: localStorage.getItem("Authorization") || "",
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
      const token = localStorage.getItem("Authorization");
      console.log(token);
      axios.defaults.headers.common["Authorization"] = token;
      commit("auth_request");
      axios
        .get("http://localhost:3000/me")
        .then((response) => {
          console.log(response);
          const user = response.data.user;
          commit("auth_success", { token, user });
          localStorage.setItem("is-manager", user.type);
          if (flag) router.replace("/");
        })
        .catch((error) => {
          commit("auth_error", "user_err");
          localStorage.removeItem("Authorization");
          console.log(error);
        });
    },
    login({ commit }, user) {
      console.log(localStorage,"hi iam in log in");
      console.log(user);
      commit("auth_request");
      axios
        .post("http://localhost:3000/login", {
          password: user.password,
          email: user.email,
          type: user.type,
        })
        .then((response) => {
          const token = response.data.token;
          localStorage.setItem("Authorization", token);
          axios.defaults.headers.common["Authorization"] = token;
          store.dispatch("Authorization/get_user", true);
        })
        .catch((error) => {
          console.log(error);
          commit("auth_error", "not user by this email");
          localStorage.removeItem("Authorization");
        });
    },
    logout({ commit }) {
      commit("logout");
        localStorage.removeItem("X-token");
        localStorage.removeItem("Authorization");
        localStorage.removeItem("is-manager");
        delete axios.defaults.headers.common["Authorization"];
        router.replace("/");
    }
  },
  getters: {
    Username: (state) => state.User.displayName,
    GetStatus: (state) => state.status,
    user: (state) => state.User,
    userid: (state) => state.User._id,
    usertype: (state) => state.User.type,
  },
};
