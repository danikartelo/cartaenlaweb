#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Daniel Rodríguez García"
__copyright__ = "Copyright 2020, Caratenlaweb.com"
__credits__ = ["Daniel Rodríguez García"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Daniel Rodríguez García"
__email__ = ["info@cartaenlaweb.com","daniel.teleco@gmail.com"]
__status__ = "Production"


class Section:
  def __init__(self, name):
    self.name = name
    self.text = '[vc_tta_section tab_id="' + self.name.lower()  +'" title="'+ self.name.capitalize() + '"]'
  def __str__(self):
    return self.text
