import axios from 'axios';

//dev_5
const http = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
});

export default http;