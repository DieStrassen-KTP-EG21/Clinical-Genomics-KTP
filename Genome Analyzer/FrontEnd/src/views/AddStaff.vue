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
          <el-select
              class="form-control"
              v-model="EmployeeType"
              placeholder="EmployeeType"
            >
              <el-option
                id="opt"
                class="form-control"
                label="DataManager"
                value="DataManager"
              ></el-option>
              <el-option
                id="opt"
                class="form-control"
                label="Doctor"
                value="Doctor"
              ></el-option>
               <el-option
                id="opt"
                class="form-control"
                label="Nurse"
                value="Nurse"
              ></el-option>

            </el-select>
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
    <p> hhhh{{msg}}</p>
  </div>
</template>

<script>
import HomeNavigation from "@/components/HomeNavigationBar.vue";
import { mapGetters } from "vuex";
export default {
  name: "AddStaff",
  components: {
    HomeNavigation,
  },
  data() {
    return {
      Name: "",
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
      this.$store.dispatch("Staff/addstaff", newMember);
      e.preventDefault();
      this.Name = "";
      this.Password = "";
      this.Gender = "";
      this.Email = "";
      this.EmployeeType = "";
      this.Address = "";
      this.Phone = "";
    },
  },
   computed: {
    ...mapGetters({
      msg: "Staff/msg"
    })
  }
};
</script>

<style scoped>
.cont {
  height: 750px;
  background-color: rgb(133, 167, 187);
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
input,.form-control
{
  margin-bottom: 10px;
}
#opt
{
  margin-bottom: 0px;
}

</style>
