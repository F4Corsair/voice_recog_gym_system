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
  // 1. Define your form.
  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      username: "soroso",
      phoneNum: "010-1234-1234",
      homeAddress: "Daegu-si",
    },
  });

  // 2. Define a submit handler.
  function onSubmit(values: z.infer<typeof formSchema>) {
    // Do something with the form values.
    const formData = new FormData();
    formData.append(
      "data",
      new Blob(
        [
          JSON.stringify({
            username: values.username,
            phoneNum: values.phoneNum,
            homeAddress: values.homeAddress,
          }),
        ],
        { type: "application/json" }
      )
    );

    if (values.voiceFile) {
      formData.append("voiceFile", values.voiceFile);
    }

    // ✅ This will be type-safe and validated.
    sendAudioToBackendForSignUp(formData);
    console.log(values);
  }

  const handleAudioFile = (file: File) => {
    form.setValue("voiceFile", file); // 폼 상태 업데이트
  };
  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-8">
        <FormField
          control={form.control}
          name="username"
          render={({ field }) => (
            <FormItem>
              <FormLabel>이름</FormLabel>
              <FormControl>
                <Input placeholder="shadcn" {...field} />
              </FormControl>
              <FormDescription>
                This is your public display name.
              </FormDescription>
              <FormMessage />
            </FormItem>
          )}
        />
        <FormField
          control={form.control}
          name="phoneNum"
          render={({ field }) => (
            <FormItem>
              <FormLabel>전화번호</FormLabel>
              <FormControl>
                <Input placeholder="shadcn" {...field} />
              </FormControl>
              <FormDescription>
                This is your public display name.
              </FormDescription>
              <FormMessage />
            </FormItem>
          )}
        />
        <FormField
          control={form.control}
          name="homeAddress"
          render={({ field }) => (
            <FormItem>
              <FormLabel>주소</FormLabel>
              <FormControl>
                <Input placeholder="shadcn" {...field} />
              </FormControl>
              <FormDescription>
                This is your public display name.
              </FormDescription>
              <FormMessage />
            </FormItem>
          )}
        />
        <FormItem>
          <FormLabel>음성 녹음</FormLabel>
          <AudioRecorder onFileReady={handleAudioFile} />
          <FormDescription>음성을 녹음해서 등록하세요.</FormDescription>
          <FormMessage />
        </FormItem>

        <Button type="submit">Submit</Button>
      </form>
    </Form>
  );
}
