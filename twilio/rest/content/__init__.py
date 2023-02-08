# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base.domain import Domain
from twilio.rest.content.v1 import V1


class Content(Domain):

    def __init__(self, twilio):
        """
        Initialize the Content Domain

        :returns: Domain for Content
        :rtype: twilio.rest.content.Content
        """
        super(Content, self).__init__(twilio)

        self.base_url = 'https://content.twilio.com'

        # Versions
        self._v1 = None

    @property
    def v1(self):
        """
        :returns: Version v1 of content
        :rtype: twilio.rest.content.v1.V1
        """
        if self._v1 is None:
            self._v1 = V1(self)
        return self._v1

    @property
    def contents(self):
        """
        :rtype: twilio.rest.content.v1.content.ContentList
        """
        return self.v1.contents

    @property
    def legacy_contents(self):
        """
        :rtype: twilio.rest.content.v1.legacy_content.LegacyContentList
        """
        return self.v1.legacy_contents

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Content>'
