# Create your views here.
from django.db import models

# Create your models here.
from tweepy.streaming import StreamListener
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from django.http import HttpResponse
from django.template.context import RequestContext
from django.template.response import TemplateResponse
import sys


# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
CONSUMER_KEY="UtaK4LruDEkr4xKEIK7Djg"
CONSUMER_SECRET="7kHOtUTON64EKcKPeAR9d3JLk6Z6kcrmppkG8y81E"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located cio nn so sonno pazzesco ...
# under "Your access token") 
ACCESS_KEY="46785646-xlDB1CQoSNowAuHjWz0QwuBbHdCcDMGoHWP4ZSYAk"
ACCESS_SECRET="gyE2RI0EToQQnbZEdJAHYfzpUqYsA8oDi7Tj9WcIKo"


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def index(request):

  statuses = tweepy.Cursor(api.user_timeline).items(10)
  return TemplateResponse(request, 'index.html', {'statuses': statuses})
 