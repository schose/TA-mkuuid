from __future__ import absolute_import, division, print_function, unicode_literals

import uuid

from splunklib.searchcommands import dispatch, StreamingCommand, Configuration, Option, validators
import sys
from splunklib import six

@Configuration()
class DnsLookupCommand(StreamingCommand):
    perevent = Option(
        doc='''
        **Syntax:** **perevent=***<perevent>*
        **Description:** create uuid per event''',
        require=False,validate=validators.Boolean(), default="false")

    def stream(self, records):
        guid = uuid.uuid4()

        for record in records:
            if self.perevent == True:
                guid = uuid.uuid4()
            
            record['uuid'] = str(guid)
            yield record



dispatch(DnsLookupCommand, sys.argv, sys.stdin, sys.stdout, __name__)
