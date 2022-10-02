<!-- eslint-disable vue/require-v-for-key -->
<template>
  <div class="section">
    <div v-if="chatData && otherPerson">
      <h2>{{ otherPerson.username }}</h2>

      <div class="messages">
        <TransitionGroup name="list">
          <div
            v-for="message in chatData.messages"
            class="message"
            :key="message.id"
          >
            <div>
              <strong>{{
                message.self ? "You: " : otherPerson.username
              }}</strong>
              {{ message.text }}
            </div>
          </div>
        </TransitionGroup>
      </div>

      <div v-if="chatData.disconnected">Chat disconnected</div>
      <input type="text" v-model="messageInput" />
      <button
        @click="send"
        :disabled="chatData.disconnected"
        class="send-button"
      >
        Send
      </button>
      <br />

      <button
        v-if="!chatData.disconnected"
        @click="dc"
        class="disconnect-button"
      >
        Disconnect
      </button>
    </div>
    <div v-else style="padding: 1rem; text-align: center; font-size: 1.5rem">
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

    const otherPerson = computed(() => {
      if (chatData.value) {
        console.log(store.users);
        return store.users.find((u) => u.peerId === props.peerId);
      } else return undefined;
    });

    // reset unread
    if (chatData.value) {
      chatData.value.unread = 0;
    }

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
      otherPerson,
    };
  },
});
</script>

<style>
.messages {
  margin-bottom: 1rem;
}

.messages .message {
  margin-bottom: 0.5rem;
}

.list-enter-active,
.list-leave-active {
  transition: all 0.5s ease;
}
.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateX(30px);
}

.send-button {
  margin-left: 0.5rem;
}

.disconnect-button {
  margin: 1rem auto;
}
</style>
