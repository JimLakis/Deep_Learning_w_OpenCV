
import cv2

def load_photo(absolute_path):
    original_image = cv2.imread(absolute_path) # Load image into object. Note use of 'r' for 'raw' string, this essentially escapes the backslash '\'.
    return original_image

def convert_photo_black_white(original_image):
    bw_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    return bw_image

def show_photo(image):
    cv2.imshow('Photo_Viewer_Window', image) # Open a window and display the image in it
    cv2.waitKey(0) # Keep the window open until a key is depressed
    cv2.destroyAllWindows() # Once the waitKey() func is ran, close window displaying image
    
def write_photo(image):
    cv2.imwrite("copy_photo.png", image) # save a new copy of the file to disk
    
def run_classifier(bw_image):
    import os
    import json
    import numpy as np
    
    cascade_path = os.path.join(cv2.data.haarcascades, "haarcascade_frontalface_default.xml")
    ## print(f"Looking for cascade file at: {cascade_path}")
    # if not os.path.isfile(cascade_path):
    #     raise Exception(f"Error: File does not exist at {cascade_path}")
        
    face_classifier = cv2.CascadeClassifier(cascade_path)
    # if face_classifier.empty():
    #     raise Exception("Error: face_classifier is empty after loading")
    
    # Produce a list of coordinates for identified faces
    faces_coords = face_classifier.detectMultiScale(bw_image, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))
    # if face_classifier.empty():
    #     raise Exception("Error: face_coords is empty after loading")
    
    faces_list = []
    for (x, y, w, h) in faces_coords:
        faces_list.append({
            "x": int(x),
            "y": int(y),
            "width": int(w),
            "height": int(h)
        })
    with open("coords.txt", "w") as f:
        json.dump(faces_list, f, indent=4)
        
    return faces_coords

def transpose_face_coord_onto_orginal_image(faces_coords, original_image):
    for (x_coord, y_coord, width, height) in faces_coords:
        cv2.rectangle(original_image, (x_coord, y_coord), (x_coord + width, y_coord + height), (255,0,0), 2)
        # Above tuple (225,0,0) is the BGR code for blue. Note, not in RGB format.
    cv2.imshow("Detected Faces", original_image)
    cv2.waitKey(0) # Keep the window open until a key is depressed
    cv2.destroyAllWindows() # Once the waitKey() func is ran, close window displaying image



def main():
    absolute_path: str = r"C:\Users\Development\Documents\Dev_Projects\2025\OpenCV\Testing_Setup\pic_of_people.png"
    original_image = load_photo(absolute_path)
    
    
    # Which color scale should the image be in, "full color" or black and white
    response = int(input("\nEnter 1 to leave the photo in the original color scale or 2 to change it to black and white.\nRember, in order to pass the image through a Classifier it should be in B&W format.")
                   )
    if response == 2:
        bw_image_object = convert_photo_black_white(original_image)
        
    if response < 1 or response > 2:
        raise Exception("Entry must be either 1 or 2")
    
    # Display the image, write it to a file or pass it to a Classifier
    response: int = int(input("Enter 1 to display the photo, 2 to write it to a file or 3 to pass it through a Classifier:"))
    if response == 1:   # Display image
        show_photo(original_image)
    if response == 2:   # Write image to a file
        write_photo(original_image)
    if response == 3:   # Identify where patterns (faces in this case) exist in image and transpose "square" over those locations in image
        face_coords = run_classifier(bw_image_object)
        transpose_face_coord_onto_orginal_image(face_coords, original_image)
        
    if response < 1 or response > 3:
        raise Exception("Entry must be either 1, 2 or 3. Try again.")


if __name__ == "__main__":
    main()