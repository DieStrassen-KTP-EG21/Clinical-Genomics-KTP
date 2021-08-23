<template>
  <div>
    <div class="cont">
      <HomeNavigation />
      <div>
        <h1>Add Staff</h1>
        <form class="row gy-2 gx-3 align-items-center">
          <div class="col-auto">
            <label class="visually-hidden" for="autoSizingInput">Name</label>
            <input
              type="text"
              v-model="Name"
              class="form-control"
              id="autoSizingInput"
              placeholder="Name"
            />
            <label class="visually-hidden" for="autoSizingInput">Gender</label>
            <input
              type="text"
              v-model="Gender"
              class="form-control"
              id="autoSizingInput"
              placeholder="Gender"
            />
            <label class="visually-hidden" for="autoSizingInput"
              >EmployeeType</label
            >
            <input
              type="text"
              v-model="EmployeeType"
              class="form-control"
              id="autoSizingInput"
              placeholder="EmployeeType"
            />
          </div>
          <div class="col-auto">
            <label class="visually-hidden" for="autoSizingInput">ID</label>
            <input
              type="number"
              v-model="ID"
              class="form-control"
              id="autoSizingInput"
              placeholder="ID"
            />
            <label class="visually-hidden" for="autoSizingInput">Email</label>
            <input
              type="text"
              v-model="Email"
              class="form-control"
              id="autoSizingInput"
              placeholder="Email"
            />
            <label class="visually-hidden" for="autoSizingInput">Phone</label>
            <input
              type="number"
              v-model="Phone"
              class="form-control"
              id="autoSizingInput"
              placeholder="Phone"
            />
          </div>
          <div class="col-auto">
            <label class="visually-hidden" for="autoSizingInput"
              >Password</label
            >
            <input
              type="text"
              v-model="Password"
              class="form-control"
              id="autoSizingInput"
              placeholder="Password"
            />
            <label class="visually-hidden" for="autoSizingInput">Address</label>
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
        ID: this.ID,
        Password: this.Password,
        Gender: this.Gender,
        Email: this.Email,
        EmployeeType: this.EmployeeType,
        Address: this.Address,
        Phone: this.Phone,
      };
      e.preventDefault();
      console.log(newMember);
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
