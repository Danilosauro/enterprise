import pandas as pd
import os
from sdv.single_table import GaussianCopulaSynthesizer
from sdv.metadata import SingleTableMetadata
from sdv.lite import SingleTablePreset
from sdv.evaluation.single_table import evaluate_quality 
from sdv.evaluation.single_table import get_column_plot 

# read database

real_data = pd.read_csv('fake_data.csv') 
occurrences = len(real_data.index) 

# getting metadata 

metadata = SingleTableMetadata()
metadata.detect_from_dataframe(real_data)
print(metadata)

# synthetis 

synthesizer = GaussianCopulaSynthesizer(metadata)
synthesizer.fit(real_data)
synthetic_data = synthesizer.sample(occurrences)


# generating synthetic dataset without hashes 

synthetic_data.to_csv('synthetic_data.csv') 

# evaluting quality 

quality_report = evaluate_quality(
    real_data,
    synthetic_data,
    metadata
) 
 
# saving metadata 

def save_metadata(metadata): 
    path = os.getcwd() 
    filename = '/metadata.json'
    complete_path = path + filename
    if os.path.exists('metadata.json'):
        os.remove('metadata.json')
    else:
        metadata.save_to_json(complete_path) 

save_metadata(metadata)

# generating graphs 

columns = synthetic_data.columns 

for column in columns: 
    fig = get_column_plot(
        real_data=real_data,
        synthetic_data=synthetic_data,
        column_name=column, 
        plot_type ='bar',
        metadata=metadata
    ) 

    fig.show() 
 

