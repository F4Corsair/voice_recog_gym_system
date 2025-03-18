import { QueryClient } from "@tanstack/react-query";
import axios, {
  AxiosRequestConfig,
  AxiosResponse,
  InternalAxiosRequestConfig,
} from "axios";
export const queryClient = new QueryClient();

export const http = axios.create({
  baseURL: "https://api.example.com",
  headers: {
    "Content-Type": "application/json",
  },
});

// 요청 인터셉터 (예: 토큰 자동 추가)
http.interceptors.request.use(
  (config: AxiosRequestConfig): InternalAxiosRequestConfig => {
    const token = localStorage.getItem("token");
    if (token) {
      if (!config.headers) {
        config.headers = {};
      }
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config as InternalAxiosRequestConfig;
  }
);

// 응답 인터셉터 (예: 에러 처리)
http.interceptors.response.use(
  (response: AxiosResponse): AxiosResponse => response,
  (error: Error): Promise<Error> => {
    console.error("API Error:", error);
    return Promise.reject(error);
  }
);
