<template>
  <!-- <div v-if="!peerInitialized">Loading...</div> -->
  <div>
    <h1 class="header">StreetMeet</h1>
    <!-- <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </nav> -->
    <router-view />
  </div>
</template>

<script lang="ts">
import { computed, defineComponent } from "vue";
import { loopKeepAlive } from "./api/keepAlive";
import { store } from "./store";
import "@/style/style.css";

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
.header {
  width: 100%;
  margin-top: 0;
  padding-top: 2rem;
  padding-bottom: 1rem;
  background: var(--brand);
  color: var(--bg-primary);
  text-align: center;
}
</style>
