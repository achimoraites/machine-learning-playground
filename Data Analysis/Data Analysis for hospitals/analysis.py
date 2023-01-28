import pandas as pd

pd.set_option('display.max_columns', 8)

general = pd.read_csv('data/general.csv')
prenatal = pd.read_csv('data/prenatal.csv')
sports = pd.read_csv('data/sports.csv')


general.drop(columns=['Unnamed: 0'], inplace=True)


prenatal.drop(columns=['Unnamed: 0'], inplace=True)
prenatal.rename(columns={'Sex': 'gender', 'HOSPITAL': 'hospital'}, inplace=True)

sports.drop(columns=['Unnamed: 0'], inplace=True)
sports.rename(columns={'Male/female': 'gender', 'Hospital': 'hospital'}, inplace=True)

hospitals = pd.concat([general, prenatal, sports], ignore_index=True)

# delete empty rows
hospitals.dropna(how='all', inplace=True)

# rename gender to 'f' and 'm'
hospitals['gender'].replace(['female', 'woman'], 'f', inplace=True)
hospitals['gender'].replace(['male', 'man'], 'm', inplace=True)
hospitals['gender'].fillna('f', inplace=True)

# fill nan's for bmi, diagnosis, blood_test, ecg, ultrasound, mri, xray, children, months
fill_with_zero_cols = ['bmi', 'diagnosis', 'blood_test', 'ecg', 'ultrasound', 'mri', 'xray', 'children', 'months']
fill_with_zero_dict = {key: 0 for key in fill_with_zero_cols}
hospitals = hospitals.fillna(fill_with_zero_dict)

# For checking the data
# print(f"Data shape: {hospitals.shape}")
# print(hospitals.sample(20, random_state=30))


# 1st question:
# Which hospital has the highest number of patients?
hospital_with_most_patients = hospitals['hospital'].mode()[0]
print(f"The answer to the 1st question is {hospital_with_most_patients}")

# 2nd question:
# What share of the patients in the general hospital suffers from stomach-related issues?
# Round the result to the third decimal place.
general_hospital = hospitals[hospitals['hospital'] == 'general']
general_hospital_stomach_issues = general_hospital[general_hospital['diagnosis'] == 'stomach']

print(f"The answer to the 2nd question is "
      f"{round(general_hospital_stomach_issues.shape[0] / general_hospital.shape[0], 3)}")

# 3rd question:
# What share of the patients in the sports hospital suffers from dislocation-related issues?
# Round the result to the third decimal place.
sports_hospital = hospitals[hospitals['hospital'] == 'sports']
dislocation_cases = sports_hospital.diagnosis.value_counts().loc['dislocation']
print(f"The answer to the 3rd question is "
      f"{round(dislocation_cases / sports_hospital.shape[0], 3)}")


# 4th question:
# What is the difference in the median ages of the patients in the general and sports hospitals?
general_hospital_median_age = general_hospital.age.median()
sports_hospital_median_age = sports_hospital.age.median()
print(f"The answer to the 4th question is "
      f"{abs(int(general_hospital_median_age - sports_hospital_median_age))}")


# 5th question:
# After data processing at the previous stages,
# the blood_test column has three values:
# t= a blood test was taken,
# f= a blood test wasn't taken,
# and 0= there is no information.
# In which hospital the blood test was taken the most often
# (there is the biggest number of t in the blood_test column among all the hospitals)?
# How many blood tests were taken?

hospitals_blood_tests = hospitals.pivot(columns="blood_test", values="hospital")['t'].dropna(how='all').value_counts()
hospital_with_most_blood_tests = hospitals_blood_tests

print(f"The answer to the 5th question is "
      f"{hospital_with_most_blood_tests.index[0]}, {hospital_with_most_blood_tests[0]} blood tests")