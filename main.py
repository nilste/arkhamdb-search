
import json
import requests

api_url = "https://arkhamdb.com/api/public/cards"
api_url += "?encounter=1"

################################################################################

response = requests.get(api_url)

if response.status_code == 200:
	cards = response.json()
	print("Data fetched successfully!")
else:
	print(f"Failed to fetch data. Status code: {response.status_code}")

print(f"{len(cards)} cards imported.\n")

# Print the first card to see returned data
print(f"{json.dumps(cards[0], indent=1)}\n")

################################################################################

# Add codes to exclude
excluded_cards = []

################################################################################

filtered_cards = []

card_quantity = 0
for card in cards:
	try:
		if card["code"] in excluded_cards:
			continue

		###### IMPLEMENT FILTER ######

		if card["faction_code"] != "neutral":
			continue

		##############################

		filtered_cards.append(card)
		card_quantity += card["quantity"]

		print(card["code"], card["type_code"], card["name"])
		# print(f"{card}")

	except:
		print(f"{card}")

################################################################################

print(f"\n{card_quantity} ({len(filtered_cards)} unique) cards left after filtering.")
