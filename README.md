# Universal kriging and geohashing

Kriging also known as Gaussian process regression is a geostatistical technique which is used in estimating values of environmental variables at unknown locations by values at known locations. It also provides mean squared error of estimation which is called as Kriging variance. 

## Steps

Create a virtual environment and run command below

pip install -r requirements.txt

py framework.py

Ordinary and Universal Kriging supports 5 variogram models which can be put in function as string parameter.
+ gaussian
+ exponential
+ spherical
+ power
+ linear

Universal Kriging has additional parameter drift_terms.

drift_terms argument is given as list of strings.
+ ["regional_linear"]

By running this command project structure i.e 5 folders [input_data, clustered_data, cluster files, krigged_data, merged_data] will be created.
It will throw error as Missing input file to interpolate data 

After putting input file inside input_data directory, code will create clusters from the dataset with the specified clustering method given by user.
Later it will perform Universal Kriging and geohashing on these cluster files and will save kriged files inside krigged_data folder. After that all kriged_files will be concatenated and saved to merged_data folder.




