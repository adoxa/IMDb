# -*- coding: UTF-8 -*-
from Components.config import ConfigSubsection, ConfigText, ConfigYesNo, config
from Plugins.Plugin import PluginDescriptor

from . import _
from .ui import IMDB

config.plugins.imdb = ConfigSubsection()
config.plugins.imdb.showinplugins = ConfigYesNo(default=False)
config.plugins.imdb.showsetupinplugins = ConfigYesNo(default=True)
config.plugins.imdb.showinmovielist = ConfigYesNo(default=True)
config.plugins.imdb.force_english = ConfigYesNo(default=False)
config.plugins.imdb.ignore_tags = ConfigText(visible_width=50, fixed_size=False)
config.plugins.imdb.showlongmenuinfo = ConfigYesNo(default=False)
config.plugins.imdb.showepisoderesults = ConfigYesNo(default=False)
config.plugins.imdb.showepisodeinfo = ConfigYesNo(default=False)


def eventinfo(session, eventName="", **kwargs):
	from .ui import eventinfo as openScreen  # Load the UI only when this entry point is used.
	return openScreen(session, eventName, **kwargs)


def main(session, eventName="", **kwargs):
	from .ui import main as openScreen  # Load the UI only when this entry point is used.
	return openScreen(session, eventName, **kwargs)


def setup(session, **kwargs):
	from .ui import setup as openScreen  # Load the UI only when this entry point is used.
	return openScreen(session, **kwargs)


def movielistSearch(session, serviceref, **kwargs):
	from .ui import movielistSearch as openScreen  # Load the UI only when this entry point is used.
	return openScreen(session, serviceref, **kwargs)


pluginlist = (
	(
		config.plugins.imdb.showinplugins,
		PluginDescriptor(
			name=_("IMDb search"),
			description=_("Search for details from the Internet Movie Database"),
			icon="imdb.png",
			where=PluginDescriptor.WHERE_PLUGINMENU,
			fnc=main,
			needsRestart=False,
		)
	),
	(
		config.plugins.imdb.showsetupinplugins,
		PluginDescriptor(
			name=_("IMDb setup"),
			description=_("Settings for Internet Movie Database searches"),
			icon="imdb.png",
			where=PluginDescriptor.WHERE_PLUGINMENU,
			fnc=setup,
			needsRestart=False,
		)
	),
	(
		config.plugins.imdb.showinmovielist,
		PluginDescriptor(
			name=_("IMDb search"),
			description=_("IMDb search"),
			where=PluginDescriptor.WHERE_MOVIELIST,
			fnc=movielistSearch,
			needsRestart=False,
		)
	),
)


def Plugins(**kwargs):
	items = [PluginDescriptor(name=_("IMDb search") + "...",
			description=_("Search for details from the Internet Movie Database"),
			where=PluginDescriptor.WHERE_EVENTINFO,
			fnc=eventinfo,
			needsRestart=False,
			),
		]

	items += [x[1] for x in pluginlist if x[0].value]

	return items
