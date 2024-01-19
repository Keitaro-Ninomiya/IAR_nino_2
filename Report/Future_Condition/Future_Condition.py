import os
import pandas as pd
import numpy as np
import locale, sys
import calendar, datetime
locale.setlocale(locale.LC_NUMERIC, 'en_US')
sys.path.append(r'C:\\Users\\Keitaro Ninomiya\\Box\\IAR_nino\\Report')
from Write import Adj, Comma


class HousingMarketFuture:
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
        S1="The median price forecast indicates "+Adj(self.TP1["AGrowthIL"][4],1)+" annual growth for "+self.PostMonth+", "+self.PPstMonth+", and "+self.PPPtMonth+" in Illinois."
        S2="The median price forecast indicates "+Adj(self.TP1["AGrowthCH"][4],1)+" annual growth for "+self.PostMonth+", "+self.PPstMonth+", and "+self.PPPtMonth+" in the Chicago PMSA. "
        S3="In Illinois, the median price is forecast to change by "+str(self.TP1["AGrowthCH"][4].round(1))+"% in "+self.PostMonth+", "+str(self.TP1["AGrowthIL"][5].round(1))+"% in "+self.PPstMonth+", and "+str(self.TP1["AGrowthIL"][6].round(1))+"% in "+self.PPPtMonth+". "
        S4="For the Chicago PMSA, the comparable figures are "+str(self.TP1["AGrowthCH"][4].round(1))+"% in "+self.PostMonth+", "+str(self.TP1["AGrowthCH"][5].round(1))+"% in "+self.PPstMonth+", and "+str(self.TP1["AGrowthCH"][6].round(1))+"% in "+self.PPPtMonth+". "
        S5="(Reference: Forecast for "+self.Month+" "+self.Year+" report table) "
        paragraph = S1+S2+S3+S4+S5
        return paragraph
        
    def P2(self):
        S1="As a complement to the median housing price index (HPI), the SHDRE HPI forecasts a "+Adj(self.TP2["foreCGrowIL"][4].round(2),4)+" growth trend for Illinois."
        S2="As a complement to the median housing price index (HPI), the SHDRE HPI forecasts a "+Adj(self.TP2["foreCGrowIL"][4].round(2),4)+" growth trend for the Chicago PMSA"
        S3="In Illinois, the SHDRE HPI (Jan 2008=1) is forecast to change by "+str(100*self.TP2["foreCGrowIL"][4].round(1))+"% in "+self.PostMonth+", "+str(100*self.TP2["foreCGrowIL"][5].round(2))+"% in "+self.PPstMonth+", and "+str(100*self.TP2["foreCGrowCH"][6].round(1))+"% in "+self.PPPtMonth+". "
        S4="The comparable figures for the Chicago PMSA are "+str(100*self.TP2["foreCGrowCH"][4].round(2))+"% in "+self.PostMonth+", "+str(100*self.TP2["foreCGrowCH"][5].round(2))+"% in "+self.PPstMonth+", and "+str(self.TP2["foreCGrowCH"][6].round(2)*100)+"% in "+self.PPPtMonth+". "
        S5="SHDRE HPI takes housing characteristics into account and constructs comparable “baskets” of homes for each month."
        S6="(Reference: Housing Price Index)"
        paragraph = S1+S2+S3+S4+S5
        return paragraph
        
    def P3(self):
        S1="The sales forecast for "+self.PostMonth+", "+self.PPstMonth+", and "+self.PPPtMonth+" suggests a "+Adj(100*self.TP3["TAGrowthIL_LB"][6].round(2),4)+" on a yearly basis for Illinois. "
        S2="The sales forecast for "+self.PostMonth+", "+self.PPstMonth+", and "+self.PPPtMonth+" suggests a "+Adj(100*self.TP3["TMGrowthIL_LB"][6].round(2),4)+" on a monthly basis for Illinois. "
        S3="The sales forecast for "+self.PostMonth+", "+self.PPstMonth+", and "+self.PPPtMonth+" suggests a "+Adj(100*self.TP3["TAGrowthCH_LB"][6].round(2),4)+" on a yearly  basis for the Chicago PMSA. "
        S4="The sales forecast for "+self.PostMonth+", "+self.PPstMonth+", and "+self.PPPtMonth+" suggests a "+Adj(100*self.TP3["TMGrowthCH_LB"][6].round(2),4)+" on a monthly basis for the Chicago PMSA. "
        S5="Annually for Illinois, the three-month average forecasts point to a "+Adj(100*self.TP3["TAGrowthIL_LB"][6].round(2),4)+" in the range of "+str(100*self.TP3["TAGrowthIL_LB"][6].round(2))+" to "+str(100*self.TP3["TAGrowthIL_UB"][6].round(2))+"%; the comparative figures for the Chicago PMSA are a "+Adj(100*self.TP3["TAGrowthCH_LB"][6].round(2),4)+" in the range of "+str(100*self.TP3["TAGrowthCH_LB"][6].round(2))+"% to "+str(100*self.TP3["TAGrowthIL_UB"][6].round(2))+"%. "
        S6="On a monthly basis, the three-month average sales are forecast to "+Adj(self.TP3["TMGrowthIL_LB"][6],4)+" in the range of "+str(100*self.TP3["TMGrowthIL_LB"][6].round(2))+"% to "+str(100*self.TP3["TMGrowthIL_UB"][6].round(2))+"% for Illinois and "+Adj(self.TP3["TMGrowthCH_LB"][6],4)+" in the range of "+str(100*self.TP3["TMGrowthCH_LB"][6].round(2))+"% to "+str(100*self.TP3["TMGrowthCH_UB"][6].round(2))+"% for the Chicago PMSA."
        S7="(Reference: Forecast for "+self.Month+" "+self.Year+" report table)"
        paragraph = S1+S2+S3+S4+S5+S6+S7
        return paragraph
                
    def P4(self):
        S1="The pending home sales index  is a leading indicator based on contract signings."
        S2="This "+self.Month+", the number of homes put under contract was "+Adj(self.TP4["pendingGrowthIL"][3],3)+" than last year in Illinois and Chicago PMSA. "
        S3="The pending home sales index is "+str(self.TP4["ILpending"][3].round(2))+" (2019=100) in Illinois, "+Adj(self.TP4["pendingGrowthIL"][3],2)+" "+str(100*self.TP4["pendingGrowthIL"][3].round(2))+"% from a year ago. "
        S4="In the Chicago PMSA, the comparable figure is "+str(self.TP4["CHpending"][3].round(2))+" "+Adj(self.TP4["pendingGrowthCH"][3],2)+" "+str(self.TP4["pendingGrowthCH"][3].round(2))+"% from a year ago. "  
        S5="(Reference: Illinois and Chicago PMSA Pending Home Sales Index figure)"
        paragraph = S1+S2+S3+S4+S5
        return paragraph        
        
    def P5(self):
        S1="In "+self.Month+" "+self.Year+", "+str(self.TP5["in_count"][3])+" houses were newly filed for foreclosure in the Chicago PMSA ("+Adj(self.TP5["in_rateyear"][3],2)+" "+str(100*self.TP5["in_rateyear"][3].round(2))+"% and "+Adj(self.TP5["in_ratemon"][3],2)+" "+str(100*self.TP5["in_ratemon"][3].round(2))+"%, respectively, from a year and a month ago). "
        S2=str(TP5["out_count"][3])+" foreclosures were completed ("+Adj(self.TP5["out_rateyear"][3],2)+" "+str(100*self.TP5["out_rateyear"][3].round(2))+"% and "+Adj(self.TP5["out_ratemon"][3],2)+" "+str(100*self.TP5["out_ratemon"][3].round(2))+"% respectively from a year and a month ago).  "
        S3="As of "+self.Month+" "+self.Year+", there are [] homes at some stage of foreclosure — the foreclosure inventory. "
        S4="The monthly average net flows of foreclosures (foreclosure inflows - outflows) were [] in the past 6 months, [] in the last 12 months, and [] in the previous 24 months. "
        S5="(Reference: Chicago PMSA Foreclosure Inflows and Outflows, and Inventory figures)."
        paragraph = S1+S2+S3+S4+S5
        return paragraph        
