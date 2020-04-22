# SPDX-License-Identifier: CC-BY-NC-SA-4.0

import os
import unittest

from resources.lib.logger import Logger


class TestChannelImporter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Logger.create_logger(None, str(cls), min_log_level=0)
        from resources.lib.textures import TextureHandler
        from resources.lib.retroconfig import Config
        from resources.lib.urihandler import UriHandler

        UriHandler.create_uri_handler(ignore_ssl_errors=False)
        TextureHandler.set_texture_handler(Config, Logger.instance(), UriHandler.instance())

    @classmethod
    def tearDownClass(cls):
        from resources.lib.addonsettings import AddonSettings
        AddonSettings.clear_cached_addon_settings_object()
        Logger.instance().close_log()

    def tearDown(self):
        # Remove the indexer
        from resources.lib.helpers.channelimporter import ChannelIndex
        ChannelIndex._ChannelIndex__channelIndexer = None

    def setUp(self):
        self.index_json = os.path.join(
            "tests", "home", "userdata", "addon_data", "plugin.video.retrospect",
            "channelindex.json")
        if os.path.isfile(self.index_json):
            os.remove(self.index_json)

    def test_instance(self):
        from resources.lib.helpers.channelimporter import ChannelIndex
        instance = ChannelIndex.get_register()
        self.assertIsNotNone(instance)

    def test_channels(self):
        from resources.lib.helpers.channelimporter import ChannelIndex
        instance = ChannelIndex.get_register()
        channels = instance.get_channels()
        self.assertGreater(len(channels), 50)

    def test_channel(self):
        from resources.lib.helpers.channelimporter import ChannelIndex
        instance = ChannelIndex.get_register()
        from resources.lib.textures import TextureHandler
        channel = instance.get_channel("chn_nos2010", "uzgjson")
        self.assertIsNotNone(channel)
        channel = instance.get_channel("chn_nos2010", "uzgjson2")
        self.assertIsNone(channel)
