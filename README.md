📝 Notes App (Flask)

A simple and modern Notes Web Application built using Flask, allowing users to create, view, and manage notes through a clean UI. This project is suitable for learning Flask fundamentals and showcasing a full-stack mini project.

🚀 Features

Create, view, and delete notes

Simple and clean UI

Flask backend with HTML/CSS frontend

Lightweight and beginner-friendly

Ready for free cloud deployment (Render/Railway)

🛠️ Tech Stack

Backend: Python, Flask

Frontend: HTML, CSS, JavaScript

Server: Gunicorn

Version Control: Git & GitHub

📁 Project Structure
Notes-app/
│
├── app.py                # Main Flask application
├── requirements.txt      # Python dependencies
├── Procfile              # Deployment configuration
├── static/               # CSS, JS, images
├── templates/            # HTML templates
└── README.md

⚙️ Installation (Local Setup)

Clone the repository

git clone https://github.com/avinash-reddy-2005/Notes-app.git
cd Notes-app


Create and activate virtual environment

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate


Install dependencies

pip install -r requirements.txt


Run the application

python app.py


Open in browser:

http://127.0.0.1:5000

🌐 Deployment (Free)

This project can be deployed for free using:

Render (Recommended)

Railway

Required files for deployment

requirements.txt

Procfile

Procfile

web: gunicorn app:app

📌 Live Demo

Add your deployed link here after deployment
Example:

https://notes-app.onrender.com

📚 Learning Outcomes

Flask routing and templates

Backend–frontend integration

Basic deployment setup

Project structuring for production

🤝 Contributing

Contributions are welcome.
Feel free to fork the repository and submit a pull request.

👤 Author

Avinash Reddy
GitHub: https://github.com/avinash-reddy-2005
