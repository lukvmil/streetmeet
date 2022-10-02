import { reactive } from "vue";
import { User } from "@/types/user";
import { DataConnection } from "peerjs";

export interface ChatData {
  conn: DataConnection;
  messages: {
    id: number;
    self?: boolean;
    text: string;
  }[];
  disconnected: boolean;
  unread: number;
}

export interface ChatStore {
  [key: string]: ChatData;
}

export const store = reactive({
  peerInitialized: false,
  users: [] as User[],
  profile: {} as User,
  chats: {} as ChatStore,
});
