import pandas as pd
import numpy as np

# Start coding here...
df = pd.read_csv("bank_marketing.csv")

# Check the columns in the dataframe
print(df.columns)

#Split
client =  df[["client_id", "age","job","marital",
             "education","credit_default","mortgage"]]
print(client)

campaign =  df[["client_id", "number_contacts","month","day",
             "contact_duration","previous_campaign_contacts","previous_outcome","campaign_outcome"]]
print(campaign)

economics =  df[["client_id", "cons_price_idx","euribor_three_months"]]
print(economics)


#client cleaning

## Clean Job column
client["job"] = client["job"].str.replace(".","_")
print(client["job"])

## Clean education column
client["education"] = client["education"].str.replace(".","_")
client["education"] = client["education"].str.replace("unknown","np.NaN")
print(client["education"])

##Clean and convert client columns to bool data type
client["credit_default"]  = client["credit_default"].apply(lambda x: 1 if str(x).strip().lower() == "yes" else 0).astype(bool)
print(client["credit_default"])

client["mortgage"]  = client["mortgage"].apply(lambda x: 1 if str(x).strip().lower() == "yes" else 0).astype(bool)
print(client["mortgage"])



## Editing the campaign dataset
##Clean and convert outcome columns to bool
# Change previous_outcome to binary values
campaign["previous_outcome"] = campaign["previous_outcome"].apply(lambda x : 1 if str(x).strip().lower() == "yes" else 0).astype(bool)
print(campaign["previous_outcome"] )

# Convert campaign_outcome to binary values
campaign["campaign_outcome"] = campaign["campaign_outcome"].apply(lambda x : 1 if str(x).strip().lower() == "success" else 0).astype(bool)
print(campaign["campaign_outcome"])

# Add year column
campaign["year"] = "2022"

# Convert day to string
campaign["day"] = campaign["day"].astype(str)

# Add last_contact_date column
campaign["last_contact_date"] = campaign["year"] + "-" + campaign["month"] + "-" + campaign["day"]

# Add last_contact_date column
campaign["last_contact_date"] = pd.to_datetime(campaign["last_contact_date"],format="%Y-%b-%d")
print(campaign["last_contact_date"])



#Save tables to csv files

client.to_csv("client.csv", index=False)
campaign.to_csv("campaign.csv", index=False)
economics.to_csv("economics.csv",index=False)
print(client)