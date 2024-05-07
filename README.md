# XÂY DỰNG MÔ HÌNH DỰ ĐOÁN NGUYÊN NHÂN GÂY SẠT LỞ ĐẤT.

## Thông tin môn học
* **Môn học:** Phân tích và trực quan dữ liệu .
* **Lớp:** DS105.M11.
* **Năm học:** HKI NH 2021-2022.
* **Giảng viên:** ThS. Phạm Thế Sơn.

## Thông tin nhóm
STT | Họ tên | MSSV | Github
--- | -------|------|--------
1 | Nguyễn Thị Minh Phương | 19522065 | https://github.com/minhphuongzzz
2 | Chu Hà Thảo Ngân | 19521882 | https://github.com/thaongan251
3 | Thái Minh Triết | 19522397 | https://github.com/triet2397

### PIPELINE

![img](https://lh3.googleusercontent.com/Lzbxq67V6Kdu1iDZM6H9fgPJB0OiZOToWvYRZtvcyNkI0QEtjUoGHfjukGMWhPrCOmoSHk84gC9M8tN9sP_n0FRuq2Ry59giv9quuHrIdTksvOAi-7vmOXxlwnZw7L5KWc8kQRR2Cpfa)

### 1. Dataset

Source code: [here](https://github.com/minhphuongzzz/DS105-final-project/blob/main/src/data_collection.ipynb)

- Bộ dữ liệu gốc: *Global Landslide Catalog* 

  Nguồn: [here](https://data.nasa.gov/Earth-Science/Global-Landslide-Catalog-Export/dd9e-wu2v)

- Dữ liệu thu thập thêm:

  -  [Thời tiết](https://www.visualcrossing.com/weather-api)
  -  [Độ cao](https://developers.airmap.com/docs/elevation-api)
  -  [Châu lục](https://pypi.org/project/pycountry-convert/)
  -  [Mùa](https://www.nationalgeographic.org/encyclopedia/season/)
  -  [Mật độ dân số](https://sedac.ciesin.columbia.edu/data/set/gpw-v4-population-density-rev11/)
  -  [Độ che phủ rừng](https://data.globalforestwatch.org/documents/134f92e59f344549947a3eade9d80783/e%20xplore/)
  -  [Kết cấu của đất](https://developers.google.com/earth%02engine/datasets/catalog/OpenLandMap_SOL_SOL_TEXTURE%02CLASS_USDA-TT_M_v02)

### 2. Data preprocessing

Source code: [here](https://github.com/minhphuongzzz/DS105-final-project/blob/main/src/data_preprocessing.ipynb)

Các bước tiền xử lý bao gồm: xử lý các thuộc tính dạng *datetime*, loại bỏ các cột chứa thông tin không cần thiết, và xử lý missing values.

### 3. EDA

Source code: [here](https://github.com/minhphuongzzz/DS105-final-project/blob/main/src/EDA.ipynb)

Các bước phân tích thăm dò bao gồm: thống kê mô tả, phân tích trực quan dữ liệu theo thời gian (time series), phân tích tổng hợp thuộc tính, phân tích trực quan trên bản đồ địa lý.

### 4. Feature selection, Feature engineering and Model development

Source code: [here](https://github.com/minhphuongzzz/DS105-final-project/blob/main/src/model_development.ipynb)

#### Feature selection

Các thuộc tính được lựa chọn để đưa vào mô hình dựa vào kết quả sau khi phân tích thăm dò, kết hợp với hai phương pháp thống kê là *One way ANOVA* và *Chi-square test*.

#### Feature engineering

Các kỹ thuât để biến đổi dữ liệu trước khi đưa vào mô hình bao gồm: kết hợp các nhóm thuộc tính có độ tương quan cao, kết hợp và mã hóa các cột chứa thông tin mô tả (text description), mã hóa one-hot cho các thuộc tính phân loại, và feature scaling.

#### Model development

Bài toán: dự đoán quy mô sạt lở đất (*landslide size*).

Biến mục tiêu bị mất cân bằng (imbalanced class), nên chúng tôi sử dụng kỹ thuật *ADASYN* để oversampling cho các lớp có ít dữ liệu hơn nhằm xử lý vấn đề mất cân bằng trước khi đưa vào mô hình huấn luyện.

Mô hình phân lớp: Logistic Regression, Support Vector Machine, Random  Forest và PassiveAggressiveClassifier.

Độ đo đánh giá: macro F1-score và accuracy.

Sau khi thử nghiệm và đánh giá, chúng tôi tinh chỉnh siêu tham số cho mô hình đang có được kết quả tốt nhất và thu được kết quả sau:

![img](https://lh3.googleusercontent.com/_ur1jZhgcSfCbiETV91lvRAer_DoKhItTmsPIXSQkiYC4Kq8GLsHWQdoWLsHBTJ8WknQ_PlOsazzeAIfYqaIcfjCoPPRWfb53DZD7tT_f3kdKUbnddhqFsw1kGl7v8ZNEHPTJX6Hru-t)
