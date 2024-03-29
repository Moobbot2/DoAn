from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib
from datasets import X, Y

# Chia dữ liệu thành tập huấn luyện và tập kiểm thử
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Tạo và huấn luyện mô hình Random Forest trên tập huấn luyện
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train, y_train)

# Dự đoán trên tập kiểm thử
y_pred_rf = rf_classifier.predict(X_test)

# Tính các độ đo
accuracy_rf = accuracy_score(y_test, y_pred_rf)
precision_rf = precision_score(y_test, y_pred_rf)
recall_rf = recall_score(y_test, y_pred_rf)
f1_rf = f1_score(y_test, y_pred_rf)

# In kết quả
print(f'Random Forest Classifier:')
print(f'Accuracy: {accuracy_rf:.4f}')
print(f'Precision: {precision_rf:.4f}')
print(f'Recall: {recall_rf:.4f}')
print(f'F1 Score: {f1_rf:.4f}')

# Lưu mô hình Random Forest vào một tệp
joblib.dump(rf_classifier, 'output_tree/random_forest_model_6_4.joblib')

# loaded_rf_model = joblib.load('output_tree/random_forest_model.joblib')
