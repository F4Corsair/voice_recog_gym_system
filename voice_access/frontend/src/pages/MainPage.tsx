import AudioRecorder from "@/components/audio/AudioRecorder";
import { Button } from "@/components/ui/button";
import { Link } from "react-router-dom";

const MainPage = () => {
  // FIXME: 오류 방지를 위한 임시 핸들러
  const handleAudioFile = () => {
    console.log("handle audio file temp");
  };
  return (
    <>
      <p>음성으로 사용자를 인증하는 메인 페이지</p>
      <AudioRecorder onFileReady={handleAudioFile} />
      <Button variant={"link"}>
        <Link to="/signup">회원등록</Link>
      </Button>
    </>
  );
};

export default MainPage;
