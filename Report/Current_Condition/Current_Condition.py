import os
import pandas as pd
import numpy as np
import locale,sys
locale.setlocale(locale.LC_NUMERIC, 'en_US')
import calendar, datetime
sys.path.append(r'C:\\Users\\Keitaro Ninomiya\\Box\\IAR_nino\\Report')
from Write import Adj, Comma

class HousingMarketCurrent:
    def __init__(self, Month, Year, TP1,TP2):
        self.TP1=TP1
        self.TP2=TP2
        self.Year=Year
        self.Month=Month
        
        mname = Month
        mnum = list(calendar.month_name).index(Month)
        self.PostMonth=calendar.month_name[(mnum+1) %12]
        self.PPstMonth=calendar.month_name[(mnum+2) %12]
        self.PPPtMonth=calendar.month_name[(mnum+3) %12]
        
        self.HI_IL=[]
        self.HI_CH=[]
        self.EHIL=[]
        self.EHIL_Pre=[]
        self.EHCH=[]
        self.EHCH_Pre=[]


    def P1(self):
        S1 = "In " + self.Month+", housesales in Illinois sales experienced a "+Adj(self.TP1["Sales_AGrowthIL"][3],1)+" annual change, the median prices experienced a "+Adj(self.TP1["Price_AGrowthIL"][3],1)+" annual change. The housesales in Chicago PMSA experienced a " +Adj(self.TP1["Sales_AGrowthCH"][3],1)+" annual change, the median prices experienced a "+Adj(self.TP1["Price_AGrowthCH"][3],1)+" annual change."
        S2 =  str(Comma(np.around(self.TP1["Sales_IL_sells"][3],-2)))+ " houses were sold in Illinois, changing by "+ str(self.TP1["Sales_AGrowthIL"][3].round(1))+"% from a year ago and "+ str(self.TP1["Sales_MGrowthIL"][3].round(1)) +"% from a month ago."
        S3 = " In the Chicago PMSA, " +str(Comma(np.around(self.TP1["Sales_CH_sells"][3],-2)))+ " houses were sold, changing by " + str(self.TP1["Sales_AGrowthCH"][3].round(1))+ "% from a year ago and " + str(self.TP1["Sales_MGrowthCH"][3].round(1)) +"% from a month ago."
        S4 = "The median price was $" +  str(Comma(self.TP1["Price_IL_price"][3]))+ " in Illinois, changing by " + str(self.TP1["Price_AGrowthIL"][3].round(1))+" from "+self.Month+" last year; the comparable figure for the Chicago PMSA was $" + str(Comma(self.TP1["Price_CH_price"][3]))+", changing by "+ str(self.TP1["Price_AGrowthCH"][3].round(1)) +"% from " + self.Month+ " last year."
        paragraph = S1+S2+S3+S4
        return paragraph

    def P2(self):
        
        S1="In "+self.Month+", for the Chicago PMSA, the percentage of foreclosed sales (e.g. REOs) among the total sales was "+str(100*self.TP2["fratio"][3].round(3))+"%. "
        S2=str(Comma(np.around(self.TP2["Regular_Sale"][3],-2)))+" regular sales were made, "+ str(self.TP2["RS_AGrowth"][3].round(1)) +"% "+Adj(self.TP2["RS_AGrowth"][3],3)+" than last year. "
        S3=str(Comma(self.TP2["ForeCProp"][3]))+" foreclosed properties were sold, "+str(self.TP2["FCP_AGrowth"][3].round(1))+"% "+Adj(self.TP2["FCP_AGrowth"][3],3)+" than last year."
        S4="The median price was $"+str(Comma(self.TP2["MedianPrice"][3]))+" for regular property sales, "+Adj(self.TP2["MP_AGrowth"][3],1)+" "+str(self.TP2["MP_AGrowth"][3].round(3))+"% from last year; the comparable figure for the foreclosed properties was $"+str(Comma(self.TP2["MedianPrice_FC"][3]))+", "+Adj(self.TP2["MPFC_AGrowth"][3],2)+" "+str(self.TP2["MPFC_AGrowth"][3].round(1))+"% from last year. "
        S5="(Reference: Ratio of Foreclosed Sales over Total Sales, Sales & Median Prices: Foreclosed vs. Regular Sales figures)"
        paragraph = S1+S2+S3+S4+S5
        return paragraph

    def P3(self):
        S1="In "+self.Month+", at the latest average annual pending sales rate, Illinois had enough housing inventory for "+str(self.HI_IL)+" months ([Relative to last year]).  "
        S2="In the Chicago PMSA, the comparable figure was "+str(self.HI_CH)+" months ([Relative to last year]). "
        S3="Months of supply for homes in the lowest price ranges (<100K) experienced [] in Illinois. "
        S4="Months of supply for homes in the lowest price ranges (<100K) experienced [] in the Chicago PMSA. "
        S5="(Reference: Illinois and Chicago PMSA Annual Months’ Supply by Price Range figures) "
        paragraph = S1+S2+S3+S4+S5
        return paragraph
        
    def P4(self):
        S1="In "+self.Month+", the market shares of homes in the [] experienced the largest change compared to a year ago for Illinois."
        S2="In "+self.Month+", the market shares of homes in the [] experienced the largest change compared to a year ago for the Chicago PMSA. "
        S3="In Illinois, the market share for homes at $100-200K decreased to "+str(self.EHIL)+"% from "+str(self.EHIL_Pre)+"% a year ago. "
        S4="In the Chicago PMSA, the market share for homes at $100-200K decreased to "+str(self.EHCH)+"% from "+str(self.EHCH_Pre)+"% a year ago. "
        S5="(Reference: Illinois and Chicago PMSA Price Stratification figures)  "
        paragraph = S1+S2+S3+S4+S5
        return paragraph