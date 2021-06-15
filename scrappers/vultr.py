import requests
import logging
import re
import pandas as pd
from bs4 import BeautifulSoup

def extract_vultr():
    """
    Function that returns a DataFrame to easily vizualize
    the products of cloud compute of Vultr.

    Returns a Dataframe with the data ready to be vizualized and a row counts
    or an error message and row count 0.
    """
    url = "https://www.vultr.com/products/cloud-compute/#pricing"
    df = pd.DataFrame(columns=["Storage", "CPU", "Memory", "Bandwidth", "Price"])

    response = requests.get(url)
    if response.status_code != 200:
        error = "The url doesn't return status_code equals to 200."
        return error, 0
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("div", attrs={"class": "pt__body js-body"})
    if table is None:
        logging.error(
            "BeautifulSoup Doesn't find the table check if the path is still the same."
        )
        error = "Unable to find the table please check the logfile."
        return error, 0
    try:
        rows = table.find_all("div", attrs={"class": "pt__row"})
    except Exception as e:
        logging.error(str(e))
        erro = "Unable to find the rows of the table please check the logfile."
        return error, 0

    row_count = 0
    for row in rows:
        cells = row.find_all("div", attrs={"class": "pt__cell"})
        current_row = normalize_row(cells)
        df.loc[row_count] = current_row
        row_count += 1
    return df, row_count

def normalize_row(cells):
    """
    Normalize each one of the cells in the current row
    """
    cells_text = [re.sub(r"\s", "", cell.get_text()) for cell in cells]
    cells_text.pop(0)
    cells_text[2] = cells_text[2].replace("Ram", "")
    cells_text[3] = cells_text[3].replace("Bandwidth", "")
    cells_text[-1] = "$" + cells_text[-1].split("$")[1]
    return cells_text
