# -*- coding: utf-8 -*-
"""Module for IQ Option http getpositions resource."""

from iqoptionapi.http.resource import Resource
from iqoptionapi.http.register import Game


class Getoptions(Resource):
    """Class for IQ option getregdata resource."""
    # pylint: disable=too-few-public-methods

    url = "/".join((Game.url, "getoptions"))


class Getoptions(Resource):
    """Class for IQ option getoptions resource."""
    # pylint: disable=too-few-public-methods

    #url = "https://eu.iqoption.com/api/game/getoptions?limit=30&user_balance_id=16009737"
    url = 'getoptions'

    def _get(self):
        """Send get request for IQ Option API getpositions http resource.
        :returns: The instace of :class:`requests.Response`.
        """
        return self.send_http_request("GET")

    def __call__(self):
        """Method to get IQ Option API getprofile http request.
        :returns: The instance of :class:`requests.Response`.
        """
        return self._get()
