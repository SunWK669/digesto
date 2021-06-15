# digesto

Digesto scrapper challenge

## Dependencies
- Python v3.8.0
- requests v2.25.1
- beautifulsoup4 v4.9.3
- pandas v1.2.4
- html5lib v1.1
- lxml v4.6.3

## Installation

OS X & Linux:

```sh
$ cd digesto
$ py -m venv venv
$ pip install -r requirements.txt
$ source venv/bin/activate
```

## Installation Windows

```cmd
> cd digesto
> py -m venv venv
> pip install -r requirements.txt
> cd venv/scripts
> activate
> cd..
> cd..
```

## Usage example

```sh
$ py main.py --print
```

```cmd
> py main.py --print
```

## Observations
I chose to use the BeautifulSoup library due to its simplicity in finding items inside html pages and mainly because it is not such a high level library as well as selenium and scrappy which can present some impediments due to its high abstraction levels. If you need to use something related to XPath it is also possible to convert the BeatifulSoup object into lxml and work through lxml.xpath()
