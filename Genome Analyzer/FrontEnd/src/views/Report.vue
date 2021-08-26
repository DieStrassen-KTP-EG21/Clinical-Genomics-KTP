<template
  ><div>
    <div class="cont justify-content-center px-0 ">
      <HomeNavigation />
      <div class="re justify-content-center px-0 ">
       <h1>Report</h1>
       <h3>success --> {{success}}</h3>
       <h3> comparison done correctly or not ? {{message}}</h3>
      <br/>
     <p> Disease Scors ->{{ DiseaseScors}}</p>
     <br/>
      Result Disease -> {{ResultDisease}}
      <br/>
   ResultDiseaseScore -> {{ResultDiseaseScore}}
    <br/>
    <br/>
    <br/>
      <div class="sales" >
      <lineChart
        :chartdata="chartdataSales"
        :options="options"
      />
    </div>
    <br/>
    </div>
    </div>
  </div>
</template>

<script>
import HomeNavigation from "@/components/HomeNavigationBar.vue";
import LineChart from "../components/LineChart";
import { mapGetters } from "vuex";
export default {
  name: "Report",
  components: {
    HomeNavigation,
    LineChart,
  },
  data: function () {
    return {
      chartdataSales: {
        labels: [],
        datasets: [
          {
            backgroundColor: "rgba(192,160,91,0.6)",
            pointBackgroundColor: "#846b36",
            pointBorderColor: "#846b36",
            borderColor: ["#846b36"],
            borderWidth: 2,
          },
        ],
      },
      chartdataRate: {
        labels: [1, 2, 3, 4, 5],
        datasets: [
          {
            label: "Blossom Ratings",
            backgroundColor: "rgba(192,160,91,0.6)",
            borderColor: [
              "#846b36",
              "#846b36",
              "#846b36",
              "#846b36",
              "#846b36",
            ],
            borderWidth: 2,
          },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
      },
    };
  },
   computed: {
    ...mapGetters({
    DiseaseScors:"Patient/DiseaseScors",
    ResultDisease:"Patient/ResultDisease",
    ResultDiseaseScore:"Patient/ResultDiseaseScore",
    message:"Patient/message",
    success:"Patient/success",
    })
  }
};
</script>

<style scoped>
.cont {
  height: calc(200vh);
  background-color:rgb(133, 167, 187);;
}
.home {
  background-repeat: no-repeat;
  height: calc(70vh);
  width: 100%;
  background-position: center;
  background-size: 100% 100%;
  position: absolute;
}
h1{
text-decoration: underline;
color: rgb(12, 96, 102);
}
.re
{
  background-color: rgba(128, 173, 187, 0.432);
  width: 80%;
  margin-left: 10%;
}
</style>
