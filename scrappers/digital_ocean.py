import requests
import logging
import re
import pandas as pd
from bs4 import BeautifulSoup

def extract_digital_ocean():
    """
    Function that returns a DataFrame to easily vizualize
    the products of cloud compute of Digital Ocean.

    Returns a Dataframe with the data ready to be vizualized and a row counts
    or an error message and row count 0.
    """
    url = "https://www.digitalocean.com/pricing/"
    df = pd.DataFrame(columns=["Storage", "CPU", "Memory", "Bandwidth", "Price"])

    response = requests.get(url)
    if response.status_code != 200:
        error = "The url doesn't return status_code equals to 200."
        return error, 0
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("ul", attrs={"class": "priceBox"})
    if table is None:
        logging.error(
            "BeautifulSoup Doesn't find the table check if the path is still the same."
        )
        error = "Unable to find the table please check the logfile."
        return error, 0
    try:
        rows = table.find_all("li", attrs={"class": "priceBoxItem"})
    except Exception as e:
        logging.error(str(e))
        erro = "Unable to find the rows of the table please check the logfile."
        return error, 0

    row_count = 0
    for row in rows:
        content_divs = row.find_all("div")
        current_row = normalize_row(content_divs)
        df.loc[row_count] = current_row
        row_count += 1
    return df, row_count

def normalize_row(content_divs):
    """
    Normalize each one of the fields in the current row
    """
    current_row = []
    infos = [item.get_text() for item in content_divs[2].find_all("li")]
    current_row.append(infos[1].replace("Disk", "").strip())
    current_row.append(infos[0].split("/")[1].strip())
    current_row.append(infos[0].split("/")[0].strip())
    current_row.append(infos[-1].replace("transfer", "").strip())
    current_row.append(content_divs[0].get_text().split(" ")[0])
    return current_row
