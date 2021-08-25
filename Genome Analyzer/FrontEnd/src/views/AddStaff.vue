<template>
  <div>
    <div class="cont">
      <HomeNavigation />
      <div>
        <h1>Add Staff</h1>
        <form class="row  align-items-center">
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
              type="text"
              v-model="EmployeeType"
              class="form-control"
              id="autoSizingInput"
              placeholder="EmployeeType"
            />
            <input
              type="number"
              v-model="ID"
              class="form-control"
              id="autoSizingInput"
              placeholder="ID"
            />
            <input
              type="text"
              v-model="Email"
              class="form-control"
              id="autoSizingInput"
              placeholder="Email"
            />
            <input
              type="number"
              v-model="Phone"
              class="form-control"
              id="autoSizingInput"
              placeholder="Phone"
            /><label class="visually-hidden">Password</label>
            <input
              type="text"
              v-model="Password"
              class="form-control"
              id="autoSizingInput"
              placeholder="Password"
            />
            <input
              type="text"
              v-model="Address"
              class="form-control"
              id="autoSizingInput"
              placeholder="Address"
            />
            <button @click="AddMember" type="submit" class="btn btn-primary">
              Add
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
  name: "AddStaff",
  components: {
    HomeNavigation,
  },
  data() {
    return {
      Name: "",
      ID: "",
      Password: "",
      Gender: "",
      Email: "",
      EmployeeType: "",
      Address: "",
      Phone: "",
    };
  },
  methods: {
    AddMember(e) {
      const newMember = {
        Name: this.Name,
        Password: this.Password,
        Gender: this.Gender,
        Email: this.Email,
        EmployeeType: this.EmployeeType,
        Address: this.Address,
        Phone: this.Phone,
      };
      console.log(newMember);
      this.$store.dispatch("Authorization/addstaff", newMember);
      e.preventDefault();
      this.Name = "";
      this.ID = "";
      this.Password = "";
      this.Gender = "";
      this.Email = "";
      this.EmployeeType = "";
      this.Address = "";
      this.Phone = "";
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
#opt {
  cursor: pointer;
}
button {
  margin-top: 20px;
}

</style>
