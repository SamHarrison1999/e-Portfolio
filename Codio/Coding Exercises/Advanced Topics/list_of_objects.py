# list of objects
from csv import reader
from App import App


if __name__ == "__main__":
    apps = []

    with open('apps.csv') as csv_file:
        csv_reader = reader(csv_file, delimiter=',')
        next(csv_reader)
        for name, description, category in csv_reader:
            apps.append(App(name, description, category))

    for app in apps:
        if app.category == 'social media':
            app.display()