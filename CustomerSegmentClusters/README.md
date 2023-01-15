# Customer Segment Clusters
Using data on the general population identify the core customer base for a mail-order sales company in Germany.

Must give credit to Arvato for the data. Since the terms and conditions prohibited us from keeping the data, no data is provided in this repository.

## 📓 Files used

- `Udacity_AZDIAS_Subset.csv`: Demographic data for the general population of Germany.
- `Udacity_CUSTOMERS_Subset.csv`: Demographic data for customers of a mail-order company.
- `Data_Dictionary.md`: Information file about the features in the provided datasets.
- `AZDIAS_Feature_Summary.csv`: Summary of feature attributes for demographic data.
- `Identify_Customer_Segments.ipynb`: Jupyter Notebook divided into sections and guidelines for completing the project. The notebook provides more details and tips than the outline given here.


## 🥼 Results

### Started with the data exploration and data preprocessing
- Cleaned the data
- Performed feature engineering
- Applied feature scaling (very important for distance based algorithms)

### Performed PCA (Principal Component Analysis) for dimentionality reduction
- Had 69 features
- Kept 30 features that can explain the 88.51% of variabillity.
- Investigated the top 3 components

### Clustering
 - Analysed the data and decided to use 11 clusters based on the analysis results
 - Used KMEANS

### Compared the customer data with the general population data

**The most popular segments with the company** are the clusters 5 and 9, that is associated with males that
- have a financial typology of a low financial interest
- have been involved with the environmental sustainability in their youth and were influnced by the movement of their youth.

**The less popular segments with the company** are clusters 6 and 8 that are associated with individuals that have a personality typologies of
- culture and family-minded
- rational and dutiful

## 👏 Credits
Must give credit to Arvato for the data. Since the terms and conditions prohibited us from keeping the data, no data is provided in this repository.