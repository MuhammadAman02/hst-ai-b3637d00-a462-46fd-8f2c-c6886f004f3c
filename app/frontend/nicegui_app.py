from nicegui import ui, app
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import os
from datetime import datetime

# Configure the app
app.title = "ML Engineer Portfolio"
app.favicon = "🧠"

# Sample data for skills visualization
skills_data = {
    'Skill': ['Python', 'TensorFlow', 'PyTorch', 'Scikit-Learn', 'Deep Learning', 
              'NLP', 'Computer Vision', 'MLOps', 'Data Visualization', 'SQL'],
    'Proficiency': [95, 90, 85, 92, 88, 80, 85, 75, 90, 85]
}

# Sample project data
projects = [
    {
        'title': 'Computer Vision for Medical Imaging',
        'description': 'Developed a deep learning model to detect anomalies in medical scans with 94% accuracy.',
        'technologies': ['PyTorch', 'CNN', 'Transfer Learning', 'DICOM'],
        'image': 'static/images/medical_imaging.jpg',
        'github': 'https://github.com/username/medical-imaging',
    },
    {
        'title': 'NLP for Customer Sentiment Analysis',
        'description': 'Built an end-to-end pipeline for analyzing customer feedback using BERT-based models.',
        'technologies': ['Transformers', 'HuggingFace', 'BERT', 'Flask API'],
        'image': 'static/images/nlp_sentiment.jpg',
        'github': 'https://github.com/username/sentiment-analysis',
    },
    {
        'title': 'Time Series Forecasting for Energy Consumption',
        'description': 'Implemented LSTM and Prophet models to predict energy usage patterns for smart grid optimization.',
        'technologies': ['TensorFlow', 'LSTM', 'Prophet', 'Time Series Analysis'],
        'image': 'static/images/time_series.jpg',
        'github': 'https://github.com/username/energy-forecasting',
    },
    {
        'title': 'MLOps Pipeline for Model Deployment',
        'description': 'Created a CI/CD pipeline for ML models with automated testing, versioning, and monitoring.',
        'technologies': ['Docker', 'Kubernetes', 'GitHub Actions', 'MLflow'],
        'image': 'static/images/mlops.jpg',
        'github': 'https://github.com/username/mlops-pipeline',
    }
]

# Publications data
publications = [
    {
        'title': 'Advances in Transfer Learning for Low-Resource Medical Imaging',
        'journal': 'Journal of Machine Learning Research',
        'year': 2023,
        'link': 'https://example.com/paper1',
        'authors': 'Your Name, Collaborator One, Collaborator Two'
    },
    {
        'title': 'Efficient Transformer Architectures for Edge Deployment',
        'journal': 'Conference on Neural Information Processing Systems (NeurIPS)',
        'year': 2022,
        'link': 'https://example.com/paper2',
        'authors': 'Your Name, Collaborator Three'
    },
    {
        'title': 'Explainable AI Methods for Healthcare Applications',
        'journal': 'IEEE Transactions on Medical Imaging',
        'year': 2021,
        'link': 'https://example.com/paper3',
        'authors': 'Collaborator Four, Your Name, Collaborator Five'
    }
]

# Create a responsive layout with custom CSS
@ui.page('/')
def portfolio_page():
    with ui.header().classes('bg-blue-900 text-white'):
        ui.label('ML Engineer Portfolio').classes('text-h4 q-my-md')
        with ui.row().classes('items-center ml-auto'):
            ui.link('About', '#about').classes('text-white q-mx-md')
            ui.link('Skills', '#skills').classes('text-white q-mx-md')
            ui.link('Projects', '#projects').classes('text-white q-mx-md')
            ui.link('Publications', '#publications').classes('text-white q-mx-md')
            ui.link('Contact', '#contact').classes('text-white q-mx-md')
    
    # Hero section
    with ui.section().classes('bg-blue-800 text-white text-center py-20'):
        ui.label('John Doe').classes('text-h2 q-mb-md')
        ui.label('Machine Learning Engineer').classes('text-h4 q-mb-lg')
        ui.label('Building intelligent systems that solve real-world problems').classes('text-h6')
        with ui.row().classes('justify-center q-mt-lg'):
            ui.button('View Projects', on_click=lambda: ui.navigate('#projects')).classes('bg-white text-blue-800')
            ui.button('Contact Me', on_click=lambda: ui.navigate('#contact')).classes('bg-transparent border-white text-white q-ml-md')
    
    # About section
    with ui.section().classes('py-16 px-4').style('max-width: 1200px; margin: 0 auto;'):
        ui.label('About Me', id='about').classes('text-h3 q-mb-xl text-center text-blue-900')
        with ui.row().classes('items-start'):
            with ui.column().classes('col-12 col-md-4 q-pa-md'):
                ui.image('static/images/profile.jpg').classes('rounded-borders').style('width: 100%; max-width: 300px; margin: 0 auto;')
            
            with ui.column().classes('col-12 col-md-8 q-pa-md'):
                ui.label('''
                I'm a Machine Learning Engineer with 5+ years of experience developing and deploying ML solutions across healthcare, finance, and retail domains. 
                My expertise lies in deep learning, computer vision, and natural language processing, with a focus on creating scalable and production-ready systems.
                
                Previously, I worked at TechCorp where I led the development of an automated medical imaging analysis platform that reduced diagnosis time by 60%. 
                I hold a Master's degree in Computer Science with a specialization in Artificial Intelligence from Stanford University.
                
                My approach combines strong theoretical foundations with practical engineering skills to deliver ML systems that create real business impact.
                ''').classes('text-body1')
                
                with ui.row().classes('q-mt-md'):
                    ui.button('Resume', icon='description').classes('bg-blue-800 text-white')
                    ui.button('LinkedIn', icon='link').classes('bg-blue-600 text-white q-ml-sm')
                    ui.button('GitHub', icon='code').classes('bg-gray-800 text-white q-ml-sm')
    
    # Skills section
    with ui.section().classes('py-16 px-4 bg-gray-100').style('max-width: 1200px; margin: 0 auto;'):
        ui.label('Skills', id='skills').classes('text-h3 q-mb-xl text-center text-blue-900')
        
        with ui.row().classes('items-start'):
            # Skills visualization
            with ui.column().classes('col-12 col-md-6 q-pa-md'):
                df = pd.DataFrame(skills_data)
                fig = px.bar(df, x='Skill', y='Proficiency', 
                             color='Proficiency', 
                             color_continuous_scale='Blues',
                             labels={'Proficiency': 'Expertise Level (%)'})
                fig.update_layout(
                    title='Technical Skills',
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    margin=dict(l=20, r=20, t=40, b=20),
                    height=400
                )
                ui.plotly(fig).classes('w-full')
            
            # Skills categories
            with ui.column().classes('col-12 col-md-6 q-pa-md'):
                with ui.card().classes('w-full'):
                    ui.label('Skill Categories').classes('text-h5 q-mb-md text-blue-900')
                    
                    with ui.expansion('Machine Learning', icon='psychology').classes('q-mb-sm'):
                        ui.label('• Supervised Learning: Classification, Regression')
                        ui.label('• Unsupervised Learning: Clustering, Dimensionality Reduction')
                        ui.label('• Reinforcement Learning: Q-Learning, Policy Gradients')
                        ui.label('• Ensemble Methods: Random Forests, Gradient Boosting')
                    
                    with ui.expansion('Deep Learning', icon='memory').classes('q-mb-sm'):
                        ui.label('• Neural Network Architectures: CNN, RNN, LSTM, GAN')
                        ui.label('• Frameworks: TensorFlow, PyTorch, Keras')
                        ui.label('• Transfer Learning & Fine-tuning')
                        ui.label('• Model Optimization & Quantization')
                    
                    with ui.expansion('MLOps & Engineering', icon='engineering').classes('q-mb-sm'):
                        ui.label('• CI/CD for ML: GitHub Actions, Jenkins')
                        ui.label('• Containerization: Docker, Kubernetes')
                        ui.label('• Model Serving: TensorFlow Serving, TorchServe')
                        ui.label('• Monitoring: Prometheus, Grafana')
                    
                    with ui.expansion('Data Engineering', icon='storage').classes('q-mb-sm'):
                        ui.label('• ETL Pipelines: Airflow, Spark')
                        ui.label('• Databases: SQL, MongoDB, Redis')
                        ui.label('• Big Data: Hadoop, Spark')
                        ui.label('• Data Visualization: Matplotlib, Plotly, Tableau')
    
    # Projects section
    with ui.section().classes('py-16 px-4').style('max-width: 1200px; margin: 0 auto;'):
        ui.label('Projects', id='projects').classes('text-h3 q-mb-xl text-center text-blue-900')
        
        with ui.grid(columns=2).classes('q-col-gutter-md'):
            for project in projects:
                with ui.card().classes('w-full'):
                    ui.image(project['image']).classes('w-full')
                    with ui.card_section():
                        ui.label(project['title']).classes('text-h5 text-blue-900')
                        ui.label(project['description']).classes('text-body1 q-mb-md')
                        
                        with ui.row().classes('q-gutter-xs'):
                            for tech in project['technologies']:
                                ui.badge(tech).classes('bg-blue-200 text-blue-900')
                        
                        with ui.row().classes('q-mt-md'):
                            ui.button('View Details', icon='visibility').classes('bg-blue-800 text-white')
                            ui.button('GitHub', icon='code', on_click=lambda url=project['github']: ui.open(url)).classes('bg-gray-800 text-white q-ml-sm')
    
    # Publications section
    with ui.section().classes('py-16 px-4 bg-gray-100').style('max-width: 1200px; margin: 0 auto;'):
        ui.label('Publications', id='publications').classes('text-h3 q-mb-xl text-center text-blue-900')
        
        for pub in publications:
            with ui.card().classes('q-mb-md w-full'):
                with ui.card_section():
                    ui.label(pub['title']).classes('text-h5 text-blue-900')
                    ui.label(pub['authors']).classes('text-subtitle1 text-gray-700')
                    ui.label(f"{pub['journal']} ({pub['year']})").classes('text-body2 text-gray-600')
                
                with ui.card_actions().classes('justify-end'):
                    ui.button('Read Paper', icon='article', on_click=lambda url=pub['link']: ui.open(url)).classes('bg-blue-800 text-white')
    
    # Contact section
    with ui.section().classes('py-16 px-4').style('max-width: 1200px; margin: 0 auto;'):
        ui.label('Contact Me', id='contact').classes('text-h3 q-mb-xl text-center text-blue-900')
        
        with ui.row().classes('justify-center'):
            with ui.card().classes('w-full').style('max-width: 600px;'):
                with ui.card_section():
                    ui.label('Get in touch').classes('text-h5 text-blue-900 q-mb-md')
                    
                    with ui.row().classes('q-col-gutter-md'):
                        with ui.column().classes('col-12 col-md-6'):
                            ui.input('Name').classes('w-full')
                        with ui.column().classes('col-12 col-md-6'):
                            ui.input('Email').classes('w-full')
                    
                    ui.input('Subject').classes('w-full q-mt-md')
                    ui.textarea('Message').classes('w-full q-mt-md')
                    
                    with ui.row().classes('justify-end q-mt-md'):
                        ui.button('Send Message', icon='send').classes('bg-blue-800 text-white')
    
    # Footer
    with ui.footer().classes('bg-blue-900 text-white text-center py-8'):
        ui.label('© 2023 John Doe - ML Engineer').classes('text-subtitle1')
        with ui.row().classes('justify-center q-mt-sm'):
            ui.button(icon='mail').props('flat round').classes('text-white')
            ui.button(icon='code').props('flat round').classes('text-white')
            ui.button(icon='rss_feed').props('flat round').classes('text-white')
            ui.button(icon='school').props('flat round').classes('text-white')

# Add custom CSS
ui.add_head_html('''
<style>
    body {
        font-family: 'Roboto', sans-serif;
    }
    section {
        scroll-margin-top: 80px;
    }
    .q-card {
        transition: transform 0.3s ease;
    }
    .q-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }
    @media (max-width: 600px) {
        .text-h2 {
            font-size: 2.5rem;
        }
        .text-h4 {
            font-size: 1.5rem;
        }
    }
</style>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
''')

# Add viewport meta tag for responsive design
ui.add_head_html('<meta name="viewport" content="width=device-width, initial-scale=1.0">')