import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { useState } from "react";
import { useMutation } from "@tanstack/react-query";
import { apiRequest } from "@/lib/queryClient";
import { useToast } from "@/hooks/use-toast";

export default function Home() {
  const [prompt, setPrompt] = useState("");
  const { toast } = useToast();
  const [previewUrl, setPreviewUrl] = useState<string | null>(null);

  const generateEmoji = useMutation({
    mutationFn: async (prompt: string) => {
      const res = await apiRequest("POST", "/api/generate-emoji", { prompt });
      return res.json();
    },
    onSuccess: (data) => {
      setPreviewUrl(data.spectrogram);
      toast({
        title: "Success",
        description: "Emoji generated successfully!",
      });
    },
    onError: (error) => {
      toast({
        title: "Error",
        description: "Failed to generate emoji. Please try again.",
        variant: "destructive",
      });
    },
  });

  return (
    <div className="min-h-screen bg-background p-6">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-4xl font-bold text-center mb-8">AI Emoji Generator</h1>

        <div className="grid md:grid-cols-2 gap-6">
          {/* Controls Panel */}
          <Card>
            <CardContent className="pt-6">
              <div className="space-y-4">
                <div className="space-y-2">
                  <Label>Enter text for emoji</Label>
                  <Input 
                    placeholder="e.g., happy robot"
                    value={prompt}
                    onChange={(e) => setPrompt(e.target.value)}
                  />
                </div>

                <Button 
                  className="w-full"
                  onClick={() => generateEmoji.mutate(prompt)}
                  disabled={generateEmoji.isPending || !prompt.trim()}
                >
                  {generateEmoji.isPending ? "Generating..." : "Generate Emoji"}
                </Button>
              </div>
            </CardContent>
          </Card>

          {/* Preview Panel */}
          <Card>
            <CardContent className="pt-6">
              <div className="aspect-square bg-muted rounded-lg flex items-center justify-center">
                {previewUrl ? (
                  <img 
                    src={previewUrl} 
                    alt="Generated emoji" 
                    className="w-full h-full object-contain rounded-lg"
                  />
                ) : (
                  <p className="text-muted-foreground">Preview will appear here</p>
                )}
              </div>

              <div className="flex gap-2 mt-4">
                <Button 
                  variant="outline" 
                  className="flex-1"
                  disabled={!previewUrl}
                  onClick={() => {
                    // TODO: Implement export
                    toast({
                      description: "Export feature coming soon!",
                    });
                  }}
                >
                  Export
                </Button>
                <Button 
                  variant="outline" 
                  className="flex-1"
                  disabled={!previewUrl}
                  onClick={() => {
                    // TODO: Implement share
                    toast({
                      description: "Share feature coming soon!",
                    });
                  }}
                >
                  Share
                </Button>
              </div>
            </CardContent>
          </Card>
        </div>
      </div>
    </div>
  );
}