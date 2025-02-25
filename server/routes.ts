import type { Express } from "express";
import { createServer, type Server } from "http";
import { storage } from "./storage";
import { generateSpectrogram } from "./riffusion";

export async function registerRoutes(app: Express): Promise<Server> {
  // Emoji generation endpoint
  app.post("/api/generate-emoji", async (req, res) => {
    try {
      const { prompt } = req.body;
      if (!prompt || typeof prompt !== 'string') {
        return res.status(400).json({ 
          error: "Invalid prompt. Please provide a non-empty text prompt." 
        });
      }

      console.log(`Generating emoji for prompt: "${prompt}"`);
      const spectrogram = await generateSpectrogram(prompt);

      console.log('Successfully generated spectrogram');
      return res.json({ spectrogram });
    } catch (error) {
      console.error("Error generating emoji:", error);
      const message = error instanceof Error ? error.message : 'Unknown error';
      return res.status(500).json({ 
        error: "Failed to generate emoji. Please try again.",
        details: message
      });
    }
  });

  const httpServer = createServer(app);
  return httpServer;
}