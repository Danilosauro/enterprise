import pandas as pd

from sdv.single_table import GaussianCopulaSynthesizer
from sdv.metadata import SingleTableMetadata
from sdv.lite import SingleTablePreset
from sdv.evaluation.single_table import evaluate_quality 
from sdv.evaluation.single_table import get_column_plot 

# readind database to synthetis 

real_data = pd.read_csv('fake_data.csv') 

# getting metadata 

metadata = SingleTableMetadata()
metadata.detect_from_dataframe(real_data)
print(metadata)

# synthetis 

synthesizer = GaussianCopulaSynthesizer(metadata)
synthesizer.fit(real_data)
synthetic_data = synthesizer.sample(1000)


# generating synthetic dataset without hashes 

synthetic_data.to_csv('synthetic_data.csv') 

# evaluting quality 

quality_report = evaluate_quality(
    real_data,
    synthetic_data,
    metadata
) 
 
# saving metadata 

metadata.save_to_json('/home/danilo/Documentos/prototype_synthetic_data_python/metadata.json')

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
 

