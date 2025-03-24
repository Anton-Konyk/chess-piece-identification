## chess-piece-identification 

The WEB application "Identification of Chess Piece Type" is designed to 
determine the type of chess piece - one of six types ("Bishop", "King",
"Knight", "Pawn", "Queen", "Rook").
For this purpose, the web interface has the functionality of loading 
a user image with some chess piece. After loading, the application will 
respond about the expected type of figure with the percentage probability
of determination.

The type of chess piece is determined using a model trained in 
the Google Colab (Many thanks for Google for this service with T4 GPU!)
environment based on convolutional neural networks and 
the functionality of the keras, tensorflow library.
https://colab.research.google.com/drive/1JEGjnhaymSYYUCMEoX3z6igVqJVJUcpU?usp=drive_link

The chess dataset was used as a basis 
https://www.kaggle.com/datasets/niteshfre/chessman-image-dataset. 
Which was checked, edited and supplemented to 109 images for each of 
the 6 types of chess pieces. To create more extended datasets, 
augmentation methods of generating images based on the basic ones 
were used.
After which images were obtained for training the model.
Found 3924 files belonging to 6 classes.
Using 3140 files for training.
Found 3924 files belonging to 6 classes.
Using 784 files for validation.

More than 8 types of models with different parameters were created and 
about 20 trainings from 30 to 60 epochs were performed.
![train_process.png](README_Screenshots%2Ftrain_process.png)
The choice was made on the model that showed the following results:
Epoch 56/70
99/99 ━━━━━━━━━━━━━━━━━━━━━ 20s 125ms/step - 
accuracy: 0.9872 - loss: 0.6870 - val_accuracy: 0.9745 - val_loss: 0.6728

## Installing / Getting started

Python3 must be already installed
Docker must be already installed and running

```shell
git clone https://github.com/Anton-Konyk/chess-piece-identification
cd chess_identification
Python3 -n venv venv
source venv/bin/activate (for MacOS/Linux) or venv/scripts/activate (for Windows)
pip install -r requirenents.txt
docker-compose build
docker-compose up
http://http://127.0.0.1:5000/  # satart page
```
![start_page.png](README_Screenshots%2Fstart_page.png)

## Contributing

It's open source code.
If you'd like to contribute, please fork the repository and use a feature
branch. Pull requests are warmly welcome.

## Demo
![start_page.png](README_Screenshots%2Fstart_page.png)
![result_page.png](README_Screenshots%2Fresult_page.png)
