import logging


def process_country_name(value):
    return "".join(value).strip()


def process_courts_product_name(value):
    return value.strip()


def extract_courts_product_curr_price(value):
    return int(value.strip(".").strip("S$").replace(",", ""))


def extract_courts_product_old_price(value):
    return int(value.strip(".").strip("S$").replace(",", "")) if value else None



def extract_courts_product_price_currency(value):
    if "S$" in value:
        return "SGD"
    elif "US$" in value:
        return "USD"


def should_abort_request(req):

    if req.resource_type == "image":
        logging.log(logging.INFO, f"Ignoring Image {req.url}")
        return True

    if req.method.lower() == "post":
        logging.log(logging.INFO, f"Ignoring {req.method} {req.url} ")
        return True

    return False
