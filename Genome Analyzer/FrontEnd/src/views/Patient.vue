<template
  ><div>
    <div class="cont">
      <HomeNavigation />
       <h1>Patient</h1>
    </div>
  </div>
</template>

<script>
import HomeNavigation from "@/components/HomeNavigationBar.vue";
export default {
  name: "Patient",
  components: {
    HomeNavigation,
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
</style>
