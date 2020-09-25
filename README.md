# Scrapy-Idealista

## Description

Scrapping data from Real Estate site www.idealista.com

## Requirements

* `>= python3.6.*`
* `pip`

Execute to install pip packages:

```
pip install -r requirements.txt
```

## How to crawl Real Estate info from a URL in idealista website

1. Add the URL to be crawled in the variable `start_urls` in `./idealista/spiders/idealista_spider.py`. Example:
```
start_urls = ["http://www.idealista.com/venta-viviendas/madrid/retiro/"]
```
*Note*: crawl only one url since all records will be exported to the same csv file

2. At the top of the project, execute the following command to crawl the URL saved in `start_urls`:
```
scrapy crawl idealista -t csv -o <flats_file>.csv
```
*Note*: where `<flats_file>` is the csv file where all the records are saved


## Use with Docker

1. Download repository:

```
git clone git@github.com:David-Carrasco/Scrapy-Idealista.git
```

2. Build image:
*Note: Remember modify your URL to crawl.*

```
docker build -t <image>:<tag> .
```

3. Run container:

```
docker run --name <name_container> --rm -it -v <your-dir>:/data <image>:<tag> <flats_file>
```

Your data will appear on `<your-dir>` directory such as `idealista.csv` by default or with your `<flats_file>` filename. Example:

```
docker run --name scrapy_idealista --rm -it -v /home/myuser/idealista:/data scrapy_idealista:latest
```