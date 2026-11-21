"use client";

import Link from "next/link";
import { LockKeyhole } from "lucide-react";
import { Feedback, Field, Submit, useMutation } from "@/components/dashboard/OperationsUI";

export default function LoginForm() {
  const operation = useMutation("login");
  return (
    <main className="min-h-screen flex items-center justify-center px-5 py-12 bg-section-lavender">
      <div className="w-full max-w-md">
        <Link href="/" className="inline-block mb-5 font-semibold text-primary underline underline-offset-4">← Situs Bimbel Artha</Link>
        <section className="rounded-2xl border-2 border-[#111118] bg-white shadow-[5px_5px_0_0_#111118] overflow-hidden">
          <div className="bg-primary px-7 py-6 text-white">
            <LockKeyhole size={25} aria-hidden="true" />
            <p className="mt-4 font-bold text-sm tracking-widest uppercase">Bimbel Artha</p>
            <h1 className="text-3xl font-extrabold mt-1">Masuk ke SIMBA</h1>
            <p className="mt-2 text-sm">Sistem manajemen operasional cabang dan manajemen pusat.</p>
          </div>
          <form onSubmit={operation.submit} className="grid gap-4 px-7 py-6">
            <Field label="Email" name="email" type="email" autoComplete="username" />
            <Field label="Kata sandi" name="password" type="password" autoComplete="current-password" />
            <Feedback error={operation.error} />
            <Submit busy={operation.busy}>Masuk</Submit>
          </form>
        </section>
      </div>
    </main>
  );
}
