import concurrent.futures
from venv import logger
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Get_info import get_vieclam24

        

def main():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    try:
        with webdriver.Chrome(options=chrome_options) as driver:        
            data = get_vieclam24(driver, 10)
            data = list(filter(None, data))
            print(len(data))
           #save_data_into_DB(data)
    except Exception as e:
        logger.error(f"Error occurred while scraping data: {e}")
    print('>> Done')
    
if __name__ == '__main__':
    main()