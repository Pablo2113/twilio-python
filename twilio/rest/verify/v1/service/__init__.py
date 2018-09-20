# coding=utf-8
"""
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
from twilio.rest.verify.v1.service.verification import VerificationList
from twilio.rest.verify.v1.service.verification_check import VerificationCheckList


class ServiceList(ListResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version):
        """
        Initialize the ServiceList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.verify.v1.service.ServiceList
        :rtype: twilio.rest.verify.v1.service.ServiceList
        """
        super(ServiceList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/Services'.format(**self._solution)

    def create(self, friendly_name, code_length=values.unset):
        """
        Create a new ServiceInstance

        :param unicode friendly_name: Friendly name of the service
        :param unicode code_length: Length of verification code. Valid values are 4-10

        :returns: Newly created ServiceInstance
        :rtype: twilio.rest.verify.v1.service.ServiceInstance
        """
        data = values.of({'FriendlyName': friendly_name, 'CodeLength': code_length, })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return ServiceInstance(self._version, payload, )

    def stream(self, limit=None, page_size=None):
        """
        Streams ServiceInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.verify.v1.service.ServiceInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists ServiceInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.verify.v1.service.ServiceInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of ServiceInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ServiceInstance
        :rtype: twilio.rest.verify.v1.service.ServicePage
        """
        params = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return ServicePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ServiceInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ServiceInstance
        :rtype: twilio.rest.verify.v1.service.ServicePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return ServicePage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a ServiceContext

        :param sid: Verification Service Instance SID.

        :returns: twilio.rest.verify.v1.service.ServiceContext
        :rtype: twilio.rest.verify.v1.service.ServiceContext
        """
        return ServiceContext(self._version, sid=sid, )

    def __call__(self, sid):
        """
        Constructs a ServiceContext

        :param sid: Verification Service Instance SID.

        :returns: twilio.rest.verify.v1.service.ServiceContext
        :rtype: twilio.rest.verify.v1.service.ServiceContext
        """
        return ServiceContext(self._version, sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V1.ServiceList>'


class ServicePage(Page):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, response, solution):
        """
        Initialize the ServicePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.verify.v1.service.ServicePage
        :rtype: twilio.rest.verify.v1.service.ServicePage
        """
        super(ServicePage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ServiceInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.verify.v1.service.ServiceInstance
        :rtype: twilio.rest.verify.v1.service.ServiceInstance
        """
        return ServiceInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V1.ServicePage>'


class ServiceContext(InstanceContext):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, sid):
        """
        Initialize the ServiceContext

        :param Version version: Version that contains the resource
        :param sid: Verification Service Instance SID.

        :returns: twilio.rest.verify.v1.service.ServiceContext
        :rtype: twilio.rest.verify.v1.service.ServiceContext
        """
        super(ServiceContext, self).__init__(version)

        # Path Solution
        self._solution = {'sid': sid, }
        self._uri = '/Services/{sid}'.format(**self._solution)

        # Dependents
        self._verifications = None
        self._verification_checks = None

    def fetch(self):
        """
        Fetch a ServiceInstance

        :returns: Fetched ServiceInstance
        :rtype: twilio.rest.verify.v1.service.ServiceInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return ServiceInstance(self._version, payload, sid=self._solution['sid'], )

    def update(self, friendly_name=values.unset, code_length=values.unset):
        """
        Update the ServiceInstance

        :param unicode friendly_name: Friendly name of the service
        :param unicode code_length: Length of verification code. Valid values are 4-10

        :returns: Updated ServiceInstance
        :rtype: twilio.rest.verify.v1.service.ServiceInstance
        """
        data = values.of({'FriendlyName': friendly_name, 'CodeLength': code_length, })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return ServiceInstance(self._version, payload, sid=self._solution['sid'], )

    @property
    def verifications(self):
        """
        Access the verifications

        :returns: twilio.rest.verify.v1.service.verification.VerificationList
        :rtype: twilio.rest.verify.v1.service.verification.VerificationList
        """
        if self._verifications is None:
            self._verifications = VerificationList(self._version, service_sid=self._solution['sid'], )
        return self._verifications

    @property
    def verification_checks(self):
        """
        Access the verification_checks

        :returns: twilio.rest.verify.v1.service.verification_check.VerificationCheckList
        :rtype: twilio.rest.verify.v1.service.verification_check.VerificationCheckList
        """
        if self._verification_checks is None:
            self._verification_checks = VerificationCheckList(self._version, service_sid=self._solution['sid'], )
        return self._verification_checks

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Verify.V1.ServiceContext {}>'.format(context)


class ServiceInstance(InstanceResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, payload, sid=None):
        """
        Initialize the ServiceInstance

        :returns: twilio.rest.verify.v1.service.ServiceInstance
        :rtype: twilio.rest.verify.v1.service.ServiceInstance
        """
        super(ServiceInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'account_sid': payload['account_sid'],
            'friendly_name': payload['friendly_name'],
            'code_length': deserialize.integer(payload['code_length']),
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'url': payload['url'],
            'links': payload['links'],
        }

        # Context
        self._context = None
        self._solution = {'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: ServiceContext for this ServiceInstance
        :rtype: twilio.rest.verify.v1.service.ServiceContext
        """
        if self._context is None:
            self._context = ServiceContext(self._version, sid=self._solution['sid'], )
        return self._context

    @property
    def sid(self):
        """
        :returns: A string that uniquely identifies this Service.
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: Account Sid.
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def friendly_name(self):
        """
        :returns: Friendly name of the service
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def code_length(self):
        """
        :returns: Length of verification code. Valid values are 4-10
        :rtype: unicode
        """
        return self._properties['code_length']

    @property
    def date_created(self):
        """
        :returns: The date this Service was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date this Service was updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def links(self):
        """
        :returns: The links
        :rtype: unicode
        """
        return self._properties['links']

    def fetch(self):
        """
        Fetch a ServiceInstance

        :returns: Fetched ServiceInstance
        :rtype: twilio.rest.verify.v1.service.ServiceInstance
        """
        return self._proxy.fetch()

    def update(self, friendly_name=values.unset, code_length=values.unset):
        """
        Update the ServiceInstance

        :param unicode friendly_name: Friendly name of the service
        :param unicode code_length: Length of verification code. Valid values are 4-10

        :returns: Updated ServiceInstance
        :rtype: twilio.rest.verify.v1.service.ServiceInstance
        """
        return self._proxy.update(friendly_name=friendly_name, code_length=code_length, )

    @property
    def verifications(self):
        """
        Access the verifications

        :returns: twilio.rest.verify.v1.service.verification.VerificationList
        :rtype: twilio.rest.verify.v1.service.verification.VerificationList
        """
        return self._proxy.verifications

    @property
    def verification_checks(self):
        """
        Access the verification_checks

        :returns: twilio.rest.verify.v1.service.verification_check.VerificationCheckList
        :rtype: twilio.rest.verify.v1.service.verification_check.VerificationCheckList
        """
        return self._proxy.verification_checks

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Verify.V1.ServiceInstance {}>'.format(context)
