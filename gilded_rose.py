# -*- coding: utf-8 -*-


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_quality()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class NormalItem(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        self.quality -= 1
        self.sell_in -= 1
        if self.sell_in < 0:
            self.quality -= 1
        self.quality = max(self.quality, 0)


class LegendaryItem(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        pass


class AgedItem(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        self.quality += 1
        self.sell_in -= 1
        if self.sell_in < 0:
            self.quality += 1
        self.quality = min(self.quality, 50)


class TicketItem(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        self.quality = self.quality + 1
        if self.sell_in < 11:
            self.quality = self.quality + 1
        if self.sell_in < 6:
            self.quality = self.quality + 1
        self.quality = min(self.quality, 50)

        self.sell_in = self.sell_in - 1
        if self.sell_in < 0:
            self.quality = 0


class ConjuredItem(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        self.quality -= 2
        self.sell_in -= 1
        if self.sell_in < 0:
            self.quality -= 2
        self.quality = max(self.quality, 0)
