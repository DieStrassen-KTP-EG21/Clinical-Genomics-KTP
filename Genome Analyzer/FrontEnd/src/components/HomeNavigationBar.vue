<template>
  <div class="navbar-container justify-content-center">
    <div class="navbar-list">
      <router-link to="/">
        <ul id="firstul">
          <img src="../assets/images.png" id="logo" />
          <li>
            Hospital Mangement System
          </li>
        </ul>
      </router-link>

      <ul id="secul">
        <router-link to="/" tag="li">
          <a>Home</a>
        </router-link>

        <router-link to="/Login" tag="li" v-if="isLoggedIn !='success'">
          <a>Login</a>
        </router-link>

        <Button class="btn float-right logout_btn" @click="logout()" v-if="isLoggedIn=='success'">Log out</Button>

      </ul>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "HomeNavigation",
    methods: {
    logout() {
      console.log("log out");
          this.$store.dispatch("Authorization/logout");
        
    },
  },
   computed: {
    ...mapGetters({
      isLoggedIn: "Authorization/GetStatus"
    })
  }
  };
</script>

<style scoped>
#logo {
  margin: 15px 0px;
  height: 40px;
}
#firstul {
  float: left;
}
#secul {
  float: right;
  margin-right: 10%;
}
.navbar-container {
  width: 100%;
  margin: 0%;
  height: 80px;
  z-index: 2000;
}
ul {
  margin: 0%;
  list-style-type: none;
  display: inline-flex;
}
li {
  padding: 25px 17px;
  text-align: center;
  float: right;
  color: #ffffff;
}
a {
  color: #ffffff;
  font-size: 15px;
  text-decoration: none;
  padding: 0%;
  display: block;
}
a:hover {
  color: #0f0f0f;
}
#separator {
  color: #ffffff;
}
.navbar-list {
  background-color: rgb(37, 91, 122);
  width: 100%;
  font-family: Helvetica, Arial, sans-serif;
  font-size: 16px;
  font-weight: 700;
  line-height: 1.5;
  position: fixed;
  margin: 0;
}
#logout {
  background-color: rgb(96, 155, 189);
  border-radius: 10px;
  height: 50px;
  margin-top: 20px;
}

.logout_btn
{
  color:white;
}
</style>
