import { Plus_Jakarta_Sans, Inter } from "next/font/google";
import { TooltipProvider } from "@/components/ui/tooltip";
import "./globals.css";

const plusJakarta = Plus_Jakarta_Sans({
  variable: "--font-plus-jakarta",
  subsets: ["latin"],
  weight: ["400", "500", "600", "700", "800"],
  display: "swap",
});

const inter = Inter({
  variable: "--font-inter",
  subsets: ["latin"],
  weight: ["400", "500", "600", "700"],
  display: "swap",
});

export const metadata = {
  title: "Bimbel Artha: Bimbingan Belajar Terpercaya di Balikpapan Sejak 1997",
  description:
    "Bimbingan Belajar Artha adalah bimbel terpercaya di Balikpapan sejak 1997. Program Calistung, SD, SMP, SMA, dan Bahasa Inggris dengan 8 cabang, pengajar berpengalaman, dan kelas maksimal 10 anak.",
  keywords:
    "bimbel balikpapan, bimbingan belajar artha, les privat balikpapan, kursus matematika, les bahasa inggris balikpapan, bimbel SD SMP SMA",
  authors: [{ name: "Bimbel Artha Balikpapan" }],
  openGraph: {
    title: "Bimbel Artha: Bimbingan Belajar Terpercaya di Balikpapan",
    description:
      "Raih Prestasi Gemilang Bersama Bimbingan Belajar Yang Terpercaya. 8 Cabang di Balikpapan, Berdiri Sejak 1997.",
    type: "website",
    locale: "id_ID",
    url: "https://bimbelartha.id",
    siteName: "Bimbel Artha Balikpapan",
  },
};

export default function RootLayout({ children }) {
  return (
    <html
      lang="id"
      className={`${plusJakarta.variable} ${inter.variable} h-full antialiased`}
    >
      <body className="min-h-full flex flex-col">
        <TooltipProvider>{children}</TooltipProvider>
      </body>
    </html>
  );
}
