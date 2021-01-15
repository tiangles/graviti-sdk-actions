import logging
import time

logger = logging.getLogger()


def main():
    logger.info('application started.')
    for i in range(40):
        logger.info(f'\toutput with index {i}')
        time.sleep(2000)
    logger.info('application finished.')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - [%(levelname)s] - %(message)s')
    main()
