# -*- coding:utf-8 -*-
from werkzeug.local import LocalProxy
from ..lib.cache import init_memcached
from .. import config as pi_config

_memcached = None


def _create_memecached():
    """

    :param server:
    :param key_prefix:
    :return:
    """
    global _memcached
    if _memcached is None:
        _memcached = init_memcached(pi_config.MEMCACHED_SERVERS, pi_config.MEMCACHED_KEY_PREFIX)
    return _memcached


memcached = LocalProxy(_create_memecached)