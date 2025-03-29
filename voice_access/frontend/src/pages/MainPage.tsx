import AudioRecorder from "@/components/audio/AudioRecorder";
import { Button } from "@/components/ui/button";
import { sendAudioToBackendForLogin } from "@/lib/utils";
import { Link } from "react-router-dom";

const MainPage = () => {
  // FIXME: 오류 방지를 위한 임시 핸들러
  const handleAudioFile = (formData: FormData) => {
    sendAudioToBackendForLogin(formData);
  };
  const formData = new FormData();
  return (
    <>
      <p>음성으로 사용자를 인증하는 메인 페이지</p>
      <AudioRecorder
        onFileReady={(file) => {
          formData.append("audio", file);
        }}
      />
      <Button
        onClick={() => handleAudioFile(formData)}
        className="bg-emerald-400"
      >
        로그인
      </Button>
      <Button variant={"link"}>
        <Link to="/signup">회원등록</Link>
      </Button>
    </>
  );
};

export default MainPage;
