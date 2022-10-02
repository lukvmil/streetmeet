<template>
  <div>
    <h1>People</h1>
    <div class="person" v-for="person in store.users" :key="person._id">
      <h3>{{ person.username }}</h3>
      <div>Topic: {{ person.topic }}</div>
      <div v-if="store.chats[person.peerId]?.unread">
        Unread: {{ store.chats[person.peerId].unread }}
      </div>
      <router-link :to="`message/${person.peerId}`">Message</router-link>
    </div>
  </div>
</template>

<script lang="ts">
import { computed, defineComponent, onBeforeUnmount } from "vue";
import api from "@/api";
import { store } from "@/store";

export default defineComponent({
  name: "PeopleList",

  setup() {
    const profile = computed(() => store.profile);

    const loadPeople = async () => {
      const res = await api.get("/match/" + store.profile._id);
      store.users = res.data;
    };
    loadPeople();

    const interval = setInterval(loadPeople, 2000);

    onBeforeUnmount(() => {
      clearInterval(interval);
    });

    return {
      profile,
      store,
    };
  },
});
</script>

<style>
.person {
  padding: 1rem;
  background: var(--bg-secondary);
  border-radius: 10px;
  margin-bottom: 1rem;
}

.person h3 {
  margin-top: 0;
}
</style>