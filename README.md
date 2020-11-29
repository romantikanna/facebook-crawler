# facebook-crawler
Facebook crawler using python and Facebook Graph API.

Program:
- Extracts last 10 posts from a specific public Facebook page. 
(For example: http://facebook.com/153080620724) 
- Saves a JSON file for each post with the following fields: 
url, 
text,
date, 
num_likes 

Guidlines:
1. Run: pip3 install facebook-sdk
2. Change token to "<App ID>|<App Secret>"
3. App should have permissions to https://developers.facebook.com/docs/permissions/reference/pages_read_user_content is order to run.
