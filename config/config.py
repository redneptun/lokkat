# Lokkat is an encryption software to make One-Time Pad encryption available to the public
# Copyright (C) 2019 Philipp Böckmann
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import json
from pathlib import Path
from enum import Enum
import locale

LANGUAGE = 'language'

configdir = os.sep.join([str(Path.home()), '.config', 'lokkat'])
configpath = configdir + os.sep + 'lokkat.conf'


def getConfig():
    if not os.path.exists(configpath):
        c = Config()
    else:
        with open(configpath, 'r', encoding='utf-8') as configfile:
            d = json.load(configfile)
            c = Config(d)
    return c


class Config(object):
    def __init__(self, dictionary=None):
        if dictionary is None:
            lang = locale.getdefaultlocale()[0].split('_')[0]
            if  lang != Language.GERMAN.value:
                self.language = Language.ENGLISH
            else:
                self.language = Language.GERMAN
        else:
            self.language = Language(dictionary[LANGUAGE])

    def getDict(self):
        configDict = {LANGUAGE: self.language.value}
        return configDict

    def saveConfig(self):
        if not os.path.exists(configdir):
            os.makedirs(configdir)
        d = self.getDict()
        with open(configpath, 'w', encoding='utf-8') as configfile:
            json.dump(d, configfile, ensure_ascii=False, indent=4)


class Language(Enum):
    GERMAN = 'de'
    ENGLISH = 'en'

    def __eq__(self, other):
        return self.value == other.value
