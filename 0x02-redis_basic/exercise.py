#!/usr/bin/env python3
'''Redis practice'''
from redis import Redis
from functools import wraps
from uuid import uuid4
from typing import Callable, Optional, Union


def count_calls(method: Callable) -> Callable:
    '''Decrator that counts the number of times a method is called'''
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''Wrapper function'''
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    '''Decorator that tore the history of inputs and outputs'''
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''Wrapper function'''
        key = method.__qualname__
        self._redis.rpush(key + ":inputs", str(args))
        returns = method(self, *args, *kwargs)
        return self._redis.rpush(key + ":outputs", returns)

    return wrapper


def replay(fn: Callable) -> None:
    '''display the history of calls of a particular function'''
    name = fn.__qualname__
    r = Redis()
    call_no = r.get(name).decode('utf-8')  # type: ignore
    print(f'{name} was called {call_no} times:')
    input_list = r.lrange(name + ":inputs", 0, -1)
    output_list = r.lrange(name + ":outputs", 0, -1)
    for i, o in zip(input_list, output_list):
        print(f'{name}(*{i.decode("utf-8")}) -> {o.decode("utf-8")}')


class Cache():
    '''Work with a redis cache'''
    def __init__(self) -> None:
        '''Initializes Redis client'''
        self._redis = Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''Takes a data argument and returns a string'''
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None)\
            -> Union[str, bytes, int, float, None]:
        '''Retieves value of a key'''
        ret_val = self._redis.get(key)
        if ret_val and fn and callable(fn):
            return fn(ret_val)
        else:
            return ret_val

    def get_str(self, key: str) -> str:
        '''Converts argument to a string'''
        return self.get(arg, lambda d: d.decode("utf-8"))  # type: ignore

    def get_int(self, key: str) -> int:
        '''Converts argument to an integer'''
        return self.get(arg, lambda d: int(d.decode("utf-8")))  # type: ignore
