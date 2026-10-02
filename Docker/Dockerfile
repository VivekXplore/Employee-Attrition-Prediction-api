#base imgae
FROM python:3.11

#set working directory 
WORKDIR /app_predict

#copy requirement 
COPY Requirements/require.txt .
RUN pip install --no-cache-dir -r require.txt
#copy rest of application code 

COPY . .

# Expose port 
EXPOSE 8000


# cmd to start fastapi application 
CMD ["uvicorn","Fastapi.api:app","--host","0.0.0.0","--port","8000"]