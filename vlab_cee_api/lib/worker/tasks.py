# -*- coding: UTF-8 -*-
"""
Entry point logic for available backend worker tasks
"""
from celery import Celery
from celery.utils.log import get_task_logger

from vlab_cee_api.lib import const
from vlab_cee_api.lib.worker import vmware

app = Celery('cee', backend='rpc://', broker=const.VLAB_MESSAGE_BROKER)
logger = get_task_logger(__name__)
logger.setLevel(const.VLAB_CEE_LOG_LEVEL.upper())


@app.task(name='cee.show')
def show(username):
    """Obtain basic information about CEE instance a user owns

    :Returns: Dictionary

    :param username: The name of the user who wants info about their CEE instances
    :type username: String
    """
    resp = {'content' : {}, 'error': None, 'params': {}}
    logger.info('Task starting')
    try:
        info = vmware.show_cee(username)
    except ValueError as doh:
        logger.error('Task failed: {}'.format(doh))
        resp['error'] = '{}'.format(doh)
    else:
        logger.info('Task complete')
        resp['content'] = info
    return resp


@app.task(name='cee.create')
def create(username, machine_name, image, network):
    """Deploy a new instance of CEE

    :Returns: Dictionary

    :param username: The name of the user who wants to create a new default gateway
    :type username: String

    :param machine_name: The name of the new instance of CEE
    :type machine_name: String

    :param image: The image/version of CEE to create
    :type image: String

    :param network: The name of the network to connect the new instance up to
    :type network: String
    """
    resp = {'content' : {}, 'error': None, 'params': {}}
    logger.info('Task starting')
    try:
        resp['content'] = vmware.create_cee(username, machine_name, image, network)
    except ValueError as doh:
        logger.error('Task failed: {}'.format(doh))
        resp['error'] = '{}'.format(doh)
    logger.info('Task complete')
    return resp


@app.task(name='cee.delete')
def delete(username, machine_name):
    """Destory an instance of CEE

    :Returns: Dictionary

    :param username: The name of the user who wants to destory an instance of CEE
    :type username: String

    :param machine_name: The name of the instance of CEE
    :type machine_name: String
    """
    resp = {'content' : {}, 'error': None, 'params': {}}
    logger.info('Task starting')
    try:
        vmware.delete_cee(username, machine_name)
    except ValueError as doh:
        logger.error('Task failed: {}'.format(doh))
        resp['error'] = '{}'.format(doh)
    else:
        logger.info('Task complete')
    return resp


@app.task(name='cee.image')
def image():
    """Obtain a list of available images/versions of CEE that can be created

    :Returns: Dictionary
    """
    resp = {'content' : {}, 'error': None, 'params': {}}
    logger.info('Task starting')
    resp['content'] = {'image': vmware.list_images()}
    logger.info('Task complete')
    return resp
