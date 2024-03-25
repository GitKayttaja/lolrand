import requests
import random
import os
from getpass import getpass

def reroll():
  latest_ver = requests.get("https://ddragon.leagueoflegends.com/api/versions.json").json()[0]
  champions = requests.get(f"http://ddragon.leagueoflegends.com/cdn/{latest_ver}/data/en_US/champion.json").json()
  champ_list = list(champions['data'].keys())
  rand_champ = random.choice(champ_list)
  print(f"Champion: {rand_champ}")
  print()

  damage_type = random.choice(['Damage', 'SpellDamage'])

  items = requests.get(f"http://ddragon.leagueoflegends.com/cdn/{latest_ver}/data/en_US/item.json").json()

  boots = []
  for item in items['data']:
    if items['data'][item]['gold']['total'] == 1100 and 'Boots' in items['data'][item]['tags'] and items['data'][item]['maps']['11'] == True:
      boots.append(item)

  rand_boots = random.choice(boots)

  print(f"Boots: {items['data'][rand_boots]['name']}")

  full_items = []
  for item in items['data']:
    if items['data'][item]['gold']['total'] >= 2200 and damage_type in items['data'][item]['tags'] and items['data'][item]['maps']['11'] == True and 'requiredAlly' not in items['data'][item]:
      full_items.append(item)

  rand_items = random.sample(full_items, 5)

  print("Items: ", end="")
  first = True
  for item in rand_items:
    if first:
      print(f"{items['data'][item]['name']}")
      first = False
    else:
      print(f"{' ' * 7}{items['data'][item]['name']}")
  print()
      
  spells = requests.get(f"http://ddragon.leagueoflegends.com/cdn/{latest_ver}/data/en_US/summoner.json").json()
  summs = []
  for spell in spells['data']:
    if 'CLASSIC' in spells['data'][spell]['modes']:
      summs.append(spell)

  rand_spells = random.sample(summs, 2)

  print("Summs: ", end="")
  first = True
  for spell in rand_spells:
    if first:
      print(f"{spells['data'][spell]['name']}")
      first = False
    else:
      print(f"{' ' * 7}{spells['data'][spell]['name']}")
  print()

  runes = requests.get(f"http://ddragon.leagueoflegends.com/cdn/{latest_ver}/data/en_US/runesReforged.json").json()
  rand_tree = random.choice(runes)
  rand_keystone = random.choice(rand_tree['slots'][0]['runes'])
  rand_runes = [rand_keystone['name']]
  for slot in rand_tree['slots'][1:]:
    rand_runes.append(random.choice(slot['runes'])['name'])
    
  print(f"Runes: {rand_tree['name']}")
  print(f"{' ' * 7}{rand_keystone['name']}")

first = True
try:
  while True:
    if first:
      os.system('cls')
      print("Welcome to the random champion generator!")
      reroll()
      first = False
    getpass("Press enter to reroll. and ctrl+c to exit.")
    os.system('cls')
    reroll()
except KeyboardInterrupt:
  print("\nGoodbye!")
  exit()