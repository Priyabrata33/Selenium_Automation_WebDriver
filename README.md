# Selenium_Automation_WebDriver
This repository contains a Selenium automation script written in Python that retrieves values from a web page using XPath and then forms a CSV file. This script can be used to automate data extraction tasks from websites.
Prerequisites
Before running the script, make sure you have the following installed:
Python (version 3.6 or higher)
Selenium library for Python
Chrome WebDriver (compatible with your Chrome browser version)
Installation
Clone this repository to your local machine:
bash

Copy

   git clone https://github.com/your-username/your-repo.git
Install the required dependencies using pip:
bash

Copy

   pip install selenium
Download the Chrome WebDriver and place it in the project directory. You can download the WebDriver from the following link: Chrome WebDriver
Usage
Open the main.py file in a text editor.
Modify the url variable to the URL of the web page you want to retrieve values from.
Modify the xpath variable to the XPath expression that identifies the elements containing the values you want to retrieve.
Run the script using the following command:
bash

Copy

   python main.py
The script will open a Chrome browser window and navigate to the specified URL. It will then retrieve the values using the provided XPath expression and store them in a CSV file named output.csv.
Example
Suppose you want to retrieve the prices of products listed on a web page. The XPath expression for the price elements might be something like:
python

Copy

xpath = "//div[@class='product-price']"
After running the script, the output.csv file will contain the retrieved prices in CSV format.
Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
License
This project is licensed under the MIT License. Feel free to use and modify the code as per your needs.
Acknowledgements
Selenium - Web browser automation framework
Chrome WebDriver - WebDriver for Chrome browser
Contact
If you have any questions or need further assistance, please feel free to contact me at your-email@example.com.
