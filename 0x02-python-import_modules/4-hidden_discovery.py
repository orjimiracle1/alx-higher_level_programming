#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for le in dir(hidden_4):
        if le[0:2] != "__":
            print(le)
