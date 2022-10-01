import { Peer } from "peerjs";
import { store } from "@/store";

export const peer = new Peer();
peer.on("open", () => {
  store.peerInitialized = true;
});

// DEBUG
(window as any).peer = peer;
