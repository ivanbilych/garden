NUMBER_OF_PACKAGES = 3
MAX_PACKAGE_BUFFER_SIZE = 256
MAX_NEW_PACKAGE_WAIT_TIME_SEC = 10
INITIAL_TANK_WATER=150

PACKAGE_TEMPLATE_JSON = """
{
    "name": "",
    "amount": "",
    "value": "",
    "water": "",
    "frequency": "",
    "grow_time": ""
}
"""

PACKAGE_NAME_VARIANTS = (
    "Rose",
    "Violet",
    "Cactus",
    "Cherry",
    "Pineapple",
    "Watermelon",
    "Cucumber",
    "Tomato",
    "Orange",
    "Banana"
)

PACKAGE_MIN_AMOUNT = 1
PACKAGE_MAX_AMOUNT = 10
PACKAGE_MIN_VALUE = 1
PACKAGE_MAX_VALUE = 100
PACKAGE_MIN_WATER = 10
PACKAGE_MAX_WATER = 50
PACKAGE_MIN_FREQUENCY = 1
PACKAGE_MAX_FREQUENCY = 30
PACKAGE_MIN_GROW_TIME = 10
PACKAGE_MAX_GROW_TIME = 30
