<template>
  <div class="home">
    <h1>StreetMeet</h1>
    <Info v-if="!profile._id" />
    <PeopleList v-else />
  </div>
</template>

<script lang="ts">
import { computed, defineComponent } from "vue";
// import LocationVue from "@/components/Location.vue";
// import MessagingVue from "@/components/Messaging.vue";
import Info from "@/components/Info.vue";
import { store } from "@/store";
import PeopleList from "@/components/PeopleList.vue";

export default defineComponent({
  name: "HomeView",
  components: {
    // LocationVue,
    // MessagingVue,
    Info,
    PeopleList,
  },

  setup() {
    const profile = computed(() => store.profile);

    return {
      profile,
    };
  },
});
</script>
