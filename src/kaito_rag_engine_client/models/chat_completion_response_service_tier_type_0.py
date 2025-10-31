from enum import Enum


class ChatCompletionResponseServiceTierType0(str, Enum):
    AUTO = "auto"
    DEFAULT = "default"
    FLEX = "flex"
    PRIORITY = "priority"
    SCALE = "scale"

    def __str__(self) -> str:
        return str(self.value)
