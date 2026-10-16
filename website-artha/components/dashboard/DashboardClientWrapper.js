"use client";
import { ThemeProvider, useTheme } from "./ThemeProvider";

function ThemedWrapper({ children }) {
  const { theme } = useTheme();
  const isDark = theme === "dark";
  return (
    <div
      data-dashboard
      data-theme={theme}
      className={`flex min-h-screen transition-colors duration-300 ${isDark ? "bg-slate-950" : "bg-slate-50"}`}
    >
      {children}
    </div>
  );
}

export default function DashboardClientWrapper({ children }) {
  return (
    <ThemeProvider>
      <ThemedWrapper>{children}</ThemedWrapper>
    </ThemeProvider>
  );
}
