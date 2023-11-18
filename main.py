import os
import pandas as pd

def xls_to_csv(file_path):
	try:
		df = pd.read_excel(file_path)
		file_name = os.path.splitext(os.path.basename(file_path))[0]
        	csv_path = f"{file_name}.csv"
		df.to_csv(csv_path, index=False)
        	print(f"Conversion successful: {file_path} -> {csv_path}")
	except Exception as e:
		print(f"Error converting {file_path}: {e}")

current_directory = os.getcwd()

for file_name in os.listdir(current_directory):
	if file_name.endswith(".xls"):
		file_path = os.path.join(current_directory, file_name)
		xls_to_csv(file_path)


