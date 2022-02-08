import time
import requests


def decorator(iters):
    def actual_decorator(func):
        def wrapper(url):
            for _ in range(iters):
                start = time.time()
                res = func(url)
                print(f"Status code of response is {res.status_code}")
                stop = time.time()
                print(f'Время выполнения функции {func} - {stop - start} секунд')

        return wrapper

    return actual_decorator


@decorator(iters=5)
def hello(url):
    return requests.get(url)



hello('https://webdevblog.ru/obyasnenie-classmethod-i-staticmethod-v-python/')
