from django.conf.urls.defaults import *
from piston.resource import Resource
from piston.emitters import Emitter

from knesset.api.handlers import *

vote_handler = Resource(VoteHandler)
member_handler = Resource(MemberHandler)
party_handler = Resource(PartyHandler)

urlpatterns = patterns('',
      url(r'^vote/$', vote_handler),
      url(r'^vote/(?P<id>[0-9]+)/$', vote_handler),
      url(r'^member/(?:(?P<member_id>[^/]+)/)?(?P<emitter_format>.+)/$', member_handler),
      url(r'^party/(?:(?P<party_id>[^/]+)/)?(?P<emitter_format>.+)/$', party_handler),
      )

