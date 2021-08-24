<template>
  <div>
    <div class="cont">
      <HomeNavigation />
      <div>
        <h1>Add a Patient</h1>
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
  height: calc(200vh);
  background-color: rgb(133, 167, 187);
}
.home {
  background-repeat: no-repeat;
  height: calc(70vh);
  width: 100%;
  background-position: center;
  background-size: 100% 100%;
  position: absolute;
}
.col-auto {
  margin: 20px auto;
}
</style>
