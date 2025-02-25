import json
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QApplication
from typing import Dict, Any
import os

class ThemeManager:
    def __init__(self):
        self.current_theme = "light"
        self.theme_data: Dict[str, Any] = {}
        self.load_themes()

    def load_themes(self):
        """Load theme data from JSON files"""
        theme_files = {
            "light": "app/resources/theme_light.json",
            "dark": "app/resources/theme_dark.json"
        }
        
        for theme_name, file_path in theme_files.items():
            try:
                with open(file_path, "r") as f:
                    self.theme_data[theme_name] = json.load(f)
            except Exception as e:
                print(f"Error loading theme '{theme_name}': {e}")

    def apply_theme(self, theme_name: str) -> bool:
        """Apply the specified theme to the application"""
        if theme_name not in self.theme_data:
            return False

        self.current_theme = theme_name
        theme = self.theme_data[theme_name]
        
        # Create palette for the theme
        palette = QPalette()
        colors = theme["colors"]
        
        # Set window/background colors
        palette.setColor(QPalette.ColorRole.Window, QColor(colors["window"]))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(colors["text"]))
        palette.setColor(QPalette.ColorRole.Base, QColor(colors["background"]))
        palette.setColor(QPalette.ColorRole.AlternateBase, QColor(colors["secondary"]))
        
        # Set button colors
        palette.setColor(QPalette.ColorRole.Button, QColor(colors["primary"]))
        palette.setColor(QPalette.ColorRole.ButtonText, QColor(colors["foreground"]))
        
        # Set highlight colors
        palette.setColor(QPalette.ColorRole.Highlight, QColor(colors["accent"]))
        palette.setColor(QPalette.ColorRole.HighlightedText, QColor(colors["foreground"]))
        
        # Set text colors
        palette.setColor(QPalette.ColorRole.Text, QColor(colors["text"]))
        palette.setColor(QPalette.ColorRole.PlaceholderText, QColor(colors["textSecondary"]))
        
        # Apply the palette
        QApplication.instance().setPalette(palette)
        
        # Load and apply stylesheet
        stylesheet = self._generate_stylesheet(theme["styles"])
        QApplication.instance().setStyleSheet(stylesheet)
        
        return True

    def _generate_stylesheet(self, styles: Dict[str, Dict[str, str]]) -> str:
        """Generate Qt stylesheet from theme styles"""
        stylesheet = []
        
        for widget, properties in styles.items():
            style_block = [f"{widget} {{"]
            for prop, value in properties.items():
                style_block.append(f"    {prop}: {value};")
            style_block.append("}")
            stylesheet.append("\n".join(style_block))
        
        return "\n\n".join(stylesheet)

    def toggle_theme(self) -> str:
        """Toggle between light and dark themes"""
        new_theme = "dark" if self.current_theme == "light" else "light"
        self.apply_theme(new_theme)
        return new_theme

    def get_color(self, color_name: str) -> str:
        """Get color value from current theme"""
        if self.current_theme in self.theme_data:
            return self.theme_data[self.current_theme]["colors"].get(color_name, "")
        return ""

    def get_style(self, widget_name: str) -> Dict[str, str]:
        """Get widget style from current theme"""
        if self.current_theme in self.theme_data:
            return self.theme_data[self.current_theme]["styles"].get(widget_name, {})
        return {}

# Create global theme manager instance
theme_manager = ThemeManager()
