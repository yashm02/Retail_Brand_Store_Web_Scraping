# Retail_Brand_Store_Web_Scraping

The required modules in the Retail_Brand_Store_Web_Scraping repository are:

selenium: used for web automation and web scraping.

chromedriver: a separate executable that Selenium WebDriver uses to control Chrome. It is specific to the browser and version being used.

time: used to introduce a delay between successive operations.

csv: used for reading and writing CSV files.

geopy: used for converting addresses to geographical coordinates.

beautifulsoup4: used for parsing HTML and XML documents.

webdriver_manager: used for automatically downloading the appropriate chromedriver version.

webdriver_manager.chrome: used for managing the Chrome WebDriver.

requests: used for making HTTP requests and handling responses.

Approach:
For this assignment, I chose to scrape the store locations of Adidas in India. I used Python along with Selenium, BeautifulSoup, and Geopy libraries to extract the store name, address, timings, coordinates, and phone number from the website. Here are the steps I followed:

Open the website https://www.adidas.co.in/storefinder using Selenium and navigate to the Store Finder page.
Extract the URLs of all the cities that have Adidas stores in India.
Loop through each city URL and extract the store details from each store page.
Use BeautifulSoup to parse the HTML and extract the necessary information such as store name, address, timings, and phone number.
Use Geopy to get the latitude and longitude coordinates of the store address.
Store all the extracted information in a CSV file.
Challenges faced:

Extracting the URLs of all the cities that have Adidas stores in India was a bit tricky as they were nested under multiple div tags. However, I was able to use the find_all() function to locate them.
The store timings were listed in a table format and sometimes had multiple timings for different days. I had to use the split() function to separate them and store them in a list.
Getting the coordinates using Geopy was sometimes inaccurate as the address format was not consistent across all store locations. However, I was able to use the Nominatim() function to get the most accurate coordinates possible based on the given address.
Overall, this was a fun and challenging project that helped me practice my web scraping skills. The final CSV file with all the store details can be found in the GitHub repository link provided above.


