<template
  ><div>
    <div class="cont">
      <HomeNavigation />

      <div>
        <b-table
      
          :items="items"
          :fields="fields"
          striped
          responsive="sm"
        >
          <template #cell(actions)="row">
            <b-button size="sm" @click="row.toggleDetails" class="mr-2">
              {{ row.detailsShowing ? "Hide" : "Show" }} Details
            </b-button>
            <b-button
                v-for="(index) in items"
          :key="index.ID"
              variant="danger"
              size="sm"
              @click="deletePatient(index)"
              class="mr-2"
            >
              Delete
            </b-button>
            <b-button
              variant="outline-primary"
              size="sm"
              @click="editPatient"
              class="mr-2"
            >
              Edit
            </b-button>
            <b-button
              variant="success"
              size="sm"
              @click="approvePatient"
              class="mr-2"
            >
              Approve
            </b-button>
          </template>

          <template #row-details="row">
            <b-card>
              <b-row class="mb-2">
                <b-col sm="3" class="text-sm-right"><b>Phone:</b></b-col>
                <b-col>{{ row.item.Phone }}</b-col>
              </b-row>

              <b-row class="mb-2">
                <b-col sm="3" class="text-sm-right"><b>Gender:</b></b-col>
                <b-col>{{ row.item.Gender }}</b-col>
              </b-row>
              <b-row class="mb-2">
                <b-col sm="3" class="text-sm-right"><b>Address:</b></b-col>
                <b-col>{{ row.item.Address }}</b-col>
              </b-row>
              <b-row class="mb-2">
                <b-col sm="3" class="text-sm-right"><b>Sequence:</b></b-col>
                <b-col>{{ row.item.Sequence }}</b-col>
              </b-row>

              <b-button size="sm" @click="row.toggleDetails"
                >Hide Details</b-button
              >
            </b-card>
          </template>
        </b-table>
      </div>
    </div>
  </div>
</template>

<script>
import HomeNavigation from "@/components/HomeNavigationBar.vue";
export default {
  name: "Admin",
  components: {
    HomeNavigation,
  },
  data() {
    return {
      fields: ["Name", "ID", "Actions"],
      items: [
        {
          isApproved: true,
          Phone: 404676,
          Name: "Dickerson",
          ID: 23,
          Gender: "Male",
          Address: "LA",
          Sequence: "ATCGTAGC",
        },
        {
          isApproved: false,
          Phone: 243541,
          Name: "Larsen",
          ID: 54,
          Gender: "Female",
          Address: "NY",
          Sequence: "GCTAGTACGA",
        },
        {
          isApproved: false,
          Phone: 834349,
          Name: "Geneva",
          ID: 22,
          Gender: "Female",
          Address: "Boston",
          Sequence: "TAAGAGC",
        },
        {
          isApproved: true,
          Phone: 3865454,
          Name: "Jami",
          ID: 92,
          Gender: "Male",
          Address: "Arizona",
          Sequence: "ATCGGAGC",
        },
      ],

    };
  },
  methods: {
    deletePatient: function(idx) {

      this.items.splice(idx, 1);
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
.mr-2 {
  margin: 4px;
}
</style>
