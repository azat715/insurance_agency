from _pytest import config
import pytest
import redis

from core.redis_client import RedisConfig, RedisClient


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


def test_connect():
    """Тестирование Redis"""
    r = redis.Redis(host="localhost", port=6379, db=0)
    r.set("foo", "bar")
    assert r.get("foo") == b"bar"


def test_config():
    """Тестирование RedisClient"""
    config = RedisConfig.get_config()
    assert config.host is None
    assert config.port == "6379"
