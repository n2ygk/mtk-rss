# Start here

## generate the podcast file
```text
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python mtk-rss.py  # generates podcast.xml
```

## serve podcas.xml from localhost

```
npm install http-server
http-server .
```

Looks something like this:

```text
http-server .
Starting up http-server, serving .
Available on:
  http://127.0.0.1:8080
  http://192.168.1.17:8080
  Hit CTRL-C to stop the server
```
## open podcast from podcast client

Then open, e.g. http://192.168.1.17:8080/podcast.xml from your client.

For example on Apple Podcasts:

![subscribe](./media/subscribe.png "subscribe to the podcast")

![play](./media/play.png "play the podcast")

## generalizing it

is left as an exercise for the reader
