import requests,json
from bs4 import BeautifulSoup

class Instagram:
    """
    This class provides methods to interact with the Instagram API.
    """
    def __init__(self) -> None:
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
                        "X-Ig-App-Id": "936619743392459",
                        "Content-Type": "application/x-www-form-urlencoded",
                        "X-Fb-Lsd": "AVrix1LR8Y4",
                        "Sec-Fetch-Site": "same-origin"}
        self.sess = requests.Session()
        self.sess.headers.update(self.headers)

    def profilePic(self,username):
        """
        Get the profile picture URL of an Instagram user.

        Args:
            username (str): The username of the Instagram user.

        Returns:
            str: The profile picture URL of the user.
        """
        w = self.sess.get(f"https://www.instagram.com/api/v1/users/web_profile_info/?username={username}&hl=en")
        data = w.json()["data"]["user"]["profile_pic_url_hd"]
        return self.sess.get(data).content
    
    def pic(self,url):
        """
        Get the picture URL of an Instagram post.

        Args:
            url (str): The URL of the Instagram post.

        Returns:
            str: The downloadable picture URL of the post.
        """
        sor = url.split("/p/")[1]
        shortcode = sor.split("/")[0] or sor
        w = self.sess.post("https://www.instagram.com/api/graphql",data="lsd=AVrix1LR8Y4&fb_api_req_friendly_name=PolarisPostActionLoadPostQueryQuery&variables={\"shortcode\":\"%s\"}&doc_id=10015901848480474" % (shortcode))
        print(w.json()["data"]["xdt_shortcode_media"]["display_resources"][-1]["src"])

    def reels(self,url):
        """
        Get the video URL of an Instagram Reel.

        Args:
            url (str): The URL of the Instagram Reel.

        Returns:
            str: The downloadable video URL of the Reel.
        """
        sor = url.split("/reel/")[1]
        shortcode = sor.split("/")[0] or sor
        w = self.sess.post("https://www.instagram.com/api/graphql",data="lsd=AVrix1LR8Y4&fb_api_req_friendly_name=PolarisPostActionLoadPostQueryQuery&variables={\"shortcode\":\"%s\"}&doc_id=10015901848480474" % (shortcode))
        lo = w.json()["data"]["xdt_shortcode_media"]["video_url"]
        print(json.dumps(lo,indent=5))
        # print(w.json()["data"]["xdt_shortcode_media"]["display_resources"][-1]["src"])

class Snapchat:
    """
    This class provides methods to interact with the Snapchat API.
    """

    def __init__(self) -> None:
        pass

    def downloadStories(self,url):
        """
        Download stories from a Snapchat user.

        Args:
            url (str): The URL of the Snapchat user.
        """
        w = requests.get(url)
        soup = BeautifulSoup(w.content, "html.parser")
        link = soup.find("link", attrs={"as": "video"})["href"]
        # ko = open("ko.mp4", "ab+")
        # ko.write(requests.get(link).content)

    def downloadSpotlight(self):
        """
        Download video from the Snapchat Spotlight.

        Returns:
            list: A list of downloadable video URLs.
        """
        w = requests.get("https://www.snapchat.com/add/iamsimranjainn")
        soup = BeautifulSoup(w.content, "html.parser")
        link = soup.find("script", attrs={"id": "__NEXT_DATA__"})
        js = json.loads(link.text)
        jslist = [x["snapUrls"]["mediaUrl"] for x in js["props"]["pageProps"]["story"]["snapList"]]
        return jslist

class Twitter:
    """
    This class provides methods to interact with the Twitter API.
    """

    def __init__(self) -> None:
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
            'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            'X-Guest-Token': self.getGuestToken()
        }

    def getGuestToken(self):
        r = requests.post("https://api.twitter.com/1.1/guest/activate.json",headers={"Authorization":"Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs=1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"})
        return r.json()["guest_token"]

    def getMedia(self,url):
        """
        Get the downloadable media URL of a Twitter post.

        Args:
            url (str): The URL of the Twitter post.

        Returns:
            str: The downloadable media URL of the post.
        """
        ids = url.split('/status/')[1][:19]
        w = requests.get(f"https://api.twitter.com/graphql/OGDXNj5PSaBRwg2MlpX0JQ/TweetResultByRestId?variables=%7B%22tweetId%22%3A%22{ids}%22%2C%22withCommunity%22%3Afalse%2C%22includePromotedContent%22%3Afalse%2C%22withVoice%22%3Afalse%7D&features=%7B%22creator_subscriptions_tweet_preview_api_enabled%22%3Afalse%2C%22c9s_tweet_anatomy_moderator_badge_enabled%22%3Afalse%2C%22tweetypie_unmention_optimization_enabled%22%3Afalse%2C%22responsive_web_edit_tweet_api_enabled%22%3Atrue%2C%22graphql_is_translatable_rweb_tweet_is_translatable_enabled%22%3Atrue%2C%22view_counts_everywhere_api_enabled%22%3Atrue%2C%22longform_notetweets_consumption_enabled%22%3Atrue%2C%22responsive_web_twitter_article_tweet_consumption_enabled%22%3Afalse%2C%22tweet_awards_web_tipping_enabled%22%3Afalse%2C%22freedom_of_speech_not_reach_fetch_enabled%22%3Atrue%2C%22standardized_nudges_misinfo%22%3Atrue%2C%22tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled%22%3Atrue%2C%22rweb_video_timestamps_enabled%22%3Atrue%2C%22longform_notetweets_rich_text_read_enabled%22%3Atrue%2C%22longform_notetweets_inline_media_enabled%22%3Atrue%2C%22responsive_web_graphql_exclude_directive_enabled%22%3Atrue%2C%22verified_phone_label_enabled%22%3Atrue%2C%22responsive_web_media_download_video_enabled%22%3Afalse%2C%22responsive_web_graphql_skip_user_profile_image_extensions_enabled%22%3Afalse%2C%22responsive_web_graphql_timeline_navigation_enabled%22%3Atrue%2C%22responsive_web_enhance_cards_enabled%22%3Afalse%7D",headers=self.headers)
        
        try:
            return w.json()["data"]["tweetResult"]["result"]["legacy"]["extended_entities"]["media"][0]["video_info"]["variants"][0]["url"]
        except:
            return w.json()["data"]["tweetResult"]["result"]["legacy"]["extended_entities"]["media"][0]["media_url_https"]

