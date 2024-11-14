# AAM_CV_FSAE Project

This repository contains scripts for managing and preparing the FSOCO dataset used in the Computer Vision develpment for FSAE competitions. These scripts support dataset optimization and label integrity for better object detection model performance.

## Scripts

### 1. `remove_class.py`
This script removes instances of a specified class ID from label files in the dataset and adjusts the class IDs of remaining classes accordingly.

- **Purpose**: Improve model accuracy by removing ambiguous labels, specifically the "unknown_cone" class.
- **Usage**:
  - Defines the base dataset path and target folders (`train`, `valid`, `test`).
  - Removes instances of the specified class and re-indexes other class IDs.
- **Outcome**: All label files are updated, omitting the removed class and adjusting class IDs as needed.

### 2. `count_class.py`
This script counts occurrences of each class ID across all label files, providing an overview of class distribution and detecting any unexpected class IDs.

- **Purpose**: Verify class distribution and ensure labeling consistency across the dataset.
- **Usage**:
  - Scans each label file, counts class occurrences, and provides a warning if any unexpected class IDs are found.
- **Outcome**: Prints the total class counts and flags any anomalies, helping with dataset checks.

## Getting Started

### Prerequisites
Both scripts rely on Python’s `os` module to navigate through directories and process files.

### Running the Scripts
1. Update the `base_path` variable in each script to match the location of the dataset on your system.
2. Run each script from the command line:
   ```bash
   python remove_class.py
   python count_class.py
3. The output will display any updates or warnings related to label adjustments.

## Contributing

Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please submit an issue or create a pull request.

For further questions, please contact me at [ffathy2004@gmail.com](mailto:ffathy2004@gmail.com)). 

