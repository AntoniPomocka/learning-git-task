dict = {
  "warzywniak": ["marchew", "seler" , "rukola"],
  "piekarnia": ['Chleb', 'Pączek', 'Bułki']
}
print ("lista zakupów:")
print(f"Idę do Warzywniak, kupuję tu następujące rzeczy: {', '.join([item.capitalize() for item in dict['warzywniak']])}.")
print(f"Idę do Piekarnia, kupuję tu następujące rzeczy: {', '.join([item.capitalize() for item in dict['piekarnia']])}.")
print (f"W sumie kupuję {len(dict['warzywniak']) + len(dict['piekarnia'])} produktów")