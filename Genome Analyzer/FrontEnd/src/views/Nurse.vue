<template>
  <div>
    <div class="cont">
      <HomeNavigation />
      <div class="background">
        <h1>Upload Patient's Data</h1>
        <form class="row gy-2 gx-3 align-items-center">
          <div class="col-auto">
            <label class="visually-hidden">Name</label>
            <input
              type="text"
              v-model="name"
              class="form-control"
              id="autoSizingInput"
              placeholder="Patient Name"
            />
          </div>
          <div class="col-auto">
            <label class="visually-hidden">ID</label>
            <input
              type="number"
              v-model="ID"
              class="form-control"
              id="autoSizingInput"
              placeholder="ID"
            />
          </div>
          <div class="col-auto">
            <label class="visually-hidden">DNA</label>
            <input
              type="text"
              v-model="DNA"
              class="form-control"
              id="autoSizingInput"
              placeholder="DNA"
            />
          </div>

          <div class="col-auto">
            <button @click="AddPatient" type="submit" class="btn btn-primary">
              Submit
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import HomeNavigation from "@/components/HomeNavigationBar.vue";
export default {
  name: "Nurse",
  components: {
    HomeNavigation,
  },
  data() {
    return {
      name: "",
      ID: "",
      DNA: "",
    };
  },
  methods: {
    AddPatient(e) {
      const newPatient = {
        name: this.name,
        ID: this.ID,
        DNA: this.DNA,
      };
      e.preventDefault();
      console.log(newPatient);
      this.name = "";
      this.ID = "";
      this.DNA = "";
    },
  },
};
</script>

<style scoped>
.cont {
  background-image: url("../assets/Nurse-with-chart.jpg");
}
.cont {
  background-repeat: no-repeat;
  height: calc(97vh);
  width: 100%;
  background-position: center;
  background-size: 100% 100%;
  position: absolute;
}
.col-auto {
  margin: 20px auto;
}
.background
{
  background-color: rgba(139, 138, 138, 0.507);
  border-radius: 20px;
}
</style>
