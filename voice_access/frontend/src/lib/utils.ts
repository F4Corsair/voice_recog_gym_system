import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";
import { http } from "./http";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}
// 음성 파일 전송용 함수(로그인용)
export const sendAudioToBackend = async (audioBlob: Blob) => {
  if (!audioBlob) return;

  const formData = new FormData();
  formData.append("audio", audioBlob, "recording.wav");

  const response = await http.post("api/recognize", formData, {
    headers: { "Content-Type": "multipart/form-data" }, // 요청마다 헤더 변경
  });
  return response.data;
};

// 음성 파일 전송용 함수(회원등록용)
export const sendAudioToBackendForSignUp = async (formData: FormData) => {
  if (!formData) return;
  const response = await http.post("api/signup", formData, {
    headers: { "Content-Type": "multipart/form-data" }, // 요청마다 헤더 변경
  });
  return response.data;
};

// 음성 파일 전송용 함수(로그인)
export const sendAudioToBackendForLogin = async (formData: FormData) => {
  if (!formData) return;
  const response = await http.post("api/login", formData, {
    headers: { "Content-Type": "multipart/form-data" }, // 요청마다 헤더 변경
  });
  return response.data;
};
