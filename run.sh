
set -e  
export POSTGRES_DSN="postgresql://postgres:password@db:5432/postgres"
export API_URL="https://jsonplaceholder.typicode.com/posts"


docker-compose -f infra/docker-compose.yml up --build -d

echo "Ждем 10 секунд, пока БД поднимется..."
sleep 10

docker exec -it infra-etl-1 python /app/scripts/extract.py
docker exec -it infra-etl-1 python /app/scripts/transform.py


echo "Топ пользователей по постам:"
docker exec -it infra-etl-1 psql "$POSTGRES_DSN" -c "SELECT * FROM top_users_by_posts ORDER BY posts_cnt DESC;"
