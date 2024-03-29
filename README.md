# Decision trees support the prediction of colorectal cancer in Vietnam

This is an experimental model using decision trees to support the prediction of colorectal cancer in Vietnam based on preclinical symptoms, helping to reduce costs and increase diagnosis speed.

## Features

- **Prediction API**: Provides an endpoint for predicting the likelihood of colorectal cancer based on input symptoms.
- **Data Saving API**: Allows saving patient symptoms and diagnostic results to a database.
- **Model Update API**: Enables updating the machine learning model with new data.

### Workflow User

- Import patient records (initial symptoms upon hospital admission).
- Automatically identify symptoms.
- Feature extraction from symptoms.
- Diagnosis prediction using decision tree models.

## Workflow Job

1. **Data Collection**: Import patient records containing initial symptoms upon hospital admission.
2. **Data Processing**: Automatically identify symptoms and preprocess them for model input.
3. **Model Prediction**: Utilize the machine learning model to predict the likelihood of colorectal cancer.
4. **Data Saving**: Store patient symptoms and diagnostic results in a database for future reference.
5. **Model Update**: Periodically update the machine learning model using new data to improve prediction accuracy.

## Sub-Projects

- **CART**:
- **RandomForest**:
- **XGBoost**:

## Prerequisites

- Python version: ~3.11

## Installation and Deployment

### 1. **Install Requirements**

```bash
pip install -r requirements.txt
```

### 2. **Train model**

```bash
py .\src\train.py
```

### 3. **Run the API module**

```bash
py .\src\api_module.py
```

### 4. **Access the APIs**

- Prediction API: <http://localhost:5000/api_predict>
- Data Saving API: <http://localhost:5000/api_save_data> - [Need database](#database)
- Model Update API: <http://localhost:5000/api_update_module> - [Need database](#database)

### 5. **Test demo**

The web demo by opening the [Web demo](.\web\index.html) file in a web browser.

## Sub-Modules

- `api_module.py` This module implements the Flask APIs for prediction, data saving, and model updates.
- `program_database.py` Provides functions for connecting to a database and inserting data.
- `utils.py`: Contains utility functions for symptom extraction and model management.

## Configuration [config.py](.\src\config.py)

The config.py file contains configuration settings used throughout the application:

- **PRIMARY_DATA_LINK**: Path to the primary dataset.
- **OUTPUT_LINK**: Path to the output Excel file.
- **FEATURES**: List of features used in the model.
- **KQ**: Target variable name.
- **DB_USERNAME**: Database username.
- **DB_PASSWORD**: Database password.
- **DB_HOST**: Database host.
- **DB_NAME**: Database name.
- **TABLE_NAME**: Name of the table in the database.
- **SAVE_MODEL_PATH**: Path to save trained model files.
- **SAVE_TREE_PATH**: Path to save decision tree images.
- **SAVE_LOG_PATH**: Path to save log files.
- **TEST_SIZE**: Size of the test dataset.
- **RAMDOM_STATE**: Random state for reproducibility.
- **N_ESTIMATORS**: Number of estimators for RandomForest.
- **MODEL_USE**: Type of model used (DecisionTree, RandomForest, or XGBoost)

## Data Handling [datasets.py](.\src\datasets.py)

The `datasets.py` file handles data fetching and preprocessing:

- Connects to the database.
- Fetches data from the specified table.
- Prepares features and target variables for model training.

## Data Interaction [program_database.py](.\src\program_database.py)

The `program_database.py` file manages interactions with the database:

- Connects to the database.
- Fetches data from the specified table.
- Inserts data into the specified table.

## Model Evaluation and Performance

- **Metrics**: Accuracy, Precision, Recall, F1 Score
- **Model Logging**: Log training and testing performance, elapsed time, hyperparameters, and other relevant information to track model performance over time.

## Database

### MySQL

To use the MySQL database, you need to create a new database and then import the data from the [data_ungthu.sql](.\dataset\data_ungthu.sql) file. The login information for the database is provided in the [config.py](.src\config.py) file.

- Here is the detailed structure and description of the database:

### Table Structure `trieu_chung_va_chuan_doan`

The `trieu_chung_va_chuan_doan` table stores information about symptoms and diagnosis results related to the likelihood of colorectal cancer.

|         Column Name         |  Data Type |
| :-------------------------: | ---------: |
|          dau_bung           | tinyint(1) |
|             non             | tinyint(1) |
|           chan_an           | tinyint(1) |
|           tao_bon           | tinyint(1) |
|           sut_can           | tinyint(1) |
|          tieu_chay          | tinyint(1) |
|         phan_co_mau         | tinyint(1) |
|      da_niem_mac_vang       | tinyint(1) |
|           da_sam            | tinyint(1) |
|      hoach_ngoai_bien       | tinyint(1) |
|       hach_thuong_don       | tinyint(1) |
|         bung_chuong         | tinyint(1) |
|     phan_ung_thanh_bung     | tinyint(1) |
|      cam_ung_phuc_mac       | tinyint(1) |
|       dau_hieu_ran_bo       | tinyint(1) |
|        quai_ruot_noi        | tinyint(1) |
|       so_thay_khoi_u        | tinyint(1) |
|  tham_truc_trang_co_khoi_u  | tinyint(1) |
|  chup_CT_o_bung_co_khoi_u   | tinyint(1) |
| noi_soi_dai_trang_co_khoi_u | tinyint(1) |
|       tien_su_ung_thu       | tinyint(1) |
|           ket_qua           | tinyint(1) |

Note: In the `ket_qua` column, the value 1 represents the presence of colorectal cancer, and the value 0 represents no cancer.

## Future Enhancements

- Implement additional machine learning algorithms for comparison.
- Enhance the user interface and data visualization capabilities.
- Incorporate advanced features such as anomaly detection and patient risk assessment.
