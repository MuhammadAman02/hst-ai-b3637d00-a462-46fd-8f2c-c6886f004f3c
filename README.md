# ML Engineer Portfolio

A professional portfolio website for Machine Learning Engineers to showcase their skills, projects, and publications.

## Features

- **Professional Profile**: Showcase your experience, education, and professional background
- **Skills Visualization**: Interactive charts displaying technical proficiency
- **Project Showcase**: Highlight ML projects with descriptions and technologies used
- **Publications Section**: List academic papers and research contributions
- **Contact Form**: Allow visitors to get in touch
- **Responsive Design**: Looks great on desktop, tablet, and mobile devices

## Technology Stack

- **Framework**: NiceGUI (Python-native web framework)
- **Data Visualization**: Plotly
- **Data Processing**: Pandas
- **Image Processing**: Pillow
- **Environment Management**: python-dotenv

## Getting Started

### Prerequisites

- Python 3.9 or higher

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/ml-engineer-portfolio.git
   cd ml-engineer-portfolio
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   ```
   cp .env.example .env
   # Edit .env file with your settings
   ```

### Running the Application

1. Start the application:
   ```
   python main.py
   ```

2. Open your browser and navigate to:
   ```
   http://localhost:8000
   ```

## Customization

### Updating Profile Information

Edit the data in `app/frontend/nicegui_app.py` to update:
- Personal information
- Skills and proficiency levels
- Projects and their details
- Publications

### Adding Images

1. Place your images in the `static/images/` directory
2. Reference them in the code using the path `static/images/your_image.jpg`

### Styling

The application uses custom CSS for styling. You can modify the styles in the `ui.add_head_html` section of `app/frontend/nicegui_app.py`.

## Deployment

This application can be easily deployed to platforms like Fly.io, Heroku, or any other Python-compatible hosting service.

### Deploying to Fly.io

1. Install the Fly CLI
2. Initialize your app:
   ```
   fly launch
   ```
3. Deploy:
   ```
   fly deploy
   ```

## License

This project is licensed under the MIT License - see the LICENSE file for details.