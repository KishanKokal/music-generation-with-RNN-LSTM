# Abstract
In the realm of music composition, this project aims to create a music generation system leveraging Recurrent Neural Networks with Long Short-Term Memory (RNN-LSTM). The objective is to train this system on a dataset of folk melodies and enable it to generate novel melodies that exhibit similarities to those found in the training data. This project seeks to delve into the intricacies of melody creation by treating it as a time-series prediction problem, predicting the progression of musical events in time. Through LSTM's capacity to capture long-term temporal dependencies, this project aims to replicate the structural patterns found in melodies, which often involve repeated patterns with variations in pitch content, stretching, or shrinking. The project's foundation rests on the ESAC dataset, comprising over 20,000 folk melodies from various parts of the world. The core tools and libraries employed in this project include Keras/Tensorflow for deep learning, Music21 for symbolic music data processing, and MuseScore for music notation. This collaborative effort involves team members Pratik Kithani, Kishan Kokal, Shubham Mandal, and Harsh Punjabi, under the guidance of mentor Dr. Anagha Durugkar from Thadomal Shahani Engineering College.

# Introduction
Music composition is a creative endeavor that involves the arrangement of musical elements such as notes, rests, and their temporal relationships to create melodies. In this project, we explore the use of deep learning techniques, specifically RNN-LSTM, to generate music compositions based on a dataset of folk melodies. The aim is to develop a system that can autonomously generate melodies with structural patterns similar to those found in folk music.

# Literature Survey/Existing System
The generation of music using neural networks, particularly RNN-LSTM models, has gained popularity in recent years. Various researchers have explored the use of RNNs for music generation due to their ability to capture long-term dependencies in sequential data. Some existing systems have successfully employed RNN-LSTM architectures to generate music in different genres, demonstrating the potential of these models for creative tasks.

# Limitation of Existing System or Research Gap
Despite the progress in music generation with RNN-LSTM models, there is still room for improvement in terms of generating melodies that are culturally specific, such as folk melodies. Additionally, fine-tuning the model to generate melodies with a desired level of complexity and variation remains a challenge.

# Problem Statement and Objective
To create a music generation system that can produce folk-like melodies using RNN-LSTM. The main objectives include:
1. Collecting and preprocessing a dataset of folk melodies (ESAC dataset).
2. Developing an RNN-LSTM model for music generation.
3. Training the model to generate melodies with culturally relevant patterns.
4. Evaluating the generated melodies for their musical quality.
5. Fine-tuning the model to control complexity and variation in the generated melodies.

# Proposed System
## Analysis/Framework/Algorithm
The proposed system relies on the use of RNN-LSTM architecture for music generation. LSTM networks are well-suited for capturing long-term temporal dependencies in music, making them ideal for replicating the structural patterns found in folk melodies.

## Design Details
The system will involve data preprocessing, model development, training, and evaluation. It will take as input a dataset of folk melodies and generate new melodies as output.

## Methodology
1. Data Collection: Gather a dataset of folk melodies (ESAC dataset) for training.
2. Data Preprocessing: Convert musical notation into a format suitable for training the RNN-LSTM model.
3. Model Development: Design and implement the RNN-LSTM architecture for music generation.
4. Training: Train the model on the folk melody dataset, optimizing it to capture culturally specific patterns.
5. Evaluation: Assess the quality of generated melodies using performance evaluation parameters.
6. Fine-tuning: Modify the model to control complexity and variation in generated melodies.

# Experimental Set Up
## Details of Database or Details About Input to Systems or Selected Data
The ESAC dataset, comprising over 20,000 folk songs from around the world, will serve as the primary data source for this project.

## Performance Evaluation Parameters
The quality of generated melodies will be evaluated based on musical criteria such as melody coherence (logical and consistent), harmony (a pleasing combination of musical notes), and rhythm (a regular repeated pattern of sound). Additionally, user feedback and subjective assessment will be considered for evaluation.

## Software and Hardware Set Up
The software stack will include Keras/Tensorflow for deep learning, Music21 for symbolic music data processing, and MuseScore for music notation. The project will be developed and tested on a suitable hardware configuration.

# Implementation Plan for Next Semester
The implementation plan for the next semester will include the following steps:
1. Data collection and preprocessing.
2. Model development and training.
3. Evaluation of generated melodies.
4. Fine-tuning the model for improved music generation.
5. Documentation and presentation of the project findings.

# Timeline Chart for Term 1 and Term 2
(Project Management tools can be used.)

# References
[1] Conner, Michael, et al. Music Generation Using an LSTM. arXiv, 22 Mar. 2022. http://arxiv.org/abs/2203.12105
[2] Mangal, Sanidhya, et al. ‘LSTM Based Music Generation System’. IARJSET, vol. 6, no. 5, May 2019, pp. 47–54. https://doi.org/10.17148/IARJSET.2019.6508
[3] Q. Lou, “Music Generation Using Neural Networks.” Accessed: Jul. 26, 2023. https://www.hindawi.com/journals/scn/2020/8873639/