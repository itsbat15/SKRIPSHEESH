"use client";
import { motion } from "framer-motion";
import { keunggulan } from "@/data/siteData";
import { useState, useEffect, useRef } from "react";
import {
  GraduationCap, Gift, Shield, BookOpen,
  Calendar, Wallet, Users, MessageCircle,
} from "lucide-react";

const iconMap = {
  GraduationCap, Gift, Shield, BookOpen,
  Calendar, Wallet, Users, MessageCircle,
};

export default function WhyChooseUs() {
  const [activeIndex, setActiveIndex] = useState(0);

  useEffect(() => {
    const handleScroll = () => {
      const items = document.querySelectorAll('.why-item');
      let newActiveIndex = activeIndex;
      let minDistance = Infinity;
      
      // We want to trigger when the item is around the middle-top of the viewport
      const triggerY = window.innerHeight * 0.4; 

      items.forEach((item, index) => {
        const rect = item.getBoundingClientRect();
        // Calculate how close the top of the item is to our trigger line
        const distance = Math.abs(rect.top - triggerY);
        
        if (rect.top < window.innerHeight && rect.bottom > 0) {
           if (distance < minDistance) {
              minDistance = distance;
              newActiveIndex = index;
           }
        }
      });
      
      if (newActiveIndex !== activeIndex) {
        setActiveIndex(newActiveIndex);
      }
    };

    window.addEventListener('scroll', handleScroll);
    handleScroll(); // initialize
    return () => window.removeEventListener('scroll', handleScroll);
  }, [activeIndex]);

  return (
    <section className="bg-[#FEFDF9] relative">
      <div className="max-w-[1440px] mx-auto px-4 sm:px-6 lg:px-8">
        
        <div className="flex flex-col md:flex-row relative">
          
          {/* Left Side: Scrolling Text List */}
          <motion.div 
            initial="hidden"
            whileInView="show"
            viewport={{ once: true, amount: 0.1 }}
            variants={{
              hidden: { opacity: 0 },
              show: {
                opacity: 1,
                transition: { staggerChildren: 0.1 }
              }
            }}
            className="w-full md:w-1/2 py-[20vh] md:py-[30vh] pr-0 md:pr-16 z-10"
          >
            <motion.div variants={{ hidden: { opacity: 0, y: 50 }, show: { opacity: 1, y: 0 } }} className="bg-[#1EAB55] border-[3px] border-[#111118] px-4 py-2 inline-block shadow-[4px_4px_0_0_#111118] mb-12 -rotate-2">
              <h4 className="text-white font-black uppercase tracking-widest text-sm sm:text-base">
                Kenapa Bimbel Artha?
              </h4>
            </motion.div>
            
            <div className="flex flex-col">
              {keunggulan.map((item, index) => {
                const isActive = activeIndex === index;
                return (
                  <motion.div 
                    variants={{ hidden: { opacity: 0, x: -50 }, show: { opacity: 1, x: 0 } }}
                    key={index} 
                    className="why-item border-b-[3px] border-[#111118] py-10 transition-all duration-500 cursor-default"
                  >
                    <h3 className={`text-4xl sm:text-5xl lg:text-6xl font-black uppercase transition-all duration-500 tracking-tighter leading-[1] ${isActive ? "text-[#111118]" : "text-[#111118]/20"}`}>
                      {item.title}.
                    </h3>
                    
                    {/* Expandable Description */}
                    <div 
                      className={`grid transition-all duration-500 ${isActive ? "grid-rows-[1fr] mt-6 opacity-100" : "grid-rows-[0fr] opacity-0"}`}
                    >
                      <div className="overflow-hidden">
                        <p className="text-base sm:text-lg text-[#111118] font-bold uppercase tracking-widest leading-relaxed bg-[#FFD600] border-[3px] border-[#111118] p-4 shadow-[4px_4px_0_0_#111118]">
                          {item.description}
                        </p>
                      </div>
                    </div>
                  </motion.div>
                )
              })}
            </div>
          </motion.div>

          {/* Right Side: Sticky Images/Visuals */}
          <div className="hidden md:flex w-1/2 h-screen sticky top-0 items-center justify-center py-12 pl-8">
            <motion.div 
              initial={{ opacity: 0, scale: 0.9 }}
              whileInView={{ opacity: 1, scale: 1 }}
              viewport={{ once: true }}
              transition={{ duration: 0.5 }}
              className="relative w-full h-[80%] border-[4px] border-[#111118] overflow-hidden bg-[#F5F7FF] shadow-[16px_16px_0_0_#111118]"
            >
               {keunggulan.map((item, index) => {
                  const isActive = activeIndex === index;
                  const IconComp = iconMap[item.icon] || Shield;
                  
                  // Rotate through our brand colors for the background
                  const colors = [
                    { bg: "bg-[#FFD600]", text: "text-[#111118]", card: "text-[#2727E6]" },
                    { bg: "bg-[#1EAB55]", text: "text-white", card: "text-[#FF6600]" },
                    { bg: "bg-[#8AD9E8]", text: "text-[#111118]", card: "text-[#1EAB55]" },
                    { bg: "bg-[#FFBAD2]", text: "text-[#111118]", card: "text-[#2727E6]" },
                    { bg: "bg-[#2727E6]", text: "text-white", card: "text-[#FFD600]" },
                    { bg: "bg-[#FF6600]", text: "text-white", card: "text-[#8AD9E8]" },
                  ];
                  const theme = colors[index % colors.length];

                  return (
                    <motion.div 
                      key={index}
                      initial={{ opacity: 0, y: 50 }}
                      animate={{ opacity: isActive ? 1 : 0, y: isActive ? 0 : 50 }}
                      transition={{ duration: 0.6, type: "spring", stiffness: 100 }}
                      className={`absolute inset-0 flex flex-col items-center justify-center ${theme.bg} ${isActive ? 'z-10' : 'z-0 pointer-events-none'}`}
                    >
                       {/* Background Icon (Abstract) */}
                       <IconComp size={250} className={`${theme.text} opacity-20 absolute`} />
                       
                       {/* Floating Stats/Highlight Card simulating the photo's floating card */}
                       <motion.div 
                         initial={{ y: 50, opacity: 0, rotate: -10 }}
                         animate={{ y: isActive ? 0 : 50, opacity: isActive ? 1 : 0, rotate: isActive ? -3 : -10 }}
                         transition={{ duration: 0.5, delay: 0.2, type: "spring" }}
                         className="absolute bottom-12 left-12 bg-white p-6 shadow-[8px_8px_0_0_#111118] max-w-[280px] border-[4px] border-[#111118]"
                       >
                         <div className={`text-6xl font-black mb-3 tracking-tighter ${theme.card}`}>
                           {index + 1}
                         </div>
                         <p className="text-sm text-[#111118] font-black uppercase tracking-widest leading-relaxed">
                           Membangun keunggulan lewat <br/> {item.title}.
                         </p>
                       </motion.div>
                    </motion.div>
                  )
               })}
            </motion.div>
          </div>

        </div>
      </div>
    </section>
  );
}
