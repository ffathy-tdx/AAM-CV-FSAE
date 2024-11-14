import os

# define the directories containing label files
base_path = "F:/Work/Projects/AAM CV w2/FSOCO-12"
folders = ["train", "valid", "test"]

# class ID of 'unknown_cone' (based on the original list, unknown_cone has ID 3 when the dataset was used)
class_to_remove = 3

# function to adjust labels
def process_label_file(file_path):
    new_lines = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            class_id = int(parts[0])

            # skip lines where class_id is the 'unknown_cone' ID
            if class_id == class_to_remove:
                continue
            
            # re-index class IDs after removing 'unknown_cone'
            if class_id > class_to_remove:
                class_id -= 1
            
            # update line with the new class_id
            new_line = f"{class_id} " + " ".join(parts[1:])
            new_lines.append(new_line)
    
    # write updated lines back to the file
    with open(file_path, 'w') as file:
        file.write("\n".join(new_lines) + "\n")

# traverse through the label directories and process each label file
for folder in folders:
    label_dir = os.path.join(base_path, folder, "labels")
    for root, _, files in os.walk(label_dir):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                process_label_file(file_path)

print("Finished updating label files!")
