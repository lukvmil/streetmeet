<template>
  <h1>Hello!</h1>
  <div>
    <input type="text" placeholder="Enter a username!" v-model="username" />
  </div>
  <div>
    <input
      type="text"
      placeholder="What's on your mind today?"
      v-model="topic"
    />
  </div>
  <div>
    <button @click="submit">Submit</button>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import { AppLocation } from "@/types/location";
import api from "@/api";
import { peer } from "@/messaging/webrtc";
import { store } from "@/store";

export default defineComponent({
  name: "InfoVue",

  setup() {
    const username = ref("");
    const topic = ref("");
    const location = ref<AppLocation>();

    const getLocation = (handler: any) => {
      if ("geolocation" in navigator) {
        navigator.geolocation.getCurrentPosition((position) => {
          location.value = {
            lat: position.coords.latitude,
            lon: position.coords.longitude,
          };

          handler();
        });
      } else {
        throw new Error("Location not available");
      }
    };

    const submit = () => {
      getLocation(async () => {
        const res = await api.post("/user", {
          username: username.value,
          topic: topic.value,
          peerId: peer.id,
          location: [location.value?.lon, location.value?.lat],
        });

        console.log(res.data);

        store.profile = res.data;
      });
    };

    return {
      username,
      topic,
      submit,
    };
  },
});
</script>
