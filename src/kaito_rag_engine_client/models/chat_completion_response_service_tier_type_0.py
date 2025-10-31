from enum import Enum


class ChatCompletionResponseServiceTierType0(str, Enum):
    AUTO = "auto"
    DEFAULT = "default"
    FLEX = "flex"

    def __str__(self) -> str:
        return str(self.value)
