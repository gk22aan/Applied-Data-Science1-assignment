# Import Python Packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read CSV file
data = pd.read_csv('API_19_DS2_en_csv_v2_5361599.csv', skiprows = 4)
data.describe()

#Function
def read_world_bank_data(filename, skip):
    '''This function  takes a filename as argument, reads a dataframe returns
       two dataframes: one with years as columns and one with
       countries as columns.'''
    df = pd.read_csv(filename, skiprows=skip)
    df_years = data.set_index(['Indicator Name','Country Name'])
   .drop(['Country Code', 'Indicator Code'], axis=1)
    df_countries = data.set_index(['Country Name'])
    .drop(['Country Code','Indicator Code'], axis=1).T
    return df_years, df_countries
# Call function to define color of BAR in Bar plot.
read_world_bank_data('API_19_DS2_en_csv_v2_5361599.csv',4)

#Use statistical function for data manipulation
data_countrywise = data.groupby(['Country Name','Indicator Name']).sum()
data_countrywise
df_years = data.set_index(['Indicator Name','Country Name'])
.drop(['Country Code', 'Indicator Code'], axis=1)
# Data Manipulation
df_data = read_world_bank_data('API_19_DS2_en_csv_v2_5361599.csv',4)
years = df_data[0]
country = df_data[1]
# Data Prepartion for 1st Bar graph Plot
years_data_EnergyUse =
years.loc['Energy use (kg of oil equivalent per capita)','2005':'2010']
years_data_EnergyUse = years_data_EnergyUse.dropna(axis=0)
years_data_EnergyUse =
years_data_EnergyUse.loc[['Spain','Albania','Cuba','Greece','Croatia','Italy',
                          'Australia','Nepal','Libya','Mexico'],'2005':'2010']
years_data_EnergyUse.reset_index(inplace=True)

# Bar graph Plot for 1st indicator
fig = plt.figure()
ax = years_data_EnergyUse.plot(x="Country Name", y=["2005", "2006", "2007",
                                                    "2008","2009","2010"],
                                   kind="bar",figsize = (10,10),stacked=False)
plt.title("Energy Use", fontsize = 15)
plt.ylabel('Energy use (kg of oil equivalent per capita) $\longrightarrow$'
                                                            , fontsize = 15)
plt.xlabel('Country $\longrightarrow$',fontsize = 15)
plt.xticks(rotation = 45)
plt.legend(prop={'size': 13}, loc='center left', bbox_to_anchor=(1, .9)
                                                          ,fontsize='larger')
ax.autoscale(tight=True)
plt.show()
# Data Prepartion for 2nd Bar graph Plot
years_data_C02_intensity =
years.loc['CO2 intensity (kg per kg of oil equivalent energy use)' ,
          '2005':'2010']
years_data_C02_intensity = years_data_C02_intensity.dropna(axis=0)
years_data_C02_intensity =
years_data_C02_intensity.loc[['Spain','Albania','Cuba',
                              'Greece','Croatia','Italy',
                              'Australia','Nepal','Libya','Mexico'],
                              '2005':'2010']
years_data_C02_intensity
years_data_C02_intensity.reset_index(inplace=True)

# Bar graph Plot for 2nd indicator
fig = plt.figure()
ax = years_data_C02_intensity.
plot(x="Country Name", y=["2005", "2006", "2007","2008","2009","2010"],
     kind="bar",figsize = (10,10),stacked=False)
plt.title("CO2 intensity", fontsize = 15)
plt.ylabel('kg per kg of oil equivalent energy use $\longrightarrow$',
           fontsize = 15)
plt.xlabel('Country $\longrightarrow$',fontsize = 15)
plt.xticks(rotation = 45)
plt.legend(prop={'size': 13}, loc='center left', bbox_to_anchor=(1, .9)
,fontsize='larger')
ax.autoscale(tight=True)
plt.show()
# Data Prepartion for 1st line graph Plot
years_data_CPIA =
years.loc['CPIA public sector management
          and institutions cluster average (1=low to 6=high)' , '2005':'2010']

years_data_CPIA

years_data_CPIA = years_data_CPIA.dropna(axis=0)
years_data_CPIA = years_data_CPIA.loc[['Samoa','Zimbabwe','Bangladesh',
                                       'Chad','Armenia','Georgia']
                                       ,'2005':'2010']
# line graph Plot for 1st indicator
import matplotlib
matplotlib.rc('figure', figsize=(8, 8))
years_data_CPIA.T.plot( linestyle="--", marker='*', markersize=8,linewidth=1.5)
plt.title('CPIA public sector management and institutions cluster average ')
plt.xlabel('Year $\longrightarrow$',fontsize =10)
plt.ylabel('Value in Number $\longrightarrow$')
plt.legend(prop={'size': 13}, loc='center left', bbox_to_anchor=(1, .78)
                                                        ,fontsize='larger')
plt.show()

# Data Prepartion for 2nd line graph Plot
years_data_Mortality_rate = years.loc['Mortality rate,
                                       under-5 (per 1,000 live births)'
                                       , '2005':'2010']
years_data_Mortality_rate = years_data_Mortality_rate.dropna(axis=0)
years_data_Mortality_rate


years_data_Mortality_rate = years_data_Mortality_rate.dropna(axis=0)
years_data_Mortality_rate = years_data_Mortality_rate.loc[['Samoa','Zimbabwe'
                                                           ,'Bangladesh','Chad'
                                                           ,'Armenia'
                                                           ,'Georgia']
                                                           ,'2005':'2010']
# line graph Plot for 2nd indicator
import matplotlib
matplotlib.rc('figure', figsize=(8, 8))
years_data_Mortality_rate.T.plot( linestyle="--", marker='*'
                                 ,markersize=8,linewidth=1.5)
plt.title('Mortality rate, under-5')
plt.xlabel('Year $\longrightarrow$',fontsize =10)
plt.ylabel('Number per 1,000 live births $\longrightarrow$')
plt.legend(prop={'size': 13}, loc='center left',
           bbox_to_anchor=(1, .78),fontsize='larger')
plt.show()


#Group by clause for Data Manipulation
data_countrywise = data.groupby(['Country Name','Indicator Name']).mean()
data_countrywise
data_Indicator =
data_countrywise.iloc[data_countrywise.index.get_level_values('Indicator Name')
== 'CPIA public sector management and institutions cluster average
(1=low to 6=high)']
data_Indicator.loc[:,'2005':'2010'].mean()