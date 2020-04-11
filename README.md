# Scrapy spiders
A collection of web spiders based on Scrapy framework

# Installation
1. Install Python3

2. Create virtual environment
    ```
    python3 -m venv env
    ```

3. Activate virtual environment
    ```
    . env/bin/activate
    ```
    For deactivate run
    ```
    deactivate
    ```

4. Install Scrapy
    ```
    pip install scrapy
    ```

# Run
Get all articles from a page https://www.the-village.ru/village/people in the following format
```
{
    'url': 'http://...',
    'text': 'article text...'
}
```

> Save to JSON
```sh
scrapy runspider get-the-village-people-articles.py -o the-village-people-articles.json -t json -s FEED_EXPORT_ENCODING='utf-8'
```

> Save to CSV
```sh
scrapy runspider get-the-village-people-articles.py -o the-village-people-articles.csv -t csv -s FEED_EXPORT_ENCODING='utf-8'
```
