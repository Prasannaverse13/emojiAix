import requests
import numpy as np
from PIL import Image
import io

class RiffusionService:
    def __init__(self):
        self.api_token = "7d563982e5e0be438575aae70773a4a60fce2d19"
        self.api_url = "https://api.qualcomm.com/v1/models/riffusion"
    
    def generate_spectrogram(self, prompt, style="Cartoon", intensity=50):
        """Generate spectrogram from text prompt using Riffusion API"""
        
        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }
        
        data = {
            "prompt": prompt,
            "style": style.lower(),
            "intensity": intensity / 100.0,
        }
        
        try:
            response = requests.post(self.api_url, json=data, headers=headers)
            response.raise_for_status()
            
            # Convert response to spectrogram array
            image_bytes = response.content
            image = Image.open(io.BytesIO(image_bytes))
            spectrogram = np.array(image)
            
            return spectrogram
            
        except requests.exceptions.RequestException as e:
            print(f"Error generating spectrogram: {e}")
            # Return default spectrogram
            return np.zeros((400, 400), dtype=np.uint8)
