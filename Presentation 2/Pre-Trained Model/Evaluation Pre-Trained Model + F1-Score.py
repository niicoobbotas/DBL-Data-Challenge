import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\20243314\OneDrive - TU Eindhoven\Desktop\Quartile 4\DBL Data Challenge\Presentation 2\Pre-Trained Model\Evaluation Pre-Trained Model - Hoja 1.csv")

# Rename the columns for clarity
df.columns = ["ID", "Human", "Model"]

# Clean the sentiment labels (e.g., remove extra spaces, make capitalization consistent)
df["Human"] = df["Human"].str.strip().str.capitalize()
df["Model"] = df["Model"].str.strip().str.capitalize()

# === STEP 2: Generate classification report ===
# This will compute precision, recall, F1-score, and support per class
report = classification_report(df["Human"], df["Model"])
print("📊 Classification Report:\n")
print(report)

# === STEP 3: Generate and visualize confusion matrix ===
labels = ["Positive", "Neutral", "Negative"]
cm = confusion_matrix(df["Human"], df["Model"], labels=labels)

# Plot the confusion matrix as a heatmap
sns.heatmap(cm, annot=True, fmt="d", xticklabels=labels, yticklabels=labels, cmap="Blues")
plt.xlabel("Model Prediction")
plt.ylabel("Human Label")
plt.title("Confusion Matrix")
plt.tight_layout()
plt.show()
