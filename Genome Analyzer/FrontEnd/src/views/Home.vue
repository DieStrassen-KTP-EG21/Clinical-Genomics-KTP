<template>
  <div class="cont">
    <HomeNavigation />
  <div class=" row justify-content-center home px-0 m-0">
      <div class="col-9 headers px-0 m-0">
        <h1> Hospital Mangement System</h1>
        <h4>Let's help our patients</h4>
        <div class="row justify-content-center px-0 m-0">
          <router-link
            class="costum-btn"
            id="signin-btn"
            to="/Login"
            tag="button"
          >
            Login
          </router-link>
        </div>
    </div>
  </div>
  </div>
</template>

<script>
import HomeNavigation from "@/components/HomeNavigationBar.vue";
export default {
  name: "Home",
  components: {
    HomeNavigation
  },
};
</script>

<style scoped>
.cont {
  background-color: rgb(37, 91, 122);
}
.home {
  
  background-repeat: no-repeat;
  width: 100%;
  height: 700px;
  background-position: center;
  background-size: 100% 100%;
  position:absolute;
  background-image: url("../assets/a.jpg");
    color: black;
}
.headers {
  justify-content: center;
  justify-items: center;
  padding-top: 30%;
  position: absolute;
  z-index: 0;
  margin-top: 80px;
}
h1 {
  font-size: 80px;
  font-weight: 100;
  letter-spacing: -0.04em;
  line-height: 0;
  margin-top: 0;
  text-align: center;
  width: 100%;
}
h4 {
  font-size: 18px;
  font-weight: 400;
  text-align: center;
  width: 100%;
  margin-bottom: 20px;
}
#signin-btn {
  border-radius:20px ;
  background-color: rgb(37, 91, 122);
  max-width: 320px;
  width: 200px;
  justify-self: center;
  height: 50px;
}
#signin-btn:hover {
background-color: rgb(107, 180, 185);
}
@media screen and (max-width: 1000px) {
  h1 {
    font-size: 55px;
    font-weight: 750;
    letter-spacing: -0.04em;
    line-height: 1.15;
    margin-top: 0;
    text-align: center;
    width: 100%;
  }
  h4 {
    font-size: 16px;
    font-weight: 400;
    text-align: center;
    width: 100%;
  }
}
</style>