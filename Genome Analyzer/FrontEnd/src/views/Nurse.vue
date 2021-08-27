<template>
  <div>
    <div class="cont">
      <HomeNavigation />
      <div class="background">
        <h1>Upload Patient's Data</h1>
        <form class="row gy-2 gx-3 align-items-center">
          <div class="col-auto">
            <input
              type="text"
              v-model="Name"
              class="form-control"
              id="autoSizingInput"
              placeholder="Name"
            />
            <el-select
              class="form-control"
              v-model="Gender"
              placeholder="Gender"
            >
              <el-option
                id="opt"
                class="form-control"
                label="Male"
                value="Male"
              ></el-option>
              <el-option
                id="opt"
                class="form-control"
                label="Female"
                value="Female"
              ></el-option>
            </el-select>
            <input
              type="number"
              v-model="Phone"
              class="form-control"
              id="autoSizingInput"
              placeholder="Phone"
            />
            <input
              type="text"
              v-model="Address"
              class="form-control"
              id="autoSizingInput"
              placeholder="Address"
            />
            <input
              type="text"
              v-model="Sequence"
              class="form-control"
              id="autoSizingInput"
              placeholder="Sequence"
            />
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
      Name: "",
      Phone: "",
      Sequence: "",
      Gender: "",
      Address: "",
    };
  },
  methods: {
    AddPatient(e) {
      const newPatient = {
        Name: this.Name,
        Phone: this.Phone,
        Sequence: this.Sequence,
        Gender: this.Gender,
        Address: this.Address,
      };
      e.preventDefault();
      console.log(newPatient);
      this.Name = "";
      this.Phone = "";
      this.Sequence = "";
      this.Gender = "";
      this.Address = "";
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
.background {
  background-color: rgba(139, 138, 138, 0.507);
  border-radius: 20px;
}
button {
  margin-top: 20px;
}
#opt {
  cursor: pointer;
  margin-bottom: 0px;
}
input,.form-control
{
  margin-bottom: 10px;
}
</style>
