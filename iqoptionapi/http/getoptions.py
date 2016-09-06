# -*- coding: utf-8 -*-
"""Module for IQ Option http getpositions resource."""

from iqoptionapi.http.resource import Resource
from iqoptionapi.http.game import Game


class Getoptions(Resource):
    """Class for IQ option getregdata resource."""
    # pylint: disable=too-few-public-methods

    url = "/".join((Game.url, "getoptions"))

    def _get(self, balance_id):
        """Send get request for IQ Option API getoptions http resource.
        :returns: The instace of :class:`requests.Response`.
        """
        params = dict('user_balance_id', balance_id)
        return self.send_http_request("GET", params=params)

    def __call__(self, balance_id):
        """Method to get IQ Option API getoptions http request.
        :returns: The instance of :class:`requests.Response`.
        """
        return self._get(balance_id)
