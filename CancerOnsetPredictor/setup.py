from setuptools import setup, find_packages

setup(
    name='CancerOnsetPredictor',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'joblib',
        'pandas',
    ],
    description='A package for predicting the age of onset of leukaemia from the age of onset of diseases belonging to a specific chapter in the first occurence  category in the UKBiobank data',
    author='Aakanksha Choudhary',
    author_email='aakankshachoudhary66660@gmail.com',
    include_package_data=True,
    package_data={
        'my_rf_model_package': ['rf_final_high_model.joblib', 'rf_final_low_model.joblib'],
    },
)

