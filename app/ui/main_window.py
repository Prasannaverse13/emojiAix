from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                          QPushButton, QLabel, QSpacerItem, QSizePolicy)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon
from .emoji_canvas import EmojiCanvas
from .controls_panel import ControlsPanel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Emoji Generator")
        self.setMinimumSize(1000, 700)
        
        # Create main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QHBoxLayout(main_widget)
        
        # Left panel - Controls
        self.controls = ControlsPanel(self)
        layout.addWidget(self.controls)
        
        # Right panel - Canvas
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        
        # Preview area
        self.canvas = EmojiCanvas()
        right_layout.addWidget(self.canvas)
        
        # Action buttons
        button_layout = QHBoxLayout()
        export_btn = QPushButton("Export")
        export_btn.setIcon(QIcon.fromTheme("document-save"))
        export_btn.clicked.connect(self.export_emoji)
        
        share_btn = QPushButton("Share")
        share_btn.setIcon(QIcon.fromTheme("document-share"))
        share_btn.clicked.connect(self.share_emoji)
        
        button_layout.addWidget(export_btn)
        button_layout.addWidget(share_btn)
        right_layout.addLayout(button_layout)
        
        layout.addWidget(right_panel)
        
        # Set up theme
        self.setup_theme()
    
    def setup_theme(self):
        """Initialize theme settings"""
        with open("app/resources/theme_light.json", "r") as f:
            self.light_theme = f.read()
        with open("app/resources/theme_dark.json", "r") as f:
            self.dark_theme = f.read()
            
        # Default to light theme
        self.apply_theme("light")
    
    def apply_theme(self, theme_name):
        """Apply the selected theme"""
        theme_data = self.light_theme if theme_name == "light" else self.dark_theme
        # Apply theme styles here
        
    def export_emoji(self):
        """Export the generated emoji"""
        self.canvas.save_emoji()
    
    def share_emoji(self):
        """Share the generated emoji"""
        self.canvas.share_emoji()
