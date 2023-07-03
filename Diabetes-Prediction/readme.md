# Laporan Proyek Machine Learning - Kayla Alysa Adra

## Domain Proyek
Domain digunakan pada *project* kali ini adalah **Kesehatan**

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
solusi yang akan dilakukan adalah dengan menerapkan 2 algoritma *machine learning* yakni:
* **KNN**
* **Random Forest**

**Algoritma K-Nearest Neighbor (KNN)** merupakan algoritma *machine learning* sederhana dan mudah diterapkan yang dapat digunakan untuk menyelesaikan masalah klasifikasi dan regresi. Algoritma ini termasuk dalam jenis *supervised learning*.
*KNN* adalah algoritma yang berfungsi untuk melakukan klasifikasi suatu data berdasarkan data pembelajaran (*train datasets*), yang diambil dari k tetangga terdekatnya (*nearest neighbors*). Dengan k merupakan banyaknya tetangga terdekat.


**Random Forest** adalah algoritma dalam *machine learning* yang digunakan untuk pengklasifikasian data dalam jumlah besar. Karena fungsinya bisa digunakan untuk banyak dimensi dengan berbagai skala dan performa yang tinggi. Klasifikasi ini dilakukan melalui penggabungan *tree* dalam *decision tree* dengan cara *training dataset*.

<br>

## Data Understanding
*Dataset* yang akan digunakan pada *project* kali ini adalah dataset [Diabetes](https://www.kaggle.com/datasets/johndasilva/diabetes) 

### Variabel-variabel pada dataset diabetes adalah sebagai berikut:
- *pregrancies* = jumlah kehamilan yang terjadi
- *glucose* = kadar gula pasien, yang normalnya berada diantara 80 dan 120 mg/dl
- *BloodPressure* = tekanan darah pasien
- *SkinThickness* = ketebalan kulit (dalam satuan mm)
- *insulin* = insulin
- *BMI* = *Body Mass Index* biasa digunakan untuk mendeteksi obesitas
- *Diabetes Pedigree Function (DPF)* = untuk menentukan kemungkinan diabetes pada seseorang berdasarkan riwayat keluarganya.
- *Age* = Usia

|   |Pregnancies|Glucose|BloodPressure|SkinThickness|Insulin|BMI|DiabetesPedigreeFunction|Age|Outcome|
|---|---|---|---|---|---|---|---|---|---|
|0|2|138|62|35|0|33\.6|0\.127|47|1|
|1|0|84|82|31|125|38\.2|0\.233|23|0|
|2|0|145|0|0|0|44\.2|0\.63|31|1|
|3|0|135|68|42|250|42\.3|0\.365|24|1|
|4|1|139|62|41|480|40\.7|0\.536|21|0|



*Outcome* yang akan dihasilkan adalah 1 dan 0 (*true* dan *false*). 

1. memeriksa data null

    setelah melakukan pengecekan, tidak ada data bernilai *NULL*.


2. memeriksa data *NaN Values*

    Setelah melakukan pemeriksaan, tidak ada data bernilai *NaN*.


3. *removing outliers*

    *Pregnancies*

    <img width="615" alt="Screen Shot 2023-06-27 at 03 09 58" src="https://github.com/kaylaalysa/diabetes-prediction/assets/91484757/d0163cc5-21aa-42ae-b039-0af72801e7f4">

    dalam data *Pregnancies*, ditemukan *outliers* dengan nilai lebih besar dari 12.5.

    dari gambar diatas, terdapat 3 titik yang merupakan *ouliers* dari data *Pregnancies*

    <br>

    *Glucose*

    <img width="627" alt="Screen Shot 2023-06-27 at 03 10 13" src="https://github.com/kaylaalysa/diabetes-prediction/assets/91484757/ce707078-1caf-4549-9126-72bb72c737ba">

    Untuk data *Glucose*, terdapat *outliers* bernilai 0.

    <br>

    *BloodPressure*

    <img width="631" alt="Screen Shot 2023-06-27 at 03 10 29" src="https://github.com/kaylaalysa/diabetes-prediction/assets/91484757/c1ba2838-712a-47e6-b0d8-02271058e36a">

    dalam data *BloodPressure* diatas, terdapat *outliers* yang nilainya lebih kecil dari 40 dan lebih besar dari 100.

    <br>

    *SkinThickness*

    <img width="609" alt="Screen Shot 2023-06-27 at 03 10 43" src="https://github.com/kaylaalysa/diabetes-prediction/assets/91484757/fff61440-4b7d-4326-9246-f20c296be0f0">

    untuk data *SkinThickness* terdapat *outliers* yang nilalinya lebih besar dari 60.

    <br>

    *Insulin*

    <img width="653" alt="Screen Shot 2023-06-27 at 03 10 59" src="https://github.com/kaylaalysa/diabetes-prediction/assets/91484757/b0050c2b-91f1-49f6-878b-cab7ae9d72fc">

    Untuk *Insulin*, terdapat cukup banyak *outliers* yang nilainya lebih besar dari 300.

    <br>

    *BMI*

    <img width="657" alt="Screen Shot 2023-06-27 at 03 11 23" src="https://github.com/kaylaalysa/diabetes-prediction/assets/91484757/9dc979f2-0c5f-47d0-9862-7e0e5688fd8f">

    Untuk *BMI*, terdapat cukup banyak *outliers* yang nilainya lebih  kecil dari 20 dan lebihbesar dari 50.

    <br>

    *DiabetesPedigreeFunction*

    <img width="647" alt="Screen Shot 2023-06-27 at 03 11 38" src="https://github.com/kaylaalysa/diabetes-prediction/assets/91484757/33973762-804c-4f56-b22f-8a6c5c3fb927">

    Untuk *DiabetesPedigreeFunction*, terdapat cukup banyak *outliers* yang nilainya lebih besar dari 1.25.

    <br>

    *Age*

    <img width="611" alt="Screen Shot 2023-06-27 at 03 11 51" src="https://github.com/kaylaalysa/diabetes-prediction/assets/91484757/f9a85e30-ad6d-43ad-a738-75f85b649ffb">

    Untuk *Age*, terdapat cukup banyak *outliers* yang nilainya lebih besar dari 65.


    jika dilihat dari beberapa visualisasi diatas, terlihat bahwa untuk beberapa variabel masih mengandung nilai yang *outliers*. maka dari itu, digunakan metode IQR untuk melakukkan *dropping* ( membuang data data yang *outliers* )

    dataset yang tadinya berbentuK (2000,9) menjadi (1652, 9)

    **Inter Quartile Range (IQR)** adalah metode yang saya gunakan untuk deteksi dan penghapusan *outlier*. Hal ini saya terapkan dengan menemukan kuartil pertama dan ketiga (Q1 dan Q3) kemudian menghitung nilai IQRnya dengan mengurangi Q3 dan Q1.



<br>

### **Univariate Analysis** 

*Univariate Analysis* merupakan teknik analisis data terhadap satu variabel secara mandiri.

seluruh data dalam dataset diabetes merupakan numerik

berikut ini merupakan hasil analisis univariate:

<img width="445" alt="Screen Shot 2023-07-03 at 20 04 36" src="https://github.com/kaylaalysa/diabetes-prediction/assets/91484757/2811808a-5144-47b5-a644-88e52fdf2e80">

* data pregrnancies paling banyak berada pada rentang 0-2
* rataa-rata tingkat glukosa pasien dalam dataset ini adalah 119.25
* BMI rata-rata pasien dalam dataset ini adalah 32.1 

<br>

### **Multivariate Analysis**

*Multivariate Analysis* menunjukkan hubungan antara 2 atau lebih fitur.

berikut ini merupakan hasil analisis multivariate:

<img alt="multivariate" src="https://github.com/kaylaalysa/diabetes-prediction/assets/91484757/f7a0aee0-f678-42ed-af37-9acccc9005f7">

Dari hasil visualisasi data diatas dapat disimpulkan bahwa:
* Pola sebaran data pada grafik diatas memiliki pola sebaran yang cukup merata. 


<br>

berikut ini merupakan hasil yang menunjukkan korelasi antar fitur:

<img width="877" alt="Screen Shot 2023-07-03 at 20 17 39" src="https://github.com/kaylaalysa/diabetes-prediction/assets/91484757/0ceb073d-4792-4412-99ba-f1d4b140f18c">

Dari hasil visualisasi diatas ditemukan bahwa:
* *Glucose* memiliki tingkat korelasi paling tinggi dengan *outcome*
* *SkinThickness* memiliki tingkat korelasi paling rendah dengan *outcome*



<br>

|   |Pregnancies|Glucose|BloodPressure|SkinThickness|Insulin|BMI|DiabetesPedigreeFunction|Age|Outcome|
|---|---|---|---|---|---|---|---|---|---|
|Pregnancies|1\.0|0\.1295545606754006|0\.1795756862738609|-0\.07253229760841676|-0\.1053398821148546|0\.023463822117350253|0\.030097379723195143|0\.5633863248457357|0\.23150667291857807|
|Glucose|0\.1295545606754006|1\.0|0\.21866615538641346|0\.03341730375974258|0\.27760826888618795|0\.18764471021381213|0\.06037507346589693|0\.2676513254817551|0\.5027186889656542|
|BloodPressure|0\.1795756862738609|0\.21866615538641346|1\.0|0\.07642431749572529|-0\.031761761419049225|0\.2784297872753935|0\.04027728955272792|0\.33940658432320564|0\.18656555593773316|
|SkinThickness|-0\.07253229760841676|0\.03341730375974258|0\.07642431749572529|1\.0|0\.48244677582722784|0\.4216900629677906|0\.13212595456259296|-0\.07464399362712587|0\.03712534164326731|
|Insulin|-0\.1053398821148546|0\.27760826888618795|-0\.031761761419049225|0\.48244677582722784|1\.0|0\.2116425495582916|0\.22013876887171666|-0\.0436745039216973|0\.10202343451258919|
|BMI|0\.023463822117350253|0\.18764471021381213|0\.2784297872753935|0\.4216900629677906|0\.2116425495582916|1\.0|0\.1346876954684569|0\.0651265862698683|0\.2507041588480941|
|DiabetesPedigreeFunction|0\.030097379723195143|0\.06037507346589693|0\.04027728955272792|0\.13212595456259296|0\.22013876887171666|0\.1346876954684569|1\.0|0\.058099912288044314|0\.1527819434713242|
|Age|0\.5633863248457357|0\.2676513254817551|0\.33940658432320564|-0\.07464399362712587|-0\.0436745039216973|0\.0651265862698683|0\.058099912288044314|1\.0|0\.2981854389966302|
|Outcome|0\.23150667291857807|0\.5027186889656542|0\.18656555593773316|0\.03712534164326731|0\.10202343451258919|0\.2507041588480941|0\.1527819434713242|0\.2981854389966302|1\.0|

Berikut ini merupakan hasil analisis dari tabel kolerasi diatas:

* dari hasil diatas, *glucose* atau kadar glukosa memiliki tingkat korelasi tertinggi (mendekati 1) . sehingga, dapat disimpulkan bahwa jika seseorang memiiliki kadar glukosa yang tinggi dalam dirinya maka lebih mudah terjangkit penyakit diabetes.

* bebeda dengan *glucose*, *SkinThickness* memiliki tingkat korelasi paling rendah. hal tersebut berarti *SkinThickness* bukan penyebab utama seseorang terjangkit penyakit diabetes

<br>

## Data Preparation
dalam tahap data preparation ini dilakukan
1. **Train test split**

    pada tahapan ini, kolom "Outcome" dijadikan target yang akan diprediksi.

    10% dari data akan digunakan sebagai data uji, sedangkan 90% akan digunakan sebagai data latih. 
2. **GridSearchCV** untuk menemukan parameter terbaik

    **GridSearchCV** adalah sebuah metode yang digunakan untuk melakukan pencarian parameter terbaik dalam sebuah model atau algoritma dengan menggunakan metode *grid search*. 

    *Grid search* adalah sebuah teknik yang digunakan untuk mencari kombinasi parameter terbaik yang menghasilkan performa atau skor model yang optimal.



## Modeling


### Algoritma
Algortima yang digunakan pada studi kasus kali ini adalah **K-Nearest Neighbor (KNN)** dan juga **Random Forest** . 

* K-Nearest Neighbor(KNN) bekerja dengan membandingkan jarak satu sampel ke sampel pelatihan lain dengan memilih sejumlah k tetangga terdekat.pada studi kasus kali ini, saya menggunakan 'from sklearn.neighbors import KNeighborsClassifier'. parameter yang digunakan adalah 'n_neighbors'

    *n_neighbors* = Parameter ini menentukan jumlah tetangga terdekat yang akan digunakan dalam proses klasifikasi atau regresi

* Random Forest bekerja dengan membangun banyak decision tree pada waktu pelatihan. pada studi kasus kali ini saya menggunakan f'rom sklearn.ensemble import RandomForestClassifier'. parameter yang digunakan adalah 'n_estimators' dan 'max_depth'

    *n_estimators* = jumlah pohon keputusan yang akan dibangun dalam *ensemble Random Forest*.

    *max_depth*= kedalaman maksimum setiap pohon keputusan dalam *Random Forest*.


Parameter yang digunakan untuk algoritma *KNN* adalah *n_neighbors* dan parameter yang digunakan untuk algoritma *Random Forest* adalah adalah *n_estimators* dan *max_depth*

setelah melakukan proses *GridSearchCV* ditemukan parameter yang baik untuk setiap algoritma yakni:

Algoritma *KNN* 
    
* *n_neighbors* =1

Algoritma *Random Forest*
* *n_estimators* = 500
* *max_depth* = 8

## Evaluation
Laporan klasifikasi akan mencakup beberapa metrik evaluasi untuk setiap kelas dalam masalah klasifikasi, seperti presisi (*precision*), *recall*, dan *f1-score*. Biasanya, laporan juga mencakup metrik agregat seperti akurasi dan rata-rata tertimbang dari metrik-metrik tersebut.

1. *Precision* (Presisi): *Precision* mengukur sejauh mana hasil positif yang diprediksi benar. Dalam konteks klasifikasi, *precision* mengacu pada persentase dari prediksi positif yang benar terhadap total prediksi positif. 

    Formula presisi adalah sebagai berikut:

$$Precision = \frac{{\text{True Positives}}}{{\text{True Positives} + \text{False Positives}}}$$


2. *Recall* (*Recall*): *Recall*, juga dikenal sebagai sensitivitas, mengukur sejauh mana model dapat menemukan kembali semua contoh positif yang sebenarnya. Dalam konteks klasifikasi, *recall* mengacu pada persentase contoh positif yang benar terhadap total contoh positif.

    Formula *recall* adalah sebagai berikut:

$$Recall = \frac{{\text{True Positives}}}{{\text{True Positives} + \text{False Negatives}}}$$


3. *F1-Score*: *F1-score* adalah rata-rata harmonik dari *precision* dan *recall*. Itu memberikan keselarasan antara kedua metrik ini. *F1-score* berguna ketika ingin menjaga keseimbangan antara *precision* dan *recall*.
*F1-score* dapat dihitung menggunakan formula berikut:


$$F1-Score = \frac{{2 *  (Precision \cdot Recall)}}{{Precision + Recall}}$$



4. *Support*: *Support* adalah jumlah contoh dalam setiap kelas yang muncul dalam dataset yang dievaluasi. Dalam laporan klasifikasi, *support* menunjukkan jumlah contoh aktual dalam setiap kelas.


**Classification_report untuk algoritma KNN**

  |             | precision|   recall  | f1-score  | support   |
  |-------------|----------|-----------|-----------|-----------|
  | 0           | 0.98     | 0.98      | 0.98      | 120       |
  | 1           | 0.96     | 0.96      | 0.96      | 46        |
  |accuracy     |          |           | 0.98      | 166       |
  |macro avg    | 0.97     | 0.97      | 0.97      | 166       |
  |weighted avg | 0.98     | 0.98      | 0.98      | 166       |



**Classification_report untuk algoritma Random Forest**

  |             | precision|   recall  | f1-score  | support   |
  |-------------|----------|-----------|-----------|-----------|
  | 0           | 0.95     | 0.97      | 0.96      | 120       |
  | 1           | 0.91     | 0.87      | 0.89      | 46        |
  |accuracy     |          |           | 0.94      | 166       |
  |macro avg    | 0.93     | 0.92      | 0.92      | 166       |
  |weighted avg | 0.94     | 0.94      | 0.94      | 166       |


Jika dilihat dari kedua *classification_report* diatas, **KNN** memiliki hasil yang lebih baik dibandingkan Random Forest dengan tingkat akurasi berada diatas 97% .

| Model                     | Accuracy  |
|---------------------------|-----------|
|KNeighborsClassifier       | 97.5904%  |
|RandomForestClassifier     | 93.9759%  |



<br>

Kesimpulan yang dapat diambil dari studi kasus diabetes ini adalah algoritma *KNN* lebih sesuai dan lebih baik dibandingkan algoritma *Random Forest* karena menghasilkan tingkat akurasi yang lebih baik, yakni lebih dari 97%

**Referensi:**

[1] "Kasus diabetes anak meningkat ‘sangat mengkhawatirkan’, imbas makanan-minuman manis 'mudah dijangkau' - 'regulasi belum cukup melindungi,' kata peneliti," BBC, 3 Juli 2023. [Online]. Available: https://www.bbc.com/indonesia/articles/clj6rene4y7o. [Accessed: 3 Juli 2023].

[2] "Diabetes," Halodoc, 2023. [Online]. Available: https://www.halodoc.com/kesehatan/diabetes. [Accessed: 3 Juli 2023].
