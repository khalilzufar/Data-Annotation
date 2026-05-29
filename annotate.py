"""
Phase 2: Interactive Human-in-the-Loop Text Annotation Script
Project: Localized Indonesian Sentiment Analysis Model Alignment

Objective:
This script establishes a lightweight, robust Command Line Interface (CLI) 
for manual data labeling. It features dynamic state persistence (checkpointing) 
and automated progress saving to mitigate data loss during extensive annotation sessions.

Workflow Architecture:
1. State Initialization: Scans for existing progress ('dataset_annotated.csv'). 
   If found, rehydrates the session; otherwise, initializes a new target schema.
2. Data Filtering: Identifies unmapped records utilizing explicit boundary checks.
3. User Validation Loop: Enforces precise token constraints (Strict evaluation criteria: 2/1/0).
4. Automated Serialization: Safely commits every record back to the disk 
   using verified UTF-8 encoding standards.
"""

import pandas as pd
import os

# Define environment file configurations
input_file = 'dataset_raw_sampled.csv'
output_file = 'dataset_annotated.csv'

# 1. Verify existence of previous annotation checkpoints
if os.path.exists(output_file):
    df = pd.read_csv(output_file)
    print(f"Resuming annotation session from existing progress file: {output_file}")
else:
    df = pd.read_csv(input_file)
    # Initialize the target label column if it doesn't exist
    if 'sentiment_label' not in df.columns:
        df['sentiment_label'] = None
    print(f"Initiating a brand new annotation session from: {input_file}")

print("\n--- ANNOTATION SCHEMA AND RULES ---")
print("2 = POSITIVE | 1 = NEUTRAL/MIXED | 0 = NEGATIVE")
print("Type 'q' at any prompt to save progress and exit safely.\n")

# 2. Core interactive human-in-the-loop annotation pipeline
for idx, row in df.iterrows():
    # Detect unannotated tokens using strict boundary checks
    if pd.isnull(row['sentiment_label']) or row['sentiment_label'] == "":
        print("-" * 60)
        print(f"Record {idx + 1} of {len(df)}")
        print(f"RAW TEXT VALUE:\n{row['text']}")
        print("-" * 60)
        
        # Enforce input validation rules
        while True:
            pilihan = input("Assign Label (2/1/0) or 'q' to quit: ").strip()
            if pilihan in ['0', '1', '2']:
                df.at[idx, 'sentiment_label'] = int(pilihan)
                break
            elif pilihan.lower() == 'q':
                print("\nSerializing current state and terminating session...")
                df.to_csv(output_file, index=False, encoding='utf-8')
                print(f"Session safely checkpointed at {output_file}!")
                exit()
            else:
                print("Invalid constraint! Please input exactly 0, 1, 2, or 'q'.")
        
        # Incremental automated save state to protect session integrity
        df.to_csv(output_file, index=False, encoding='utf-8')

print("\nSuccess! All data rows have been fully evaluated and annotated.")
print(f"Final structured dataset securely committed to: {output_file}")