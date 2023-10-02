from flask import Blueprint, render_template, request
from metaphor_python import Metaphor
from datetime import datetime, timedelta
import requests
from urllib import parse 


views = Blueprint('views', __name__)


@views.route('/', methods=['GET'])
def home():
    result = ''
    animals= ['dogs','cats','birds','pandas']
    for anml in animals:
        url = generateSearch(anml, 1)
        result += '<div><h3>'+anml.capitalize()+':</h3>'
        result += url
        result += '<a id='+ anml + ' href="/' + anml +'">click here to see more recent videos of ' + anml + '</a></div><br>'


    return render_template("home.html", results=result, animal='Animals')


@views.route('/dogs')
def dogs():
    dogURL = generateSearch('dog', 5)
    return render_template("home.html", results=dogURL, animal='Dogs')


@views.route('/cats')
def cats():
    catURL = generateSearch('cat',5)
    return render_template("home.html", results=catURL,animal='Cats')


@views.route('/birds')
def birds():
    birdURL = generateSearch('bird',5)
    return render_template("home.html", results=birdURL, animal='Birds')

@views.route('/pandas')
def pandas():
    pandaURL = generateSearch('panda',5)
    return render_template("home.html", results=pandaURL, animal='pandas')

@views.route('/getcreative', methods=['GET'])
def getcreative():
    return render_template("creative.html",)
@views.route('/getcreative', methods=['POST'])

def postcreative():
    animal = request.form.get('creative')
    url = generateSearch(animal, 5)
    return render_template("home.html",results=url, animal=animal.capitalize() +'s')


def generateSearch(animal, amount):
    # print(animal)
    metaphor = Metaphor("2ad6ae09-e1ed-4589-b4f7-bba79498c650")
    current_date_time = datetime.now()
    seven_days_ago = current_date_time - timedelta(days=7)
    formatted_week_ago = seven_days_ago.strftime("%Y-%m-%d")
    formatted_date = current_date_time.strftime("%Y-%m-%d")

    response = metaphor.search(
        "give me a recent viral cute video of a" + animal + " thats on youtube",
        num_results=amount,
        use_autoprompt=True,
        start_crawl_date=formatted_week_ago,
        end_crawl_date=formatted_date,
        start_published_date=formatted_week_ago,
        end_published_date=formatted_date,
    )

    
    resultURL = [result.url for result in response.results]
    embeddedLink = ''

    for url in resultURL:
        print(url)
        website = get_website_from_url(url)
        if website == 'twitter.com':
            embeddedLink += twitter_embed(url)
        elif website == 'www.youtube.com':
            embeddedLink += youtube_embed(url)
        else:
            toAppend = '<iframe src='+url+' width="800" height="600" frameborder="0" scrolling="auto"></iframe>'
            embeddedLink += toAppend
    return embeddedLink

def get_website_from_url(url):
    # Parse the URL
    parsed_url = parse.urlparse(url)
    # Get the netloc, which contains the domain
    domain = parsed_url.netloc
    return domain


def twitter_embed(url):
    oembed_url = f"https://publish.twitter.com/oembed?url={url}"
    try:
        response = requests.get(oembed_url)
        if response.status_code == 200:
            oembed_data = response.json()
            embedded_html = oembed_data.get("html", "")
            print(isinstance(embedded_html, str))
        else:
            print(
                f"Failed to fetch Twitter oEmbed data. Status Code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    return embedded_html


def youtube_embed(url):
    url_parsed = parse.urlparse(url)
    qsl = parse.parse_qs(url_parsed.query)
    videoID = qsl['v'][0]
    return f'<iframe width="560" height="315" src="https://www.youtube.com/embed/{videoID}" frameborder="0" allowfullscreen></iframe>'