import axios from "axios";
export default {
  namespaced: true,
  state: {
    msg:""
  },
  mutations: {
    auth(state,res) {
      state.msg=res;
    },
  },
  actions: {
      addstaff({commit}, staff) {
        axios.defaults.headers.common["x-access-token"] = localStorage.getItem("access-token");
        console.log(localStorage.getItem("access-token"));
        console.log(staff);
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
          commit("auth","success");
        })
        .catch(err=> {
          console.log(err);
          commit("auth","Some Thing wrong , Please try other user Name and all fied check is it not empty");
        });
    }
  }
  ,
  getters: {
    msg: (state) => state.msg,
  },
};
