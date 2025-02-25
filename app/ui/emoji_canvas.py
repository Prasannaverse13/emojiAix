from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPixmap, QPainter, QPen
import cv2
import numpy as np

class EmojiCanvas(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(400, 400)
        
        layout = QVBoxLayout(self)
        self.preview = QLabel()
        self.preview.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.preview.setMinimumSize(QSize(300, 300))
        layout.addWidget(self.preview)
        
        # Initialize empty canvas
        self.canvas = np.zeros((400, 400, 4), dtype=np.uint8)
        self.update_preview()
    
    def update_preview(self, spectrogram=None):
        """Update the preview with new spectrogram data"""
        if spectrogram is not None:
            # Convert spectrogram to emoji-style image
            self.canvas = self.process_spectrogram(spectrogram)
        
        # Convert numpy array to QPixmap
        height, width = self.canvas.shape[:2]
        bytes_per_line = width * 4
        q_img = QPixmap.fromImage(self.canvas.data, width, height, 
                                bytes_per_line, QPixmap.Format.Format_RGBA8888)
        
        # Scale and display
        scaled = q_img.scaled(300, 300, Qt.AspectRatioMode.KeepAspectRatio, 
                            Qt.TransformationMode.SmoothTransformation)
        self.preview.setPixmap(scaled)
    
    def process_spectrogram(self, spectrogram):
        """Convert spectrogram to emoji-style image"""
        # Apply image processing to create emoji effect
        processed = cv2.cvtColor(spectrogram, cv2.COLOR_GRAY2RGBA)
        
        # Add emoji-style effects
        processed = cv2.GaussianBlur(processed, (5, 5), 0)
        processed = cv2.bilateralFilter(processed, 9, 75, 75)
        
        return processed
    
    def save_emoji(self):
        """Save the emoji as PNG/SVG"""
        # Save logic here
        pass
    
    def share_emoji(self):
        """Share the emoji"""
        # Share logic here
        pass
