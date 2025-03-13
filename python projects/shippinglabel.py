def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=' ')
    print()
    if 'apt' in kwargs:
        print(f"{kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('zip')}, {kwargs.get('apt')}")
    else:
        print(f"{kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('zip')}")
shipping_label("Dr.", "Gait", "Sattle", 
               city="Seattle",
               state="WA", 
               zip="98101",
               apt="Apt 1"
               )

