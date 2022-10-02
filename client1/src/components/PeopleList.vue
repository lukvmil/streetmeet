<template>
  <div v-if="people">
    <h1>People</h1>
    <div v-for="person in people" :key="person._id">
      <h3>{{ person.username }}</h3>
      <div>Topic: {{ person.topic }}</div>
      <router-link :to="`message/${person.peerId}`">Message</router-link>
    </div>
  </div>
  <div v-else>Loading...</div>
</template>

<script lang="ts">
import { computed, defineComponent, onBeforeUnmount, ref } from "vue";
import { User } from "@/types/user";
import api from "@/api";
import { store } from "@/store";

export default defineComponent({
  name: "PeopleList",

  setup() {
    const people = ref<User[]>();
    const profile = computed(() => store.profile);

    const loadPeople = async () => {
      const res = await api.get("/match/" + store.profile._id);
      people.value = res.data;
    };
    loadPeople();

    const interval = setInterval(loadPeople, 2000);

    onBeforeUnmount(() => {
      clearInterval(interval);
    });

    return {
      people,
      profile,
    };
  },
});
</script>
