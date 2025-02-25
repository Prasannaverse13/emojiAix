from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QLineEdit, QPushButton, 
                          QLabel, QComboBox, QSlider, QColorDialog)
from PyQt6.QtCore import Qt
from ..services.riffusion_service import RiffusionService

class ControlsPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        self.riffusion = RiffusionService()
    
    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(20)
        
        # Text input
        text_label = QLabel("Enter text for emoji:")
        self.text_input = QLineEdit()
        self.text_input.setPlaceholderText("e.g. happy robot")
        layout.addWidget(text_label)
        layout.addWidget(self.text_input)
        
        # Style selector
        style_label = QLabel("Emoji style:")
        self.style_combo = QComboBox()
        self.style_combo.addItems(["Cartoon", "Pixel", "Neon", "Minimal"])
        layout.addWidget(style_label)
        layout.addWidget(self.style_combo)
        
        # Color controls
        color_label = QLabel("Color theme:")
        self.color_btn = QPushButton("Choose Color")
        self.color_btn.clicked.connect(self.choose_color)
        layout.addWidget(color_label)
        layout.addWidget(self.color_btn)
        
        # Expression intensity
        intensity_label = QLabel("Expression intensity:")
        self.intensity_slider = QSlider(Qt.Orientation.Horizontal)
        self.intensity_slider.setMinimum(0)
        self.intensity_slider.setMaximum(100)
        self.intensity_slider.setValue(50)
        layout.addWidget(intensity_label)
        layout.addWidget(self.intensity_slider)
        
        # Generate button
        self.generate_btn = QPushButton("Generate Emoji")
        self.generate_btn.clicked.connect(self.generate_emoji)
        layout.addWidget(self.generate_btn)
        
        # Theme toggle
        self.theme_btn = QPushButton("Toggle Theme")
        self.theme_btn.clicked.connect(self.toggle_theme)
        layout.addWidget(self.theme_btn)
        
        # Add vertical spacer
        layout.addStretch()
    
    def choose_color(self):
        """Open color picker"""
        color = QColorDialog.getColor()
        if color.isValid():
            # Apply color to emoji generation
            pass
    
    def generate_emoji(self):
        """Generate emoji using Riffusion"""
        text = self.text_input.text()
        if text:
            # Show loading state
            self.generate_btn.setEnabled(False)
            self.generate_btn.setText("Generating...")
            
            # Generate spectrogram
            spectrogram = self.riffusion.generate_spectrogram(
                text,
                style=self.style_combo.currentText(),
                intensity=self.intensity_slider.value()
            )
            
            # Update canvas
            if self.parent():
                self.parent().canvas.update_preview(spectrogram)
            
            # Reset button
            self.generate_btn.setEnabled(True)
            self.generate_btn.setText("Generate Emoji")
    
    def toggle_theme(self):
        """Toggle between light/dark theme"""
        if self.parent():
            current_theme = getattr(self, '_current_theme', 'light')
            new_theme = 'dark' if current_theme == 'light' else 'light'
            self.parent().apply_theme(new_theme)
            self._current_theme = new_theme
