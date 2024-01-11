import pandas as pd
def GetData(path,Type):
    if Type=='Sales':
        df=pd.read_csv(path+"Working Folder\\MSA\\table_4_price.csv")
        return(df)
    if Type=='Sales':
        df=pd.read_csv(path+"Working Folder\\MSA\\table_5_sales.csv")
        return(df)

def Count(List):
    """
    Counts number of positive elements in list.
    """

def Adj(Val):
    """
    Converts value into increase/decrease.
    """

class QuarterlyHousing:
    def __init__(self, month, year,Quarter, Sales,Price):
        self.Sales=Sales
        self.Price=Price
        self.year=year
        self.month=month   
        self.Quarter=Quarter

    def NumToWord(self):
        if self.Quarter==1:
            return('First')
        if self.Quarter==2:
            return('Second')
        if self.Quarter==3:
            return('Third')
        if self.Quarter==4:
            return('Fourth')

    def TableS(self):
        TP1=self.Sales[self.Sales['forecast1']=='3M Average']
        return(TP1)

    def TableS(self):
        TP2=self.Price[self.Sales['forecast1']=='3M Average']
        return(TP2)

    def P1(self,Quarter):
        '''
        Summary of quarterly housing market with forecasts.
        '''
        #Data for Paragraph 1
        SalesTable=TableS(self.Sales)
        PriceTable=TableP(self.Price)
        
        ILSales=SalesTable[SalesTable['area']=='IL')]['price0']
        
        PastQuarterS=SalesTable['price0'].tolist()
        ForecastS=SalesTable['price1'].tolist()

        PastQuarterP=SalesTable['price0'].tolist()
        ForecastP=SalesTable['price1'].tolist()

        #Data for Paragraph 2
        ILSalesGrowth=SalesTable[SalesTable['area']=='IL')]['annually0']
        PastQuarterS=SalesTable['price0'].tolist()

        
        #Generating Paragraphs
        S1="In the "+NumToWord(self.Quarter)+" Quarter of "+year+", overall sales in Illinois "+Adj(ILSales)+" compared to last year. Positive growth was recorded in "+Count(PastQuarterS)+" of the MSAs."
        S2="Forecasts the "+NumToWord(self.Quarter+1)+" Quarter of 2023, overall sales in Illinois are forecast to increase. "+Count(ForecastS)+" MSAs are forecast to experience an increase in their sales."
        S3="Decreasing median prices for Illinois are found in "+Count(PastQuarterP)+" MSAs in the "+NumToWord(self.Quarter)+" Quarter; Champaign-Urbana, Davenport-Moline-Rock Island, Kankakee, and Peoria-Pekin."
        S4="For the "+NumToWord(self.Quarter+1)+" Quarter of 2023, "+Count(ForecastP)+" MSAs are projected to experience a positive growth in median price; prices in Champaign-Urbana, Chicago PMSA, Kankakee, and Metro-East are expected to increase."
        S5="The remainder are forecasted to experience a decrease in median price."


    def P2(self):
        S1="Housing Market Conditions"
        S2="In the "+NumToWord(self.Quarter)+" Quarter of "+year+", Illinois experienced a "+Adj(ILSales)+" in sales, and "+Count(PastQuarterS)+" MSAs also experienced annual decreases in sales with varying degrees."  
        S3="Overall sales for Illinois decreased by "+str(ILSalesGrowth)+"% compared to a year ago."
        S4=Count(PastQuarterS)+" MSAs experienced negative changes:  Bloomington-Normal (-14.0%), Champaign-Urbana (-12.2%), Chicago PMSA (-25.6%), Davenport-Moline-Rock Island (-28.8%), Decatur (-21.3%), Kankakee (-20.8%), Metro-East (-19.0%), Peoria-Pekin (-21.5%), Rockford (-16.4%), and Springfield (-19.3%)."

    def P3(self):
        S1="In terms of housing prices, the overall median price for Illinois was unchanged over the past year.  "
        S2="The negative growth was noted in one MSAs: Kankakee (-2.9%).  "
        S3="Remaining MSAs experienced positive changes in prices: Bloomington-Normal (12.6%), Champaign-Urbana (6.7%), Chicago PMSA (1.5%), Davenport-Moline-Rock Island (16.4%), Decatur (9.8%) Peoria-Pekin (12.6%), Rockford (2.9%), Metro-East (3.2%), and Springfield (6.%)."

    def P4(self):
        "The overall quarter’s supply for Illinois is 0.5 quarters, decreasing from 0.6 of a year ago.  Two MSAs experienced positive changes: Bloomington Normal (to 0.4 from 0.6) and Davenport-Moline-Rock Island (to 0.5 from 0.4). Eight MSAs experienced negative changes: Chicago PMSA (0.4 from 0.6), Champaign-Urbana (to 0.3 from 0.4), Peoria-Pekin (to 0.3 from 0.4), Rockford (to 0.3 from 0.4), and Kankakee MSA (to 0.4 from 0.6). Two MSAs experienced no changes: Decatur and Metro-East."

    def P5(self):
        S1="Housing Market Forecasts"
        S2="Table 5 provides the sales forecast for the Third Quarter of 2023. The overall sales in Illinois are forecasted to decrease by -9.5% to -12.8% compared to a year ago. Eight MSAs are forecasted to experience decreases in sales: Bloomington-Normal (-12.6% to -17.1%), Champaign-Urbana (-2.5% to -3.3%), Chicago PMSA (-12.5% to 16.9%), Decatur (-13.4% to -18.2%), Kankakee (-9.0% to -12.2%), Metro-East (-3.6% to -4.8%), Rockford (-10.9% to -14.7%), and Peoria-Pekin (-2.2% to -3.0%).  "
        S3="Two MSAs are forecasted to experience increases in sales: Davenport-Moline-Rock Island (2.2% to 3.0%) and Springfield (1.4% to 2.0%)."

    def P6(self):
        S1 = "Table 4 provides the median price forecasts for the Third Quarter of 2023. The forecasts indicate positive annual growth for the state.  "
        S2 = "All ten MSAs are forecasted to experience increase changes: Bloomington-Normal (14.1%), Champaign-Urbana (3.9%), Chicago PMSA (6.4%), Davenport-Moline-Rock Island (3.9%), Decatur (12.0%), Kankakee (19.4%), Metro-East (4.5%), Peoria-Pekin (4.1%), Rockford (7.3%), and Springfield (2.2%)."
        S3 = "Detailed current conditions and forecasts for each MSA market are presented in the next section.  "
        S4 = "MSA Detailed Notes (to accompany figures on median prices, sales, price stratification, and inventory)"

class MSAReport():
    def __init__(self, month, Quarter, year, TP1,TP2,TP3,TP4,TP5):
        self.TP1=TP1
        self.TP2=TP2
        self.TP3=TP3
        self.TP4=TP4
        self.TP5=TP5
        self.year=year
        self.month=month

    def GetMSA(self,MSA):
        '''
        Gets the table with Housing info for specified MSA.
        '''
    def Report(self,MSA):
        Table=GetMSA(MSA)
        S1="•	Median price in "+Quarter+" "+str(Year)+" is forecasted to increase by an annual rate of 6.5%."
        S2="•	The sales forecast indicates a negative trend with annual rates of change between -9.5% to -12.8% in Q3 2023"+Quarter+" "+str(Year)+". "
        S3="•	Median prices in "+Quarter+" "+str(Year)+" were unchanged than a year ago.  "
        S4="•	Sales volume in "+Quarter+" "+str(Year)+" was -23.4% lower than a year ago.  "
        S5="•	In "+Quarter+" "+str(Year)+", market shares of homes priced at $300-500K experienced the largest change, increasing to 28.2% from 27.2% a year ago.  "
        S6="•	By "+Quarter+" "+str(Year)+", the overall quarter’s supply is 0.5 quarters, decreasing from 0.6 a year ago."

