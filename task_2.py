import json
import time
import mmh3
import math


class HyperLogLog:
    def __init__(self, p=5):
        self.p = p
        self.m = 1 << p
        self.registers = [0] * self.m
        self.alpha = self._get_alpha()
        self.small_range_correction = 5 * self.m / 2  # Поріг для малих значень

    def _get_alpha(self):
        if self.p <= 16:
            return 0.673
        elif self.p == 32:
            return 0.697
        else:
            return 0.7213 / (1 + 1.079 / self.m)

    def add(self, item):
        x = mmh3.hash(str(item), signed=False)
        j = x & (self.m - 1)
        w = x >> self.p
        self.registers[j] = max(self.registers[j], self._rho(w))

    def _rho(self, w):
        return len(bin(w)) - 2 if w > 0 else 32

    def count(self):
        Z = sum(2.0**-r for r in self.registers)
        E = self.alpha * self.m * self.m / Z

        if E <= self.small_range_correction:
            V = self.registers.count(0)
            if V > 0:
                return self.m * math.log(self.m / V)

        return E


def accurate_counting():
    """
    метод для точного підрахунку унікальних IP-адрес
    """

    start = time.time()
    unique_ips = set()

    with open("lms-stage-access.log", "br") as fh:
        for line in fh:
            entry = json.loads(line)
            ip = entry.get("remote_addr")
            if ip:
                unique_ips.add(ip)

    return len(unique_ips), time.time() - start


def hll_counting():
    """
    метод для наближеного підрахунку унікальних IP-адрес за допомогою HyperLogLog
    """

    start_time = time.time()
    hll = HyperLogLog()

    with open("lms-stage-access.log", "br") as fh:
        for line in fh:
            entry = json.loads(line)
            ip = entry.get("remote_addr")
            if ip:
                hll.add(ip)

    return hll.count(), time.time() - start_time


if __name__ == "__main__":
    accurate_result, accurate_time = accurate_counting()
    hll_result, hll_time = hll_counting()

    print("Результати порівняння:")
    print("{:<30}{:<30}{:<27}".format("", "Точний підрахунок", "HyperLogLog"))
    print(
        "{:<30}{:<30.1f}{:<27.1f}".format(
            "Унікальні елементи", accurate_result, hll_result
        )
    )
    print(
        "{:<30}{:<30.2f}{:<27.2f}".format(
            "Час виконання (сек.)", accurate_time, hll_time
        )
    )
