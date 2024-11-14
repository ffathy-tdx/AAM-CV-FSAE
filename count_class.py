import os

base_path = "F:/Work/Projects/AAM CV w2/FSOCO-12"
folders = ["train", "valid", "test"]
class_counts = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}  # adjust dictionary if you expect other IDs

for folder in folders:
    label_dir = os.path.join(base_path, folder, "labels")
    for root, _, files in os.walk(label_dir):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    for line in f:
                        parts = line.split()
                        if len(parts) > 0:
                            class_id = int(parts[0])
                            if class_id == 4:
                                print(f"Warning: Found class_id 4 in file {file_path}")
                        if class_id in class_counts:
                            class_counts[class_id] += 1
                        else:
                            class_counts[class_id] = 1  # track any unexpected class IDs

print("Class ID counts across all files:", class_counts)
