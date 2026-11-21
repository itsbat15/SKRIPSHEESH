"use client";
import { useState } from "react";
import ElegantNavbar from "@/components/landing-elegant/Navbar";
import HeroSection from "@/components/landing-elegant/HeroSection";
import ServicesSection from "@/components/landing-elegant/ServicesSection";
import AboutSection from "@/components/landing-elegant/AboutSection";
import ArticlesSection from "@/components/landing-elegant/ArticlesSection";
import WhyChooseUs from "@/components/landing-elegant/WhyChooseUs";
import TestimonialsSection from "@/components/landing-elegant/TestimonialsSection";
import TeamSection from "@/components/landing-elegant/TeamSection";
import GallerySection from "@/components/landing-elegant/GallerySection";
import BranchLocations from "@/components/landing-elegant/BranchLocations";
import FAQSection from "@/components/landing-elegant/FAQSection";
import RegistrationModal from "@/components/landing/RegistrationModal";

export default function ElegantHome() {
  const [isRegistrationOpen, setIsRegistrationOpen] = useState(false);

  return (
    <>
      <ElegantNavbar onOpenRegistration={() => setIsRegistrationOpen(true)} />
      <HeroSection onOpenRegistration={() => setIsRegistrationOpen(true)} />
      <ServicesSection />
      <AboutSection />
      <GallerySection />
      <ArticlesSection />
      <WhyChooseUs />
      <TestimonialsSection />
      <TeamSection />
      <BranchLocations />
      <FAQSection />
      <RegistrationModal
        isOpen={isRegistrationOpen}
        onClose={() => setIsRegistrationOpen(false)}
      />
    </>
  );
}
