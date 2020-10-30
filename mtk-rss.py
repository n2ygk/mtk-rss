from feedgen.feed import FeedGenerator
fg = FeedGenerator()
fg.load_extension('podcast')

fg.podcast.itunes_category('Music', 'Podcasting')

fe = fg.add_entry()
fe.id('http://localhost/file.mp3')
fe.title('The First Episode')
fe.description('Enjoy our first episode.')
fe.enclosure('https://fullduplexradio.us/audio/Full%20Duplex%20404%20-%202020-10-24.mp3', 0, 'audio/mpeg')
fg.title('mtk')
fg.description('some feed')
fg.link(link={'href': 'https://fullduplexradio.us'})
fg.rss_str(pretty=True)
fg.rss_file('podcast.xml')
