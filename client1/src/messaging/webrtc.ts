import { DataConnection, Peer } from "peerjs";
import { ChatData, store } from "@/store";

export const peer = new Peer();

peer.on("open", () => {
  store.peerInitialized = true;
});

export const connect = (id: string) => {
  const conn = peer.connect(id);
  initializeConnection(conn);
  return conn;
};

peer.on("connection", (connection) => {
  const conn = connection;
  initializeConnection(conn);
});

const initializeConnection = (conn: DataConnection) => {
  if (!conn) return;

  conn.on("data", (data) => {
    store.chats[conn.peer].messages.push({ text: data as string });
  });

  conn.on("open", () => {
    store.chats[conn.peer] = {
      messages: [],
      disconnected: false,
      conn: conn,
    };
  });

  conn.on("close", () => {
    store.chats[conn.peer].disconnected = true;
  });
};

export const sendMessage = (chat: ChatData, message: string) => {
  chat.conn.send(message);
  store.chats[chat.conn.peer].messages.push({
    self: true,
    text: message,
  });
};

export const disconnect = (chat: ChatData) => {
  chat.conn.close();
};

// DEBUG
(window as any).peer = peer;
