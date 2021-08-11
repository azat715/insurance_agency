from os import environ
import pytest
import redis

from core.redis_client import RedisConfig, RedisClient


env = environ


@pytest.fixture(name="config")
def fixture_config():
    """Config redis"""
    config = RedisConfig()
    config.host = "localhost"
    config.port = 6379
    return config


def test_client(config):
    """Тестирование RedisClient"""
    r = RedisClient(config)
    r.connect()
    r.set("test:test", "test_value")
    assert r.get("test:test") == "test_value"
    assert r.counter("test_count") == 1
    assert r.counter("test_count") == 2


def test_connect():
    """Тестирование Redis"""
    r = redis.Redis(host="localhost", port=6379, db=0)
    r.set("foo", "bar")
    assert r.get("foo") == b"bar"


@pytest.fixture(name="redis_server")
def fixture_redis_server():
    env["REDIS_SERVER"] = "localhost"


def test_config(redis_server):
    """Тестирование RedisClient"""
    config = RedisConfig.get_config()
    assert config.host == "localhost"
    assert config.port == "6379"
