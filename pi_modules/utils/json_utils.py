# -*- coding:utf-8 -*-
import json
from bson.json_util import (default as bson_object_default,
                            object_hook as bson_object_hook)


def json_load(s):
    return json.loads(s, encoding='utf-8', object_hook=bson_object_hook)


def json_dump(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, default=bson_object_default,
                      encoding='utf-8')