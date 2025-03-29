import { z } from "zod";

export const formSchema = z.object({
  username: z.string().min(2).max(50),
  phoneNum: z.string().min(2).max(50),
  homeAddress: z.string().min(2).max(100),
  voiceFiles: z
    .array(z.instanceof(File), {
      required_error: "음성 파일은 최소 1개 필요합니다.",
    })
    .min(1)
    .max(5),
});
