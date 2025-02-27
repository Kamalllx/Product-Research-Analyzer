import { Card, CardHeader, CardTitle, CardDescription, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { motion } from "framer-motion";

export default function ResearchPaperCard({
  paper,
  onDownload,
}: {
  paper: any;
  onDownload: () => void;
}) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.3 }}
    >
      <Card className="bg-white/10 backdrop-blur-md border-white/20">
        <CardHeader>
          <CardTitle className="text-xl bg-clip-text text-transparent bg-gradient-to-r from-purple-400 to-pink-600">{paper.title}</CardTitle>
          <CardDescription className="text-white/70">
            {paper.authors.join(", ")}
          </CardDescription>
        </CardHeader>
        <CardContent>
          <Button
            onClick={onDownload}
            className="w-full bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-700 hover:to-pink-700"
          >
            Download Paper
          </Button>
        </CardContent>
      </Card>
    </motion.div>
  );
}