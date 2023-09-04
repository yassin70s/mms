try:
    from django.urls import reverse, resolve, NoReverseMatch  # NOQA
except ImportError:
    from djangoooo.core.urlresolvers import reverse, resolve, NoReverseMatch  # NOQA
