import logging

from graviti import GAS

logger = logging.getLogger()

ACCESS_KEY = 'Accesskey-b282d0e49157142b76ea3105b56066f0'
DATASET_NAME = 'mint desktop background images'


def main():
    # logger.info('application started.')
    try:
        gas = GAS(ACCESS_KEY)
        dataset_client = gas.get_dataset(DATASET_NAME)
        segment = dataset_client.get_segment_object()
        logger.info(f'list images in dataset segment')
        for data in segment:
            logger.info(data.remote_path)

    except Exception as e:
        logger.exception(f'script raise exception: {e}.')

    # finally:
    #     logger.info('application finished.')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
    main()
