Scrapy-Idealista
================

Scrapping data from Real Estate site www.idealista.com

## Requirements ##
* ```pip```
* ```scrapy```

Execute:
```pip install -r requirements.txt```

## How to crawl real estate info from a url in idealista website ##

+ Add the url to be crawled in the variable ```start_urls``` in ```./idealista/spiders/idealista_spider.py```
 
  Example: ```start_urls = ["http://www.idealista.com/venta-viviendas/madrid/retiro/"]```

  Note: Crawl only one url since all records will be exported to the same csv file

+ At the top of the project, execute the following command to crawl the url saved in ```start_urls```:

  ```scrapy crawl idealista -o <flats_file>.csv -t csv```
  
  Where:
  
    + ```<flats_file>``` is the csv file where all the records are saved
  
