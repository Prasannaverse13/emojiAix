# AI-Powered Emoji Generator

A modern Windows desktop application that generates custom emojis using AI-powered spectrogram generation and image processing. The application leverages Qualcomm AI Hub's Riffusion model for spectrogram generation and advanced image processing techniques for stylization.

## 🎯 Features

- Text-to-Emoji Generation using Riffusion AI
- Multiple Emoji Styles (Cartoon, Pixel, Neon, Minimal)
- Color and Style Customization
- Export Options (PNG, SVG)
- Modern UI with Light/Dark Theme Support

## 🛠 Technology Stack

- **Frontend UI**: PyQt6 for Windows desktop interface
- **AI Models**: 
  - Riffusion (Located in `app/services/riffusion_service.py`)
  - IBM Granite v3.1.8B Instruct (To be integrated in cloud deployment)
- **Image Processing**: OpenCV and PIL (Located in `app/services/image_processor.py`)
- **Styling**: Custom QSS themes (Located in `app/resources/`)

## 📁 Project Structure

```
app/
├── main.py                 # Application entry point
├── ui/                     # UI Components
│   ├── main_window.py     # Main application window
│   ├── emoji_canvas.py    # Emoji preview canvas
│   └── controls_panel.py  # User input controls
├── services/              # Core Services
│   ├── riffusion_service.py   # Riffusion API integration
│   └── image_processor.py     # Image processing utilities
├── resources/             # Assets & Themes
│   ├── styles.qss        # Base styling
│   ├── theme_light.json  # Light theme
│   └── theme_dark.json   # Dark theme
└── utils/                # Utilities
    └── theme.py         # Theme management
```

## 🚀 Development Setup

1. Install Python dependencies:
```bash
pip install PyQt6 opencv-python numpy pillow requests
```

2. Run the application locally:
```bash
python app/main.py
```

## ☁️ Cloud Deployment Steps

To deploy on Qualcomm Cloud Device (Snapdragon Elite X):

1. Install Qualcomm AI Hub SDK:
```bash
pip install qai-hub qai-hub-models[ffnet_40s]
```

2. Configure API Token:
```bash
qai-hub configure --api_token YOUR_API_TOKEN
```

3. Install model dependencies:
```bash
pip install "qai-hub[torch]"
```

## 🔍 AI Model Integration

### Riffusion Model
- **Location**: `app/services/riffusion_service.py`
- **Purpose**: Generates spectrograms from text prompts
- **API Integration**: Uses Qualcomm AI Hub's Riffusion endpoint
- **Key Function**: `generate_spectrogram()`

### IBM Granite v3.1.8B Instruct (Cloud Deployment)
- Will be integrated during cloud deployment
- Used for enhanced text processing and prompt optimization
- Implementation will be added to Qualcomm Cloud Device setup

## 🎨 Features & Usage

1. **Text Input**: Enter descriptive text for your emoji
2. **Style Selection**: Choose from multiple styles:
   - Cartoon (Default)
   - Pixel Art
   - Neon
   - Minimal
3. **Customization**:
   - Adjust colors
   - Modify expression intensity
   - Add accessories
4. **Export Options**:
   - Save as PNG/SVG
   - Share directly

## 🔐 API Configuration

The application requires a Qualcomm AI Hub API token for cloud features:
- Development token is configured in `app/services/riffusion_service.py`
- For cloud deployment, use the Qualcomm Cloud Device configuration

## 📝 Notes

- Local development uses a simplified version of the AI processing
- Full AI capabilities (including IBM Granite) are available when deployed to Qualcomm Cloud Device
- For optimal performance, run the final version on Snapdragon Elite X hardware
