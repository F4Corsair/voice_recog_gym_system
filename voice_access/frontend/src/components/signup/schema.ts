import { z } from "zod";

export const formSchema = z.object({
  username: z.string().min(2).max(50),
  phoneNum: z.string().min(2).max(50),
  homeAddress: z.string().min(2).max(100),
  voiceFile: z.instanceof(File).optional(),
});
