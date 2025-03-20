import { SignUpForm } from "@/components/signup/SignUpForm";
import MainPage from "@/pages/MainPage";
import { createBrowserRouter } from "react-router-dom";

export const router = createBrowserRouter([
  {
    path: "/",
    children: [
      {
        index: true,
        element: <MainPage />,
      },
      {
        path: "signup",
        element: <SignUpForm />,
      },
    ],
  },
]);
