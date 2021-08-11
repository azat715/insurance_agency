from __future__ import annotations
from typing import Union
import redis
from django.conf import settings


class RedisConfig:
    """Класс настроек Redis"""

    def __init__(self) -> None:
        """
        Attribute:
            host: Redis host
            port: Redis port
            db: Redis db numer
        """
        self._host = None
        self._port = None
        self._db = None

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, value):
        if value is None:
            raise ValueError("Redis host не должен быть None")
        self._host = value

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, value):
        if value is None:
            raise ValueError("Redis port не должен быть None")
        self._port = value

    @property
    def db(self):
        if self._db is None:
            return 0
        return self._db

    @db.setter
    def db(self, value):
        if value is None:
            self._db = 0
        self._db = value

    @classmethod
    def get_config(cls) -> RedisConfig:
        """Чтение настроек redis из django.conf

        Raises:
            Exception: Если нет ключа в settings.REDIS
        """
        try:
            config = cls()
            config.host = settings.REDIS["HOST"]
            config.port = settings.REDIS["PORT"]
        except KeyError as err:
            print("KeyError: {0}".format(err))
            raise Exception("Проверьте настроки REDIS Django settings.py")
        return config


class RedisClient:
    def __init__(self, config: RedisConfig) -> None:
        self.config = config
        self.r = None

    def connect(self) -> None:
        self.r = redis.Redis(
            host=self.config.host, port=self.config.port, db=self.config.db
        )

    def set(self, key, value) -> bool:
        return self.r.set(key, value)

    def get(self, key) -> Union[str, int, None]:
        res = self.r.get(key)
        if res:
            if isinstance(res, int):
                return res
            return res.decode("utf-8")
        else:
            return None

    def is_exist(self, key) -> bool:
        if self.r.exists(key) == 1:
            return True
        return False

    def counter(self, key) -> int:
        if self.is_exist(key):
            return self.r.incr(key)
        self.set(key, 1)
        return 1
