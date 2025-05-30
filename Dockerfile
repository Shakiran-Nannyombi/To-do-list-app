# Base image
FROM python:3.9-slim

ADD requirements.txt .
ADD app.py .
ADD pages/tasks.py pages/tasks.py
ADD pages/Analysis.py pages/Analysis.py

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit's default port
EXPOSE 8501

# Command to run the app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
