import MainPage from "@/pages/MainPage";
import SignUpPage from "@/pages/SignUpPage";
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
        element: <SignUpPage />,
      },
    ],
  },
]);
