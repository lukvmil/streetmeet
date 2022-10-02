import { AppLocation } from "./location";

export interface User {
  username: string;

  topic: string;

  peerId: string;

  location: AppLocation;

  _id: string;
}
