import wikipedia as wiki
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from profantiy_filter import ProfanityFilter

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    msg = request.values.get('Body', None)

    pf = ProfanityFilter()
    if pf.is_clean(msg):
        return str(wikiScraper(msg))
    else:
        return "The phrase you entered was inappropriate, please try another one."

def wikiScraper(msg):
    try:
        return wiki.summary(msg)
    except:
        return "Unable to find the corresponding article, sorry!"

if __name__ == "__main__":
    app.run(debug=True)