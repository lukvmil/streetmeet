<template>
  <div>
    <button @click="getLocation">Get Location</button>
    <div v-if="location">
      {{ location }}
    </div>
  </div>
</template>

<script lang="ts">
import { AppLocation } from "@/types/location";
import { defineComponent, ref } from "vue";

export default defineComponent({
  name: "LocationVue",
  setup() {
    const location = ref<AppLocation>();

    const getLocation = () => {
      if ("geolocation" in navigator) {
        navigator.geolocation.getCurrentPosition((position) => {
          location.value = {
            lat: position.coords.latitude,
            lon: position.coords.longitude,
          };
        });
      } else {
        throw new Error("Location not available");
      }
    };

    return {
      location,
      getLocation,
    };
  },
});
</script>
