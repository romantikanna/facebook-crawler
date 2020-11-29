import json
import datetime
import facebook

class FacebookCrawler(object):
    def __init__(self, token,folder_for_output):
        self.token=token
        self.folder_for_output=folder_for_output

    def get_10_latest_page_posts(self,page_id):
        graph = facebook.GraphAPI(access_token=self.token, version="2.1")
        posts = graph.get_connections(id=page_id, connection_name="feed",
                                      fields="id,created_time,description,message,permalink_url,source,likes.summary(true)",
                                      until=str(datetime.datetime.now()), limit=10)

        for data in posts['data']:
            post_metadata = {}
            post_id = data['id']
            post_metadata['url'] = data['permalink_url']
            post_metadata['text'] = data['message'].encode('utf-8')
            post_metadata['date'] = data['created_time']
            post_metadata['likes'] = data['likes']['summary']['total_count']
            with open(self.folder_for_output + 'post_' + post_id + '.json', 'w') as f:
                json.dump(post_metadata, f, ensure_ascii=False)
            print'<<<<<<<<<<<< Post ' + str(post_id) + ' was downloaded to folder. >>>>>>>>>>>>'

# Uncomment to see an example of how to use this class
# Change params to fit:
# - your Facebook token
# - path of the folder to write the output to
# - Facebook page ID to crawl 10 last posts
# if __name__=='__main__':
#     # Parameters:
#     token = "FB_TOKEN"
#     folder_for_output = "/Users/username/Documents/DonaldTrump/"
#     page_id = "153080620724"
#
#     # Activation:
#     fb_crawler=FacebookCrawler(token,folder_for_output)
#     fb_crawler.get_10_latest_page_posts(page_id)