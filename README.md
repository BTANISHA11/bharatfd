# bharatfd

ntroduction
BharatFD is a multilingual FAQ management system designed to simplify the management and retrieval of FAQs in multiple languages. It integrates Redis for caching, supports a WYSIWYG editor for rich-text content, and provides RESTful APIs for seamless interaction.
Features
Multilingual FAQ support
RESTful API for CRUD operations
Redis caching for improved performance
Unit testing with Mocha and Chai
Docker support for containerization
# Installation
Prerequisites
Ensure you have the following installed on your system:
Node.js (v14 or later)
npm
Redis
Docker (optional)
Steps
Clone the Repository
git clone https://github.com/BTANISHA11/bharatfd.git
cd bharatfd
# Install Dependencies
npm install
Set Up Environment Variables Create a .env file in the root directory and add the following:
PORT=8000
MONGO_URI=mongodb+srv://<Your Username>:<Your Password>@cluster0.dp5v4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
REDIS_URI=redis://127.0.0.1:<Your Port>
Running the Application
npm run start
http://localhost:8000/api/faqs
This project is licensed under the MIT License - see the LICENSE file for details.