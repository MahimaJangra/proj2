# proj2
Used sklearn Breast Cancer Dataset to Predict target.
Target Prediction classifies the tumor as either 0 indicating malignant or 1 for benign.

in our model:-
Accuracy = 0.9298245614035088
Precision = 0.9538461538461539
Recall = 0.9253731343283582
F1 = 0.9393939393939394


we
Used AIX360 liberary (booleanRuleCG algorithm and the explainer)

The liberary explained the outcome rules as:- (in notebook)

  Predict Y=1 if ANY of the following rules are satisfied, otherwise Y=0:
  - compactness error > 0.01 AND worst concavity <= 0.22 AND worst symmetry <= 0.28
  - mean texture <= 15.46 AND mean concavity <= 0.15 AND area error <= 54.16
  - fractal dimension error > 0.00 AND worst area <= 680.60 AND worst concave points <= 0.18
  - mean concave points <= 0.05 AND perimeter error <= 3.80 AND worst area <= 930.88 AND worst smoothness <= 0.16
  
