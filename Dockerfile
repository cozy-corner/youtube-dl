# docker build --build-arg google_api_key=$GOOGLE_API_KEY -t youtube-dl/hello .

FROM python:3.8.0

WORKDIR /usr/src/app

ARG  google_api_key
ENV API_KEY=$google_api_key

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./youtube-search.py" ]