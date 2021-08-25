import axios from "axios";
import store from "../store";
export default {
  namespaced: true,
  actions: {
      addstaff({ commit }, staff) {
        axios.defaults.headers.common["access-token"] = localStorage.getItem("access-token");
        axios.post("https://genomicanalyzer.herokuapp.com/signup", {
          Name: staff.Name,
          Password: staff.Password,
          Gender: staff.Gender,
          Email: staff.Email,
          EmployeeType: staff.EmployeeType,
          Address: staff.Address,
          Phone: staff.Phone,
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
    }
  }
};
