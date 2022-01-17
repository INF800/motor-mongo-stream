docker compose up -d
sleep 5
docker exec -t mongo0 mongo --port 27017 --eval 'rs.initiate({"_id":"rs0","members":[{"_id":0,"host":"172.16.238.10:27017"},{"_id":1,"host":"172.16.238.11:27017"},{"_id":2,"host":"172.16.238.12:27017"}]})'