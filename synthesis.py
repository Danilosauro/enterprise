import pandas as pd
import hashlib 
from sdv.single_table import GaussianCopulaSynthesizer
from sdv.metadata import SingleTableMetadata
from sdv.lite import SingleTablePreset  
from sdv.evaluation.single_table import run_diagnostic 
from sdv.evaluation.single_table import evaluate_quality 



df = pd.read_csv('fake_data.csv') 


metadata = SingleTableMetadata()
metadata.detect_from_dataframe(df)
print(metadata)


#df['ID'] = df['ID'].apply(lambda x: hashlib.md5(str(x).encode()).hexdigest())

#metadata = Metadata()
#metadata.add_table('df', df.columns)

#synthesizer = SingleTablePreset(
    #metadata = metadata,
    #name='FAST_ML'
#)
#synthetizer.fit(data=df) 


synthesizer = GaussianCopulaSynthesizer(metadata)
synthesizer.fit(df)
synthetic_data = synthesizer.sample(1000)

print(synthetic_data.head()) 
synthetic_data.to_csv('synthetic_data.csv')