FROM python:3.10-alpine AS builder

# Install only necessary build dependencies
RUN apk add --no-cache gcc libc-dev linux-headers musl-dev g++

# Copy application code
ADD hello.py .

# Install Python dependencies (if any)
#RUN pip install --no-cache-dir -r requirements.txt

# Final stage: Use a lightweight base image
FROM python:3.10-alpine

# Copy only the necessary artifacts from the builder stage
COPY --from=builder ./hello.py .

# Default command
CMD ["python", "./hello.py"]
