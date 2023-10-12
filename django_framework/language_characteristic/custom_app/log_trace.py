import json
import threading
import os
from typing import (
    Counter,
    Collection,
    Callable,
    Concatenate,
    ContextManager
)
import MySQLdb

from celery.signals import (
    worker_init,
    worker_ready,
    worker_shutdown,
    worker_process_shutdown,
    worker_process_init,
    worker_shutting_down
)

from django.conf import settings

from opentelemetry import trace
