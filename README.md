Crawl paper information from
1. science direct
2. mdpi
and store into mongodb

Check `item.py` out for the details of scraped structure.

# requirements
1. docker
2. python 3.7
# run steps
1. `docker pull mongo:4.2.3`
2. `docker run -p 27017:27017 -d --name mongo mongo:4.2.3`
3. run either below methods to install dependencies
* `pip install -r requirement.txt`
* `pipenv install --python 3.7`
4. run crawler, `scrapy crawl sciencedirect  --loglevel=INFO`, where `sciencedirect` is a spider
* run `scrapy list` to display the list of crawlers 

# visual data
I recommend `Robo 3T` to query data, otherwise `mongo-shell` can do
1. connect to server
2. `db.getCollection('items').find({'abstract': {$ne: null}})`

# notes
1. visit https://docs.scrapy.org/en/latest/topics/jobs.html for pause crawl works
* e.g `scrapy crawl sciencedirect -s  JOBDIR=crawl_jobs/sciencedirect`
2. should expose file inside docker container to the machine
* determine a folder first outside, for example: `/Users/bryan/papers_crawler/mongodb`
* run `docker run -p 27017:27017 -d -v /Users/bryan/workplace/papers_crawler/mongodb:/data/db/ --name mongo mongo:4.2.3`