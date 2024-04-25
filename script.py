import json
import requests

sample_json_data = """
{
  "data": {
    "id": "123456789", 
    "name": "John Doe",
    "username": "johndoe",
    "description": "Software Engineer | Tech Enthusiast",
    "created_at": "2010-01-01T00:00:00.000Z",
    "public_metrics": {
      "followers_count": 5000,
      "following_count": 500,
      "tweet_count": 2500,
      "listed_count": 200
    },
    "profile_image_url": "https://pbs.twimg.com/profile_images/123456789/avatar.jpg",
    "location": "San Francisco, CA",
    "url": "https://twitter.com/johndoe"
  },
  "includes": {
    "tweets": [
      {
        "id": "1357246808474218497",
        "text": "Just published a new article on Medium!",
        "created_at": "2021-02-04T15:30:00.000Z",
        "public_metrics": {
          "retweet_count": 20,
          "reply_count": 5,
          "like_count": 100,
          "quote_count": 2
        }
      },
      {
        "id": "1357246810463745030",
        "text": "Excited to join Twitter Developer Community!",
        "created_at": "2021-02-04T15:31:00.000Z",
        "public_metrics": {
          "retweet_count": 10,
          "reply_count": 3,
          "like_count": 50,
          "quote_count": 1
        }
      }
    ]
  }
}
"""


def print_user_data(data):
    user_data = data['data']
    print("User Data:")
    print("Username:", user_data['username'])
    print("Name:", user_data['name'])
    print("Description:", user_data['description'])
    print("Created at:", user_data['created_at'])
    print("Followers Count:", user_data['public_metrics']['followers_count'])
    print("Tweet Count:", user_data['public_metrics']['tweet_count'])
    print("Profile URL:", user_data['url'])
    print()


def get_tweet_insights(data):
    tweet_insights = []
    tweets = data['includes']['tweets']
    for tweet in tweets:
        tweet_insight = {
            'id': tweet['id'],
            'text': tweet['text'],
            'created_at': tweet['created_at'],
            'retweet_count': tweet['public_metrics']['retweet_count'],
            'reply_count': tweet['public_metrics']['reply_count'],
            'like_count': tweet['public_metrics']['like_count'],
            'quote_count': tweet['public_metrics']['quote_count']
        }
        tweet_insights.append(tweet_insight)
    return tweet_insights


def main():

    data = json.loads(sample_json_data)
    
    print_user_data(data)
    
    tweet_insights = get_tweet_insights(data)
    
  
    print("Tweet Insights:")
    for insight in tweet_insights:
        print("Tweet ID:", insight['id'])
        print("Text:", insight['text'])
        print("Created at:", insight['created_at'])
        print("Retweet Count:", insight['retweet_count'])
        print("Reply Count:", insight['reply_count'])
        print("Like Count:", insight['like_count'])
        print("Quote Count:", insight['quote_count'])
        print()


if __name__ == "__main__":
    main()
