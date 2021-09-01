import os
import time
import cv2

# fetch the images from a folder
def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = list()

    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
    return allFiles

def main():
    dirName = 'pictures'
    listOfFiles = getListOfFiles(dirName)

    for i in range(5):
        imagePath = listOfFiles[i]
        print(imagePath)
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')  #model trained to detect faces
        image = cv2.imread(imagePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # turn image into shades of gray for better recognition

        faces = faceCascade.detectMultiScale(gray, scaleFactor = 1.1, 
                                                   minNeighbors = 10,    
                                                   minSize = ( 30,30 ) )

        #draw a rectangle in detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle( image, ( x,y ), ( x + w , y + h ), ( 0, 255, 0 ), 2)

        cv2.imshow("Faces found", image) #show image in desktop
        cv2.waitKey(2)
        time.sleep(2) #wait before killing the window
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

