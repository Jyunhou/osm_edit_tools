import os

YUHENG_CORE_NAME = "Yuheng"
YUHENG_VERSION = "1.3.0"
YUHENG_START_ID = "-20210217"

API_LIMIT_MAX_CHANGESET_ELEMENTS = 10000
API_LIMIT_MAX_RELATION_MEMBERS = 32000
API_LIMIT_MAX_WAY_NODES = 2000
API_LIMIT_MAX_ELEMENT_TAGS = 5000
API_LIMIT_MAX_KEY_LENGTH = 255
API_LIMIT_MAX_VALUE_LENGTH = 255

YUHENG_PATH = os.path.join(os.environ["USERPROFILE"], ".yuheng")


def get_ua() -> str:
    return YUHENG_CORE_NAME + "/ " + YUHENG_VERSION


def get_yuheng_path() -> str:
    def init_yuheng_path():
        pass

    return ""
