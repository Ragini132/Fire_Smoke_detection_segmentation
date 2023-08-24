# Replace the filepaths list with the paths to the .txt files you want to combine
filepaths = ['/home/ragini/fire_data/week2/Fire_Detection/n1_train.txt', 
'/home/ragini/fire_data/week2/Wildfire/n1_train.txt',
'/home/ragini/fire_data/week2/fire2/n1_train.txt',
'/home/ragini/fire_data/week2/Fire_Images.v2-train-test-val.yolov5pytorch/n1_train.txt',
'/home/ragini/fire_data/week2/df.v2-smhum.yolov5pytorch/n1_train.txt',
'/home/ragini/fire_data/week2/Eunchan_ws.v12i.yolov5pytorch/n1_train.txt',
'/home/ragini/fire_data/week2/final_year_project/n1_train.txt',
'/home/ragini/fire_data/week2/fire_and_smoke/n1_train.txt',
'/home/ragini/fire_data/week2/Fire_and_Smoke_2_remake/n1_train.txt',
'/home/ragini/fire_data/week2/Fire_and_Smoke_Detection/n1_train.txt',
'/home/ragini/fire_data/week2/Fire_and_Smoke_v1/n1_train.txt',
'/home/ragini/fire_data/week2/Fire_Detection_2/n1_train.txt',
'/home/ragini/fire_data/week2/fire-dataset-final-2/n1_train.txt',
'/home/ragini/fire_data/week2/Fire_Detection.v1i.yolov5pytorch/n1_train.txt',
'/home/ragini/fire_data/week2/Fire_Detector_2022.v4i.yolov5pytorch/n1_train.txt',
'/home/ragini/fire_data/week2/Fire5.v3-original.yolov5pytorch/n1_train.txt',
'/home/ragini/fire_data/week2/FireandSmokeDetection.v2i.yolov5pytorch/n1_train.txt',
'/home/ragini/fire_data/week2/FireDetect.v4-validationsetcorrect.yolov5pytorch/n1_train.txt',
'/home/ragini/fire_data/week2/istiklal_iha/n1_train.txt',
'/home/ragini/fire_data/week2/splitup.v1-labelled.yolov5pytorch/n1_train.txt',
'/home/ragini/fire_data/week2/thuan/n1_train.txt',
'/home/ragini/fire_data/week2/yolov5.v1i.yolov5pytorch/n1_train.txt']

# Change the output file name to the desired name
output_file = 'train_combined.txt'

# Open the output file in write mode
with open(output_file, 'w') as outfile:

    # Loop through each file path in the filepaths list
    for filepath in filepaths:

        # Open the file in read mode and read its contents
        with open(filepath, 'r') as infile:
            contents = infile.read()

            # Write the contents of the file to the output file
            outfile.write(contents)
