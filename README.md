> `chmod +x ./scripts/setup.sh`

URI: `'mongodb://<HOSTNAME>:27017,<HOSTNAME>:27018,<HOSTNAME>:27019/<DBNAME>'`. If on Linux / MacOS add the following to your `/etc/hosts` file in the host machine. Then replace `<HOSTNAME>` with `localhost`.

```text
127.0.0.1  mongo1
127.0.0.1  mongo2
127.0.0.1  mongo3
```