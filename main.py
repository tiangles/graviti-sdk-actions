import logging

from graviti import GAS

logger = logging.getLogger()

ACCESS_KEY = 'Accesskey-b5df9e1e22866b882dc146e5ba0f5645'


def main():
    logger.info('application started.')
    try:
        gas = GAS(ACCESS_KEY)
        datasets = gas.list_datasets()
        for item in datasets:
            logger.info(f'get dataset item {item}.')
    except Exception as e:
        logger.exception(f'script raise exception: {e}.')
    finally:
        logger.info('application finished.')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - [%(levelname)s] - %(message)s')
    main()
