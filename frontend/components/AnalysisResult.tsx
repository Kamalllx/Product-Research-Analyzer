import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
import { motion } from "framer-motion";
import ReactMarkdown from 'react-markdown';

export default function AnalysisResult({ analysis }: { analysis: string }) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 50 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
    >
      <Card className="bg-white/10 backdrop-blur-md border-white/20">
        <CardHeader>
          <CardTitle className="text-3xl bg-clip-text text-transparent bg-gradient-to-r from-purple-400 to-pink-600">AI Analysis</CardTitle>
        </CardHeader>
        <CardContent>
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.5, duration: 0.5 }}
            className="prose prose-invert max-w-none break-words overflow-wrap-anywhere"
          >
            <ReactMarkdown>{analysis}</ReactMarkdown>
          </motion.div>
        </CardContent>
      </Card>
    </motion.div>
  );
}