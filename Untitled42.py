
# coding: utf-8

# In[129]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# In[130]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# In[131]:


driver = webdriver.Firefox()
driver.get("https://www.google.com")


# In[132]:


input_element = driver.find_element_by_name("q")
input_element.send_keys("Mr. Majnu ")
input_element.submit()
#get_div = driver.find_element_by_id("cst")
#find_elements_by_xpath('.//span[@class = "gbts"])')[2].text


# In[133]:


#get_div = driver.find_element_by_class_name("ifM9O")
get_dive = driver.find_element_by_class_name("NY3LVe").text
#get_divee = driver.find_element_by_class_name("NFQFxe CQKTwc mod").text
print(get_dive)


# In[101]:


gsrt IZACzd
yQ8hqd ksSzJd w6Utff


# In[120]:


aa=driver.find_elements_by_xpath(Xpath=//*[contains(text (),’10’)])


# In[121]:


qw=browser.find_elements_by_xpath('//a[@class = "NY3LVe"]')


# In[118]:


elem = driver.find_element(By.XPATH,'//span[text()="10"]').text

#/html/body/div[6]/div[3]/div[10]/div[1]/div[3]/div/div/div/div[1]/div/div[1]/div[2]/div[3]/div/a[1]/span[1]
print(elem)

