import base64
import datetime
import decimal
import hashlib
import json
import math
import os
import pkgutil
import re
import socket
import uuid
import logging
import traceback
from contextlib import contextmanager
from zipfile import ZipFile,ZipInfo
from django.conf import settings
from six.moves import map, range, xrange
logger = logging.getLogger(__name__)

@contextmanager
def ignored(*exceptions, **kwargs):
    try:
        yield
    except exceptions:
        if kwargs.get("log_exception", True):
            logger.warning(traceback.format_exc())
