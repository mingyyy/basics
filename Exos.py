#
# In order to solve the problems below you can import any standard
# python3 library.
#
# If you don't know Python, implement it in any other language.
#
# Good luck!
#


############
#
# Cheap Crowdfunding Problem
#
# There is a crowdfunding project that you want to support. This project
# gives the same reward to every supporter, with one peculiar condition:
# the amount you pledge must not be equal to any earlier pledge amount.
#
# You would like to get the reward, while spending the least amount > 0.
#
# You are given a list of amounts pledged so far in an array of integers.
# You know that there is less than 100,000 of pledges and the maximum
# amount pledged is less than $1,000,000.
#
# Implement a function find_min_pledge(pledge_list) that will return
# the amount you should pledge.
#
############

def find_min_pledge(pledge_list):
    '''
    input: a list of amounts pledged so far (array of intergers)
    output: the minimum amount you pledge (a positive integer)
    '''

    # Because there is less than 100k of pledges,even every pledge is       # unqiue there should be amount available in the set of 1 to 1           # million. Therefore assume there is always a solution.
    if type(pledge_list) is list:
        n = len(pledge_list)
        if n == 0:
            return 1

        for i in range(1, n + 1):
            if i not in pledge_list:
                return i
        return i + 1
    else:
        return None


import pytest


def test_empty():
    assert find_min_pledge([]) == 1


def test_middle():
    assert find_min_pledge([1, 3, 6, 4, 1, 2]) == 5


def test_upper():
    assert find_min_pledge([1, 2, 3]) == 4


def test_negative():
    assert find_min_pledge([-1, -3]) == 1


def test_duplicate():
    assert find_min_pledge([1, 1, 1]) == 2


def test_nonlist():
    assert find_min_pledge(1) == None


pytest.main()

############
#
# Extract Titles from RSS feed
#
# Implement get_headlines() function. It should take a url of an RSS feed
# and return a list of strings representing article titles.
#
############

# Method 1 - requests_html is not part of the standard library
# from requests_html import HTMLSession
# def get_headlines(rss_url):
#     """
#     @returns a list of titles from the rss feed located at `rss_url`
#     """
#     session = HTMLSession()
#     page = session.get(rss_url)

#     # Assume we only want title under 'item', meaning excluding the main title, e.g. Top stories - Google News
#     title = page.html.find('item>title', first=False)
#     list_title =[]
#     for i in title:
#         list_title.append(i.text)
#     return list_title
# import requests

# Method 2
import requests

google_news_url = "https://news.google.com/news/rss"


def get_headlines(rss_url):
    """
    input: a valid url ('rss_url')
    @returns a list of titles from the rss feed located at `rss_url`
    """
    try:
        response = requests.get(rss_url)
    except:
        print("Sorry, your url is not valid!")

    if response.status_code != 200:
        print("Sorry, please check your url!")

    total = response.text
    title_list = []
    for i in range(len(total)):
        if total[i:i + 7] == '<title>':
            j = i + 7
            title = ''
            while total[j:j + 8] != '</title>':
                title += total[j]
                j += 1
            title_list.append(title)

    # Assume we want all article titles only, meaning excluding the main title, e.g. Top stories - Google News
    return title_list[1:]


print(get_headlines(google_news_url))

############
#
# Streaming Payments Processor
#
# The function `process_payments()` is processing a large, but finite
# amount of payments in a streaming fashion.
#
# It relies on two library functions to do its job. The first function
# `stream_payments_to_storage(storage)` reads the payments from a payment
# processor and writes them to storage by calling `storage.write(buffer)`
# on it's `storage` argument. The `storage` argument is supplied by
# calling `get_payments_storage()` function. The API is defined below.
#
# TODO: Modify `process_payments()` to print a checksum of bytes written
# by `stream_payments_to_storage()`. The existing functionality
# should be preserved.
#
# The checksum is implemented as a simple arithmetic sum of bytes.
#
# For example, if bytes([1, 2, 3]) were written, you should print 6.
#
#
# NOTE: you need to take into account the following restrictions:
# - You are allowed only one call each to `get_payments_storage()` and
#       to `stream_payments_to_storage()`
# - You can not read from the storage.
# - You can not use disk as temporary storage.
# - Your system has limited memory that can not hold all payments.
#
############
import io


# import functools
# def cache(func):
#     """Keep a cache of previous function calls"""
#     @functools.wraps(func)
#     def wrapper_cache(*args, **kwargs):
#         cache_key = args + tuple(kwargs.items())
#         if cache_key not in wrapper_cache.cache:
#             wrapper_cache.cache[cache_key] = func(*args, **kwargs)
#         return wrapper_cache.cache[cache_key]
#     wrapper_cache.cache = dict()
#     return wrapper_cache

class Storage():
    def __init__(self):
        self.total = 0
        self.storage = None

    def get_storage(self):
        self.storage = get_payments_storage()

    def write(self, nums):
        self.total = sum(nums)
        self.storage.write(nums)

# This is a library function, you can't modify it.
def get_payments_storage():
    """
    @returns an instance of
    https://docs.python.org/3/library/io.html#io.BufferedWriter
    """
    # Sample implementation to make the code run in coderpad.
    # Do not rely on this exact implementation.
    return open('/dev/null', 'wb')


# This is a library function, you can't modify it.
# @cache
def stream_payments_to_storage(storage):
    """
    Loads payments and writes them to the `storage`.
    Returns when all payments have been written.

    @parameter `storage`: is an instance of
    https://docs.python.org/3/library/io.html#io.BufferedWriter
    """
    # Sample implementation to make the code run in coderpad.
    # Do not rely on this exact implementation.
    for i in range(10):
        storage.write(bytes([1, 2, 3]))


def process_payments():
    """
    TODO:
    Modify `process_payments()` to print the checksum of data
    generated by the `stream_payments_to_storage()` call.
    """

    payments_storage = Storage()
    payments_storage.get_storage()
    stream_payments_to_storage(payments_storage)
    # Here print the check sum of all of the bytes written by
    # `stream_payments_to_storage()`
    print(payments_storage.total)


print(process_payments())

############
# Streaming Payments Processor, two vendors edition.
#
# We decided to improve the payment processor from the previous
# exercise and hired two vendors. One was to implement `stream_payments()`
# function, and another `store_payments()` function.
#
# The function `process_payments_2()` is processing a large, but finite
# amount of payments in a streaming fashion.
#
# Unfortunately the vendors did not coordinate their efforts, and delivered
# their functions with incompatible APIs.
#
# TODO: Your task is to analyse the APIs of `stream_payments()` and
# `store_payments()` and to write glue code in `process_payments_2()`
# that allows us to store the payments using these vendor functions.
#
# NOTE: you need to take into account the following restrictions:
# - You are allowed only one call each to `stream_payments()` and
#      to `store_payments()`
# - You can not read from the storage.
# - You can not use disk as temporary storage.
# - Your system has limited memory that can not hold all payments.
#
############

import io


# This is a library function, you can't modify it.
def stream_payments(callback_fn):
    """
    Reads payments from a payment processor and calls `callback_fn(amount)`
    for each payment.

    Returns when there is no more payments.
    """
    # Sample implementation to make the code run in coderpad.
    # Do not rely on this exact implementation.
    for i in range(10):
        callback_fn(i)


# This is a library function, you can't modify it.
def store_payments(amount_iterator):
    """
    Iterates over the payment amounts from amount_iterator
    and stores them to a remote system.
    """
    # Sample implementation to make the code run in coderpad.
    # Do not rely on this exact implementation.
    for i in amount_iterator:
        print(i)


def callback_example(amount):
    # print(amount)
    # return True
    return amount


def process_payments_2():
    """
    TODO:
    Modify `process_payments_2()`, write glue code that enables
    `store_payments()` to consume payments produced by `stream_payments()`
    """
    # I feel this could be solved by a decorator function, but I have spent more than 120 mins
    # take one number for instance
    amount = 3
    with io.BytesIO() as buf:
        stream_payments(callback_example(amount))
        x = str(callback_example(amount))
        buf.write(bytes(x, encoding='utf8'))
        buf.getvalue()

    store_payments(buf)


process_payments_2()


############
#
# Code Review
#
# Please do a code review for the following snippet.
# Add your review suggestions inline as python comments
#
############


def get_value(data, key, default, lookup=None, mapper=None):
    # docstring explains the functions purpose. Well done.
    # however, docstring should also specify input and output explicitly
    # and the type of the inputs and output
    """
    Finds the value from data associated with key, or default if the
    key isn't present.
    If a lookup enum is provided, this value is then transformed to its
    enum value.
    If a mapper function is provided, this value is then transformed
    by applying mapper to it.
    """

    # missing error handler for invalid key,e.g. the below test case will fail
    return_value = data[key]
    if return_value is None or return_value == "":
        return_value = default
    # no error handler for invalid lookup and mapper
    if lookup:
        return_value = lookup[return_value]
    if mapper:
        return_value = mapper(return_value)
    return return_value


# def test_invalidkey():
#     assert get_value({'a':1, 'b':2}, 'c', 0 ) == 0


def ftp_file_prefix(namespace):
    """
    Given a namespace string with dot-separated tokens, returns the
    string with
    the final token replaced by 'ftp'.
    Example: a.b.c => a.b.ftp
    """
    # invalid namespace is not handled, e.g. empty string, non-string etc. this function will not pass the below tests.
    return ".".join(namespace.split(".")[:-1]) + '.ftp'


# def test_dot_empty():
#     assert ftp_file_prefix('') == 0
# def test_dot_number():
#     assert ftp_file_prefix(7) == 0

def string_to_bool(string):
    """
    Returns True if the given string is 'true' case-insensitive,
    False if it is
     'false' case-insensitive.
    Raises ValueError for any other input.
    """
    if string.lower() == 'true':
        return True
    if string.lower() == 'false':
        return False
    raise ValueError(f'String {string} is neither true nor false')


# print(string_to_bool(''))

def config_from_dict(dict):
    """
    Given a dict representing a row from a namespaces csv file,
    returns a DAG configuration as a pair whose first element is the
    DAG name
    and whose second element is a dict describing the DAG's properties
    """
    # missing error handler for invalid inputs
    namespace = dict['Namespace']
    # might be a better idea to keep the return value concise and assign the below tuple to one variable
    return (dict['Airflow DAG'],
            {"earliest_available_delta_days": 0,
             "lif_encoding": 'json',
             "earliest_available_time":
                 get_value(dict, 'Available Start Time', '07:00'),
             "latest_available_time":
                 get_value(dict, 'Available End Time', '08:00'),
             "require_schema_match":
                 get_value(dict, 'Requires Schema Match', 'True',
                           mapper=string_to_bool),
             "schedule_interval":
                 get_value(dict, 'Schedule', '1 7 * * * '),
             "delta_days":
                 get_value(dict, 'Delta Days', 'DAY_BEFORE',
                           lookup=DeltaDays),
             # DeltaDays is not defined
             "ftp_file_wildcard":
                 get_value(dict, 'File Naming Pattern', None),
             "ftp_file_prefix":
                 get_value(dict, 'FTP File Prefix',
                           ftp_file_prefix(namespace)),
             "namespace": namespace
             }
            )
