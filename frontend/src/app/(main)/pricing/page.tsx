"use client";

import { motion } from "framer-motion";
import {
  Check,
  Sparkles,
  MessageSquare,
  Camera,
  FileText,
  Settings,
  Video,
  Code,
  FlaskConical,
} from "lucide-react";
import { Button } from "@/components/ui/button";
import Link from "next/link";
import { useState } from "react";
import TextReveal from "@/components/animations/TextReveal";
import { useMouseWheelScroll } from "@/hooks/use-mouse-wheel-scroll";

const plans = [
  {
    name: "Plus",
    price: "$25",
    period: "USD / month",
    slogan: "More access to advanced intelligence",
    currentPlan: false,
    features: [
      { text: "GPT-grade TradeBerg reasoning with finance focus", icon: Sparkles },
      { text: "Expanded messaging and uploads for trading insights", icon: MessageSquare },
      { text: "Expanded and faster chart/image analysis", icon: Camera },
      { text: "Expanded memory and context per chat", icon: FileText },
      { text: "Deep research agent mode for markets", icon: FlaskConical },
      { text: "Projects, tasks, custom strategies", icon: Settings },
    ],
    footer: "Limits apply",
    footerLink: "Limits apply",
  },
  {
    name: "Pro",
    price: "$250",
    period: "USD / month",
    slogan: "Full access to institutional‑grade TradeBerg",
    currentPlan: false,
    features: [
      { text: "Pro‑level reasoning and execution agent", icon: Sparkles },
      { text: "Unlimited messages, uploads and chart screenshots", icon: MessageSquare },
      { text: "Maximum context window for complex strategies", icon: FileText },
      { text: "Advanced deep research and agent mode", icon: FlaskConical },
      { text: "Expanded projects, tasks and strategy workspaces", icon: Settings },
      { text: "Priority-speed data + execution pipelines", icon: Video },
      { text: "API access for algorithmic trading", icon: Code },
    ],
    footer: "Unlimited subject to fair‑use guardrails. Learn more",
    footerLink: "Learn more",
  },
];

export default function PricingPage() {
  const [planType, setPlanType] = useState<"Personal" | "Business">("Personal");
  const scrollRef = useMouseWheelScroll<HTMLDivElement>();

  return (
    <div
      ref={scrollRef}
      className="flex-1 flex flex-col h-full overflow-y-auto show-scrollbar-on-hover bg-background"
    >
      <div className="max-w-7xl mx-auto px-4 py-8 w-full">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
          className="mb-8"
        >
          <TextReveal className="text-center mb-6">
            <h1 className="text-2xl font-semibold text-foreground">
              Upgrade your plan
            </h1>
          </TextReveal>

          {/* Toggle */}
          <div className="flex justify-center mb-8">
            <div className="inline-flex rounded-full border border-[var(--tradeberg-card-border)] bg-[var(--tradeberg-card-bg)] p-1 shadow-[0_10px_30px_rgba(0,0,0,0.55)]">
              <button
                onClick={() => setPlanType("Personal")}
                className={`px-6 py-2 rounded-full text-sm font-medium transition-colors ${
                  planType === "Personal"
                    ? "bg-white text-black shadow-sm"
                    : "text-[var(--tradeberg-text-secondary)] hover:text-[var(--tradeberg-text-primary)]"
                }`}
              >
                Personal
              </button>
              <button
                onClick={() => setPlanType("Business")}
                className={`px-6 py-2 rounded-full text-sm font-medium transition-colors ${
                  planType === "Business"
                    ? "bg-white text-black shadow-sm"
                    : "text-[var(--tradeberg-text-secondary)] hover:text-[var(--tradeberg-text-primary)]"
                }`}
              >
                Business
              </button>
            </div>
          </div>
        </motion.div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-5xl mx-auto">
          {plans.map((plan, index) => {
            return (
              <motion.div
                key={plan.name}
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5, delay: index * 0.1 }}
                className="flex flex-col rounded-2xl p-6 bg-[var(--tradeberg-card-bg)] border border-[var(--tradeberg-card-border)] shadow-[0_20px_45px_rgba(0,0,0,0.65)]"
              >
                <div className="mb-4">
                  <h3 className="text-xl font-semibold text-foreground mb-2">
                    {plan.name}
                  </h3>
                  <div className="mb-3">
                  <div className="text-sm text-foreground mb-1">
                    {plan.price} <span className="text-xs text-[var(--tradeberg-text-secondary)]">{plan.period}</span>
                  </div>
                  <p className="text-sm text-[var(--tradeberg-text-secondary)]">
                      {plan.slogan}
                    </p>
                  </div>
                </div>

                <div className="flex-1 mb-6">
                  <ul className="space-y-3">
                    {plan.features.map((feature, idx) => {
                      const Icon = feature.icon;
                      return (
                        <li key={idx} className="flex items-start gap-3">
                          <Icon className="w-4 h-4 text-muted-foreground flex-shrink-0 mt-0.5" />
                          <span className="text-sm text-foreground">
                            {feature.text}
                          </span>
                        </li>
                      );
                    })}
                  </ul>
                </div>

                <div className="mt-auto">
                  <Button
                    className="w-full rounded-full bg-white text-black hover:bg-gray-200"
                    asChild
                  >
                    <Link href="/billing">Get {plan.name}</Link>
                  </Button>

                  <p className="text-xs text-[var(--tradeberg-text-secondary)] mt-3 text-center">
                    {plan.footer}{" "}
                    {plan.footerLink && (
                      <Link
                        href="#"
                        className="underline hover:text-foreground"
                      >
                        {plan.footerLink}
                      </Link>
                    )}
                  </p>
                </div>
              </motion.div>
            );
          })}
        </div>

        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.5, delay: 0.4 }}
          className="mt-12 text-center"
        >
          <div className="flex items-center justify-center gap-2 text-sm text-muted-foreground mb-4">
            <div className="flex items-center gap-1">
              <div className="w-4 h-4 rounded-full bg-muted-foreground/20 flex items-center justify-center">
                <div className="w-2 h-2 rounded-full bg-muted-foreground"></div>
              </div>
            </div>
            <span>
              Need more capabilities for your business?{" "}
              <Link href="#" className="underline hover:text-foreground">
                See TradeBerg Enterprise
              </Link>
            </span>
          </div>
        </motion.div>
      </div>
    </div>
  );
}
