import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver = webdriver.Firefox() 
driver.get("https://id.elsevier.com/as/authorization.oauth2?platSite=SC%2Fscopus&ui_locales=en-US&scope=openid+profile+email+els_auth_info+els_analytics_info+urn%3Acom%3Aelsevier%3Aidp%3Apolicy%3Aproduct%3Aindv_identity&els_policy=idp_policy_indv_identity_plus&response_type=code&redirect_uri=https%3A%2F%2Fwww.scopus.com%2Fauthredirect.uri%3FtxGid%3D07f2ce0970823e3918795e73ee216430&state=txId%3D51E33EC2DAE83A28B6C8F7888441BF08.i-054590b6191076542%3A5&authType=bulk&prompt=login&client_id=SCOPUS")
# driver.get("https://www.tutorialspoint.com/javascript/javascript_dialog_boxes.htm")
# Locate the dropdown element
button = driver.find_element(By.ID,"bdd-elsPrimaryBtn")
# button = driver.find_element(By.CSS_SELECTOR,'input[type="submit"][value="Click Me"]')
button.click()  # Clicks on the located button element

# Switch to the alert
alert = driver.switch_to.alert 
alert.accept() # Simulates 'OK' and Accepts the alert dialog, and then dismisses the alert.
# alert.dismiss() is used to simulate 'Cancel'