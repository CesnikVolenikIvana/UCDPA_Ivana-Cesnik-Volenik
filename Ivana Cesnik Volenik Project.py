#importing all neccessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings
#supressing all the  warnings
warnings.filterwarnings("ignore")
#getting my working directory
os.getcwd()

#defining the function I will use during my data analysis later on
def percentage(a,b):
    return round(a / b * 100, 2)


#importing my chosen cvs file
coffee_shop = pd.read_csv(r'file:///C:/Users/nicht/Documents/base_dataset.csv')

#DATA INSPECTION
#checking first 5 rows of my dataset
print(coffee_shop.head())
#expanding the output display to see all Data Frame columns
pd.set_option('display.max_columns', 14)
#displaying top and bottom 5 rows
print(coffee_shop.head())
print(coffee_shop.tail())
#number of rows and columns
print(coffee_shop.shape)
#I want to know name of columns in this dataset
print(coffee_shop.columns)
#showing info on each of the columns
print(coffee_shop.info())
#calculation of few summary statistics for each column
print(coffee_shop.describe())
#checking the level of the dataset that is the primary key
print(len(coffee_shop.id.unique()))

#DATA CLEANING
#checking is there any missing values
print(coffee_shop.isnull().sum())
#replacing values in column with mean and displaying to see was mean added as missing value
coffee_shop["competitor_satisfaction"].fillna(coffee_shop["competitor_satisfaction"].mean(), inplace=True)
print(coffee_shop.isnull().sum())
#checking is there any duplicates in my dataset
print(coffee_shop.duplicated())
drop_duplicates = coffee_shop.drop_duplicates()
print(coffee_shop.shape,drop_duplicates.shape)
#unique values in beverage_preference column
print(coffee_shop.beverage_preference.unique())
print(type(coffee_shop.beverage_preference.unique()))
#replacing multiple values in dataframe with dictionary of different replacement passed as an argument
coffee_shop = coffee_shop.replace({'beverage_preference': {"cffee":"coffee", "coffeee":"coffee",
        "cfofee":"coffee","cofefe":"coffee", "cofee":"coffee", "coffe":"coffee"}})
coffee_shop = coffee_shop.replace({'beverage_preference' : {"te":"tea", "ta":"tea", "tae":"tea"}})
coffee_shop = coffee_shop.replace({'beverage_preference' : {"bee" : "beer", "ber" : "beer", "bere":"beer"}})
coffee_shop = coffee_shop.replace({'beverage_preference': {"sod":"soda", "sda":"soda", "soad":"soda",
        "soa":"soda", "sdoa":"soda"}})
coffee_shop = coffee_shop.replace({'beverage_preference': {"wter":"water", "watre":"water", "wate":"water",
        "waetr":"water", "wtaer":"water", "watr":"water", "waer":"water"}})
coffee_shop = coffee_shop.replace({'beverage_preference': {"wter":"wine", "wien":"wine", "wie":"wine",
        "wnie":"wine", "wne":"wine", "win":"wine"}})
#checking values in column again
print(coffee_shop.beverage_preference.unique())
#unique values in owns_coffee_machine column
print(coffee_shop.owns_coffee_machine.unique())
#replacing multiple values with dictionary of different replacement passed as an argument
coffee_shop = coffee_shop.replace({'owns_coffee_machine': {"YES":"Yes", "y":"Yes", "yup":"Yes",
        "yes":"Yes", "ya":"Yes"}})
coffee_shop = coffee_shop.replace({'owns_coffee_machine': {"nope":"No", "no":"No", "nah":"No",
        "n":"No", "NO":"No"}})
coffee_shop = coffee_shop.replace({'owns_coffee_machine': {"dunno":"I don't know"}})
print(coffee_shop.owns_coffee_machine.unique())
print(coffee_shop.employment.unique())
coffee_shop = coffee_shop.replace({'employment': {"fll-time":"full-time", "full-tie":"full-time",
        "fll-time":"full-time","ful-time":"full-time", "fulltime":"full-time", "full-tiem":"full-time",
        "ful-ttime":"full-time","fullt-ime":"full-time","flul-time":"full-time","full-itme":"full-time",
        "full-tmie":"full-time","full-tim":"full-time","full-ime":"full-time", "full-tme":"full-time",
        "ful-ltime":"full-time"}})
coffee_shop = coffee_shop.replace({'employment': {"part-tim":"part-time", "part-tie":"part-time",
        "pat-time":"part-time","part-tmie":"part-time", "part-ime":"part-time", "parttime":"part-time",
        "patr-time":"part-time","partt-ime":"part-time","prat-time":"part-time","par-itme":"part-time",
        "part-tiem":"part-time","part-itme":"part-time","par-ttime":"part-time","part-tme":"part-time",
        "par-time": "part-time"}})
coffee_shop = coffee_shop.replace({'employment': {"studen":"student", "stuent":"student",
        "stuednt":"student","studetn":"student", "studet":"student", "stduent":"student",
        "studnt":"student","sudent":"student","sutdent":"student","stdent":"student",
        "studnet":"student"}})
coffee_shop = coffee_shop.replace({'employment': {"unemployde":"unemployed", "uneployed":"unemployed",
        "unemplyed":"unemployed","uenmployed":"unemployed", "unmployed":"unemployed", "unempolyed":"unemployed",
        "unemlpoyed":"unemployed","unempoyed":"unemployed","uemployed":"unemployed", "unemployd":"unemployed",
        "unemplyoed":"unemployed", "unemploye":"unemployed", "unemploed":"unemployed","unepmloyed":"unemployed",
        "unemploeyd":"unemployed","unemloyed":"unemployed"}})
coffee_shop = coffee_shop.replace({'employment': {"rtired":"retired", "retred":"retired",
        "retird":"retired","retierd":"retired", "rteired":"retired", "retried":"retired",
        "retied":"retired","reitred":"retired","reired":"retired"}})
print(coffee_shop.employment.unique())
#checking values in other columns
print(coffee_shop.owns_car.unique())
print(coffee_shop.state.unique())
print(coffee_shop.dob.unique())
#changing the format of "dob" column
coffee_shop['dob'] = pd.to_datetime(coffee_shop.dob)
coffee_shop.sort_values(["dob"], inplace=True, ascending=False)
print(coffee_shop["dob"])
#filtering rows from data frame
coffee_shop1 = coffee_shop[(coffee_shop['dob'] > '2022-01-01') & (coffee_shop['dob'] < '2070-12-30')]
print(coffee_shop1["dob"].tail())
print(coffee_shop[["dob"]].max())
print(coffee_shop[["dob"]].min())
#droping filtered rows
coffee_shop = coffee_shop.drop(coffee_shop[(coffee_shop['dob'] > '2022-01-01') &
             (coffee_shop['dob'] < '2070-12-30')].index)
#checking how my dataset looks like now
print(coffee_shop.head())
print(coffee_shop.shape)
print(coffee_shop[["dob"]].max())
print(coffee_shop[["dob"]].min())
#changing column values to integers-passed list with column names as an argument
columns = ["competitor_satisfaction","bought_coffee", "owns_car", "owns_home","number_of_bags_purchased_competitor"]
for col in columns:
    coffee_shop[col] = coffee_shop[col].apply(lambda x: int(x) if x == x else "")
#checking my data set again to see type of values through columns
print(coffee_shop.info())
#subsetting columns to create new data frame
coffee_dmgf = coffee_shop[["id", "dob", "city", "gender", "employment"]]
coffee_pref = coffee_shop[["id", "beverage_preference","number_of_bags_purchased_competitor",
                           "competitor_satisfaction","bought_coffee"]]
#merging two new tables (data frames)
clean_coffee_shop = coffee_dmgf.merge(coffee_pref, on="id")
print(clean_coffee_shop.head())
print(clean_coffee_shop.shape)
#setting column as an index in new Data Frame
clean_coffee_shop_srt = clean_coffee_shop.set_index("id").sort_index()
print(clean_coffee_shop_srt.head())

#MY QUESTIONS AND DATA VISUALIZATION
#Question no 1-What is gender distribution in my dataset?
#Index has been set so loc can be used to slice my data
gender_data = clean_coffee_shop_srt.loc[:, "gender"].value_counts()
print(gender_data)
#displaying gender distribution in my dataset
female_percentage = percentage(15507,28657)
print(female_percentage)
my_colors = "red","blue"
fig,ax = plt.subplots()
gender_data.plot(kind="bar",color=my_colors, width=0.8)
ax.set_title("Coffee_shop distribution by gender")
plt.xticks(rotation=0)
fig.set_size_inches([5,3])
plt.savefig("Dataset distribution by gender.png",dpi=300)
plt.show()

#Question no 2-What is the most popular beverage among customers?
beverage_pref_dist = clean_coffee_shop_srt[["beverage_preference"]].value_counts()
labels = ("Coffee", "Tea","Water", "Wine","Soda")
fig,ax = plt.subplots()
beverage_pref_dist.plot(kind="bar",color='blue',width=0.8)
ax.xaxis.set(ticklabels=["Coffee","Beer","Tea","Water","Wine", "Soda"])
ax.set(ylabel="Number of Customers", title="Beverage preference by customers")
plt.savefig("Beverage preference.png", bbox_inches='tight')
plt.show()
#Percentage distribution of specific beverage preference with defined function through numpy array
beverage_percentage = np.array([["coffee",percentage(14202,28657)],
            ["beer",percentage(4221,28657)],
             ["wine",percentage(3154,28657)],
             ["water",percentage(2683,28657)],
             ["soda",percentage(2217,28657)],
            ["tea",percentage(2180,28657)]])
print(beverage_percentage)

#Question no 3-What are the locations where customers purchased coffee bags with competitor the most?
competitor_coffee_purchase_vs_city = \
    clean_coffee_shop_srt.groupby(["city"]).agg({"number_of_bags_purchased_competitor":"sum"})
print(competitor_coffee_purchase_vs_city)
competitor_coffee_purchase_vs_city.plot(kind="bar", color="purple")
plt.xlabel("City")
plt.xticks(rotation=45)
plt.title("Number of coffee bags purchased with competitor by city")
plt.savefig("Number of coffee bags purchased with competitor by city.png")
plt.show()

#Question no 4-What are the locations where customers purchased our coffee bags the most?
coffee_bought_vs_city = clean_coffee_shop_srt.groupby(["city"]).agg({"bought_coffee":"count"})
print(coffee_bought_vs_city)
coffee_bought_vs_city.plot(kind="bar", color="green")
plt.xlabel("City")
plt.xticks(rotation=45)
plt.title("Number of coffee bags purchased by city")
plt.savefig("Number of coffee bags purchased by city.png")
plt.show()

#Question no 5-What is average distribution of bought coffee by gender?
sns.set_style("whitegrid")
sns.set_palette("RdBu")
sns.catplot(x="gender",y="bought_coffee",
            kind="bar",
            data=clean_coffee_shop_srt)
plt.title("Average distribution of bought coffee by gender")
plt.savefig("Average distribution of bought coffee by gender.png")
plt.show()

#Question no 6-Competitior satisfaction scores distribution (What is the avarage score?)
median = (clean_coffee_shop_srt["competitor_satisfaction"]).median()
mean = (clean_coffee_shop_srt["competitor_satisfaction"]).mean()
print(mean)
sns.set(color_codes=True)
fig, ax = plt.subplots()
sns.distplot(clean_coffee_shop_srt["competitor_satisfaction"],ax=ax)
ax.set(xlabel="Competitor satisfaction", ylabel="Scores", title="Competitor satisfaction")
ax.axvline(x=median, color="m", label="Median", linestyle="--")
ax.axvline(x=mean,color="b", label="Mean", linestyle="-")
ax.legend()
plt.savefig("Competitor satisfaction.png")
plt.show()

#Question no 7-Competitor satisfaction by employment and gender
g = sns.catplot(x="employment",y="competitor_satisfaction",
            data=clean_coffee_shop_srt, hue="gender",
            kind="box")
g.fig.suptitle("Competitor satisfaction by employment and gender")
g.fig.subplots_adjust(top=0.9)
g.set_axis_labels("Employment", "Competitor satisfaction")
plt.savefig("Competitor satisfaction by employment and gender.png")
plt.show()

