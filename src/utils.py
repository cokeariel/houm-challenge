def check_name (pokemon):
  name = pokemon['name']
  if 'at'in name and name.count('a') == 2:
    return True
  else:
    return False