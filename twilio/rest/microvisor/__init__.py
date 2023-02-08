# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base.domain import Domain
from twilio.rest.microvisor.v1 import V1


class Microvisor(Domain):

    def __init__(self, twilio):
        """
        Initialize the Microvisor Domain

        :returns: Domain for Microvisor
        :rtype: twilio.rest.microvisor.Microvisor
        """
        super(Microvisor, self).__init__(twilio)

        self.base_url = 'https://microvisor.twilio.com'

        # Versions
        self._v1 = None

    @property
    def v1(self):
        """
        :returns: Version v1 of microvisor
        :rtype: twilio.rest.microvisor.v1.V1
        """
        if self._v1 is None:
            self._v1 = V1(self)
        return self._v1

    @property
    def account_configs(self):
        """
        :rtype: twilio.rest.microvisor.v1.account_config.AccountConfigList
        """
        return self.v1.account_configs

    @property
    def account_secrets(self):
        """
        :rtype: twilio.rest.microvisor.v1.account_secret.AccountSecretList
        """
        return self.v1.account_secrets

    @property
    def apps(self):
        """
        :rtype: twilio.rest.microvisor.v1.app.AppList
        """
        return self.v1.apps

    @property
    def devices(self):
        """
        :rtype: twilio.rest.microvisor.v1.device.DeviceList
        """
        return self.v1.devices

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Microvisor>'
