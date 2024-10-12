# Setup Guide

## Prerequisites

- Install Docker: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)
- Install Docker Compose: [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/)
- Install Git: [https://git-scm.com/downloads](https://git-scm.com/downloads)

## Steps

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/real-time-data-platform.git
    cd real-time-data-platform
   ```

2. **Build and Run Services**

   ```bash
   docker-compose up --build
   ```

3. **Verify Services**

   Check if all containers are running:

   ```bash
   docker ps
   ```
   
4. **Access the Application**

   Frontend: http://localhost:3000  
   Backend API: http://localhost:5000/api/data


5. **Troubleshooting**

   Common Issues

   If a service fails to start, check the logs:
   
   ```bash
   docker-compose logs [service_name]
   ```
   Kafka Connection Errors:
   
   Ensure that Kafka and Zookeeper are properly configured and running.  
   Database Connection Errors  
   
   Verify that MongoDB is running and accessible at mongodb:27017.  
   Additional Resources  
   Docker Documentation: https://docs.docker.com/  
   Kafka Documentation: https://kafka.apache.org/documentation/  
   Spark Documentation: https://spark.apache.org/docs/latest/  
