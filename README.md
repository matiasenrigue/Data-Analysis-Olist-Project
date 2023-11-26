# Olist Profit Optimization Project

## Project Overview

This project aims to analyze a dataset provided by the e-commerce marketplace Olist with the objective of addressing the CEO's question:

* How could Olist increase its profit? *

Exploring data from 2016 to 2018, comprising approximately 100,000 orders. The analysis focuses on identifying areas for potential profit enhancement and proposing actionable insights.


### What is Olist?

Olist is a prominent e-commerce service in Brazil that facilitates connections between merchants and major marketplaces. The platform provides diverse services, including inventory management, review handling, customer interaction, and logistics.

Sellers on Olist are subject to a monthly fee, which varies based on the volume of orders they receive. The workflows for sellers and customers are outlined below:

Seller:
- Joins Olist
- Uploads product catalog
- Notified upon product sale
- Hands over item to logistic carrier
- Note: Multiple sellers can be involved in a single customer order.

Customer:
- Browses products on the marketplace
- Makes purchases on Olist.store
- Receives an expected delivery date
- Receives the order
- Leaves a review
- Note: Reviews can be submitted even before the customer receives the product.


## Project Organization

#### Data:

Contains 9 CSV with all the data we need, further explanation about the data is provided in the folder

#### Olist:

Constains all the Logic of the code:
- data.py is the module to in charge of organizing our data in a dictionary of dataframes
- order.py treats all the data concerning orders
- product.py treats all data concerning products
- sellers.py treats all data concerning sellers
- utils.py has functions that will be needed througouht the code


#### CEO_request.ipynb

Is the asnwer the question: "How can Olists profits be improved?"
