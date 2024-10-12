# Real-Time Data Processing and Analytics Platform

## Project Overview

This project is a real-time data processing and analytics platform that ingests streaming data, processes it using Apache Spark and Kafka, and provides interactive visualizations through a web interface.

## Architecture

![Architecture Diagram](docs/architecture_diagram.png)

## Technologies Used

- **Programming Languages**: Python, JavaScript
- **Big Data Tools**: Apache Kafka, Apache Spark
- **Databases**: MongoDB
- **Web Frameworks**: Flask, React.js
- **Visualization Libraries**: Chart.js
- **Containerization**: Docker
- **Orchestration**: Docker Compose
- **Version Control**: Git

## Setup Instructions

### Prerequisites

- Docker and Docker Compose installed
- Git installed

### Clone the Repository

```bash
git clone https://github.com/yourusername/real-time-data-platform.git
cd real-time-data-platform
```


### Start the Services
```bash
docker-compose up
```
### Access the Application

Frontend: http://localhost:3000  
Backend API: http://localhost:5000/api/data  
### Usage
The application will start ingesting data automatically.  
Real-time data will be visualized on the frontend.  

### Contributing

Contributions are welcome! Please open an issue or submit a pull request.

### License

This project is licensed under the MIT License.