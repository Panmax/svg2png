git pull
docker rm -f svg2png
docker build -t panmax/svg2png .
docker run -d --name svg2png --restart=always -p 5000:5000 panmax/svg2png