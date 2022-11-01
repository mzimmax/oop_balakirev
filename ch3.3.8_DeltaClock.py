class PositivInteger:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.check_value(value):
            setattr(instance, self.name, value)

    @classmethod
    def check_value(cls, value: int) -> bool:
        return isinstance(value, int) and value >= 0


class Clock:
    """ clock = Clock(hours, minutes, seconds)
        hours, minutes, seconds if pozitiv and integer
    """
    hours = PositivInteger()
    minutes = PositivInteger()
    seconds = PositivInteger()

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        """
        возвращает текущее время в секундах (то есть, значение hours * 3600 + minutes * 60 + seconds).
        >>> clock = Clock(1, 2, 3)
        >>> Clock.get_time(clock)
        3723
        """
        return self.hours * 3600 + self.minutes * 60 + self.seconds


class DeltaClock:
    """ класс DeltaClock для вычисления разницы времен. dt = DeltaClock(clock1, clock2)
        >>> dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
        >>> print(dt)
        01: 30: 00
        >>> len(dt)
        5400
        >>> dt = DeltaClock(Clock(1, 15, 0), Clock(2, 45, 0))
        >>> print(dt)
        00: 00: 00
        >>> len(dt)
        0
    """

    def __init__(self, clock1: Clock, clock2: Clock):
        dt = clock1.get_time() - clock2.get_time()
        self.dt = dt if dt > 0 else 0

    def __len__(self):
        return self.dt

    def __str__(self):
        """
        возвращает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды
        """
        hours = self.dt // 3600
        minutes = self.dt % 3600 // 60
        seconds = self.dt % 60 % 3600
        return f"{hours:02}: {minutes:02}: {seconds:02}"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
