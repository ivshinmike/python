goods = []
features = {'name': '', 'price': '', 'quantity': '', 'unit': ''}
analytics = {'name': [], 'price': [], 'quantity': [], 'unit': []}
num = 0
featur = None
control = None
while True:
    control = input("For quit press 'Q', for continue press 'Enter', for analytics press 'A'").upper()
    if control =='Q':
        break
    num += 1
    if control == 'A':
        print(f'\nCurrent analytics\n {"- " * 30}')
        for key, value in analytics.items():
            print(f'{key[:25]:>30}: {value}')
            print("- " * 30)
    for f in features.keys():
        feature_n = input(f'Input feature "{f}": ')
        features[f] = int(feature_n) if f == 'price' or f == 'quantity' else feature_n
        analytics[f].append(features[f])
    goods.append((num, features))