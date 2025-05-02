docker-compose up -d
	2.	브라우저에서 확인:
 ì£¼ì†Œ
ì„œë¹„ìŠ¤
http://ui.localhost
React
http://api.localhost
FastAPI
http://grafana.localhost
Grafana

docker ps & traefik dashboard: http://localhost:8080 → 연결 상태 확인


docker compose -f docker-compose.yaml -f docker-compose.traefik.yaml up -d --build
