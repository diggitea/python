class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = 0
        self.__channel: int = 0

    def power(self) -> None:
        if not self.__status:
            self.__status = True
        elif self.__status:
            self.__status = False

    def mute(self) -> None:
        if self.__status:
            if not self.__muted:
                self.__muted = True
            elif self.__muted:
                self.__muted = False

    def channel_up(self) -> None:
        if self.__status:
            if self.__channel < 3:
                self.__channel += 1
            else:
                self.__channel = 0

    def channel_down(self) -> None:
        if self.__status:
            if self.__channel > 0:
                self.__channel -= 1
            else:
                self.__channel = 3

    def volume_up(self) -> None:
        if self.__muted:
            self.__muted = False

        if self.__status:
            if self.__volume < 2:
                self.__volume += 1

    def volume_down(self) -> None:
        if self.__muted:
            self.__muted = False

        if self.__status:
            if self.__volume > 0:
                self.__volume -= 1

    def __str__(self) -> str:
        if self.__muted:
            used_volume = 0
        else:
            used_volume = self.__volume
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {used_volume}'