This script uses two folders of documents to check how feasible simple Logistic Regression can distinguish between those two folders. One with the positive examples called "positives" and the other called "negatives" which should be folders outside of the repository.

Folder structure:

.

├── negatives

│ ├── example 1.txt

│ └── ...

├── positives

│ ├── example 1.txt

│ └── ...

└── basicNLP

  ├── bagOfChars.py

  └── README.md


It doesn't matter what the names of the files are, so long as the documents are in separate files for now.

The script requires Python, using sklearn for vectorization and classification. Due to the nature of the text and the small number of texts the vectorizer has, hard coded, the number of features to use from the vectorization process at 100, and the length of substrings to explore, which is everything between 3 and 7 substrings. This can probably be changed without any negative effects.

It isn't a rigorous data science methodology due to the small number of data, but there are techniques that could be used to improve the amount of data, such as splitting the text into parts and using each as a document of its own.

This analysis provides understanding around how distinguishable these two folders of text are. If you are interested in exploring which factors determine the separability, that could be explored through the model you create or an alternate approach using Feature Selection with various techniques.

Enjoy!
