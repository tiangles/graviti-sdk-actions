import logging
import os
import sys

from graviti import GAS

logger = logging.getLogger()

DATASET_NAME = 'mint desktop background images'


def main():
    try:
        access_key = os.getenv('ACCESS_KEY', '')
        if not access_key:
            raise Exception('failed to get access key from environment.')

        dataset_name = os.getenv('DATASET_NAME', '')
        if not dataset_name:
            raise Exception('failed to get dataset name from environment.')

        logger.info(f'get dataset by name: {dataset_name}')
        gas = GAS(access_key)
        dataset_client = gas.get_dataset(dataset_name)

        logger.info(f'get segment object')
        segment = dataset_client.get_segment_object()
        for data in segment:
            import time
            time.sleep(0.01)
            logger.info(f'{data.remote_path}')

    except Exception as e:
        logger.exception(f'script raise exception: {e}.')

    finally:
        logger.info('application finished.')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    main()
