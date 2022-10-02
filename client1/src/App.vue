<template>
  <div v-if="!peerInitialized">Loading...</div>
  <div v-else>
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </nav>
    <router-view />
  </div>
</template>

<script lang="ts">
import { computed, defineComponent } from "vue";
import { loopKeepAlive } from "./api/keepAlive";
import { store } from "./store";

export default defineComponent({
  name: "App",
  setup() {
    const peerInitialized = computed(() => store.peerInitialized);

    // disconnect handler
    window.addEventListener("beforeunload", () => {
      // api.post("user/disconnect");
    });

    // ping keep alive
    loopKeepAlive();

    return {
      peerInitialized,
    };
  },
});
</script>

<style>
html,
body {
  margin: 0;
  padding: 0;
  font-family: sans-serif;
}
</style>
