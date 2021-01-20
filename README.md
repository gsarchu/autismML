# Regression analysis of autism and mental health trend data

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/gsarchu/autismML/main)
[![App](https://heroku-badge.herokuapp.com/?app=heroku-badge)](https://autismsd.herokuapp.com/)

#### Coded and deployed by Archana

## Abstract

#### Machine learning delivers better analysis of behavioral sciences to enhance diagnostic and intervention research and may be especially useful in investigations involving the highly prevalent and heterogeneous syndrome of autism spectrum disorder. Autism spectrum disorder (ASD) research has been a notable increase in research literature evaluating the effectiveness of machine learning for diagnosing ASD, exploring its genetic underpinnings, and designing effective interventions. The goal of the project is to identify and describe supervised machine learning trends in ASD as well as inform and guide researchers interested in expanding the body of clinically, computationally, and statistically sound approaches for mining ASD data. My aim is to find a better method of machine learning approach for finding a correlation between autism characteristics and mental health data. Through the machine learning models, the highly correlated factors could be identified and the possibility of autism can be predicted by an app. Our ﬁnding shows that Support Vector Machines (SVM) classiﬁer performs best overall other machine learning algorithms in terms of accuracy during the detection of ASD cases for the Toddler dataset and produces fewer classiﬁcation errors compared to other algorithms.
------

## Introduction

#### Autism Spectrum Disorder (ASD) is a category of neurodevelopmental disabilities that include autism proper and Asperger’s syndrome. ASD cannot be cured but its early detection is desirable as it allows more effective mitigating treatment. However, ASD is very difficult to detect and diagnose by conventional behavioral studies. ASD is most often identified at around two years of age but can be later, depending on the severity of the symptoms. While there are a number of clinical tools to detect ASD as early as possible, in practice these involve onerous diagnostic processes that are not often used unless there is a strong suspicion or high risk of ASD development.
------

## Requirement analysis

#### There have been a number of studies that have attempted to detect and diagnose ASD using a variety of ML techniques. Thabtah et al. proposed a computational intelligence (CI) method called Variable Analysis (VA) which showed feature-to-class and feature-to-feature correlations and used support vector machine (SVM), decision tree (DT), and logistic regression (LR) for robust ASD diagnoses and prognoses. Duda et al. analyzed ASD data with different classifiers and found that 5 out of 65 features were sufficient to distinguish ASD from attention deficit hyperactivity disorder (ADHD). Crippa et al. analyzed ASD and TD children and identified 15 preschool ASD from them using only 7 features. 
------

## Dataset

#### In this work, we gathered ASD datasets relating to studies of ASD characteristics in toddlers from the Kaggle and UCI ML repository. Several feature transformation (FT) methods were applied to these dataset which converted them into a suitable format for these analyses. Different classifiers were then applied to these transformed datasets and we identified well performing ML approaches. In addition, we also explored how data transformation may improve the performance of classifiers. Several feature selection techniques (FST) were then applied to these transformed datasets to determine which classifiers gave the best results in prioritising ASD risk factors in toddlers. Thus, these studies indicate that ML can be utilized to determine ASD risk factors. In addition, we determined which were the best ML models to explore the predictive risk factors of ASD.
------

## Data Preprocessing

#### Thabtah et al. developed the ASDTests app which is used Q-CHAT-10for screening and identifying ASD risk factors. This app calculates a score, which ranges from 0 to 10, with a final individual score of more than 4 out of 10 indicates a positive prediction of ASD. Each item is assigned values from 1 to 10. We collected toddlers (N = 1054) data from Kaggle and UCI ML repository where ASDTests was used to aggregate datasets.
------

### Tables 1 show a brief feature description of the different datasets used in this study.

[![Data1](https://ieeexplore.ieee.org/mediastore_new/IEEE/content/media/6287639/8600701/8895818/moni.t1-2952609-large.gif)]

### Tables 2 show a brief feature description of the different datasets used in this study.

[![Data2](https://ieeexplore.ieee.org/mediastore_new/IEEE/content/media/6287639/8600701/8895818/moni.t2-2952609-large.gif)]

## Modelling and methods

#### The datasets employed contained noisy, missing, and unwanted records which were replaced by mean values. In addition, different categorical features were encoded by corresponding integer values. Thus, different FT methods were used to reduce skewness, spread equality, the linear and additive relationship of ASD datasets. I have applied the Logistic Regression model, RandomForest Classification model, Naive Bayes Model, and SVM model to the same set of features. Out of 10 features, we have considered only the best 9 features based on the feature importance, and only those are used for the model prediction.
------

## Model Comparison

#### Table 1: Displays the accuracy values of the used models

|                          Methods                          |   Accuracy  |
|:---------------------------------------------------------:|:-----------:|
| Logistic Regression Model                                 | 0.930599369 |
| RandomForest Classification(considering all the features) | 0.952681388 |
| RandomForest Classification model for selected features   | 0.94637224  |
| Gaussian Naive Bayes model                                | 0.94637224  |
| SVM rbf kernel model                                      | 0.96214511  |
| SVM linear model                                          | 0.96214511  |
| Tuned SVM model                                           | 0.955835962 |

#### Table 2: Displays the classification report for the used models

|                           Methods                           | Values | Precision | Recall | F1-score | Support |
|:-----------------------------------------------------------:|:------:|:---------:|:------:|:--------:|:-------:|
| Logistic Regression Model                                   | 0      | 0.9       | 0.87   | 0.89     | 98      |
|                                                             | 1      | 0.94      | 0.96   | 0.95     | 219     |
| RandomForest Classification(considering all the features)   | 0      | 0.96      | 0.89   | 0.92     | 101     |
|                                                             | 1      | 0.95      | 0.98   | 0.97     | 216     |
| RandomForest Classification model for selected features     | 0      | 0.92      | 0.91   | 0.92     | 101     |
|                                                             | 1      | 0.96      | 0.96   | 0.96     | 216     |
| Gaussian Naive Bayes model                                  | 0      | 0.92      | 0.91   | 0.92     | 101     |
|                                                             | 1      | 0.96      | 0.96   | 0.96     | 216     |
| SVM RBF kernel model                                        | 0      | 0.97      | 0.91   | 0.94     | 101     |
|                                                             | 1      | 0.96      | 0.99   | 0.97     | 216     |
| SVM Linear model                                            | 0      | 0.98      | 0.9    | 0.94     | 101     |
|                                                             | 1      | 0.96      | 0.99   | 0.97     | 216     |
| Tuned SVM model                                             | 0      | 0.98      | 0.9    | 0.94     | 101     |
|                                                             | 1      | 0.96      | 0.99   | 0.97     | 216     |

Notes: 0 = False, 1 = True


## Score and inferences

#### We are considering only 9 out of 10 features to avoid overfitting while we predict the Score. If the total score(other than the 10th feature) is more than 4, then the result will be identified as an autistic characteristic.
------

## Model Deployment

#### We have used Jupyter notebook, Streamlit, Github and Heroku
------

## System Requirements

## Python and library requirements

## Future perspectives

## References
