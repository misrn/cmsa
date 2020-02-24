import redis
from app import *


class Redis(object):
    def __init__(self):
        self.RedisConnect = redis.Redis(
            host=app.config['REDIS_CONFIG'].get('host'),
            port=app.config['REDIS_CONFIG'].get('port'),
            db=app.config['REDIS_CONFIG'].get('db'),
            password=app.config['REDIS_CONFIG'].get('password'),
            decode_responses=True
        )

    def set(self, key, value, ex=None):
        return self.RedisConnect.set(key, value, ex=ex)

    def get(self, key):
        return self.RedisConnect.get(key)

    def delete(self, key):
        return self.RedisConnect.delete(key)

    def exists(self, key):
        return self.RedisConnect.exists(key)

    def expire(self, key, ex):
        return self.RedisConnect.expire(key, ex)
