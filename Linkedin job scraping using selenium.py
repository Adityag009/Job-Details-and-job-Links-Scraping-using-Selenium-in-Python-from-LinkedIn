#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
import time
import pandas as pd 
import os

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys


# Create a new instance of the Chrome driver
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')


# In[2]:


url1 = "https://www.linkedin.com"


driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get(url1)


# In[3]:


username=driver.find_element_by_id("session_key")

username.send_keys("johnbell789@yahoo.com")


# In[4]:


password = driver.find_element_by_id("session_password")
password.send_keys("jOHN789@")


# In[5]:


login_button = driver.find_element_by_class_name("sign-in-form__submit-btn--full-width")


# In[6]:


login_button.click()


# In[7]:


driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3450108431&distance=25&f_TPR=r604800&geoId=90009496&keywords=%22chief%20financial%20officer%22&sortBy=DD")


# In[9]:


# Get all links for these offers
links = []

# Navigate  pages
print('Links are being collected now.')
try: 
    for page in range(2,4):
        time.sleep(2)
        jobs_block = driver.find_element_by_class_name('scaffold-layout__list-detail-inner')
        jobs_list= jobs_block.find_elements(By.CSS_SELECTOR, '.jobs-search-results__list-item')
        
        
    
        for job in jobs_list:
            all_links = job.find_elements_by_tag_name('a')
            for a in all_links:
                if str(a.get_attribute('href')).startswith("https://www.linkedin.com/jobs/view") and a.get_attribute('href') not in links: 
                    links.append(a.get_attribute('href'))
                else:
                    pass
            # scroll down for each job element
            driver.execute_script("arguments[0].scrollIntoView();", job)
        
        print(f'Collecting the links in the page: {page-1}')
        # go to next page:
        driver.find_element_by_xpath(f"//button[@aria-label='Page {page}']").click()
        time.sleep(3)
except:
    pass
print('Found ' + str(len(links)) + ' links for job offers')


# In[10]:



# Create empty lists to store information
job_titles = []
company_names = []
company_locations = []

post_dates = []
company_sizes = []
company_industries = []
i = 0
j = 1
# Visit each link one by one to scrape the information
print('Visiting the links and collecting information just started.')
for i in range(len(links)):
    try:
        driver.get(links[i])
        i=i+1
        time.sleep(2)
        # Click See more.
        driver.find_element_by_class_name("artdeco-card__actions").click()
        time.sleep(2)
    except:
        pass
        # Find the general information of the job offers
    contents = driver.find_elements_by_class_name('p5')
    for content in contents:
        try:
            job_titles.append(content.find_element_by_tag_name("h1").text)
            company_names.append(content.find_element_by_class_name("jobs-unified-top-card__company-name").text)
            company_locations.append(content.find_element_by_class_name("jobs-unified-top-card__bullet").text)
            post_dates.append(content.find_element_by_class_name("jobs-unified-top-card__posted-date").text)
            print(f'Scraping the Job Offer {j} DONE.')
            j+= 1
            
        except:
            pass
        time.sleep(2)
       # Scraping the company info
        company_info = driver.find_elements_by_class_name('jobs-company__box')
        for info in company_info:
            job_text = info.find_element_by_css_selector(".jobs-company__inline-information").text
            company_sizes.append(job_text)
            
            time.sleep(2)
            
            c_indus = driver.find_element_by_xpath("//div[@class='t-14 mt5']")
            industry = c_indus.text.split("\n")[0]
            company_industries.append(industry)
            print(f'Scraping the Job Offer {j}')
            time.sleep(2)


# In[11]:


df = pd.DataFrame(list(zip(company_names,company_sizes,company_industries,job_titles,company_locations,post_dates,links)),columns =['company_name','company_sizes','company_industries','job_titles','company_locatio','post_date','links'])


# In[12]:


df


# In[13]:


df.to_csv("jobsearch.csv")


# In[ ]:




