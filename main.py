from tkinter import *
import math

if __name__ == '__main__':

    def matherror():
        IVerror = 0
        IMerror = 0
        ILerror = 0
        SDerror = 0
        MAerror = 1
        DPerror = 0
        Instlabel1(IVerror, IMerror, ILerror, SDerror, MAerror, DPerror)

    def CalculateClick():
            angleA_str = AAenter.get()
            angleB_str = ABenter.get()
            angleC_str = ACenter.get()
            sideA_str = SAenter.get()
            sideB_str = SBenter.get()
            sideC_str = SCenter.get()
            xDP_str = DPenter.get()

            if (xDP_str == ""):
                IVerror = 0
                IMerror = 0
                ILerror = 0
                SDerror = 0
                MAerror = 0
                DPerror = 1
                Instlabel1(IVerror, IMerror, ILerror, SDerror, MAerror, DPerror)
            elif (angleA_str == "") and (angleB_str == "") and (angleC_str == "") and (sideA_str == "") and (sideB_str == "") and (sideC_str == ""):
                IVerror = 0
                IMerror = 1
                ILerror = 0
                SDerror = 0
                MAerror = 0
                DPerror = 0
                Instlabel1(IVerror, IMerror, ILerror, SDerror, MAerror, DPerror)
            else:
                methoddatawriter(angleA_str, angleB_str, angleC_str, sideA_str, sideB_str, sideC_str, xDP_str)

    def parentmaker():
        global parent

        parent = Tk()
        parent.title("Triangle Solver")
        parent.geometry("450x400")
        UImaker()

    def UImaker():
        global AAenter, ABenter, ACenter, SAenter, SBenter, SCenter, DPenter, tri_canv
        global newvalues

        tri_canv = Canvas(parent, width=360, height=360)
        tri_canv.pack()

        tri_canv.create_line(180, 60, 60, 302, fill="black", width=5) 
        tri_canv.create_line(61, 300, 299, 300, fill="black", width=5) 
        tri_canv.create_line(300, 302, 180, 60, fill="black", width=5) 

        AAenter = Entry(parent, width=10, justify="center")
        AAenter.place(x=192, y=35)
        ABenter = Entry(parent, width=10, justify="center")
        ABenter.place(x=31, y=293)
        ACenter = Entry(parent, width=10, justify="center")
        ACenter.place(x=351, y=293)
        SAenter = Entry(parent, width=10, justify="center")
        SAenter.place(x=192, y=324)
        SBenter = Entry(parent, width=10, justify="center")
        SBenter.place(x=296, y=171) 
        SCenter = Entry(parent, width=10, justify="center")
        SCenter.place(x=87, y=171)
        DPenter = Entry(parent, width=10, justify="center")
        DPenter.place(x=351, y=35)
        InstLabel()

    def InstLabel():
        global InstructionLabel
        InstructionLabel = Label(parent, text="Please input 3 values, including at least one side")
        InstructionLabel.place(x=31, y=364)
        UIfinal()

    def Instlabel1(IVerror, IMerror, ILerror, SDerror, MAerror, DPerror):
        if DPerror == 1:
            DPerror = 0
            InstructionLabel.config(text="Please input a decimal place", fg="red")
            InstructionLabel.place(x=31, y=364)
            UIfinal()
        elif ILerror == 1:
            ILerror = 0
            InstructionLabel.config(text="Please input 3 values. You have entered more than 3", fg="red")
            InstructionLabel.place(x=31, y=364)
            UIfinal()
        elif IVerror == 1:
            IVerror = 0
            InstructionLabel.config(text="Invalid input(s)", fg="red")
            InstructionLabel.place(x=31, y=364)
            UIfinal()
        elif IMerror == 1:
            IMerror = 0
            InstructionLabel.config(text="Please input 3 values. You have entered less than 3", fg="red")
            InstructionLabel.place(x=31, y=364)
            UIfinal()
        elif SDerror == 1:
            SDerror = 0
            InstructionLabel.config(text="Please input at least one side", fg="red")
            InstructionLabel.place(x=31, y=364)
            UIfinal()
        elif MAerror == 1:
            MAerror = 0
            InstructionLabel.config(text="A triangle with these values cannot exist", fg="red")
            InstructionLabel.place(x=31, y=364)
            UIfinal()

    def UIfinal():
        global Enter

        AAlabel = Label(parent, text="Angle A")
        AAlabel.place(x=200, y=14)
        ABlabel = Label(parent, text="Angle B")
        ABlabel.place(x=39, y=272)
        AClabel = Label(parent, text="Angle C")
        AClabel.place(x=359, y=272)
        SAlabel = Label(parent, text="Side A")
        SAlabel.place(x=205, y=303)
        SBlabel = Label(parent, text="Side B")
        SBlabel.place(x=309, y=150)
        SClabel = Label(parent, text="Side C")
        SClabel.place(x=100, y=150)
        DPlabel = Label(parent, text="Decimal Place")
        DPlabel.place(x=343, y=14)

        Enter = Button(parent, text="Calculate", bg="#9ef0a8", command=CalculateClick)
        Enter.place(x=353, y=361)

        parent.resizable(False, False)
        parent.mainloop()

    def methoddatawriter(angleA_str, angleB_str, angleC_str, sideA_str, sideB_str, sideC_str, xDP_str):
        if angleA_str == "":
            angleA_str = 0
        else:
            angleA_str = angleA_str

        if angleB_str == "":
            angleB_str = 0
        else:
            angleB_str = angleB_str

        if angleC_str == "":
            angleC_str = 0
        else:
            angleC_str = angleC_str

        if sideA_str == "":
            sideA_str = 0
        else:
            sideA_str = sideA_str

        if sideB_str == "":
            sideB_str = 0
        else:
            sideB_str = sideB_str

        if sideC_str == "":
            sideC_str = 0
        else:
            sideC_str = sideC_str

        if xDP_str == "":
            xDP_str == 2.0
        else:
            xDP_str = xDP_str

        converter(angleA_str, angleB_str, angleC_str, sideA_str, sideB_str, sideC_str, xDP_str)

    def converter(angleA_str, angleB_str, angleC_str, sideA_str, sideB_str, sideC_str, xDP_str):
        try:
            value = 0
            angleA = float(angleA_str)
            angleB = float(angleB_str)
            angleC = float(angleC_str)
            sideA = float(sideA_str)
            sideB = float(sideB_str)
            sideC = float(sideC_str)
            xDP = int(xDP_str)

            if angleA > 0:
                value = value + 1
            else:
                value = value
        
            if angleB > 0:
                value = value + 1
        
            if angleC > 0:
                value = value + 1
            else:
                value = value

            if sideA > 0:
                value = value + 1
            else:
                value = value

            if sideB > 0:
                value = value + 1
            else:
                value = value

            if sideC > 0:
                value = value + 1
            else:
                value = value
            
            if xDP == 0:
                xDP = 2
            elif xDP > 5:
                xDP = 5
            else:
                xDP = xDP

            if angleA < 0 or angleB < 0 or angleC < 0 or sideA < 0 or sideB < 0 or sideC < 0 or xDP < 0:
                IVerror = 1
                IMerror = 0
                ILerror = 0
                SDerror = 0
                MAerror = 0
                DPerror = 0
                Instlabel1(IVerror, IMerror, ILerror, SDerror, MAerror, DPerror)
            else:
                pass

            if value == 0:
                IVerror = 0
                IMerror = 1
                ILerror = 0
                SDerror = 0
                MAerror = 0
                DPerror = 0
                Instlabel1(IVerror, IMerror, ILerror, SDerror, MAerror, DPerror)
            elif value > 3:
                IVerror = 0
                IMerror = 0
                ILerror = 1
                SDerror = 0
                MAerror = 0
                DPerror = 0
                Instlabel1(IVerror, IMerror, ILerror, SDerror, MAerror, DPerror)
            elif value < 3:
                IVerror = 0
                IMerror = 1
                ILerror = 0
                SDerror = 0
                MAerror = 0
                DPerror = 0
                Instlabel1(IVerror, IMerror, ILerror, SDerror, MAerror, DPerror)
            else:
                finder(angleA, angleB, angleC, sideA, sideB, sideC, xDP)
        except ValueError:
            IVerror = 1
            IMerror = 0
            ILerror = 0
            SDerror = 0
            MAerror = 0
            DPerror = 0
            Instlabel1(IVerror, IMerror, ILerror, SDerror, MAerror, DPerror)

    def finder(angleA, angleB, angleC, sideA, sideB, sideC, xDP, ):
        if ((angleA > 0 and angleB > 0) or (angleA > 0 and angleC > 0) or (angleB > 0 and angleC > 0)) and ((sideA > 0) or (sideB > 0) or (sideC > 0)):
            solverangle(angleA, angleB, angleC, sideA, sideB, sideC, xDP)
        elif ((angleA > 0 and sideC > 0 and sideB > 0) or (angleB > 0 and sideA > 0 and sideC > 0) or (angleC > 0 and sideB > 0 and sideA > 0)):
            CosRuleSide(angleA, angleB, angleC, sideA, sideB, sideC, xDP)
        elif ((angleA > 0 and sideA > 0 and sideC > 0) or (angleB > 0 and sideA > 0 and sideB > 0) or (angleC > 0 and sideB > 0 and sideC > 0)):
            SineRuleAng(angleA, angleB, angleC, sideA, sideB, sideC, xDP)
        elif ((angleA > 0 and sideA > 0 and sideB > 0) or (angleB > 0 and sideB > 0 and sideC > 0) or (angleC > 0 and sideA > 0 and sideC > 0)):
            SineRuleAng(angleA, angleB, angleC, sideA, sideB, sideC, xDP)
        elif (sideA > 0 and sideB > 0 and sideC > 0) and (angleA == 0 and angleB == 0 and angleC == 0):
            anglesolver(angleA, angleB, angleC, sideA, sideB, sideC, xDP)
        else:
            IVerror = 0
            IMerror = 0
            ILerror = 0
            SDerror = 1
            MAerror = 0
            Instlabel1(IVerror, IMerror, ILerror, SDerror, MAerror)

    def solverangle(angleA, angleB, angleC, sideA, sideB, sideC, xDP):
            if angleA > 0 and angleB > 0:
                angleC = 180 - (angleA+angleB)
            elif angleA > 0 and angleC > 0:
                angleB = 180 - (angleA+angleC)
            elif angleB > 0 and angleC > 0:
                angleA = 180 - (angleC+angleB)

            print(angleB)

            if (angleA <= 0) or (angleB <= 0) or (angleC <= 0):
                matherror()
            else:
                sidesolver(angleA, angleB, angleC, sideA, sideB, sideC, xDP)

    def sidesolver(angleA, angleB, angleC, sideA, sideB, sideC, xDP):
        try:
            angleA_radians = math.radians(angleA)
            angleB_radians = math.radians(angleB)
            angleC_radians = math.radians(angleC)
            if sideA > 0:
                sideB = ((sideA*math.sin(angleB_radians))/(math.sin(angleA_radians)))
                sideC = math.sqrt((sideA*sideA)+(sideB*sideB) - 2*sideA*sideB*(math.cos(angleC_radians)))
            elif sideB > 0:
                sideA = ((sideB*math.sin(angleA_radians))/math.sin(angleB_radians))
                sideC = math.sqrt((sideA*sideA)+(sideB*sideB) - 2*sideA*sideB*(math.cos(angleC_radians)))
            elif sideC > 0:
                sideB = ((sideC*math.sin(angleB_radians))/math.sin(angleC_radians))
                sideA = math.sqrt((sideB*sideB)+(sideC*sideC)-2*sideB*sideC*(math.cos(angleA_radians)))
            if (angleA <= 0) or (angleB <= 0) or (angleC <= 0):
                    matherror()
            elif (angleA + angleB + angleC) != 180:
                matherror()
            else:
                resultreturner(angleA, sideA, sideB, angleB, sideC, angleC , xDP)
        except ValueError:
            matherror()

    def SineRuleAng(angleA, angleB, angleC, sideA, sideB, sideC, xDP):
        if angleA > 0 and sideA > 0 and sideC > 0:
            try:
                angleA_radians = math.radians(angleA)
                angleC_radians = math.asin(math.sin(angleA_radians)*sideC/sideA)
                angleC = math.degrees(angleC_radians)
                angleB = 180 - (angleA + angleC)
                angleB_radians = math.radians(angleB)
                sideB = math.sqrt((sideA*sideA)+(sideC*sideC)-2*sideA*sideC*(math.cos(angleB_radians)))
                if (angleA <= 0) or (angleB <= 0) or (angleC <= 0):
                    matherror()
                elif (angleA + angleB + angleC) != 180:
                    matherror()
                else:
                    resultreturner(angleA, sideA, sideB, angleB, sideC, angleC , xDP)
            except ValueError:
                matherror()
        elif angleA > 0 and sideA > 0 and sideB > 0:
            try:
                angleA_radians = math.radians(angleA)
                angleB_radians = math.asin(math.sin(angleA_radians)*sideB/sideA)
                angleB = math.degrees(angleB_radians)
                angleC = 180 - (angleA + angleB)
                angleC_radians = math.radians(angleC)
                sideC = math.sqrt((sideA*sideA)+(sideB*sideB)-2*sideA*sideB*(math.cos(angleC_radians)))
                if (angleA <= 0) or (angleB <= 0) or (angleC <= 0):
                    matherror()
                elif (angleA + angleB + angleC) != 180:
                    matherror()
                else:
                    resultreturner(angleA, sideA, sideB, angleB, sideC, angleC , xDP)
            except ValueError:
                matherror()

        if angleB > 0 and sideA > 0 and sideB > 0:
            try:
                angleB_radians = math.radians(angleB)
                angleA_radians = math.asin(math.sin(angleB_radians)*sideA/sideB)
                angleA = math.degrees(angleA_radians)
                angleC = 180 - (angleA + angleB)
                angleC_radians = math.radians(angleC)
                sideC = math.sqrt((sideA*sideA)+(sideB*sideB)-2*sideA*sideB*(math.cos(angleC_radians)))
                if (angleA <= 0) or (angleB <= 0) or (angleC <= 0):
                    matherror()
                elif (angleA + angleB + angleC) != 180:
                    matherror()
                else:
                    resultreturner(angleA, sideA, sideB, angleB, sideC, angleC , xDP)
            except ValueError:
                matherror()
        elif angleB > 0 and sideB > 0 and sideC > 0:
            try:
                angleB_radians = math.radians(angleB)
                angleC_radians = math.asin(math.sin(angleB_radians)*sideC/sideB)
                angleC = math.degrees(angleC_radians)
                angleA = 180 - (angleB+angleC)
                angleA_radians = math.radians(angleA)
                sideA = math.sqrt((sideB*sideB)+(sideC*sideC)-2*sideB*sideC*(math.cos(angleA_radians)))
                if (angleA <= 0) or (angleB <= 0) or (angleC <= 0):
                    matherror()
                elif (angleA + angleB + angleC) != 180:
                    matherror()
                else:
                    resultreturner(angleA, sideA, sideB, angleB, sideC, angleC , xDP)
            except ValueError:
                matherror()
        
        if angleC > 0 and sideB > 0 and sideC > 0:
            try:
                angleC_radians = math.radians(angleC)
                angleB_radians = math.asin(math.sin(angleC_radians)*sideB/sideC)
                angleB = math.degrees(angleB_radians)
                angleA = 180 - (angleC+angleB)
                angleA_radians = math.radians(angleA)
                sideA = math.sqrt((sideB*sideB)+(sideC*sideC)-2*sideB*sideC*(math.cos(angleA_radians)))
                if (angleA <= 0) or (angleB <= 0) or (angleC <= 0):
                    matherror()
                elif (angleA + angleB + angleC) != 180:
                    matherror()
                else:
                    resultreturner(angleA, sideA, sideB, angleB, sideC, angleC , xDP)
            except ValueError:
                matherror()
        elif angleC > 0 and sideA > 0 and sideC > 0:
            try:
                angleC_radians = math.radians(angleC)
                angleA_radians = math.asin(math.sin(angleC_radians)*sideA/sideC)
                angleA = math.degrees(angleA_radians)
                angleB = 180 - (angleC+angleA)
                angleB_radians = math.radians(angleB)
                sideB = math.sqrt((sideA*sideA)+(sideC*sideC)-2*sideA*sideC*(math.cos(angleB_radians)))
                if (angleA <= 0) or (angleB <= 0) or (angleC <= 0):
                    matherror()
                elif (angleA + angleB + angleC) != 180:
                    matherror()
                else:
                    resultreturner(angleA, sideA, sideB, angleB, sideC, angleC , xDP)
            except ValueError:
                matherror()

    def CosRuleSide(angleA, angleB, angleC, sideA, sideB, sideC, xDP):
        if angleA > 0 and sideB > 0 and sideC > 0:
            try:
                angleA_radians = math.radians(angleA)
                sideA = math.sqrt((sideB*sideB)+(sideC*sideC)-2*sideB*sideC*(math.cos(angleA_radians)))
                angleC_radians = math.asin(math.sin(angleA_radians)*sideC/sideA)
                angleC = math.degrees(angleC_radians)
                angleB = 180 - (angleA+angleC)
                if (angleA <= 0) or (angleB <= 0) or (angleC <= 0):
                    matherror()
                elif (angleA + angleB + angleC) != 180:
                    matherror()
                else:
                    resultreturner(angleA, sideA, sideB, angleB, sideC, angleC , xDP)
            except ValueError:
                matherror()
        elif angleB > 0 and sideA > 0 and sideC > 0:
            try:
                angleB_radians = math.radians(angleB)
                sideB = math.sqrt((sideA*sideA)+(sideC*sideC)-2*sideA*sideC*(math.cos(angleB_radians)))
                angleC_radians = math.asin(math.sin(angleB_radians)*sideC/sideB)
                angleC = math.degrees(angleC_radians)
                angleA = 180 - (angleB+angleC)
                if (angleA <= 0) or (angleB <= 0) or (angleC <= 0):
                    matherror()
                elif (angleA + angleB + angleC) != 180:
                    matherror()
                else:
                    resultreturner(angleA, sideA, sideB, angleB, sideC, angleC , xDP)
            except ValueError:
                matherror()
        elif angleC > 0 and sideA > 0 and sideB > 0:
            try:
                angleC_radians = math.radians(angleC)
                sideC = math.sqrt((sideA*sideA)+(sideB*sideB)-2*sideA*sideB*(math.cos(angleC_radians)))
                angleB_radians = math.asin(math.sin(angleC_radians)*sideB/sideC)
                angleB = math.degrees(angleB_radians)
                angleA = 180 - (angleB+angleC)
                if (angleA <= 0) or (angleB <= 0) or (angleC <= 0):
                    matherror()
                elif (angleA + angleB + angleC) != 180:
                    matherror()
                else:
                    resultreturner(angleA, sideA, sideB, angleB, sideC, angleC , xDP)
            except ValueError:
                matherror()

    def anglesolver(angleA, angleB, angleC, sideA, sideB, sideC, xDP):
        numerator = (sideB*sideB+sideC*sideC-sideA*sideA)
        denominator = (2*sideB*sideC)
        angleA_radians = math.acos(numerator/denominator)
        angleA = math.degrees(angleA_radians)
        angleB_radians = math.asin(math.sin(angleA_radians)*sideB/sideA)
        angleB = math.degrees(angleB_radians)
        angleC = 180 - (angleA+angleB)
        if (angleA <= 0) or (angleB <= 0) or (angleC <= 0):
            matherror()
        elif (angleA + angleB + angleC) != 180:
            matherror()
        else:
            resultreturner(angleA, sideA, sideB, angleB, sideC, angleC , xDP)

    def resultreturner(angleA, sideA, sideB, angleB, sideC, angleC , xDP):
        angleAans = round(angleA, xDP)
        angleBans = round(angleB, xDP)
        angleCans = round(angleC, xDP)
        sideAans = round(sideA, xDP)
        sideBans = round(sideB, xDP)
        sideCans = round(sideC, xDP)
        
        if (angleAans == 60) and (angleBans == 60) and (angleCans == 60):
                triangle = "Equilateral"
        elif (angleAans == 90) or (angleBans == 90) or (angleCans == 90):
                triangle = "Right Angled"
        elif (sideAans != sideBans) and (sideAans != sideCans) and (sideBans != sideCans):
                triangle = "Scalene"
        else:
            triangle = "Isosceles"  

        typetext = ("Your triangle is " + triangle + "")

        AAenter.delete(0, END)
        AAenter.insert(0, (angleAans,"°"))

        ABenter.delete(0, END)
        ABenter.insert(0, (angleBans,"°"))

        ACenter.delete(0, END)
        ACenter.insert(0, (angleCans,"°"))

        SAenter.delete(0, END)
        SAenter.insert(0, sideAans)

        SBenter.delete(0, END)
        SBenter.insert(0, sideBans)

        SCenter.delete(0, END)
        SCenter.insert(0, sideCans)
            
        InstructionLabel.config(text=typetext, fg="black")
        InstructionLabel.place(x=31, y=364)

        Enter.config(text="Start New", command=newinstance)
        Enter.place(x=353, y=361)

    def newinstance():
        Enter.config(text="Calculate")
        Enter.place(x=353, y=361)
        
        AAenter.destroy 
        ABenter.destroy 
        ACenter.destroy 
        SAenter.destroy 
        SBenter.destroy 
        SCenter.destroy 
        DPenter.destroy 
        tri_canv.destroy
        
        UImaker()

    parentmaker()