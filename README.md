`init.sh`
```
# make file executable inside docler
chmod +x ./scripts/setup.sh

# URI: `'mongodb://<HOSTNAME>:27017,<HOSTNAME>:27018,<HOSTNAME>:27019/<DBNAME>'`
# If on Linux / MacOS add the following to your `/etc/# hosts` file in the host machine. 
# Then replace `<HOSTNAME>` with `localhost`.

echo "127.0.0.1 mongo1" >> /etc/hosts
echo "127.0.0.1 mongo2" >> /etc/hosts
echo "127.0.0.1 mongo3" >> /etc/hosts
``` 

Todo: Add password auth to mongo express connection and client connection