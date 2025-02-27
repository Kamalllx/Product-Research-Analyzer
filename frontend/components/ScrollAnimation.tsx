import { motion, useScroll, useTransform } from "framer-motion";
import { ReactNode } from "react";

export default function ScrollAnimation({ children }: { children: ReactNode }) {
  const { scrollYProgress } = useScroll();
  const scale = useTransform(scrollYProgress, [0, 1], [0.9, 1]);

  return (
    <motion.div
      style={{ scale }}
      initial={{ opacity: 0, y: 50 }}
      whileInView={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
    >
      {children}
    </motion.div>
  );
}