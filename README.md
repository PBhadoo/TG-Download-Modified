### Host it on VPS or Locally

* Modify the commands as per your needs.

```sh
sudo su

sudo apt-get -y update && sudo apt-get -y upgrade && sudo apt -y update && sudo apt -y upgrade &&
git clone https://github.com/PBhadoo/TG-Download-Modified bot &&
cd bot &&
sudo snap install docker

sudo docker build . -t stream-bot
sudo docker run -d --restart unless-stopped --name fsb -v /home/bhadoo/bot/.env:/app/.env -p 80:80 stream-bot
```

````
sudo docker stop $(docker ps -a -q)
sudo docker rm $(docker ps -a -q)
sudo docker images -a
sudo docker rmi Image Image2
````

````
docker logs -f --until=2s fsb
````

* Don't Ask Questions, I don't know much Python. Good Luck!

### Source and Credits

* https://github.com/EverythingSuckz/TG-FileStreamBot