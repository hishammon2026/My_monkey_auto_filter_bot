# Debian Buster-ന് പകരം പുതിയ Bullseye ഉപയോഗിക്കുന്നു (ഇത് എറർ ഒഴിവാക്കും)
FROM python:3.10-slim-bullseye

# സിസ്റ്റം ഡിപെൻഡൻസികൾ
RUN apt-get update && apt-get install -y \
    git \
    gcc \
    python3-dev \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "mt_botz.py"]
