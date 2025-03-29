import { useEffect, useRef, useState } from "react";
import { Button } from "../ui/button";

const AudioRecorder = ({
  onFileReady,
}: {
  onFileReady: (file: File) => void;
}) => {
  const [isRecording, setIsRecording] = useState(false);
  const [audioBlob, setAudioBlob] = useState<Blob | null>(null);
  const mediaRecorderRef = useRef<MediaRecorder | null>(null);
  const audioChunksRef = useRef<Blob[]>([]);

  const startRecording = async () => {
    if (!navigator.mediaDevices?.getUserMedia) {
      console.error("getUserMedia is not supported");
      return;
    }

    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      const recorder = new MediaRecorder(stream);
      mediaRecorderRef.current = recorder;
      audioChunksRef.current = [];

      recorder.ondataavailable = (event) => {
        audioChunksRef.current.push(event.data);
      };

      recorder.onstop = () => {
        const blob = new Blob(audioChunksRef.current, { type: "audio/wav" });
        setAudioBlob(blob);
        const file = new File([blob], "recording.wav", { type: "audio/wav" });
        onFileReady(file);
      };

      recorder.start();
      setIsRecording(true);

      setTimeout(() => {
        if (recorder.state === "recording") {
          recorder.stop();
          setIsRecording(false);
        }
      }, 5000);
    } catch (err) {
      console.error("녹음 실패:", err);
    }
  };

  useEffect(() => {
    return () => {
      mediaRecorderRef.current?.stream
        .getTracks()
        .forEach((track) => track.stop());
    };
  }, []);

  return (
    <div className="space-y-2">
      <Button
        onClick={startRecording}
        disabled={isRecording}
        className="bg-blue-500"
      >
        녹음 시작
      </Button>
      {isRecording && <p>녹음 중... (5초 후 자동 종료)</p>}
      {audioBlob && <audio controls src={URL.createObjectURL(audioBlob)} />}
    </div>
  );
};

export default AudioRecorder;
