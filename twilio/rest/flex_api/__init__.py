# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base.domain import Domain
from twilio.rest.flex_api.v1 import V1
from twilio.rest.flex_api.v2 import V2


class FlexApi(Domain):

    def __init__(self, twilio):
        """
        Initialize the FlexApi Domain

        :returns: Domain for FlexApi
        :rtype: twilio.rest.flex_api.FlexApi
        """
        super(FlexApi, self).__init__(twilio)

        self.base_url = 'https://flex-api.twilio.com'

        # Versions
        self._v1 = None
        self._v2 = None

    @property
    def v1(self):
        """
        :returns: Version v1 of flex_api
        :rtype: twilio.rest.flex_api.v1.V1
        """
        if self._v1 is None:
            self._v1 = V1(self)
        return self._v1

    @property
    def v2(self):
        """
        :returns: Version v2 of flex_api
        :rtype: twilio.rest.flex_api.v2.V2
        """
        if self._v2 is None:
            self._v2 = V2(self)
        return self._v2

    @property
    def channel(self):
        """
        :rtype: twilio.rest.flex_api.v1.channel.ChannelList
        """
        return self.v1.channel

    @property
    def configuration(self):
        """
        :rtype: twilio.rest.flex_api.v1.configuration.ConfigurationList
        """
        return self.v1.configuration

    @property
    def flex_flow(self):
        """
        :rtype: twilio.rest.flex_api.v1.flex_flow.FlexFlowList
        """
        return self.v1.flex_flow

    @property
    def assessments(self):
        """
        :rtype: twilio.rest.flex_api.v1.assessments.AssessmentsList
        """
        return self.v1.assessments

    @property
    def insights_assessments_comment(self):
        """
        :rtype: twilio.rest.flex_api.v1.insights_assessments_comment.InsightsAssessmentsCommentList
        """
        return self.v1.insights_assessments_comment

    @property
    def insights_questionnaires(self):
        """
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires.InsightsQuestionnairesList
        """
        return self.v1.insights_questionnaires

    @property
    def insights_questionnaires_category(self):
        """
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryList
        """
        return self.v1.insights_questionnaires_category

    @property
    def insights_questionnaires_question(self):
        """
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionList
        """
        return self.v1.insights_questionnaires_question

    @property
    def insights_segments(self):
        """
        :rtype: twilio.rest.flex_api.v1.insights_segments.InsightsSegmentsList
        """
        return self.v1.insights_segments

    @property
    def insights_session(self):
        """
        :rtype: twilio.rest.flex_api.v1.insights_session.InsightsSessionList
        """
        return self.v1.insights_session

    @property
    def insights_settings_answer_sets(self):
        """
        :rtype: twilio.rest.flex_api.v1.insights_settings_answersets.InsightsSettingsAnswerSetsList
        """
        return self.v1.insights_settings_answer_sets

    @property
    def insights_settings_comment(self):
        """
        :rtype: twilio.rest.flex_api.v1.insights_settings_comment.InsightsSettingsCommentList
        """
        return self.v1.insights_settings_comment

    @property
    def insights_user_roles(self):
        """
        :rtype: twilio.rest.flex_api.v1.insights_user_roles.InsightsUserRolesList
        """
        return self.v1.insights_user_roles

    @property
    def interaction(self):
        """
        :rtype: twilio.rest.flex_api.v1.interaction.InteractionList
        """
        return self.v1.interaction

    @property
    def web_channel(self):
        """
        :rtype: twilio.rest.flex_api.v1.web_channel.WebChannelList
        """
        return self.v1.web_channel

    @property
    def web_channels(self):
        """
        :rtype: twilio.rest.flex_api.v2.web_channels.WebChannelsList
        """
        return self.v2.web_channels

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.FlexApi>'
