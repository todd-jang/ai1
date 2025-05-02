import os
from dotenv import load_dotenv

load_dotenv()

DOMAIN = os.getenv("DOMAIN")
SERVICES = {
    "frontend": 3000,
    "backend": 8000,
    "grafana": 3001,
}

with open("docker-compose.generated.yaml", "w") as f:
    f.write("version: '3.9'\nservices:\n")
    for name, port in SERVICES.items():
        sub = name
        f.write(f"""  {name}:
    build: ./services/{name}
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.{name}.rule=Host(`{sub}.{DOMAIN}`)"
      - "traefik.http.routers.{name}.entrypoints=websecure"
      - "traefik.http.routers.{name}.tls.certresolver=myresolver"
      - "traefik.http.services.{name}.loadbalancer.server.port={port}"
""")
