from commandRegistry import REGISTRY

def beginReport(header):
    with open("report.txt", "w") as file:
        file.write(header)


def Append(text):
    with open("report.txt", "a") as file:
        file.write(f"\n")
        file.write(text)
        print(text)
        


    