# -*- coding: utf-8 -*-
"""Diabetes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1U-XjSoT_aFIZVUjJzEPCdo1dZ48HLuC-

# Prediksi Diabetes

## Domain Proyek
Domain yang saya gunakan pada project kali ini adalah **Kesehatan**

Ikatan Dokter Anak Indonesia (IDAI) sebelumnya merilis data yang menunjukkan bahwa prevalensi anak penderita diabetes meningkat 70 kali lipat pada Januari 2023 dibanding 2010.

Selain itu, Direktur Utama Badan Penyelenggaraan Jaminan Sosial (BPJS) Kesehatan Ali Ghufron juga mengatakan pasien anak yang menderita diabetes meningkat sekitar 1.000 kasus pada 2022 dibandingkan 2018.

diabetes dikhawatirkan dapat menimbulkan penyakit komplikasi lanjutan seperti Penyakit kardiovaskular, Kerusakan mata (retinopati), Kerusakan saraf (neuropati), kerusakan ginjal, disfungsi seksual, hingga keguguran sebagai komplikasinya.
masalah yang harus diselesaikan ialah bagaimana caranya pasien dapat memprediksi dini penyakit diabetes yang dideritanya guna mengurangi penyakit komplikasi lanjutan tersebut


<br>

## Business Understanding

### Problem Statements
1. Bagaimana Pengaruh kadar gula,tekanan darah, ketebalan kulit terhadap penderita diabetes?
2. bagaimana pengaruh berat badan terhadap penderita diabetes?
3. bagaimana pengaruh ibu hamil terhadap penderita diabetes?

### Goals
1. mengetahui hubungan kadar gula, tekanan darah, dan ketebalan kulit terhadap penyakit diabetes
2. mengetahui pengaruh berat badan terhadap resiko terkena penyakit diabetes
3. mengetahui resiko terkena penyakit diabetes ketika hamil

### Solution statements
solusi yang akan dilakukan adalah dengan menerapkan 2 algoritma machine learning yakni:
* **KNN**
* **Random Forest**

**Algoritma K-Nearest Neighbor (KNN)** merupakan algoritma machine learning sederhana dan mudah diterapkan yang dapat digunakan untuk menyelesaikan masalah klasifikasi dan regresi. Algoritma ini termasuk dalam jenis supervised learning.
KNN adalah algoritma yang berfungsi untuk melakukan klasifikasi suatu data berdasarkan data pembelajaran (train data sets), yang diambil dari k tetangga terdekatnya (nearest neighbors). Dengan k merupakan banyaknya tetangga terdekat.


**Random Forest** adalah algoritma dalam machine learning yang digunakan untuk pengklasifikasian data set dalam jumlah besar. Karena fungsinya bisa digunakan untuk banyak dimensi dengan berbagai skala dan performa yang tinggi. Klasifikasi ini dilakukan melalui penggabungan tree dalam decision tree dengan cara training dataset.
"""

from google.colab import drive
drive.mount('/content/drive')

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# %matplotlib inline
import seaborn as sns

diabetes = pd.read_csv("/content/drive/MyDrive/Bangkit 2023/diabetes-prediction/diabetes.csv")
diabetes.head()

"""## Data Understanding
Dataset yang akan digunakan pada project kali ini adalah dataset [Diabetes](https://www.kaggle.com/datasets/johndasilva/diabetes)

### Variabel-variabel pada dataset diabetes adalah sebagai berikut:
- pregrancies = jumlah kehamilan yang terjadi
- glucose = kadar gula pasien, yang normalnya berada diantara 80 dan 120 mg/dl
- BloodPressure = tekanan darah pasien
- SkinThickness = ketebalan kulit (dalam satuan mm)
- insulin = insulin
- BMI = Body Mass Index biasa digunakan untuk mendeteksi obesitas
- Diabetes Pedigree Function (DPF) = untuk menentukan kemungkinan diabetes pada seseorang berdasarkan riwayat keluarganya.
- Age = Usia
"""

diabetes.shape

diabetes.info()

"""### Handling Outliers"""

diabetes.isnull().sum()

diabetes.isna().sum()

sns.boxplot(x=diabetes['Pregnancies'])

sns.boxplot(x=diabetes['Glucose'])

sns.boxplot(x=diabetes['BloodPressure'])

sns.boxplot(x=diabetes['SkinThickness'])

sns.boxplot(x=diabetes['Insulin'])

sns.boxplot(x=diabetes['BMI'])

sns.boxplot(x=diabetes['DiabetesPedigreeFunction'])

sns.boxplot(x=diabetes['Age'])

Q1 = diabetes.quantile(0.25)
Q3 = diabetes.quantile(0.75)
IQR=Q3-Q1
diabetes=diabetes[~((diabetes<(Q1-1.5*IQR))|(diabetes>(Q3+1.5*IQR))).any(axis=1)]

# checking dataset after droping outliers
diabetes.shape

sns.catplot(x="Outcome",data=diabetes, kind="count");



"""## Univariate Analysis"""

diabetes.hist(figsize=(10,10),bins=50, xlabelsize=5, ylabelsize=5)
plt.show()

"""## Multivariate Analysis"""

# Mengamati hubungan antar fitur numerik dengan fungsi pairplot()
sns.pairplot(diabetes, diag_kind = 'kde')

correlations = diabetes.corr(method = 'pearson')
type(correlations)
correlations

sns.heatmap(diabetes.corr(), linewidths = 1);

"""## Data Preparation
dalam tahap data preparation ini dilakukan
1. Train test split

    pada tahapan ini, kolom "Outcome" dijadikan target yang akan diprediksi.

    10% dari data akan digunakan sebagai data uji, sedangkan 90% akan digunakan sebagai data latih.
2. **GridSearchCV** untuk menemukan parameter terbaik

    **GridSearchCV** adalah sebuah metode yang digunakan untuk melakukan pencarian parameter terbaik dalam sebuah model atau algoritma dengan menggunakan metode grid search.

    Grid search adalah sebuah teknik yang digunakan untuk mencari kombinasi parameter terbaik yang menghasilkan performa atau skor model yang optimal.

### Train test split
"""

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report,mean_squared_error

X = diabetes.drop(["Outcome"],axis =1)
y = diabetes["Outcome"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 123)

"""### GridSearchCV"""

from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

models = [
    {
        'name': 'KNN',
        'model':KNeighborsClassifier() ,
        'parameters': {
            'n_neighbors': range(1,20)
        }
    },
    {
        'name': 'Random Forest',
        'model': RandomForestClassifier(),
        'parameters': {
            'n_estimators': [10, 500, 1000],
            'max_depth': [2, 5, 8]
        }
    }
]

for model in models:
    grid_search = GridSearchCV(estimator=model['model'], param_grid=model['parameters'], cv=5)
    grid_search.fit(X_train, y_train)

    best_params = grid_search.best_params_
    best_score = grid_search.best_score_

    print(f"Best parameters for {model['name']}: {best_params}")
    print(f"Best score for {model['name']}: {best_score}\n")

"""## Modeling


### Algoritma
Algortima yang digunakan pada studi kasus kali ini adalah **K-Nearest Neighbor (KNN)** dan juga **Random Forest** .

* K-Nearest Neighbor(KNN) bekerja dengan membandingkan jarak satu sampel ke sampel pelatihan lain dengan memilih sejumlah k tetangga terdekat.pada studi kasus kali ini, saya menggunakan from sklearn.neighbors import KNeighborsClassifier. parameter yang digunakan adalah 'n_neighbors'

    *n_neighbors* = Parameter ini menentukan jumlah tetangga terdekat yang akan digunakan dalam proses klasifikasi atau regresi

* Random Forest bekerja dengan membangun banyak decision tree pada waktu pelatihan. pada studi kasus kali ini saya menggunakan from sklearn.ensemble import RandomForestClassifier. parameter yang digunakan adalah 'n_estimators' dan 'max_depth'

    *n_estimators* = jumlah pohon keputusan yang akan dibangun dalam ensemble Random Forest.

    *max_depth*= kedalaman maksimum setiap pohon keputusan dalam Random Forest.
"""

knn = KNeighborsClassifier(n_neighbors=1)
knn_model = knn.fit(X_train, y_train)
knn_model

y_pred = knn_model.predict(X_test)
accuracy_score(y_test, y_pred)

confusion_matrix(y_test, y_pred)
print(classification_report(y_test, y_pred))

"""### Random Forest"""

rf = RandomForestClassifier(max_depth=8, n_estimators=1000).fit(X_train, y_train)
y_pred = rf.predict(X_test)
accuracy_score(y_test, y_pred)

confusion_matrix(y_test, y_pred)
print(classification_report(y_test, y_pred))

"""## Evaluation"""

models = [
    knn,
    rf

]


for model in models:
    name = model.__class__.__name__
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print("-"*28)
    print(name + ":" )
    print("Accuracy: {:.4%}".format(accuracy))

result = []

results = pd.DataFrame(columns= ["Models","Accuracy"])

for model in models:
    name = model.__class__.__name__
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    result = pd.DataFrame([[name, accuracy*100]], columns= ["Models","Accuracy"])
    results = results.append(result)


sns.barplot(x= 'Accuracy', y = 'Models', data=results, color='g')
plt.xlabel('Accuracy Rate %')
plt.title('Models Accuracy');
