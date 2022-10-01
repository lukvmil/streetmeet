<template>
  <div>
    <input v-model="remoteId" type="text" placeholder="Remote ID" />
    <button @click="connect" :disabled="connected">Connect</button>
    <div>Local ID: {{ peerInitialized ? localId : "Loading..." }}</div>

    <div v-if="connected">
      <div>Connected!</div>
      <h2>Messages</h2>
      <div v-for="message in messages" :key="message">
        <div>{{ message }}</div>
      </div>
      <input type="text" v-model="messageInput" />
      <button @click="sendMessage">Send</button> <br />
      <button @click="disconnect">Disconnect</button>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, computed } from "vue";
import { peer } from "@/messaging/webrtc";
import { DataConnection } from "peerjs";
import { store } from "@/store";

export default defineComponent({
  name: "MessageVue",

  setup() {
    const remoteId = ref("");
    const localId = ref(peer.id);
    const messageInput = ref("");
    const connected = ref(false);
    const peerInitialized = computed(() => store.peerInitialized);

    let conn: DataConnection | null = null;

    peer.on("open", () => {
      localId.value = peer.id;
    });

    const messages = ref<string[]>([]);

    const connect = () => {
      conn = peer.connect(remoteId.value);
      initializeConnection();
    };

    peer.on("connection", (connection) => {
      conn = connection;
      initializeConnection();
    });

    const initializeConnection = () => {
      if (!conn) return;

      conn.on("data", (data) => {
        messages.value.push(data as string);
      });
      conn.on("open", () => {
        connected.value = true;
      });
      conn.on("close", () => {
        connected.value = false;
      });
    };

    const sendMessage = () => {
      if (conn) {
        conn.send(messageInput.value);
        messages.value.push(messageInput.value);
      }
    };

    const disconnect = () => {
      if (conn) {
        conn.close();
      }
    };

    return {
      remoteId,
      localId,
      connect,
      messages,
      connected,
      messageInput,
      sendMessage,
      disconnect,
      peerInitialized,
    };
  },
});
</script>
