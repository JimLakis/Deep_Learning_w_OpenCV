
import cv2

def load_photo(absolute_path):
    image_object = cv2.imread(absolute_path) # Load image into object. Note use of 'r' for 'raw' string, this essentially escapes the backslash '\'.
    return image_object

def convert_photo_black_white(image_object):
    bw_image_object = cv2.cvtColor(image_object, cv2.COLOR_BGR2GRAY)
    return bw_image_object

def show_photo(image_object):
    cv2.imshow('Photo_Viewer_Window', image_object) # Open a window and display the image in it
    cv2.waitKey(0) # Keep the window open until a key is depressed
    cv2.destroyAllWindows() # Once the waitKey() func is ran, close window displaying image
    
def write_photo(image_object):
    cv2.imwrite("copy_photo.png", image_object) # save a new copy of the file to disk


def main():
    absolute_path: str = r"C:\Users\Development\Documents\Dev_Projects\2025\OpenCV\Testing_Setup\pic_of_people.png"
    image_object = load_photo(absolute_path)
    
    color_response = int(input("Enter 1 to leave the photo in the original color scale or 2 to change it to black and white:"))
    if color_response == 2:
        image_object = convert_photo_black_white(image_object)
    if color_response < 1 or color_response > 2:
        raise Exception("Entry must be either 1 or 2")
    
    display_save_response: int = int(input("Enter 1 to display the photo or 2 to write it to a file:"))
    if display_save_response == 1:
        show_photo(image_object)
    if display_save_response == 2:
        write_photo(image_object)
    if display_save_response < 1 or display_save_response > 2:
        raise Exception("Entry must be either 1 or 2")
    
    
    
    # group_photo = cv2.imread(r"C:\Users\Development\Documents\Dev_Projects\2025\OpenCV\Testing_Setup\pic_of_people.png") # Load image into object. Note use of 'r' for 'raw' string, this essentially escapes the backslash '\'.
    # cv2.imshow('Photo_Viewer_Window', group_photo) # Open a window and display the image in it

    # cv2.waitKey(0) # Keep the window open until a key is depressed
    # cv2.destroyAllWindows() # Once the waitKey() func is ran, close window displaying image
   

if __name__ == "__main__":
    main()