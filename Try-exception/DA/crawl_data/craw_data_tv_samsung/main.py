from craw_lib.craw_dien_may_xanh import scrape_dienmayxanh
from craw_lib.craw_meta import scrape_meta
from craw_lib.craw_pico import scrape_pico
from craw_lib.craw_hc import scrape_hc
import logging

logging.basicConfig(
    filename='log/app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logging.info("============== Start Log: main.py ==============")

if __name__ == "__main__":
    try: 
        scrape_dienmayxanh()
        scrape_meta()
        scrape_pico()
        scrape_hc()
    except Exception as e:
        logging.error(f'ERROR: {e}')

