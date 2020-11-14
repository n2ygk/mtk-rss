#!/usr/bin/env python
import re
import requests
from datetime import datetime
from dateutil import tz
from feedgen.feed import FeedGenerator

def add_episode(fg, match):
    """
    Add an episode to the feed.
    :param fg: FeedGenerator
    :param match: re.match result.
    """
    print(f"Episode {match['ep']}: {match['rel']}")
    response = requests.get('https://fullduplexradio.us/' + match['rel'])
    if response.status_code == 200:
        description = []
        file_url = None
        rows = response.content.decode().split('\n')
        for row in rows:
            descr = re.match(r'<p .*>(?P<text>.*)</p>', row)
            href = re.match(r'<a href="(?P<rel>[^"]*)', row)
            if descr:
                description.append(descr['text'])
            elif href:
                file_url = 'https://fullduplexradio.us' + href['rel']
                break

        if file_url:
            fe = fg.add_entry()
            fe.id(file_url)
            pub_time = datetime.strptime(match['date'], '%Y-%m-%d')
            local_tz = tz.tzlocal()
            pub_time = pub_time.astimezone(local_tz)
            fe.published(pub_time)
            fe.title(f"Episode {match['ep']}: {match['title']}")
            fe.description('\n'.join(description))
            fe.enclosure(file_url, 0, 'audio/mpeg')

fdr = 'https://fullduplexradio.us'
fg = FeedGenerator()
fg.load_extension('podcast')

fg.podcast.itunes_category('Music', 'Podcasting')
fg.title('Full Duplex Radio')
fg.description("R&R play what they like, which is a lot. And they tell you about it.")
fg.link(link={'href': fdr})
local_tz = tz.tzlocal()
fg.lastBuildDate(datetime.now(tz=local_tz))
fg.rss_str(pretty=True)

response = requests.get(fdr)
if response.status_code == 200:
    rows = response.content.decode().split('\n')
    # '<a href="pl/FD406.html">Episode #406: Do You Know Any Nice Jewish Girls? (2020-11-07)</a>'
    for row in rows:
        match = re.match(r'<a href="(?P<rel>[^"]*)">Episode #(?P<ep>[0-9]+): (?P<title>.*) \((?P<date>.*)\)</a>', row)
        if match:
            add_episode(fg, match)

urls = ['https://fullduplexradio.us/audio/Full%20Duplex%20405%20-%202020-10-31.mp3',]

fg.rss_file('podcast.xml')
