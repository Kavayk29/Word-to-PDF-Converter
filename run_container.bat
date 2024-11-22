@echo off
REM This script provides instructions to run the Docker container on Windows

REM Check if Docker is installed
where docker >nul 2>nul
if errorlevel 1 (
    echo Docker is not installed. Please install Docker first.
    exit /b 1
)

REM Provide instructions
echo ------------------------------------------------------------
echo Instructions to run the Docker container:
echo ------------------------------------------------------------
echo.
echo 1. Build the Docker image (if not already built):
echo    docker build -t kavay29/newapp:latest .
echo.
echo 2. Run the Docker container:
echo    docker run -d --name mycontainer -p 8501:8501 kavay29/newapp:latest
echo.
echo 3. Verify the container is running:
echo    docker ps
echo.
echo 4. Access your application at: http://localhost:8501
echo.
echo ------------------------------------------------------------
echo You can stop the container using:
echo    docker stop your_container_name
echo To remove the container:
echo    docker rm your_container_name
echo ------------------------------------------------------------
