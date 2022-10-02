import axios from "axios";

let baseURL;
if (process.env.NODE_ENV == "production")
  baseURL = "http://streetmeet.lukvmil.com/api";
else baseURL = "/api";

const api = axios.create({ baseURL });

export default api;
