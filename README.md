# BIA-Web-Scraping-Workshop

## Table of contents
1. [Introduction](#introduction)
2. [Slides](#slides)
3. [Installation Guide](#installation)
4. [Directory for Scrapy Spider](#directory)

## Introduction <a name="introduction"></a>
This repository is for SMU Business Intelligence & Analytics (BIA) Club's 2022 Web Scraping Workshop.

---
## Slides <a name="slides"></a>
Powerpoint Slides can be found here [here](https://docs.google.com/presentation/d/1t8OSbUX9dvG6IqL46JcsOhKldwvD912Z/edit?rtpof=true). You can access it using your SMU email address.

---
## Installation Guide <a name="installation"></a>
You may follow the following commands to install required dependencies and create a project folder.

1) Change to any directory you wish to use
```
cd <path_to_directory>
```

2) Create a project folder
```
mkdir <folder_name>
```

3) Create a virtual environment
```
python -m venv <env_name>
# OR
python3 -m venv <env_name>
```

4) Activate your virtual environment
```
# For Windows users
<env_name>\Scripts\activate.bat

# For Mac/Linux users
source <env_name>/bin/activate
```

4) Install necessary dependencies
```
pip install scrapy scrapy_playwright Pillow pandas
playwright install
```

5) To start a Scrapy project and work with it
```
scrapy startproject <project_name>
cd <project_name>
```
---

## Directory for Scrapy Spider <a name="directory"></a>
This section briefly explains what each spider python script in [spiders](https://github.com/CJianYu98/BIA-Web-Scraping-Workshop/tree/main/tutorial/tutorial/spiders) folder is meant for. 

1) [lab1.py](https://github.com/CJianYu98/BIA-Web-Scraping-Workshop/blob/main/tutorial/tutorial/spiders/lab1.py) -> Code for Lab 1
2) [lab2_v1.py](https://github.com/CJianYu98/BIA-Web-Scraping-Workshop/blob/main/tutorial/tutorial/spiders/lab2_v1.py) -> Code for Lab 2 (hardcoding the year)
3) [lab2_v2.py](https://github.com/CJianYu98/BIA-Web-Scraping-Workshop/blob/main/tutorial/tutorial/spiders/lab2_v2.py) -> Code for Lab 2 (sending duplicate requests for all years)
4) [lab2_v3.py](https://github.com/CJianYu98/BIA-Web-Scraping-Workshop/blob/main/tutorial/tutorial/spiders/lab2_v3.py) -> Code for Lab 2 (sequetial scripting for each year)
5) [pandas_read_html.ipynb](https://github.com/CJianYu98/BIA-Web-Scraping-Workshop/blob/main/tutorial/tutorial/spiders/pandas_read_html.ipynb) -> Demo on how to get table data using Pandas
6) [tut1_part1.py](https://github.com/CJianYu98/BIA-Web-Scraping-Workshop/blob/main/tutorial/tutorial/spiders/tut1_part1.py) -> Tutorial 1, basic scripting, intro to CSS and Xpath selectors
7) [tut2_part1.py](https://github.com/CJianYu98/BIA-Web-Scraping-Workshop/blob/main/tutorial/tutorial/spiders/tut2_part1.py) -> Tutorial 2, intro to Scrapy Item class
8) [tut2_part2.py](https://github.com/CJianYu98/BIA-Web-Scraping-Workshop/blob/main/tutorial/tutorial/spiders/tut2_part2.py) -> Tutorial 2, intro to Scrapy Itemloader class
9) [tut3_part1.py](https://github.com/CJianYu98/BIA-Web-Scraping-Workshop/blob/main/tutorial/tutorial/spiders/tut3_part1.py) -> Tutorial 3, scraping multiple URLs/pages (hardcoding)
10) [tut3_part2.py](https://github.com/CJianYu98/BIA-Web-Scraping-Workshop/blob/main/tutorial/tutorial/spiders/tut3_part2.py) -> Tutorial 3, web crawling (using next page href)
11) [tut3_part3.py](https://github.com/CJianYu98/BIA-Web-Scraping-Workshop/blob/main/tutorial/tutorial/spiders/tut3_part3.py) -> Tutorial 3, web crawling (using pagination)
12) [tut3_part4.py](https://github.com/CJianYu98/BIA-Web-Scraping-Workshop/blob/main/tutorial/tutorial/spiders/tut3_part4.py) -> Tutorial 3, Scrapy FormRequest to login
13) [tut3_part5.py](https://github.com/CJianYu98/BIA-Web-Scraping-Workshop/blob/main/tutorial/tutorial/spiders/tut3_part5.py) -> Tutorial 3, downloading images using Scrapy in-built image pipelines
14) [main.py](https://github.com/CJianYu98/BIA-Web-Scraping-Workshop/blob/main/tutorial/main.py) (tut3 part6) -> Tutorial 3, run multiple Spiders in 1 python file
15) [tut3_part7.py](https://github.com/CJianYu98/BIA-Web-Scraping-Workshop/blob/main/tutorial/tutorial/spiders/tut3_part7.py) -> Tutorial 3, bypassing with User Agent/proxy
16) [tut4_part1.py](https://github.com/CJianYu98/BIA-Web-Scraping-Workshop/blob/main/tutorial/tutorial/spiders/tut4_part1.py) -> Tutorial 4, basic scraping of Javascript rendered websites using Scrapy-Playwright
17) [tut4_part2.py](https://github.com/CJianYu98/BIA-Web-Scraping-Workshop/blob/main/tutorial/tutorial/spiders/tut4_part2.py) -> Tutorial 4, scraping multiple pages/crawling with Scrapy-Playwright
18) [tut4_part3.py](https://github.com/CJianYu98/BIA-Web-Scraping-Workshop/blob/main/tutorial/tutorial/spiders/tut4_part3.py) -> Tutorial 4, scrolling all the way down
19) [tut4_part4.py](https://github.com/CJianYu98/BIA-Web-Scraping-Workshop/blob/main/tutorial/tutorial/spiders/tut4_part4.py) -> Tutorial 4, taking screenshot
20) [tut4_part5.py](https://github.com/CJianYu98/BIA-Web-Scraping-Workshop/blob/main/tutorial/tutorial/spiders/tut4_part5.py) -> Tutorial 4, Demo on Opencart Login website (filling input fields and clicking)
21) [tut4_part6.py](https://github.com/CJianYu98/BIA-Web-Scraping-Workshop/blob/main/tutorial/tutorial/spiders/tut4_part6.py) -> Tutorial 4, Demo on Twitch website (typing in search bar, keyboard press) 
22) [tut4_part7.py](https://github.com/CJianYu98/BIA-Web-Scraping-Workshop/blob/main/tutorial/tutorial/spiders/tut4_part7.py) -> Tutorial 4, Demo on Lazada website (Scrapy-Playwright optimization)

