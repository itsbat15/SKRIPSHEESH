"use client";
import { useState } from "react";
import HeroSection from "@/components/landing/HeroSection";
import AroundTheWebSection from "@/components/landing/AroundTheWebSection";
import ServicesSection from "@/components/landing/ServicesSection";
import AboutSection from "@/components/landing/AboutSection";
import ArticlesSection from "@/components/landing/ArticlesSection";
import WhyChooseUs from "@/components/landing/WhyChooseUs";
import TestimonialsSection from "@/components/landing/TestimonialsSection";
import BranchLocations from "@/components/landing/BranchLocations";
import TeamSection from "@/components/landing/TeamSection";
import FAQSection from "@/components/landing/FAQSection";
import RegistrationModal from "@/components/landing/RegistrationModal";

export default function Home() {
  const [isRegistrationOpen, setIsRegistrationOpen] = useState(false);

  return (
    <>
      <HeroSection onOpenRegistration={() => setIsRegistrationOpen(true)} />
      <ServicesSection />
      <AboutSection />
      <ArticlesSection />
      <WhyChooseUs />
      <TestimonialsSection />
      <div className="h-16 sm:h-24"></div>
      <TeamSection />
      <div className="h-16 sm:h-24"></div>
      <BranchLocations />
      <FAQSection />
      <RegistrationModal
        isOpen={isRegistrationOpen}
        onClose={() => setIsRegistrationOpen(false)}
      />
    </>
  );
}
