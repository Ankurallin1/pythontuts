#Article reading
import requests
import json
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)
print("Hello fellow listner welcome to the daily news fetcher..")
speak("Hello fellow listner welcome to the daily news fetcher..") 
print("Today news is as follows...")
speak("Today news is as follows...")
url="https://newsapi.org/v2/top-headlines?country=in&apiKey=4404060df36a4b419e108c42b65eaf1d"
news = requests.get(url).text
#converting the content in dictionary using json
news_dict = json.loads(news)
arts = news_dict['articles']
for article in arts:
    print(article['title'])
    speak(article['title'])
    print()
print("Thank you for hearing, see you tomorrow !!!")
speak("Thank you for hearing, see you tomorrow")