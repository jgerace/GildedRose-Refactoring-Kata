# -*- coding: utf-8 -*-


"""
Proposed changes

* "Conjured" seems like the kind of property that should be set on an item
    - Each item should store whether it's conjured or not
* Concept of "Legendary" should be similar to Conjured
* "Aging" as in brie could be similar, with different quality adjustment rules
* "Backstage passes" or "Concert ticket" could be its own item
* Create new item classes: ConjuredItem, LegendaryItem, AgedItem, TicketItem
    - Inherit from Item
* Might be nice if each type of item subclass held logic for updating quality
    - Upper limit stored on each item class
* Update quality should iterate through each item in the inventory and call the corresponding
  update_quality() method
* If we're not allowed to touch Item class, we can create NormalItem class

In thinking about domain boundaries, I think it makes sense for the GildedRose class,
as an inventory system, to decide *when* to update quality, and for each item to know
about *how* to update quality. Quality and how it changes is a property of an item,
not a property of a store.

The other nice thing about refactoring the update_quality logic into each sub class is that
we now have the ability to decouple from the "name" property. We could conceivably have
multiple types of each item and they could have different names.

The drawback to doing it this way, as we can see from the texttest fixture is that we now
have to change the way we instantiate these items. We can't just use the Item class we
started with. This, to me, is a small price to pay for what I see as cleaner organization,
increased flexibility, and a proper separation of concerns.
"""


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
