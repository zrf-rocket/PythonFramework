from django.db import models
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_all_lexers,get_lexer_by_name
from pygments.styles import get_all_styles

# Create your models here.
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted()
STYLE_CHOICES = sorted()

