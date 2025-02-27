import { motion } from "framer-motion";

export default function AnimatedGradient() {
  return (
    <motion.div
      className="fixed inset-0 z-0 animated-gradient"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ duration: 1 }}
    />
  );
}