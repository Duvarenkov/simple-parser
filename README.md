Deployment instructions:

1. `virtualenv venv -p python3`
2. `. venv/bin/activate`
3. `pip install -r requirements.txt`
4. `python manage.py migrate`
5. `python manage.py runserver`

Usage:
1. Make a POST request on "http://localhost:8000/scrape/" with "application/json" formatted URL string one-liner.
You can also navigate to http://localhost:8000/scrape/ in a browser and make a request from the interface.
2. You will receive application/json response with parsed data
3. GET request to "http://localhost:8000/scrape/result" will return application/json response with all previously parsed urls
