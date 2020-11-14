# Start here

## generate the podcast file
```text
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python mtk-rss.py  # generates podcast.xml
Episode 407: pl/FD407.html
Episode 406: pl/FD406.html
Episode 405: pl/FD405.html
...
Episode 3: pl/FD003.html
Episode 2: pl/FD002.html
Episode 1: pl/FD001.html
```

## serve podcast.xml from localhost

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

--

And you can download and play the episode:

![play](./media/play.png "play the podcast episode")

--

And even see the show details:

![details](./media/details.png "see episode details")

