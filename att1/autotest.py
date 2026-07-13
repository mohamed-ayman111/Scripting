from selenium import webdriver
print("Befor chrom.")
driver = webdriver.Chrome()
print("Chrome opened.")
driver.get("https://www.google.com")
input("Press enter to exit...")
driver.quit()