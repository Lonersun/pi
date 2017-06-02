# -*- coding:utf-8 -*-
from werkzeug.contrib.cache import MemcachedCache as _MemcachedCache, text_type


class MemcachedCache(_MemcachedCache):

    def add(self, key, value, timeout=None):
        if timeout is None:
            timeout = self.default_timeout
        if isinstance(key, text_type):
            key = key.encode('utf-8')
        if self.key_prefix:
            key = self.key_prefix + key
        return self._client.add(key, value, timeout)


def init_memcached(server, key_prefix):
    memcached = MemcachedCache(server, key_prefix=key_prefix)
    return memcached
