# pandas-soup
Sample 1 hour class on web crawling, basic ML and deploying for 1st/2nd year undergraduates

[Class slides](https://docs.google.com/presentation/d/e/2PACX-1vT4EU1tMVcgYPd4hXaUvJ1cxHcfx3Qo7CWdk_j8SqYkkxCI3-nif8Q_1pd-VvOKEgDqKqLJKWDBGRq3/pub?start=false&loop=false&delayms=60000)

# Installation

[Python 3](https://www.python.org/download/releases/3.0/) is required. The libraries used can be installed with `python3 -m pip install -r requirements.txt`.

If you would to run the examples in a notebook, [jupyter](https://jupyter.org/install) is required

# Example:
Scrape all the refrigerators from [here](https://www.magazineluiza.com.br/geladeira-refrigerador/eletrodomesticos/s/ed/refr/) and the washers from [here](https://www.magazineluiza.com.br/lavadora-de-roupas-lava-e-seca/eletrodomesticos/s/ed/ela1/)

Create a file with the following data for each product:	code, title, brand, model, price, category.

Train a ML model to predict if it is a washer or a refrigerator.

Deploy the model as a API.


