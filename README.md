---

### <a name="section-a"></a>1.  Project Overview
##### The goal of this project to build an automated service (web) to constantly update a prediction model with happenings in the marketplace so that, at every point in time, users can get semi-accurate prediction of the prices of proposed cars or advice them to make price adjustments for existing ones.

---

### <a name="section-b"></a>2.  Actions



- link_Scraper_Carfax.py -This script gets all the links to the page of the car site that would be scrapped.
- WebScrapping_Script.py - This script scrapes all the links from the above script and stores the car data in a file.
- Data_Cleaning.py - Cleans the car data after scraping.
- Data_Model_create.py - Creates a machine learning model for the prediction of the car price which will be updated in the web app

#### Tools Used: Sklearn, StatsModels, Scipy, Patsy Selenium, Beautiful Soup, Python, Pandas, Matplotlib and Seaborn.




