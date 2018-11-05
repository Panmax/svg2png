## 一个用来提供 svg 转 png 的服务

- `docker build -t panmax/svg2png .`
- `docker run -d --name svg2png --restart=always -p 5000:5000 panmax/svg2png`