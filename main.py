from flask import Flask, render_template
from flask import request
from flask_bootstrap import Bootstrap
import tweepy 

Api_key = ""
Api_Secret_Key = ""
Access_Token = ""
Access_Token_Secret = ""

auth = tweepy.OAuthHandler(Api_key, Api_Secret_Key)

auth.set_access_token(Access_Token, Access_Token_Secret)

api = tweepy.API(auth)

app = Flask(__name__)

Bootstrap(app)

@app.route('/')

def index():

    return render_template('index.html')

@app.route('/welcome',methods=['GET', 'POST'])	

def hola():

  usuario = request.args.get('usuario')

  user = api.get_user(id=usuario)



  public_tweets = api.user_timeline(id=usuario)

  return render_template('index.html', m = request.method, r = user.screen_name,f=user.followers_count)





    
app.run(debug=True)
