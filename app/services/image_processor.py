import cv2
import numpy as np
from PIL import Image

class ImageProcessor:
    @staticmethod
    def spectrogram_to_emoji(spectrogram, style="Cartoon"):
        """Convert spectrogram to emoji-style image"""
        # Convert to RGB if grayscale
        if len(spectrogram.shape) == 2:
            spectrogram = cv2.cvtColor(spectrogram, cv2.COLOR_GRAY2RGB)
        
        # Apply style-specific processing
        if style == "Cartoon":
            processed = ImageProcessor._apply_cartoon_effect(spectrogram)
        elif style == "Pixel":
            processed = ImageProcessor._apply_pixel_effect(spectrogram)
        elif style == "Neon":
            processed = ImageProcessor._apply_neon_effect(spectrogram)
        else:
            processed = ImageProcessor._apply_minimal_effect(spectrogram)
            
        return processed
    
    @staticmethod
    def _apply_cartoon_effect(image):
        """Apply cartoon-style effect"""
        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        
        # Apply bilateral filter
        smooth = cv2.bilateralFilter(image, 9, 75, 75)
        
        # Detect edges
        edges = cv2.adaptiveThreshold(gray, 255,
                                    cv2.ADAPTIVE_THRESH_MEAN_C,
                                    cv2.THRESH_BINARY,
                                    9, 9)
        
        # Combine smooth image with edges
        cartoon = cv2.bitwise_and(smooth, smooth, mask=edges)
        
        return cartoon
    
    @staticmethod
    def _apply_pixel_effect(image):
        """Apply pixel art effect"""
        h, w = image.shape[:2]
        
        # Reduce image size
        temp = cv2.resize(image, (32, 32), interpolation=cv2.INTER_LINEAR)
        
        # Scale back up with nearest neighbor
        pixelated = cv2.resize(temp, (w, h), interpolation=cv2.INTER_NEAREST)
        
        return pixelated
    
    @staticmethod
    def _apply_neon_effect(image):
        """Apply neon glow effect"""
        # Convert to HSV
        hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
        
        # Increase saturation
        hsv[:, :, 1] = cv2.add(hsv[:, :, 1], 50)
        
        # Apply gaussian blur for glow
        blurred = cv2.GaussianBlur(hsv, (0, 0), 3)
        
        # Convert back to RGB
        neon = cv2.cvtColor(blurred, cv2.COLOR_HSV2RGB)
        
        return neon
    
    @staticmethod
    def _apply_minimal_effect(image):
        """Apply minimal/flat effect"""
        # Reduce color palette
        colors = 8
        div = 256 // colors
        image = image // div * div + div // 2
        
        # Apply slight blur
        minimal = cv2.GaussianBlur(image, (3, 3), 0)
        
        return minimal
