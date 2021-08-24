<template>
  <div>
    <div class="cont">
      <HomeNavigation />
      <div>
        <h1>Add Staff</h1>
        <form class="row gy-2 gx-3 align-items-center">
          <div class="col-auto">
            <label class="visually-hidden">Name</label>
            <input
              type="text"
              v-model="Name"
              class="form-control"
              id="autoSizingInput"
              placeholder="Name"
            />
            <label class="visually-hidden">Gender</label>
            <input
              type="text"
              v-model="Gender"
              class="form-control"
              id="autoSizingInput"
              placeholder="Gender"
            />
            <label class="visually-hidden">EmployeeType</label>
            <input
              type="text"
              v-model="EmployeeType"
              class="form-control"
              id="autoSizingInput"
              placeholder="EmployeeType"
            />
          </div>
          <div class="col-auto">
            <label class="visually-hidden">Email</label>
            <input
              type="text"
              v-model="Email"
              class="form-control"
              id="autoSizingInput"
              placeholder="Email"
            />
            <label class="visually-hidden">Phone</label>
            <input
              type="number"
              v-model="Phone"
              class="form-control"
              id="autoSizingInput"
              placeholder="Phone"
            />
          </div>
          <div class="col-auto">
            <label class="visually-hidden">Password</label>
            <input
              type="text"
              v-model="Password"
              class="form-control"
              id="autoSizingInput"
              placeholder="Password"
            />
            <label class="visually-hidden">Address</label>
            <input
              type="text"
              v-model="Address"
              class="form-control"
              id="autoSizingInput"
              placeholder="Address"
            />
          </div>

          <div class="col-auto">
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
</style>
