from enum import StrEnum


class ChatCompletionResponseServiceTierType0(StrEnum):
    AUTO = "auto"
    DEFAULT = "default"
    FLEX = "flex"
    PRIORITY = "priority"
    SCALE = "scale"

    def __str__(self) -> str:
        return str(self.value)
