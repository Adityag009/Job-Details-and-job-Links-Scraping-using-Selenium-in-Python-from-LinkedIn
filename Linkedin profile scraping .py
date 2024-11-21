#!/usr/bin/env python
# coding: utf-8

# In[13]:


import requests
from bs4 import BeautifulSoup


# In[14]:


linkedin_profile_url = "https://www.linkedin.com/in/gaurang-khanna-6a0a2026g/"


# In[15]:


# Send a GET request to the LinkedIn profile URL
response = requests.get(linkedin_profile_url)


# In[16]:


# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')


# In[17]:


# Fetch the HTML content of the website
url = 'https://www.linkedin.com/in/aditya-ghadge-a82b30240/'
response = requests.get(url)
html_content = response.text

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')


# In[18]:


soup


# In[5]:


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

from selenium.common.exceptions import NoSuchElementException


# Create a new instance of the Chrome driver
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')


# In[3]:


url1 = "https://www.linkedin.com/in/chiragjhumkhawala/"


driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get(url1)


# In[4]:


# Find the SVG element
svg_element = driver.find_element_by_css_selector('svg.artdeco-icon')

# Click on the SVG element
svg_element.click()


# # Name 

# In[4]:


# Find the name element
name_element = driver.find_element_by_class_name('top-card-layout__title')

# Extract the name
name = name_element.text.strip()

# Print the extracted name
print("Name:", name)


# # Image 

# In[5]:


# Find the image element
image_element = driver.find_element_by_css_selector('img.top-card__profile-image')

# Extract the image URL
image_url = image_element.get_attribute('src')

# Print the extracted image URL
print("Image URL:", image_url)


# # Cover Image 

# In[6]:


# Find the image element
cover_image_element = driver.find_element_by_css_selector('img.cover-img__image')

# Extract the image source
cover_image_src = image_element.get_attribute('src')

print("Cover Image URL:",cover_image_src)


# # About

# In[7]:


# Find and extract the desired information
section_element = driver.find_element_by_css_selector('section[data-section="summary"]')
title_element = section_element.find_element_by_css_selector('h2.core-section-container__title')
content_element = section_element.find_element_by_css_selector('div.core-section-container__content')

title = title_element.text if title_element else 'Title not found'
content = content_element.text if content_element else 'Content not found'

print("Title:", title)
print("Content:", content)


# # Experience

# In[8]:


# Find and extract the desired information
section_element = driver.find_element_by_css_selector('section.core-section-container.experience')
experience_items = section_element.find_elements_by_css_selector('li.profile-section-card.experience-item')

experiences = []

for item in experience_items:
    title_element = item.find_element_by_css_selector('h3.profile-section-card__title')
    subtitle_element = item.find_element_by_css_selector('h4.profile-section-card__subtitle')
    duration_element = item.find_element_by_css_selector('p.experience-item__duration')
    location_elements = item.find_elements_by_css_selector('p.experience-item__location')
    
    title = title_element.text if title_element else 'Title not found'
    subtitle = subtitle_element.text if subtitle_element else 'Subtitle not found'
    duration = duration_element.text if duration_element else 'Duration not found'
    location = location_elements[0].text if location_elements else 'Location not found'
    
    experiences.append({
        'title': title,
        'subtitle': subtitle,
        'duration': duration,
        'location': location
    })

# Print the extracted experiences
for experience in experiences:
    print("Title:", experience['title'])
    print("Subtitle:", experience['subtitle'])
    print("Duration:", experience['duration'])
    print("Location:", experience['location'])
    print()


# In[9]:


# Close the browser
driver.quit()


# In[10]:


url1 = "https://www.linkedin.com/in/manish-kumar-shah/"


driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get(url1)


# In[11]:


# Find the name element
name_element = driver.find_element_by_class_name('top-card-layout__title')

# Extract the name
name = name_element.text.strip()

# Print the extracted name
print("Name:", name)


# In[12]:


# Find the image element
image_element = driver.find_element_by_css_selector('img.top-card__profile-image')

# Extract the image URL
image_url = image_element.get_attribute('src')

# Print the extracted image URL
print("Image URL:", image_url)


# In[68]:


# Find the div element with the class 'cover-img__image-frame'
div_element = driver.find_element_by_css_selector('div.cover-img__image-frame')

# Find the img element within the div element
img_element = div_element.find_element_by_css_selector('img.cover-img__image')

# Extract the src attribute value of the img element
cover_image_url = img_element.get_attribute('src')

# Print the cover image URL
print(cover_image_url)


# In[69]:


# Find and extract the desired information
section_element = driver.find_element_by_css_selector('section[data-section="summary"]')
title_element = section_element.find_element_by_css_selector('h2.core-section-container__title')
content_element = section_element.find_element_by_css_selector('div.core-section-container__content')

title = title_element.text if title_element else 'Title not found'
content = content_element.text if content_element else 'Content not found'

print("Title:", title)
print("Content:", content)


# In[70]:


# Find and extract the desired information
section_element = driver.find_element_by_css_selector('section.core-section-container.experience')
experience_items = section_element.find_elements_by_css_selector('li.profile-section-card.experience-item')

experiences = []

for item in experience_items:
    title_element = item.find_element_by_css_selector('h3.profile-section-card__title')
    subtitle_element = item.find_element_by_css_selector('h4.profile-section-card__subtitle')
    duration_element = item.find_element_by_css_selector('p.experience-item__duration')
    location_elements = item.find_elements_by_css_selector('p.experience-item__location')
    
    title = title_element.text if title_element else 'Title not found'
    subtitle = subtitle_element.text if subtitle_element else 'Subtitle not found'
    duration = duration_element.text if duration_element else 'Duration not found'
    location = location_elements[0].text if location_elements else 'Location not found'
    
    experiences.append({
        'title': title,
        'subtitle': subtitle,
        'duration': duration,
        'location': location
    })

# Print the extracted experiences
for experience in experiences:
    print("Title:", experience['title'])
    print("Subtitle:", experience['subtitle'])
    print("Duration:", experience['duration'])
    print("Location:", experience['location'])
    print()


# In[72]:


get_ipython().system('pip install linkedin-scraper')


# In[ ]:


from linkedin_scraper import Person, actions
from selenium import webdriver
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
email = "johnbell789@yahoo.com"
password = "jOHN789@"
actions.login(driver, email, password)

person = Person("https://www.linkedin.com/in/karishma-kumar-70251046/", driver = driver, scrape=True)


# In[ ]:





# # klnfvk

# In[91]:


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

from selenium.common.exceptions import NoSuchElementException


# Create a new instance of the Chrome driver
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')


# In[92]:


url1 = "https://www.linkedin.com/in/karishma-kumar-70251046/"


driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get(url1)


# In[93]:


# Find the SVG element
svg_element = driver.find_element_by_css_selector('svg.artdeco-icon')

# Click on the SVG element
svg_element.click()


# In[94]:


# Find the name element
name_element = driver.find_element_by_class_name('top-card-layout__title')

# Extract the name
name = name_element.text.strip()

# Print the extracted name
print("Name:", name)

#### Profile Image 
# Find the image element
image_element = driver.find_element_by_css_selector('img.top-card__profile-image')

# Extract the image URL
image_url = image_element.get_attribute('src')

# Print the extracted image URL
print("Image URL:", image_url)

### cover Photo 
# Find the div element with the class 'cover-img__image-frame'
div_element = driver.find_element_by_css_selector('div.cover-img__image-frame')

# Find the img element within the div element
img_element = div_element.find_element_by_css_selector('img.cover-img__image')

# Extract the src attribute value of the img element
cover_image_url = img_element.get_attribute('src')

# Print the cover image URL
print(cover_image_url)

### About 

# Find and extract the desired information
section_element = driver.find_element_by_css_selector('section[data-section="summary"]')
title_element = section_element.find_element_by_css_selector('h2.core-section-container__title')
content_element = section_element.find_element_by_css_selector('div.core-section-container__content')

title = title_element.text if title_element else 'Title not found'
content = content_element.text if content_element else 'Content not found'

print("Title:", title)
print("Content:", content)

# Find and extract the desired information
section_element = driver.find_element_by_css_selector('section.core-section-container.experience')
experience_items = section_element.find_elements_by_css_selector('li.profile-section-card.experience-item')

experiences = []

for item in experience_items:
    title_element = item.find_element_by_css_selector('h3.profile-section-card__title')
    subtitle_element = item.find_element_by_css_selector('h4.profile-section-card__subtitle')
    duration_element = item.find_element_by_css_selector('p.experience-item__duration')
    location_elements = item.find_elements_by_css_selector('p.experience-item__location')
    
    title = title_element.text if title_element else 'Title not found'
    subtitle = subtitle_element.text if subtitle_element else 'Subtitle not found'
    duration = duration_element.text if duration_element else 'Duration not found'
    location = location_elements[0].text if location_elements else 'Location not found'
    
    experiences.append({
        'title': title,
        'subtitle': subtitle,
        'duration': duration,
        'location': location
    })

# Print the extracted experiences
for experience in experiences:
    print("Title:", experience['title'])
    print("Subtitle:", experience['subtitle'])
    print("Duration:", experience['duration'])
    print("Location:", experience['location'])
    print()


# In[95]:


# Find the education list items
education_items = driver.find_elements_by_css_selector(".education__list-item")

# Iterate over each education item and extract the desired information
for item in education_items:
    title = item.find_element_by_css_selector(".profile-section-card__title-link").text
    degree = item.find_element_by_css_selector(".education__item--degree-info").text
    duration = item.find_element_by_css_selector(".education__item--duration").text
    print("Title:", title)
    print("Degree:", degree)
    print("Duration:", duration)
    print()


# In[96]:


# Find the certifications section
certifications_section = driver.find_element_by_css_selector('section[data-section="certifications"]')

# Extract the certifications
certifications = certifications_section.find_elements_by_css_selector('.profile-section-card')

# Iterate over each certification and extract the details
for certification in certifications:
    title = certification.find_element_by_css_selector('.profile-section-card__title').text
    issuer = certification.find_element_by_css_selector('.profile-section-card__subtitle').text
    date = certification.find_element_by_css_selector('.certifications__start-date time').text

    print("Title:", title)
    print("Issuer:", issuer)
    print("Date:", date)
    print()


# In[98]:


try:
    # Find the h3 element containing the information
    h3_element = driver.find_element_by_css_selector('h3.top-card-layout__first-subline')

    # Extract the information from the h3 element
    location = h3_element.find_element_by_css_selector('.top-card__subline-item:nth-of-type(1)').text
    followers = h3_element.find_element_by_css_selector('.top-card__subline-item:nth-of-type(2)').text

    try:
        connections = h3_element.find_element_by_css_selector('.top-card__subline-item:nth-of-type(3)').text
    except NoSuchElementException:
        connections = None

    # Print the extracted information
    print("Location:", location)
    print("Followers:", followers)
    print("Connections:", connections)

except NoSuchElementException:
    print("Unable to locate the element on the page.")


# In[99]:


# Find the list of language elements
language_elements = driver.find_elements_by_css_selector('.languages__list li')

# Extract the languages from the elements
languages = [element.find_element_by_css_selector('.profile-section-card__title').text for element in language_elements]

# Print the extracted languages
for language in languages:
    print(language)


# ## Combine 

# In[105]:


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

# Create a new instance of the Chrome driver
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

url = input("Enter the LinkedIn profile URL: ")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get(url)

# Extract name
try:
    name_element = driver.find_element_by_class_name('top-card-layout__title')
    name = name_element.text.strip()
    print("Name:", name)
except NoSuchElementException:
    print("Name not found")

# Extract profile image URL
try:
    image_element = driver.find_element_by_css_selector('img.top-card__profile-image')
    image_url = image_element.get_attribute('src')
    print("Image URL:", image_url)
except NoSuchElementException:
    print("Profile image URL not found")

# Extract cover photo URL
try:
    div_element = driver.find_element_by_css_selector('div.cover-img__image-frame')
    img_element = div_element.find_element_by_css_selector('img.cover-img__image')
    cover_image_url = img_element.get_attribute('src')
    print("Cover Photo URL:", cover_image_url)
except NoSuchElementException:
    print("Cover photo URL not found")

# Extract About section
try:
    section_element = driver.find_element_by_css_selector('section[data-section="summary"]')
    title_element = section_element.find_element_by_css_selector('h2.core-section-container__title')
    content_element = section_element.find_element_by_css_selector('div.core-section-container__content')

    title = title_element.text if title_element else 'Title not found'
    content = content_element.text if content_element else 'Content not found'

    print("About Section:")
    print("Title:", title)
    print("Content:", content)
except NoSuchElementException:
    print("About section not found")

# Extract Experience section
try:
    section_element = driver.find_element_by_css_selector('section.core-section-container.experience')
    experience_items = section_element.find_elements_by_css_selector('li.profile-section-card.experience-item')

    experiences = []
    print("Experience Section:")
    for item in experience_items:
        title_element = item.find_element_by_css_selector('h3.profile-section-card__title')
        subtitle_element = item.find_element_by_css_selector('h4.profile-section-card__subtitle')
        duration_element = item.find_element_by_css_selector('p.experience-item__duration')
        location_elements = item.find_elements_by_css_selector('p.experience-item__location')

        title = title_element.text if title_element else 'Title not found'
        subtitle = subtitle_element.text if subtitle_element else 'Subtitle not found'
        duration = duration_element.text if duration_element else 'Duration not found'
        location = location_elements[0].text if location_elements else 'Location not found'

        experience = {
            'title': title,
            'subtitle': subtitle,
            'duration': duration,
            'location': location
        }
        experiences.append(experience)
        print("Title:", title)
        print("Subtitle:", subtitle)
        print("Duration:", duration)
        print("Location:", location)
        print()
except NoSuchElementException:
    print("Experience section not found")

# Extract Education section
try:
    education_items = driver.find_elements_by_css_selector('.education__list-item')
    print("Education Section:")
    for item in education_items:
        title = item.find_element_by_css_selector(".profile-section-card__title-link").text
        degree = item.find_element_by_css_selector(".education__item--degree-info").text
        duration = item.find_element_by_css_selector(".education__item--duration").text
        print("Title:", title)
        print("Degree:", degree)
        print("Duration:", duration)
        print()
except NoSuchElementException:
    print("Education section not found")

# Extract Certifications section
try:
    certifications_section = driver.find_element_by_css_selector('section[data-section="certifications"]')
    certifications = certifications_section.find_elements_by_css_selector('.profile-section-card')
    print("Certifications Section:")
    for certification in certifications:
        title = certification.find_element_by_css_selector('.profile-section-card__title').text
        issuer = certification.find_element_by_css_selector('.profile-section-card__subtitle').text
        date = certification.find_element_by_css_selector('.certifications__start-date time').text

        print("Title:", title)
        print("Issuer:", issuer)
        print("Date:", date)
        print()
except NoSuchElementException:
    print("Certifications section not found")

# Extract Location, Followers, and Connections
try:
    h3_element = driver.find_element_by_css_selector('h3.top-card-layout__first-subline')
    location = h3_element.find_element_by_css_selector('.top-card__subline-item:nth-of-type(1)').text
    followers = h3_element.find_element_by_css_selector('.top-card__subline-item:nth-of-type(2)').text

    try:
        connections = h3_element.find_element_by_css_selector('.top-card__subline-item:nth-of-type(3)').text
    except NoSuchElementException:
        connections = None

    print("Location:", location)
    print("Followers:", followers)
    print("Connections:", connections)
except NoSuchElementException:
    print("Location, Followers, and Connections not found")

# Extract Languages
try:
    language_elements = driver.find_elements_by_css_selector('.languages__list li')
    languages = [element.find_element_by_css_selector('.profile-section-card__title').text for element in language_elements]

    print("Languages:")
    for language in languages:
        print(language)
except NoSuchElementException:
    print("Languages not found")



# In[ ]:





# ## 2nd approach with login 

# In[2]:


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

from selenium.common.exceptions import NoSuchElementException


# Create a new instance of the Chrome driver
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')


# In[16]:


url1 = "https://www.linkedin.com"


driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get(url1)


# In[18]:


username=driver.find_element_by_id("session_key")

username.send_keys("johnbell789@yahoo.com")

password = driver.find_element_by_id("session_password")
password.send_keys("jOHN789@")


# In[19]:


login_button = driver.find_element_by_class_name("sign-in-form__submit-btn--full-width")
login_button.click()


# In[20]:


driver.get('https://www.linkedin.com/in/agneesh-banerjee27/')


# In[ ]:


# Find and scrape the profile photo URL
profile_photo = driver.find_element_by_css_selector("img.profile-photo").get_attribute("src")
# Find and scrape the name and connection level
name = driver.find_element_by_css_selector(".name").text
# Find and scrape the current company name 
current_company_name = driver.find_element_by_css_selector(".current-company-name").text
# Find and scrape the location
location = driver.find_element_by_css_selector(".location").text
# Find and scrape the number of connections
connections = driver.find_element_by_css_selector(".connections").text
# Print the scraped information
print("Profile Photo:", profile_photo)
print("Name:", name)
print("Current Company Name:", current_company_name)
print("Location:", location)
print("Connections:", connections)


# In[ ]:





# ## photo and Name

# In[24]:


# Find and extract the profile photo
photo_element = driver.find_element_by_css_selector('.pv-top-card-profile-picture__image')
photo_src = photo_element.get_attribute('src')

# Find and extract the profile name
name_element = driver.find_element_by_css_selector('.text-heading-xlarge')
name = name_element.text

# Print the scraped information
print('Photo URL:', photo_src)
print('Name:', name)


# ## Location 

# In[25]:


# Find and extract the location
location_element = driver.find_element_by_css_selector('.text-body-small.inline.t-black--light.break-words')
location = location_element.text.strip()

# Print the scraped location
print('Location:', location)


# ## Connection 

# In[28]:


connection_number_element = driver.find_element(By.CSS_SELECTOR, '.t-black--light .t-bold')
connection_number = connection_number_element.text
print('connection_number:',connection_number)


# ## About 

# In[33]:


# Find and extract the "About" information
about_element = driver.find_element_by_css_selector('.text-body-small.inline.t-black--light.break-words')
about_text = about_element.text

# Print the scraped "About" information
print('About:', about_text)


# In[40]:


# Find and extract the desired information
about_element = driver.find_element_by_css_selector('div.pv-shared-text-with-see-more')
content_element = about_element.find_element_by_css_selector('span[aria-hidden="true"]')

content = content_element.text if content_element else 'Content not found'

# Print the scraped information
print("Title:"  "About")
print("Content:", content)


# In[41]:


# Find and extract the desired information
job_title_element = driver.find_element_by_css_selector('div.display-flex.full-width div.display-flex.align-items-center.mr1.t-bold span[aria-hidden="true"]')
company_element = driver.find_element_by_css_selector('div.display-flex.flex-row.justify-space-between span.t-14.t-normal')
duration_element = driver.find_element_by_css_selector('div.display-flex.flex-row.justify-space-between span.t-14.t-normal.t-black--light')
location_element = driver.find_element_by_css_selector('div.display-flex.flex-row.justify-space-between span.t-14.t-normal.t-black--light:nth-child(3)')
skills_element = driver.find_element_by_css_selector('div.pv-shared-text-with-see-more span[aria-hidden="true"]')

job_title = job_title_element.text if job_title_element else 'Job Title not found'
company = company_element.text if company_element else 'Company not found'
duration = duration_element.text if duration_element else 'Duration not found'
location = location_element.text if location_element else 'Location not found'
skills = skills_element.text if skills_element else 'Skills not found'

# Print the scraped information
print("Job Title:", job_title)
print("Company:", company)
print("Duration:", duration)
print("Location:", location)
print("Skills:", skills)


# In[57]:






# In[63]:


# Find the job listing elements
job_listings = driver.find_elements(By.CSS_SELECTOR, '.pvs-entity')

# Iterate through each job listing and extract the details
for job_listing in job_listings:
    job_title_element = job_listing.find_element(By.CSS_SELECTOR, 'div.display-flex.align-items-center.mr1.t-bold span[aria-hidden="true"]')
    company_element = job_listing.find_element(By.CSS_SELECTOR, 'div.display-flex.flex-row.justify-space-between span.t-14.t-normal')
    duration_element = job_listing.find_element(By.CSS_SELECTOR, 'span.t-14.t-normal')
    location_element = job_listing.find_element(By.CSS_SELECTOR, 'span.t-14.t-normal.t-black--light:nth-child(3)')
    
    try:
        skills_element = job_listing.find_element(By.CSS_SELECTOR, 'div.inline-show-more-text span[aria-hidden="true"]')
        skills = skills_element.text
    except NoSuchElementException:
        skills = 'Skills not found'

    job_title = job_title_element.text if job_title_element else 'Job Title not found'
    company = company_element.text if company_element else 'Company not found'
    duration = duration_element.text if duration_element else 'Duration not found'
    location = location_element.text if location_element else 'Location not found'

    print('Company:', company)
    print('Job Title:', job_title)
    print('Duration:', duration)
    print('Location:', location)
    print('Skills:', skills)
    print('---')


# In[64]:


# Find the job listing elements
job_listings = driver.find_elements(By.CSS_SELECTOR, '.pvs-entity')

# Iterate through each job listing and extract the details
for job_listing in job_listings:
    job_title_element = job_listing.find_element(By.CSS_SELECTOR, 'div.display-flex.align-items-center.mr1.t-bold span[aria-hidden="true"]')
    company_element = job_listing.find_element(By.CSS_SELECTOR, 'div.display-flex.flex-row.justify-space-between span.t-14.t-normal')
    duration_element = job_listing.find_element(By.CSS_SELECTOR, 'span.t-14.t-normal')
    
    try:
        location_element = job_listing.find_element(By.CSS_SELECTOR, 'span.t-14.t-normal.t-black--light:nth-child(4)')
        location = location_element.text
    except NoSuchElementException:
        location = 'Location not found'
    
    try:
        skills_element = job_listing.find_element(By.CSS_SELECTOR, 'div.inline-show-more-text span[aria-hidden="true"]')
        skills = skills_element.text
    except NoSuchElementException:
        skills = 'Skills not found'

    job_title = job_title_element.text if job_title_element else 'Job Title not found'
    company = company_element.text if company_element else 'Company not found'
    duration = duration_element.text if duration_element else 'Duration not found'

    print('Company:', company)
    print('Job Title:', job_title)
    print('Duration:', duration)
    print('Location:', location)
    print('Skills:', skills)
    print('---')


# In[66]:


# Find the job listing elements
job_listings = driver.find_elements(By.CSS_SELECTOR, '.pvs-entity')

# Iterate through each job listing and extract the details
for job_listing in job_listings:
    job_title_element = job_listing.find_element(By.CSS_SELECTOR, 'div.display-flex.align-items-center.mr1.t-bold span[aria-hidden="true"]')
    company_element = job_listing.find_element(By.XPATH, './/div[contains(@class, "display-flex")]/span[contains(@class, "t-14")][not(contains(@class, "t-black--light"))]')
    duration_element = job_listing.find_element(By.CSS_SELECTOR, 'span.t-14.t-normal')
    
    try:
        location_element = job_listing.find_element(By.XPATH, './/span[contains(@class, "t-14") and contains(@class, "t-black--light")][3]')
        location = location_element.text
    except NoSuchElementException:
        location = 'Location not found'
    
    try:
        skills_element = job_listing.find_element(By.CSS_SELECTOR, 'div.inline-show-more-text span[aria-hidden="true"]')
        skills = skills_element.text
    except NoSuchElementException:
        skills = 'Skills not found'

    job_title = job_title_element.text if job_title_element else 'Job Title not found'
    company = company_element.text if company_element else 'Company not found'
    duration = duration_element.text if duration_element else 'Duration not found'

    print('Company:', company)
    print('Job Title:', job_title)
    print('Duration:', duration)
    print('Location:', location)
    print('Skills:', skills)
    print('---')


# In[79]:


job_elements = driver.find_elements_by_class_name("pvs-list__item--one-column")

# Iterate over each job element and extract the desired information
for job_element in job_elements:
    # Extract the job title
    job_title_element = job_element.find_element_by_class_name("t-bold")
    job_title = job_title_element.text

    # Extract the company name
    company_name_element = job_element.find_element_by_class_name("pvs-entity__info-name")
    company_name = company_name_element.text

    # Extract the job duration
    job_duration_element = job_element.find_element_by_class_name("t-14.t-normal.t-black--light")
    job_duration = job_duration_element.text

    # Extract the job location
    job_location_element = job_element.find_elements_by_class_name("t-14.t-normal.t-black--light")[1]
    job_location = job_location_element.text

    # Print the extracted information
    print("Job Title:", job_title)
    print("Company Name:", company_name)
    print("Job Duration:", job_duration)
    print("Job Location:", job_location)
    print("-----------------------------------------")


# In[76]:


experience_list


# In[ ]:




