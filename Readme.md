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

테스트 체크리스트
	•	DNS에서 다음 서브도메인 설정 완료:
	•	A 또는 CNAME:
	•	ui.mydomain.com
	•	api.mydomain.com
	•	grafana.mydomain.com
	•	traefik.mydomain.com
	•	https://traefik.mydomain.com 접속 시 대시보드 확인
	•	https://ui.mydomain.com에서 React 앱 확인
	•	https://api.mydomain.com/docs에서 FastAPI 문서 확인
	•	HTTPS 인증서가 자동 생성되는지 로그로 확인 (acme.json)
