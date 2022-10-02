<template>
  <div>
    <div v-if="chatData">
      <h2>Messages</h2>
      <div v-for="message in chatData.messages">
        <div>
          <strong>{{ message.self ? "You: " : "" }}</strong> {{ message.text }}
        </div>
      </div>
      <div v-if="chatData.disconnected">Chat disconnected</div>
      <input type="text" v-model="messageInput" />
      <button @click="send" :disabled="chatData.disconnected">Send</button> <br />
      <button v-if="!chatData.disconnected" @click="dc">Disconnect</button>
    </div>
    <div v-else>
      <button @click="connectToUser" :disabled="connectDisabled">
        Connect to user
      </button>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, computed } from "vue";
import { ChatData, store } from "@/store";
import { connect, sendMessage, disconnect } from "@/messaging/webrtc";
import router from "@/router";

export default defineComponent({
  name: "MessageVue",

  props: {
    peerId: {
      type: String,
      required: true,
    },
  },

  setup(props) {
    if (!store.profile._id) {
      router.push("/");
    }

    const messageInput = ref("");
    const chatData = computed<ChatData | undefined>(
      () => store.chats[props.peerId]
    );

    const send = () => {
      if (!chatData.value) return;
      sendMessage(chatData.value, messageInput.value);
      messageInput.value = "";
    };

    const dc = () => {
      if (chatData.value) disconnect(chatData.value);
    };

    const connectDisabled = ref(false);
    const connectToUser = () => {
      connectDisabled.value = true;
      connect(props.peerId);
    };

    return {
      chatData,
      messageInput,
      send,
      dc,
      connectToUser,
      connectDisabled,
    };
  },
});
</script>
