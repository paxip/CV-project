import random
import cv2
from keras.models import load_model
import numpy as np
import time



class RPS:

    def __init__(self):
        self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        self.computer_wins = 0
        self.user_wins = 0
        
    
    def get_winner(self, computer_choice, user_choice):
        
        if user_choice == computer_choice:
            print('It is a tie, you score 0 points.')
     
        elif (user_choice == 'Paper' and computer_choice == 'Rock') or\
            (user_choice == 'Rock' and computer_choice == 'Scissors') or\
            (user_choice == 'Scissors' and computer_choice == 'Paper'):
             self.user_wins += 1
             print(f'You win this round. You have {self.user_wins} points.')

        else:
            self.computer_wins += 1
            print('You lost this round.')
    
    def get_countdown(self):
        print('The countdown is going to start')
        countdown = 5
        while countdown > 0:
            print(f'{countdown}')
            cv2.waitKey(1000)
            countdown -= 1 
        
        print('Show your hand now')
    

    def get_prediction(self):
        end = time.time() + 3

        while time.time() < end: 
            ret, frame = self.cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            self.data[0] = normalized_image
            prediction = self.model.predict(self.data)
            cv2.imshow('frame', frame)
            # Press q to close the window
            print(prediction)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
            user_choice = game_list[prediction.argmax()]
            return user_choice

    def get_computer_choice(self):
        computer_choice = random.choice(game_list)
        return computer_choice


def play(game_list):
    game = RPS()

    while game.computer_wins < 3 and game.computer_wins < 3:
        game.get_countdown()
        computer_choice = game.get_computer_choice() 
        user_choice = game.get_prediction()
        game.get_winner(computer_choice, user_choice)
        

    # After the loop release the cap object
    game.cap.release()
        # Destroy all the windows
    cv2.destroyAllWindows()   
        

        

if __name__ == '__main__':
    game_list = ['Rock', 'Paper', 'Scissors', 'Nothing']
    play(game_list)
    