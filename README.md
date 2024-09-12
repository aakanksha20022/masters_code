Cancer Onset Predictor
----
Investigating the Interplay of Multimorbidity and Social Deprivation on leukemia Progression and Onset within the UK Biobank using Supervised and Unsupervised Machine Learning algorithms.

1.	CancerOnsetPredictor: A module designed for predicting cancer onset age based on the age of onset of broad disease classifications as defined by the UK Biobank first occurrence data.
2.	analysis_scripts:
      -Python scripts (including Jupyter Notebooks: MCA_STATS, IMD_CUT_OFF, CLUSTERING, SUPERVISED_ML, VENN_DIAGRAM_BIPLOT, ) analyzing the multimorbidity profiles of 2,149 leukemia patients          from the UK Biobank.
  	  -Script for the GUI which takes user inputs in the form of onset ages of various broad disease classifications and gives the predicted onset age of leukemia along with a force plot     
       highlighting the direction each of the features pushes the prediction to.

Installation Instructions:

git clone https://github.com/aakanksha20022/masters_code.git

cd masters_code/CancerOnsetPredictor

pip install .
