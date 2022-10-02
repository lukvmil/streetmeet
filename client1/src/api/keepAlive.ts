import { store } from "@/store";
import api from ".";

const keepAlive = () => {
  if (store.profile._id) api.post("/user/" + store.profile._id);
};

export const loopKeepAlive = () => {
  setInterval(keepAlive, 5000);
};
