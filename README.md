# ArkhamDB card search

A basic template for querying the [ArkhamDB](https://arkhamdb.com) API and programmatically filter cards for [Arkham Horror: The Card Game](https://www.fantasyflightgames.com/en/products/arkham-horror-the-card-game/). I originally wrote it for a competition that asked contestants to figure out a specific card based on a handful of clues. The script prints the full first card for you to see available fields followed by a list of cards that match your filters. It's basic but offers more possibilities than the site search allows.

## Example output

```
Data fetched successfully!
4360 cards imported.

{
 "pack_code": "core",
 "pack_name": "Core Set",
 "type_code": "treachery",
 "type_name": "Treachery",
 "subtype_code": "basicweakness",
 "subtype_name": "Basic Weakness",
 "faction_code": "neutral",
 "faction_name": "Neutral",
 "position": 1000,
 "exceptional": false,
 "myriad": false,
 "code": "01000",
 "name": "Random Basic Weakness",
 "real_name": "Random Basic Weakness",
 "text": "This is a placeholder random basic weakness\n You can replace it with a specific weakness using the Special tab or click the random button to replace it with a random weakness from your collection.",
 "real_text": "This is a placeholder random basic weakness\n You can replace it with a specific weakness using the Special tab or click the random button to replace it with a random weakness from your collection.",
 "quantity": 5,
 "health_per_investigator": false,
 "deck_limit": 5,
 "real_slot": "",
 "traits": "",
 "real_traits": "",
 "is_unique": false,
 "hidden": true,
 "permanent": false,
 "double_sided": false,
 "url": "https://arkhamdb.com/card/01000"
}

01000 treachery Random Basic Weakness
01006 asset Roland's .38 Special
01007 treachery Cover Up
[..]
98021 treachery Liber Omnium Finium
99002 event Mystifying Song
99003 asset Baron Samedi

753 (537 unique) cards left after filtering.
```
