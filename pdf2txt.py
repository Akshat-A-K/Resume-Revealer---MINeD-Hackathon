import torch
from torch.utils.data import Dataset, DataLoader
from transformers import BertTokenizer, BertForSequenceClassification, AdamW
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Sample dataset - replace with your own labeled dataset
texts = [
    "Develop server-side logic and databases using Python.",
    "Experience with Java for web application development.",
    "Node.js proficiency for scalable server applications."
]

# Binary labels for each skill (1 if present, 0 if not)
labels = [[1, 0, 1], [1, 1, 0], [0, 0, 1]]

# Tokenize and encode text data
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
encoded_data = tokenizer(texts, return_tensors='pt', padding=True, truncation=True)

# Create DataLoader
class SkillsDataset(Dataset):
    def __init__(self, texts, labels):
        self.texts = texts
        self.labels = labels

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        return {'input_ids': self.texts['input_ids'][idx],
                'attention_mask': self.texts['attention_mask'][idx],
                'labels': torch.tensor(self.labels[idx])}

dataset = SkillsDataset(encoded_data, labels)
train_dataset, val_dataset = train_test_split(dataset, test_size=0.2, random_state=42)

train_dataloader = DataLoader(train_dataset, batch_size=3, shuffle=True)
val_dataloader = DataLoader(val_dataset, batch_size=3, shuffle=False)

# Model definition
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=3)  # Adjust num_labels based on your task

# Training loop
optimizer = AdamW(model.parameters(), lr=1e-5)

num_epochs = 5
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

for epoch in range(num_epochs):
    model.train()
    for batch in train_dataloader:
        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)
        labels = batch['labels'].long().to(device)  # Adjust data type if needed

        optimizer.zero_grad()
        outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
        loss = outputs.loss
        loss.backward()
        optimizer.step()

    # Validation
    model.eval()
    all_val_labels = []
    all_val_preds = []

    with torch.no_grad():
        for batch in val_dataloader:
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            labels = batch['labels'].long().to(device)  # Adjust data type if needed

            outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
            logits = outputs.logits
            preds = torch.sigmoid(logits)

            all_val_labels.append(labels.cpu().numpy())
            all_val_preds.append(preds.cpu().numpy())

    val_labels = torch.vstack(all_val_labels)
    val_preds = torch.vstack(all_val_preds)

    # Evaluation
    val_accuracy = accuracy_score(val_labels, (val_preds > 0.5).astype(int))
    print(f"Epoch {epoch + 1}/{num_epochs}, Validation Accuracy: {val_accuracy}")

# Now you would use the trained model for predictions on new data
