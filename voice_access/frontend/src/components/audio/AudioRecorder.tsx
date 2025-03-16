import { Button } from "@/components/ui/button";
import { useState, useRef, useEffect } from "react";
import { sendAudioToBackend } from "@/lib/utils";

const AudioRecorder = () => {
  const [isRecording, setIsRecording] = useState<boolean>(false);
  const [audioBlob, setAudioBlob] = useState<Blob | null>(null);
  const mediaRecorderRef = useRef<MediaRecorder | null>(null); // mediaRecorder의 상태를 추적하는 ref
  const isRecordingRef = useRef<boolean>(false); // 녹음 상태를 추적하는 ref

  let audioChunks: Blob[] = [];

  const startRecording = async () => {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    const recorder = new MediaRecorder(stream);
    mediaRecorderRef.current = recorder;
    isRecordingRef.current = true; // 녹음 시작 시 true로 설정

    recorder.start();

    recorder.ondataavailable = (event) => {
      audioChunks.push(event.data);
    };

    recorder.onstop = async () => {
      const blob = new Blob(audioChunks, { type: "audio/wav" });
      setAudioBlob(blob);
      audioChunks = [];

      console.log("녹음 완료, 음성 데이터 전송...");
      await handleSendAudio(blob);
    };

    setIsRecording(true);

    // 5초 후 자동 종료
    setTimeout(() => {
      if (isRecordingRef.current) {
        stopRecording();
      }
    }, 5000);
  };

  const stopRecording = () => {
    if (mediaRecorderRef.current && isRecordingRef.current) {
      mediaRecorderRef.current.stop();
      isRecordingRef.current = false; // 녹음 중지 후 false로 변경
      setIsRecording(false);
    }
  };

  const handleSendAudio = async (blob: Blob) => {
    try {
      const response = await sendAudioToBackend(blob);
      console.log("Authentication Result:", response);
    } catch (error) {
      console.error("Failed to send audio:", error);
    }
  };

  // 컴포넌트 언마운트 시 미디어 스트림 정리
  useEffect(() => {
    return () => {
      if (mediaRecorderRef.current) {
        mediaRecorderRef.current.stream
          .getTracks()
          .forEach((track) => track.stop());
      }
    };
  }, []);

  return (
    <>
      <Button onClick={startRecording} disabled={isRecording}>
        녹음 시작
      </Button>
      {isRecording && <p>녹음 중... (5초 후 자동 종료)</p>}
      <Button onClick={stopRecording} disabled={!isRecording}>
        녹음 종료
      </Button>
      {audioBlob && (
        <div>
          <audio controls src={URL.createObjectURL(audioBlob)}></audio>
        </div>
      )}
    </>
  );
};

export default AudioRecorder;
