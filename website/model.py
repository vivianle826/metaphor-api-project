from metaphor_python import Metaphor
from datetime import datetime, timedelta
from urllib import parse

# Get the current date and time
current_datetime = datetime.now()
# Calculate the datetime of 7 days ago
seven_days_ago = current_datetime - timedelta(days=7)
print(seven_days_ago)


# Test the function
# url_to_check = 'https://twitter.com/buitengebieden/status/1534564404943106056'
# website = get_website_from_url(url_to_check)
# url = 'https://www.youtube.com/watch?v=02tpVtZgARg&ab_channel=GirlWithTheDogs2'
# url_parsed = parse.urlparse(url)
# qsl = parse.parse_qs(url_parsed.query)
# print(qsl['v'][0])


# def generateSearch(animal):
#     metaphor = Metaphor("2ad6ae09-e1ed-4589-b4f7-bba79498c650")

#     response = metaphor.search(
#         "give me a recent viral cute youtube video of a" + animal,
#         num_results=1,
#         start_crawl_date="2023-09-24",
#         end_crawl_date="2023-09-30",
#         start_published_date="2023-09-24",
#         end_published_date="2023-09-30",
#     )

#     current_date_time = datetime.now()
#     formatted_date = current_date_time.strftime("%Y-%m-%d")
#     # print(formatted_date)

#     resultURL = [result.url for result in response.results]
#     print(resultURL)
#     return resultURL[0]
#     for i in resultURL:
#         print(i)
