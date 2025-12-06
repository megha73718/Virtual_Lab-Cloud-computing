A microservices-based Virtual Lab platform that provides a modular, scalable, and containerized environment for managing virtual experiments. Built with React, Docker, and multiple backend services, it supports user profiling, intelligent scoring, personalized recommendations, and real-time notifications.

🏗️ Architecture Overview This project consists of four microservices and a React frontend, all connected using Docker Compose for seamless orchestration.

🔧 Microservices:

👤 Profile Management Service Handles:
User registration, login & authentication

Profile updates

Session management

JWT-based authentication

REST API for frontend interaction

🔔 Notification Service Sends real-time alerts and updates to users
Notifies users about:

Experiment updates

Deadlines

Scoring feedback

Queued/async support (optional via Redis/RabbitMQ)

🧠 Marks Calculation Service Dynamically computes scores based on:
Experiment difficulty

Time taken

Accuracy

Applies weighted logic to calculate final marks

Stores and shares reports with other services

🎯 Recommendation Service Recommends:
Next experiments based on user performance

Difficulty adjustments

Learning paths or supplementary resources

Implements basic AI logic (e.g., rule-based or ML)

💻 Frontend (React) User dashboard with:

Profile overview

Notifications panel

Experiment progress

Recommended experiments

REST API-based communication with backend

Responsive and interactive design
