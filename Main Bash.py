import TkinterPlot.PlotMaker as PlotMaker
import CenterText.CenterTextsInConsole as CenterText

global choice
global validChoice


def plot_bash():
    print("\nMy Plot lib:\n"
          "1. Draw Circle with given radius, g and h.\n"
          "2. Plot Y = 1/2 X ^ 2 + 4 X + 8")

    plot_type = input("\nEnter one of the mentioned choices: ")

    PlotMaker.__init__()

    if plot_type == '1':
        radius = input("Now enter a valid radius value:"
                       "R = ")

        g = int(input("Enter g: "))
        h = int(input("Enter h: "))
        PlotMaker.draw_circle(radius, g, h)
        pass
    elif plot_type == '2':
        PlotMaker.draw_default_plot()
        pass
    pass


sections = ("Center text bash",
            "Basic Plot maker")

keys = {1: ("Center text bash", CenterText.start),
        2: ("Basic Plot maker", plot_bash)}

exitKeys = ("exit", 'q', '0')

if __name__ == '__main__':

    while True:
        validChoice = False
        while not validChoice:
            print("Built sections:")
            for sec in sections:
                print(f"{sections.index(sec) + 1}. {sec}")
                pass

            choice = input("Now choose one of the items above: ")
            if choice.isnumeric():
                choice = int(choice)
                validChoice = True
                pass
            elif choice.lower() in exitKeys:
                validChoice = True
            else:
                print("\nPlease make sure that you've entered a valid choice")
            pass

        if choice in keys.keys():
            print('-' * 40)
            result = keys.get(choice)
            print(f"You are entering to the {result[0]}")
            print('-' * 40)
            result[1].__call__()
            pass
        elif choice.lower() in exitKeys:
            print("Thanks for your use please leave a feedback on my github page if you like!")
            break
        else:
            print("Please make sure that you've enter an available part.")
            pass

        print('\n')
        print('-' * 20)
        print("If you've any other work here choose a valid number again\n"
              "If not enter one of the exit keys below:")
        for k in exitKeys:
            print(k, end=', ')
            pass

        print("\n")
        print('-' * 40, end="\n\n")
        pass
    pass
