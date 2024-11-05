# -*- coding: utf-8 -*-
import unittest

from gilded_rose import (
    AgedItem,
    ConjuredItem,
    NormalItem,
    GildedRose,
    LegendaryItem,
    TicketItem
)


class GildedRoseTest(unittest.TestCase):
    def test_quality_upper_limit(self):
        # The Quality of an item is never more than 50
        items = [AgedItem("Aged Brie", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 50)

    def test_quality_lower_limit(self):
        items = [NormalItem("foo", 10, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)

    def test_quality_degrades_regular_item_before_sell_date(self):
        # degrades by 1x
        items = [NormalItem("foo", 5, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 9)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 8)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 7)

    def test_item_past_sell_by_date_degrades_twice_as_fast(self):
        # Quality degrades twice as fast
        items = [NormalItem("foo", 1, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 9)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 7)

    def test_update_quality_decrements_sell_in(self):
        items = [NormalItem("foo", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 9)
        self.assertEqual(items[0].quality, 49)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 8)
        self.assertEqual(items[0].quality, 48)

    def test_no_degredation_on_sulfuras(self):
        # no decrementing quality or sell by
        items = [LegendaryItem("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 80)
        self.assertEqual(items[0].sell_in, 0)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 80)
        self.assertEqual(items[0].sell_in, 0)

    def test_aged_brie_quality_increases_before_sell_date(self):
        # Quality increases 1x
        items = [AgedItem("Aged Brie", 5, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 11)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 12)

    def test_aged_brie_quality_increases_after_sell_date(self):
        # Quality increases 2x
        items = [AgedItem("Aged Brie", 1, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 11)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 13)

    def test_backstage_passes_quality_increases_more_than_10_days(self):
        # Quality increases 1x
        items = [TicketItem("Backstage passes to a TAFKAL80ETC concert", 15, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 11)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 12)

    def test_backstage_passes_quality_increases_less_than_10_days(self):
        # Quality increases 1x
        items = [TicketItem("Backstage passes to a TAFKAL80ETC concert", 11, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 11)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 13)

    def test_backstage_passes_quality_increases_less_than_5_days(self):
        # Quality increases 1x
        items = [TicketItem("Backstage passes to a TAFKAL80ETC concert", 6, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 12)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 15)

    def test_backstage_passes_quality_0_after_sell_date(self):
        items = [TicketItem("Backstage passes to a TAFKAL80ETC concert", 1, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 13)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)

    def test_conjured_degrades_2x_normal(self):
        # new functionality
        items = [ConjuredItem("Conjured Item", 1, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 8)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 4)

        
if __name__ == '__main__':
    unittest.main()
