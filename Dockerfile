# Use a suitable Python base image
FROM python:3.11-slim

# Install necessary system dependencies for Playwright
RUN apt-get update && apt-get install -y \
    xvfb \
    fonts-liberation \
    fontconfig \
    libfreetype6 \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libdbus-1-3 \
    libdrm2 \
    libgbm1 \
    libgtk-3-0 \
    libnspr4 \
    libnss3 \
    libu2f-udev \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxkbcommon0 \
    libxrandr2 \
    wget \
    xdg-utils \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers
RUN playwright install --with-deps

# Copy the rest of the code
COPY . .
RUN chmod +x /app/entrypoint.sh

# Use entrypoint.sh to start Xvfb + tests
ENTRYPOINT ["/app/entrypoint.sh"]