import argparse

def get_input_args():
    """
    Retrieves and parses the 3 command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's 
    argparse module to create and define these 3 command line arguments. If 
    the user fails to provide some or all of the 3 arguments, then the default 
    values are used for the missing arguments.
    Command Line Arguments:
      1. Image Folder as --dir with default value 'pet_images'
      2. CNN Model Architecture as --arch with default value 'vgg'
      3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
    This function returns these arguments as an ArgumentParser object.
    """
    # Create Parse using ArgumentParser
    parser = argparse.ArgumentParser()

    # Create 3 command line arguments as mentioned above
    parser.add_argument('--dir', type=str, default='pet_images/',
                        help='Path to the folder of pet images')

    parser.add_argument('--arch', type=str, default='vgg',
                        help='CNN model architecture: resnet, alexnet, or vgg')

    parser.add_argument('--dogfile', type=str, default='dognames.txt',
                        help='Text file that contains names of all dogs')

    # Replace None with parser.parse_args() parsed argument collection
    return parser.parse_args()
