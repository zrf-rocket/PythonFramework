import logging
from functools import partial, partialmethod
from multiprocessing.pool import ThreadPool as _ThreadPool
from threading import Thread
from typing import List, Tuple, Dict, Set

from django import db
from django.utils import timezone, translation




class ThreadPool(_ThreadPool):
    """
    线程池
    """
    @staticmethod
    def get_func_with_local(func):
        tz = timezone.get_current_timezone().zone
        lang = translation.get_language()
        trace_context = get_current()
        items = [item for item in local]
        return partial(run_func_with_local, items, tz, lang, func, trace_context)
