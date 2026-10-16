"use client";
import { marqueeTexts } from "@/data/siteData";

export default function MarqueeBanner() {
  // Double the items for seamless infinite scroll
  const items = [...marqueeTexts, ...marqueeTexts, ...marqueeTexts, ...marqueeTexts];

  return (
    <div className="relative bg-[#2727E6] text-white py-2.5 overflow-hidden border-b border-[#111118]/10">
      <div className="flex w-max animate-marquee whitespace-nowrap">
        {items.map((text, i) => (
          <span key={i} className="flex items-center mx-6 text-xs sm:text-sm font-bold tracking-[0.15em] uppercase">
            <span className="w-1.5 h-1.5 rounded-full bg-white/60 mr-4 shrink-0" />
            {text}
          </span>
        ))}
      </div>
    </div>
  );
}
