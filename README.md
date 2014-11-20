
#<b>Exercise with Django and Tweetpy plugin</p>.#

##<b>BRIEF/BACKGOUND PROJECT</b>##

When I was about to develop the re-branding website for JPC (Creative Company), we were looking to building a Django CMS app 
displaying company Tweets. From there we will creating other kind of CMS app based on Twiteer API.

##<b>DESCRIPTION</b>##

At the moment is a page displaying the last 10 tweets from my personale account.

##<b>ACCESS TO THE PROJECT</b>##

There s no online access to this project.

If want to check out and see how it s working :

        git clone https://github.com/artitudinale1/tweepy-exercise.git
        
        cd WHERE/YOU/DOWNLOAD/PROJECT
        
I'd suggest to create a virtual enviroment first: (if dont have virtualenv installed here a great doc: http://docs.python-guide.org/en/latest/dev/virtualenvs/)

      virtualenv YOUVIRTUALENVNAME
      
then activate it
      
      source venv/bin/activate
        
then if you have PIP installed:
  
        pip install requirements.txt
        
        python manage.py runserver
        
and the app should start at http://127.0.0.1:8000/

otherwise install PIP first
  
        easy_install pip

##<b>CROSS-BROWSER TESTING</b>##

This project has been tested in : Chrome 38.0

##<b>TECHNOLOGIES USED</b>##

HTML5, Django 1.6.1, tweepy 2.1, wsgiref 0.1.2

##<b>FUTURE IMPROVEMENT</b>##
<i>Those are bugs to fix and some ideas to improve the project</i>

 - Deploy what so far done on Heroku
 - Add CSS , formatting and style
 - Add more functionality to create an Hook App for Django CMS (maybe updating Django as well :-/)
   
<b>PLESE IF YOU EXPERIMENT ANY BUGS/ERRORS/PROBLEMS TESTiNG OR CHECKING OUT THIS PROJECT</b> report it though GITHUB or @ alex.garulli@gmail.com
