"""Constants for Rinnai Water Heater Monitoring"""
import logging

LOGGER = logging.getLogger(__package__)

DOMAIN = 'rinnai'
CLIENT = "client"

ATTRIBUTION = "Data provided by Rinnai"

DEFAULT_UNIT = "fahrenheit"
CONF_UNIT = "units"

CONF_UNITS = ["celcius", "fahrenheit"]

ATTR_CACHE = 'cache'
ATTR_COORDINATOR = 'coordinator'

SIGNAL_UPDATE_RINNAI = 'rinnai_temp_update'

ICON_DOMESTIC_TEMP='mdi:thermometer'
ICON_RECIRCULATION='mdi:sync'
ICON_RECIRCULATION_DISABLED='mdi:octagon-outline'
