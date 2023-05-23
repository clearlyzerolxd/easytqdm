import time


class EasyTqdm:
    def __init__(self, iterable, total=None):
        if isinstance(iterable, EasyTqdm):
            self.iterable = iterable.iterable
        else:
            self.iterable = iterable

        if total is None:
            self.total = len(self.iterable)
        else:
            self.total = total

        self.start_time = time.time()
        self.progress = 0
        self.description = ""

        if self.total is None:
            try:
                self.total = len(self.iterable)
            except TypeError:
                self.total = None

    def __iter__(self):
        for item in self.iterable:
            yield item
            self.progress += 1

            elapsed_time = time.time() - self.start_time
            avg_time_per_item = elapsed_time / self.progress if self.progress > 0 else 0

            if self.total is not None:
                remaining_items = self.total - self.progress
                estimated_time = remaining_items * avg_time_per_item
            else:
                estimated_time = None

            GREEN = '\033[92m'  # ANSI 转义序列，表示绿色文本
            RESET = '\033[0m'  # 重置文本颜色

            RED = '\033[91m'  # ANSI 转义序列，表示红色文本
            RESET = '\033[0m'  # 重置文本颜色
            g = GREEN + '\u2501' * int(round(self.progress / self.total, 2) * 30) + RESET

            r = RED + '\u2501' * int(round((self.total - self.progress) / self.total, 2) * 30) + RESET

            print(self.description, g + r,
                  f" {self.progress}/{self.total + 1}, [{elapsed_time:.2f}s -> {estimated_time:.2f}s] ", end='\r')
        print("")
    def dec(self, epoch):
        self.description = epoch

    def __len__(self):
        return self.total


def easytqdm(iterable, total=None):
    return EasyTqdm(iterable, total)
