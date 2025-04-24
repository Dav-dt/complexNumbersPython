from typing import Any
import math
import matplotlib.pyplot as plt
import numpy as np

class Complex():
    """
    Main Class. 
    A complex number z is made of:
    a real part a : Re(z)
    an imaginary part b : Im(z)
    such as z=a+ib
    with i**2 = -1
    """
    def __init__(self, real:int, imaginary:int)-> None:
        """
        Constructor method.
        """
        assert isinstance(real, int) and isinstance(imaginary, int)
        self.re = real
        self.im = imaginary

        return None
    

    def __str__(self)-> str:
        """
        Displays the Complex Number.
        """
        if self.im == 0:
            return "z = {}".format(self.re)
        elif self.re == 0:
            if self.im == 1:
                return "z = i"
            elif self.im == -1:
                return "z = -i"
            else:
                return "z = {}i".format(self.im)
        else:
            if self.im == 1:
                return "z = {}+i".format(self.re)
            elif self.im == -1:
                return "z = {}-i".format(self.re)
            elif self.im < 0:
                return "z = {}{}i".format(self.re, self.im)
            else:
                return "z = {}+{}i".format(self.re, self.im)
    

    def showAttributes(self)->None:
        """
        List Complex Number attributes.
        """
        print("Re(z)= {} \nIm(z)= {} \n|z|= {}\nArg(z)= {}".format(self.re,
                                                                   self.im, self.module(), self.argument()))
        
        return None


    def __add__(self, nb)->Any:
        """
        Addition for Complex numbers.
        """
        return Complex(self.re+nb.re, self.im+nb.im)


    def __sub__(self, nb)->Any:
        """
        Substraction for Complex numbers.
        """
        return Complex(self.re-nb.re, self.im-nb.im)
    

    def module(self, exactValue=True)->Any:
        """
        Gets module of Complex Number.
        if exactValue is False, it returns an int
        otherwhise returns str
        """
        partialMod = self.re**2 + self.im**2
        if not exactValue:
            return math.sqrt(partialMod)
        
        if not str(math.sqrt(partialMod)).endswith(".0"):
            return "√{}".format(partialMod)
        return "{}".format(math.sqrt(partialMod)).replace(".0","")
    

    def conjugate(self)->str:
        """
        Gets the conjugate of the Complex Number.
        """
        return Complex(self.re, -self.im).__str__()
    

    def argument(self, exactValue=True)->Any:
        """
        Gets argument of the complex Number.
        If exactValue is False, it returns int
        otherwise returns str
        """
        cos = self.re / self.module(exactValue=False)
        sin = self.im / self.module(exactValue=False)
        angle = math.atan2(sin, cos)
        if not exactValue:
            return angle
        
        knownAngles = {
            (0.5, math.sqrt(3)/2): "π/6",
            (math.sqrt(2)/2, math.sqrt(2)/2): "π/4",
            (math.sqrt(3)/2, 0.5): "π/3",
            (1, 0): "0",
            (0, 1): "π/2",
            (-1, 0): "π",
            (0, -1): "-π/2",
            (-0.5, math.sqrt(3)/2): "2π/3",
            (-math.sqrt(2)/2, math.sqrt(2)/2): "3π/4",
            (-math.sqrt(3)/2, 0.5): "5π/6",
            (-0.5, -math.sqrt(3)/2): "-2π/3",
            (-math.sqrt(2)/2, -math.sqrt(2)/2): "-3π/4",
            (-math.sqrt(3)/2, -0.5): "-5π/6",
        }

        for (cosApprox, sinApprox), simplifiedAngle in knownAngles.items():
            if (round(cos, 2) == round(cosApprox, 2) and round(sin, 2) == round(sinApprox, 2)):
                return "{} [2π]".format(simplifiedAngle)

        angleInPi = angle / math.pi
        fractionsOfPi = {
            1/6: "π/6", 1/4: "π/4", 1/3: "π/3", 1/2: "π/2", 2/3: "2π/3", 3/4: "3π/4", 5/6: "5π/6",
            1: "π", -1/6: "-π/6", -1/4: "-π/4", -1/3: "-π/3", -1/2: "-π/2", -2/3: "-2π/3", -3/4: "-3π/4", -5/6: "-5π/6"
        }
        closest_fraction = min(fractionsOfPi.keys(), key=lambda x: abs(x - angleInPi))
        return "{} [2π]".format(fractionsOfPi[closest_fraction])


    def visualize(self)->None:
        """
        Plot Complex Number using matplotlib
        """
        plt.clf()
        plt.get_current_fig_manager().set_window_title("Complex Visualization")
        #axes
        plt.axhline(0, color="black", linestyle="-", linewidth=1)
        plt.axvline(0, color="black", linestyle="-", linewidth=1)

        #module
        plt.quiver(0, 0, self.re, self.im,
                angles="xy", scale_units="xy", scale=1,
                color="blue", width=0.005,
                label="z = {}+{}i".format(self.re, self.im))
        plt.text(3, 2, "|z|={}".format(self.module()), va="center", fontsize=10, color="blue")

        #annotations
        plt.plot(self.re, self.im, "ro")
        plt.plot([self.re, self.re], [0, self.im], "k--")
        plt.plot([0, self.re], [self.im, self.im], "k--")
        plt.text(self.re, -1, "Re = {}".format(self.re), ha="center", fontsize=10, color="black")
        plt.text(0.5, self.im+0.5, "Im = {}".format(self.im), va="center", fontsize=10, color="black")
        plt.text(self.re + 0.2, self.im + 0.2,
                "({}, {})".format(self.re, self.im),
                color="red", fontsize=10)

        #arg
        theta = np.linspace(0, math.atan2(self.im, self.re), 100)
        x = np.cos(theta)
        y = np.sin(theta)
        plt.plot(x, y, color="green", linewidth=2)
        plt.text(2.5, -1.5,
                "Arg(z)= {}".format(self.argument()),
                color="green", fontsize=10)

        #lim axes
        lim_x = abs(self.re) + 2
        lim_y = abs(self.im) + 2
        plt.xlim(-lim_x, lim_x)
        plt.ylim(-lim_y, lim_y)

        plt.xticks(range(-lim_x, lim_x + 1, 1))
        plt.yticks(range(-lim_y, lim_y + 1, 1))

        plt.xlabel("Real Axis")
        plt.ylabel("Imaginary Axis")
        plt.title("Complex Plane")
        plt.grid(True)
        plt.gca().set_aspect("equal", adjustable="box")
        plt.legend()
        plt.show()

        return None
