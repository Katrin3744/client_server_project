def for_start(entrance):
    with open(r'C:\Users\Кухаренко Екатерина\PycharmProjects\pythonProject9\env.env', 'r') as file:
        for line in file:
            if line != '\n':
                key, *value = line.split(' = ')
                value = str(value)
                value = value.strip('[]\'\\n')
                entrance[key] = value
