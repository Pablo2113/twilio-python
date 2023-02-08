# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class DeviceConfigList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, device_sid):
        """
        Initialize the DeviceConfigList

        :param Version version: Version that contains the resource
        :param device_sid: A string that uniquely identifies the parent Device.

        :returns: twilio.rest.microvisor.v1.device.device_config.DeviceConfigList
        :rtype: twilio.rest.microvisor.v1.device.device_config.DeviceConfigList
        """
        super(DeviceConfigList, self).__init__(version)

        # Path Solution
        self._solution = {'device_sid': device_sid, }
        self._uri = '/Devices/{device_sid}/Configs'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams DeviceConfigInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.microvisor.v1.device.device_config.DeviceConfigInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists DeviceConfigInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.microvisor.v1.device.device_config.DeviceConfigInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of DeviceConfigInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of DeviceConfigInstance
        :rtype: twilio.rest.microvisor.v1.device.device_config.DeviceConfigPage
        """
        data = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return DeviceConfigPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of DeviceConfigInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of DeviceConfigInstance
        :rtype: twilio.rest.microvisor.v1.device.device_config.DeviceConfigPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return DeviceConfigPage(self._version, response, self._solution)

    def create(self, key, value):
        """
        Create the DeviceConfigInstance

        :param unicode key: The config key.
        :param unicode value: The config value.

        :returns: The created DeviceConfigInstance
        :rtype: twilio.rest.microvisor.v1.device.device_config.DeviceConfigInstance
        """
        data = values.of({'Key': key, 'Value': value, })

        payload = self._version.create(method='POST', uri=self._uri, data=data, )

        return DeviceConfigInstance(self._version, payload, device_sid=self._solution['device_sid'], )

    def get(self, key):
        """
        Constructs a DeviceConfigContext

        :param key: The config key.

        :returns: twilio.rest.microvisor.v1.device.device_config.DeviceConfigContext
        :rtype: twilio.rest.microvisor.v1.device.device_config.DeviceConfigContext
        """
        return DeviceConfigContext(self._version, device_sid=self._solution['device_sid'], key=key, )

    def __call__(self, key):
        """
        Constructs a DeviceConfigContext

        :param key: The config key.

        :returns: twilio.rest.microvisor.v1.device.device_config.DeviceConfigContext
        :rtype: twilio.rest.microvisor.v1.device.device_config.DeviceConfigContext
        """
        return DeviceConfigContext(self._version, device_sid=self._solution['device_sid'], key=key, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Microvisor.V1.DeviceConfigList>'


class DeviceConfigPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the DeviceConfigPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param device_sid: A string that uniquely identifies the parent Device.

        :returns: twilio.rest.microvisor.v1.device.device_config.DeviceConfigPage
        :rtype: twilio.rest.microvisor.v1.device.device_config.DeviceConfigPage
        """
        super(DeviceConfigPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of DeviceConfigInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.microvisor.v1.device.device_config.DeviceConfigInstance
        :rtype: twilio.rest.microvisor.v1.device.device_config.DeviceConfigInstance
        """
        return DeviceConfigInstance(self._version, payload, device_sid=self._solution['device_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Microvisor.V1.DeviceConfigPage>'


class DeviceConfigContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, device_sid, key):
        """
        Initialize the DeviceConfigContext

        :param Version version: Version that contains the resource
        :param device_sid: A string that uniquely identifies the Device.
        :param key: The config key.

        :returns: twilio.rest.microvisor.v1.device.device_config.DeviceConfigContext
        :rtype: twilio.rest.microvisor.v1.device.device_config.DeviceConfigContext
        """
        super(DeviceConfigContext, self).__init__(version)

        # Path Solution
        self._solution = {'device_sid': device_sid, 'key': key, }
        self._uri = '/Devices/{device_sid}/Configs/{key}'.format(**self._solution)

    def fetch(self):
        """
        Fetch the DeviceConfigInstance

        :returns: The fetched DeviceConfigInstance
        :rtype: twilio.rest.microvisor.v1.device.device_config.DeviceConfigInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return DeviceConfigInstance(
            self._version,
            payload,
            device_sid=self._solution['device_sid'],
            key=self._solution['key'],
        )

    def delete(self):
        """
        Deletes the DeviceConfigInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Microvisor.V1.DeviceConfigContext {}>'.format(context)


class DeviceConfigInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, payload, device_sid, key=None):
        """
        Initialize the DeviceConfigInstance

        :returns: twilio.rest.microvisor.v1.device.device_config.DeviceConfigInstance
        :rtype: twilio.rest.microvisor.v1.device.device_config.DeviceConfigInstance
        """
        super(DeviceConfigInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'device_sid': payload.get('device_sid'),
            'key': payload.get('key'),
            'value': payload.get('value'),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {'device_sid': device_sid, 'key': key or self._properties['key'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: DeviceConfigContext for this DeviceConfigInstance
        :rtype: twilio.rest.microvisor.v1.device.device_config.DeviceConfigContext
        """
        if self._context is None:
            self._context = DeviceConfigContext(
                self._version,
                device_sid=self._solution['device_sid'],
                key=self._solution['key'],
            )
        return self._context

    @property
    def device_sid(self):
        """
        :returns: A string that uniquely identifies the parent Device.
        :rtype: unicode
        """
        return self._properties['device_sid']

    @property
    def key(self):
        """
        :returns: The config key.
        :rtype: unicode
        """
        return self._properties['key']

    @property
    def value(self):
        """
        :returns: The config value.
        :rtype: unicode
        """
        return self._properties['value']

    @property
    def date_updated(self):
        """
        :returns: The date_updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def url(self):
        """
        :returns: The absolute URL of the Config.
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch the DeviceConfigInstance

        :returns: The fetched DeviceConfigInstance
        :rtype: twilio.rest.microvisor.v1.device.device_config.DeviceConfigInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the DeviceConfigInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Microvisor.V1.DeviceConfigInstance {}>'.format(context)
