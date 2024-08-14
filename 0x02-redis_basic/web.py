#!/usr/bin/env python3
'''A module with tools for request caching and tracking.
'''
import redis
import requests
from functools import wraps
from typing import Callable


redis_store = redis.Redis()
'''The module-level Redis instance.
'''


def data_cacher(method: Callable) -> Callable:
    '''Caches the output of fetched data.
    '''
    @wraps(method)
    def invoker(url) -> str:
        '''The wrapper function for caching the output.
        '''
        # Increment the access count for the URL
        redis_store.incr(f'count:{url}')
        
        # Check if the result is already in the cache
        result = redis_store.get(f'result:{url}')
        
        if result:
            # If result is cached, return the cached result
            return result.decode('utf-8')
        
        # If not cached, fetch the content
        result = method(url)
        
        # Cache the fetched result with a 10-second expiration
        redis_store.setex(f'result:{url}', 10, result)
        
        return result
    return invoker


@data_cacher
def get_page(url: str) -> str:
    '''Returns the content of a URL after caching the request's response,
    and tracking the request.
    '''
    # Make the HTTP GET request
    response = requests.get(url)
    response.raise_for_status()  # Ensure the request was successful
    return response.text


if __name__ == "__main__":
    # URL for testing, simulating a slow response
    test_url = "http://slowwly.robertomurray.co.uk/delay/3000/url/https://www.example.com"

    # Fetching the page content for the first time
    print("First request:")
    content1 = get_page(test_url)
    print(content1[:100])  # Print first 100 characters of content for brevity

    # Fetching the page content again (should be from cache)
    print("\nSecond request (should be from cache):")
    content2 = get_page(test_url)
    print(content2[:100])  # Print first 100 characters of content for brevity

    # Access count of the URL
    access_count = redis_store.get(f'count:{test_url}').decode('utf-8')
    print(f"\nAccess count for {test_url}: {access_count}")
