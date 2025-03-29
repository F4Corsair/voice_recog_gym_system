import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";

import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";
import { z } from "zod";
import { Input } from "../ui/input";
import { Button } from "../ui/button";
import AudioRecorder from "../audio/AudioRecorder";
import { formSchema } from "./schema";
import { sendAudioToBackendForSignUp } from "@/lib/utils";

export function SignUpForm() {
  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      username: "soroso",
      phoneNum: "010-1234-1234",
      homeAddress: "Daegu-si",
      voiceFiles: [],
    },
  });

  const voiceFiles = form.watch("voiceFiles");

  function onSubmit(values: z.infer<typeof formSchema>) {
    const formData = new FormData();
    formData.append("username", values.username);
    formData.append("phoneNumber", values.phoneNum);
    formData.append("homeAddress", values.homeAddress);

    values.voiceFiles.forEach((file) => {
      formData.append("voiceFiles", file);
    });

    sendAudioToBackendForSignUp(formData);
    console.log(values);
  }

  const handleAudioFile = (index: number, file: File) => {
    const currentFiles = form.getValues("voiceFiles") || [];
    const updatedFiles = [...currentFiles];
    updatedFiles[index] = file;

    const cleanedFiles = updatedFiles.filter((f): f is File => !!f);
    form.setValue("voiceFiles", cleanedFiles);
  };

  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-8">
        {/* 이름 */}
        <FormField
          control={form.control}
          name="username"
          render={({ field }) => (
            <FormItem>
              <FormLabel>이름</FormLabel>
              <FormControl>
                <Input placeholder="홍길동" {...field} />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />

        {/* 전화번호 */}
        <FormField
          control={form.control}
          name="phoneNum"
          render={({ field }) => (
            <FormItem>
              <FormLabel>전화번호</FormLabel>
              <FormControl>
                <Input placeholder="010-0000-0000" {...field} />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />

        {/* 주소 */}
        <FormField
          control={form.control}
          name="homeAddress"
          render={({ field }) => (
            <FormItem>
              <FormLabel>주소</FormLabel>
              <FormControl>
                <Input placeholder="대구시..." {...field} />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />

        {/* 녹음 입력 */}
        {Array.from({ length: 5 }).map((_, index) => (
          <FormItem key={index}>
            <FormLabel>{`음성 녹음 ${index + 1}`}</FormLabel>
            <AudioRecorder
              onFileReady={(file) => handleAudioFile(index, file)}
            />
            <FormDescription>음성을 녹음해서 등록하세요.</FormDescription>
            <FormMessage />
          </FormItem>
        ))}

        <Button type="submit">회원가입</Button>
      </form>
    </Form>
  );
}
