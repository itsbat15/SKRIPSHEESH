import { redirect } from "next/navigation";
import { currentUser, dashboardFor } from "@/lib/artha-session";
import LoginForm from "./LoginForm";

export const metadata = {title:"Masuk | Bimbel Artha"};

export default async function LoginPage() {
  const user = await currentUser();
  if (user) redirect(dashboardFor(user));
  return <LoginForm />;
}
