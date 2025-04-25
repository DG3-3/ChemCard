import os
import pandas as pd

reactions_folder = 'reactions'

all_data = pd.DataFrame(columns=['EquationStr'])

for file_name in os.listdir(reactions_folder):
    if file_name.endswith('.csv'):
        file_path = os.path.join(reactions_folder, file_name)
        print(f"Reading file: {file_path}")
        df = pd.read_csv(file_path, encoding='utf-8')
        all_data = pd.concat([all_data, df], ignore_index=True)

all_data.drop_duplicates(inplace=True)

output_file = 'merged_reactions.csv'
all_data.to_csv(output_file, index=False, encoding='utf-8')
print(f"Merged and deduplicated data saved to {output_file}")