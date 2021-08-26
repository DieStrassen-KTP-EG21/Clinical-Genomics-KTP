 import axios from "axios";
 import router from "../router/index";
export default {
  namespaced: true,
  state: {
    Patients: [],
    Patient:{},
    DiseaseScors:{"Alenquer virus segment L, complete sequence": "40.0",
    "Alenquer virus segment M, complete sequence": "40.0",
    "Alenquer virus segment S, complete sequence": "40.0",
    "HIV-1 isolate Pat3 from Russia envelope glycoprotein (env) gene, partial cds": "40.0",
    "HIV-1 isolate PatT57day1clone_067_R envelope glycoprotein (env) gene, partial cds": "40.0",
    "HIV-1 isolate Y03911_21.2014-10-20 from USA nef protein (nef) gene, complete cds": "40.0",
    "Influenza A virus (A/California/07/2009(H1N1)) segment 4 hemagglutinin (HA) gene, complete cds": "40.0",
    "Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome": "40.0",
    "Severe fever with thrombocytopenia syndrome virus strain HNXH segment L, complete sequence": "40.0",
    "Severe fever with thrombocytopenia syndrome virus strain HNXH segment M, complete sequence": "40.0",
    "Severe fever with thrombocytopenia syndrome virus strain HNXH segment S, complete sequence": "40.0",
    "Zaire ebolavirus isolate Ebolavirus/H.sapiens-wt/COD/2020/Ituri-BEN55665, partial genome": "40.0"},
    ResultDisease:"Alenquer virus segment L, complete sequence",
    ResultDiseaseScore:40.0,
    message:"Comparison Done Successfully",
    success:true
  },
  mutations: {
    setReport(state,data)
    {
    state.DiseaseScors=data["Disease Scores"];
    state.ResultDisease=data["ResultDisease"];
    state.ResultDiseaseScore=data["ResultDiseaseScore"];
    state.message=data["message"];
    state.success=data["success"];
    }
  
  },
  actions: {
    analayzer({ commit }) {
      router.replace("/Report");
      axios
        .get("https://genomicanalyzer.herokuapp.com/analyzer")
        .then((response) => {
          console.log(response);
          commit("setReport",response.data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    // login({ commit }, user) {
    //   console.log("hi iam in log in");
    //   console.log(user);
    //   commit("auth_request");
    //   axios
    //     .post("https://genomicanalyzer.herokuapp.com/login", {
    //       Password: user.Password,
    //       Name: user.Name
    //     })
    //     .then((response) => {
    //       console.log(response);
    //       const token = response.data.access_token;
    //       console.log(token);
    //       localStorage.setItem("access-token", token);
    //       axios.defaults.headers.common["access-token"] = token;
    //       store.dispatch("Authorization/get_user", true);
    //     })
    //     .catch((error) => {
    //       console.log(error);
    //       commit("auth_error", "not user by this email");
    //       localStorage.removeItem("access-token");
    //     });
    // }
  },
  getters: {
    Patients: (state) => state.Patients,
    Patient: (state) => state.Patient,
    DiseaseScors:(state) => state.DiseaseScors,
    ResultDisease:(state) => state.ResultDisease,
    ResultDiseaseScore:(state) => state.ResultDiseaseScore,
    message:(state) => state.message,
    success:(state) => state.success
  },
};
