import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { motion } from "framer-motion";

export default function SearchBar({
  url,
  setUrl,
  handleSearch,
}: {
  url: string;
  setUrl: (url: string) => void;
  handleSearch: () => void;
}) {
  return (
    <motion.div
      initial={{ opacity: 0, y: -20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
      className="flex gap-4"
    >
      <Input
        type="text"
        placeholder="Enter product URL"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        className="flex-1 bg-white/10 backdrop-blur-md border-white/20 text-white placeholder:text-white/50"
      />
      <Button
        onClick={handleSearch}
        className="bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-700 hover:to-pink-700"
      >
        Search
      </Button>
    </motion.div>
  );
}