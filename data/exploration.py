import matplotlib.pyplot as plt
import pandas as pd

from data_loader import DataLoader

data = DataLoader()

# =============================================================================
# PLOT UNDERLYING CLASS DISTRIBUTIONS
# =============================================================================

df_train = data.df_train.merge(data.labels, left_on='label', right_index=True)
df_train = df_train.sort_index()

freq_labels = df_train.groupby('labels').count()[['label']]
freq_labels = freq_labels.rename(columns={'label': 'count'})
freq_labels = freq_labels.sort_values(by='count', ascending=False)
print(freq_labels.head())

freq_labels.head(50).plot.bar(figsize=(15,10))
plt.xticks(rotation=90);
plt.xlabel("Cars");
plt.ylabel("Count");

plt.show()

# =============================================================================
# TEST DATA LOADER IF IT EVENS OUT THE CLASS DISTRIBUTION THROUGH OVERSAMPLING
# =============================================================================

ds = data.get_pipeline()
labels = []
for _, label_batch in ds.take(300):
    labels.extend(label_batch.numpy())
labels = pd.Series(labels)
label_dict = data.labels.to_dict()['labels']
df = labels.map(label_dict)
df_freq_labels = df.value_counts()
print(df_freq_labels.head())


df_freq_labels.head(50).plot.bar(figsize=(15,10))
plt.xticks(rotation=90);
plt.xlabel("CARS");
plt.ylabel("Count");

plt.show()

