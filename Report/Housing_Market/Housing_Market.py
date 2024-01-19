import os
import pandas as pd
import numpy as np
import locale, sys
import calendar, datetime
locale.setlocale(locale.LC_NUMERIC, 'en_US')
sys.path.append(r'C:\\Users\\Keitaro Ninomiya\\Box\\IAR_nino\\Report')
from Write import Adj, Comma

class HousingMarket:
    def __init__(self, Month, Year, TP1,TP2,TP3,TP4,TP5):
        self.TP1=TP1
        self.TP2=TP2
        self.TP3=TP3
        self.TP4=TP4
        self.TP5=TP5
        self.Year=Year
        self.Month=Month
        
        mname = Month
        mnum = list(calendar.month_name).index(Month)
        self.PostMonth=calendar.month_name[(mnum+1) %12]
        self.PPstMonth=calendar.month_name[(mnum+2) %12]
        self.PPPtMonth=calendar.month_name[(mnum+3) %12]
    
    
    def P1(self):
        S1 = "In " + self.Month +", housesales in Illinois sales experienced a "+Adj(self.TP1["Sales_IL_sells"][3],1)+" annual change, the median prices experienced a "+Adj(self.TP1["Sales_IL_sells"][3],1)+" annual change. The housesales in Chicago PMSA experienced a " +Adj(self.TP1["Sales_CH_sells"][3],1)+" annual change, the median prices experienced a "+Adj(self.TP1["Price_CH_price"][3],1)+" annual change."
        S2 =  str(Comma(np.around(self.TP1["Sales_IL_sells"][3],-2)))+ " houses were sold in Illinois, changing by "+ str(self.TP1["Sales_AGrowthIL"][3].round(1))+"% from a year ago and "+ str(self.TP1["Sales_MGrowthIL"][3].round(1)) +"% from a month ago."
        S3 = " In the Chicago PMSA, " +str(Comma(np.around(self.TP1["Sales_CH_sells"][3],-2)))+ " houses were sold, changing by " + str(self.TP1["Sales_AGrowthCH"][3].round(1))+ "% from a year ago and " + str(self.TP1["Sales_MGrowthCH"][3].round(1)) +"% from a month ago."
        S4 = "The median price was $" +  str(Comma(self.TP1["Price_IL_price"][3]))+ " in Illinois, changing by " + str(self.TP1["Price_AGrowthIL"][3].round(1))+" from "+self.Month+" last year; the comparable figure for the Chicago PMSA was $" + str(Comma(self.TP1["Price_CH_price"][3]))+", changing by "+ str(self.TP1["Price_AGrowthCH"][3].round(1)) +"% from " + self.Month+ " last year."
        paragraph = S1+S2+S3+S4
        return paragraph
    
    def P2(self):
        S1="In "+self.Month+", for the Chicago PMSA, the percentage of foreclosed sales (e.g. REOs) among the total sales was "+str(100*self.TP2["fratio"][3].round(3))+"%. "
        S2=str(Comma(np.around(self.TP2["Regular_Sale"][3],-2)))+" regular sales were made, "+ str(self.TP2["RS_AGrowth"][3].round(1)) +"% "+Adj(self.TP2["RS_AGrowth"][3],3)+" than last year. "+str(Comma(self.TP2["ForeCProp"][3]))+" foreclosed properties were sold, "+str(self.TP2["FCP_AGrowth"][3].round(1))+"% "+Adj(self.TP2["FCP_AGrowth"][3],3)+" than last year."
        S3="The median price was $"+str(Comma(self.TP2["MedianPrice"][3]))+" for regular property sales, "+Adj(self.TP2["MP_AGrowth"][3],1)+" "+str(self.TP2["MP_AGrowth"][3].round(3))+"% from last year; the comparable figure for the foreclosed properties was $"+str(Comma(self.TP2["MedianPrice_FC"][3]))+", "+Adj(self.TP2["MPFC_AGrowth"][3],3)+" "+str(self.TP2["MPFC_AGrowth"][3].round(1))+"% from last year. "
        paragraph = S1+S2+S3
        return paragraph
    
    
    def P3(self):
        S1="The sales forecast for "+self.PostMonth+", "+self.PPstMonth+", and "+self.PPPtMonth+" suggests a "+Adj(self.TP3["TAGrowthIL_LB"][6],4)+" on a yearly basis for both Illinois."
        S2="The sales forecast for "+self.PostMonth+", "+self.PPstMonth+", and "+self.PPPtMonth+" suggests a "+Adj(self.TP3["TMGrowthIL_LB"][6],4)+" on a monthly basis for both Illinois."
        S3="The sales forecast for "+self.PostMonth+", "+self.PPstMonth+", and "+self.PPPtMonth+" suggests a "+Adj(self.TP3["TAGrowthCH_LB"][6],4)+" on a yearly basis for both Illinois."
        S4="The sales forecast for "+self.PostMonth+", "+self.PPstMonth+", and "+self.PPPtMonth+" suggests a "+Adj(self.TP3["TMGrowthCH_LB"][6],4)+" on a monthly basis for both Illinois."
        S5="Annually for Illinois, the three-month average forecasts point to a "+Adj(self.TP3["TAGrowthIL_LB"][6],4)+" in the range of "+str(self.TP3["TAGrowthIL_LB"][6].round(3)*100)+" to "+str(self.TP3["TAGrowthIL_UB"][6].round(3)*100)+"%; the comparative figures for the Chicago PMSA are a "+Adj(self.TP3["TAGrowthCH_LB"][6],4)+" in the range of "+str(self.TP3["TAGrowthCH_LB"][6].round(3)*100)+"% to "+str(self.TP3["TAGrowthCH_UB"][6].round(3)*100)+"%. "
        S6="On a monthly basis, the three-month average sales are forecast to "+Adj(self.TP3["TMGrowthIL_LB"][6],4)+" in the range of "+str(self.TP3["TMGrowthIL_LB"][6].round(3)*100)+"% to "+str(self.TP3["TMGrowthIL_UB"][6].round(3)*100)+"% for Illinois and "+Adj(self.TP3["TMGrowthCH_LB"][6],4)+" in the range of "+str(self.TP3["TMGrowthCH_LB"][6].round(3)*100)+"% to "+str(self.TP3["TMGrowthCH_UB"][6].round(3)*100)+"% for the Chicago PMSA."
        paragraph = S1+S2+S3+S4+S5+S6
        return paragraph
    
    def P4(self):
        S1="The pending home sales index  is a leading indicator based on contract signings."
        S2="This "+self.Month+", the number of homes put under contract was less than last year in Illinois and Chicago PMSA. "
        S3="The pending home sales index is "+str(self.TP4["ILpending"][3].round(1))+" (2019=100) in Illinois, down "+str(self.TP4["pendingGrowthIL"][3].round(1))+"% from a year ago. "
        S4="In the Chicago PMSA, the comparable figure is "+str(self.TP4["CHpending"][3].round(1))+" down "+str(self.TP4["pendingGrowthCH"][3].round(1))+"% from a year ago. "  
        S5="At the latest average annual pending sales rate, Illinois had enough housing inventory for 2.0 months (remaining the same as last year) . "
        S6="In the Chicago PMSA, the comparable figure was 2.0 months (remaining the same as last year). "
        S7="The lowest price ranges (<$100K) showed the largest decline both in Illinois, and in the Chicago PMSA."
        paragraph = S1+S2+S3+S4+S5+S6+S7
        return paragraph
        
    def P5(self):
        S1="The median price forecast indicates "+Adj(self.TP5["AGrowthIL"][4],1)+" annual growth for "+self.PostMonth+", "+self.PPstMonth+", and "+self.PPPtMonth+" in Illinois."
        S2="The median price forecast indicates "+Adj(self.TP5["AGrowthCH"][4],1)+" annual growth for "+self.PostMonth+", "+self.PPstMonth+", and "+self.PPPtMonth+" in the Chicago PMSA. "
        S3="In Illinois, the median price is forecast to change by "+str(self.TP5["AGrowthIL"][4].round(1))+"% in "+self.PostMonth+", "+str(self.TP5["AGrowthIL"][5].round(1))+"% in "+self.PPstMonth+", and "+str(self.TP5["AGrowthIL"][6].round(1))+"% in "+self.PPPtMonth+". "
        S4="For the Chicago PMSA, the comparable figures are "+str(self.TP5["AGrowthCH"][4].round(1))+"% in "+self.PostMonth+", "+str(self.TP5["AGrowthCH"][5].round(1))+"% in "+self.PPstMonth+", and "+str(self.TP5["AGrowthCH"][6].round(1))+"% in "+self.PPPtMonth+". "
        S5="As a complement to the median housing price index (HPI), the SHDRE HPI forecasts a positive growth trend for both Illinois and the Chicago PMSA.  "
        S6="In Illinois, the SHDRE HPI (Jan 2008=1) is forecast to change by "+str(self.TP5["foreCGrowIL"][4].round(3)*100)+"% in "+self.PostMonth+", "+str(self.TP5["foreCGrowIL"][5].round(3)*100)+"% in "+self.PPstMonth+", and "+str(self.TP5["foreCGrowIL"][6].round(3)*100)+"% in "+self.PPPtMonth+". "
        S7="The comparable figures for the Chicago PMSA are "+str(self.TP5["foreCGrowCH"][4].round(3)*100)+"% in "+self.PostMonth+", "+str(self.TP5["foreCGrowCH"][5].round(3)*100)+"% in "+self.PPstMonth+", and "+str(self.TP5["foreCGrowCH"][6].round(3)*100)+"% in "+self.PPPtMonth+". "
        S8="SHDRE HPI takes housing characteristics into account and constructs comparable “baskets” of homes for each month."
        paragraph = S1+S2+S3+S4+S5+S6+S7+S8
        return paragraph
        
    def P6(self):
        S1="In "+self.Month+", the Conference Board Consumer Confidence Index [https://www.conference-board.org/topics/consumer-confidence], whereas the University of Michigan Consumer Sentiment Index [http://www.sca.isr.umich.edu/]. "
        S2="The Conference Board Consumer Confidence Index survey noted that [https://www.conference-board.org/topics/consumer-confidence] "
        S3="The University of Michigan Consumer Sentiment Index survey noted that [http://www.sca.isr.umich.edu/]."
        paragraph = S1+S2+S3
        return paragraph
    
    def Adj(self,Value,Type):
        if Type==1:
            if np.sign(Value)==-1:
                return("negative")
            if np.sign(Value)==1:
                return("positive")
            else:
                return('unchanged')
        if Type==2:
            if np.sign(Value)==-1:
                return("down")
            if np.sign(Value)==1:
                return("up")
            else:
                return('unchanged at')
        if Type==3:
            if np.sign(Value)==-1:
                return("less")
            if np.sign(Value)==1:
                return("more")
            else:
                return('unchanged at')

        if Type==4:
            if np.sign(Value)==-1:
                return("decrease")
            if np.sign(Value)==1:
                return("increase")
            else:
                return('unchanged')

    def Comma(self,Value):
        return(locale.format_string("%d", Value,-2))
        
