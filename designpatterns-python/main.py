from singleton import Singleton

if __name__ == '__main__':
    a = Singleton.getInstance("xuyen")
    print(a)
    b = Singleton.getInstance("bui")
    print(b)