<template>
  <div class="home">
    <h1>StreetMeet</h1>
    <LocationVue />
    <MessagingVue />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import LocationVue from "@/components/Location.vue";
import MessagingVue from "@/components/Messaging.vue";

export default defineComponent({
  name: "HomeView",
  components: {
    LocationVue,
    MessagingVue,
  },
});
</script>
