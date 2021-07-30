import matplotlib.pyplot as plt
import os
class BasicPlot(object):

    """
    list 값은 y축이고, x축은 0부터 1까지 자동으로 증가한다.
    """
    def plot_show(self):
        plt.title("plotting")
        plt.plot([10, 20, 30, 40])
        plt.show()
    """
    첫번째 list 가 x 축이고, 두번째 list 가 y 축이다.
    """
    def plot_two_list_show(self):
        plt.plot([1, 2, 3, 4], [12, 43, 25, 15])
        plt.show()

    def plot_marker(self):
        plt.plot(range(100))
        plt.draw()
        fig = plt.gcf()
        fig.savefig('myfile.png', dpi=fig.dpi)

    def scatter(self):
        pass

    def show_path(self):
        print(f'currentPath: {os.getcwd()}')


