# Selenium_Automation_WebDriver
This repository contains a Selenium automation script written in Python that retrieves values from a web page using XPath and then forms a CSV file. This script can be used to automate data extraction tasks from websites.
Prerequisites
Before running the script, make sure you have the following installed:
Python (version 3.6 or higher)
Selenium library for Python
Chrome WebDriver (compatible with your Chrome browser version)

Installation
Clone this repository to your local machine:
   git clone https://github.com/your-username/your-repo.git
   
Install the required dependencies using pip:
   pip install selenium
   
Download the Chrome WebDriver and place it in the project directory. You can download the WebDriver from the following link: Chrome WebDriver
Usage
Open the main.py file in a text editor.
Modify the url variable to the URL of the web page you want to retrieve values from.
Modify the xpath variable to the XPath expression that identifies the elements containing the values you want to retrieve.

Run the script using the following command:
   python main.py
   
The script will open a Chrome browser window and navigate to the specified URL. It will then retrieve the values using the provided XPath expression and store them in a CSV file named output.csv.
Example
Suppose you want to retrieve the prices of products listed on a web page. The XPath expression for the price elements might be something like:
xpath = "//div[@class='product-price']"
