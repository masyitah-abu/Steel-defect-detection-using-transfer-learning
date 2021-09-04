# Steel defect detection using transfer learning
- This work is to analysis performance of steel defect using several types of transfer learning
- This work had publish under IOP Publication and MobileNet model had shown the best performance in this work.

- In this work, the GUI System is develop for Research and Innovation Exhibition UniMAP [(EREKA 2021)](https://ereka.unimap.edu.my/images/result/RESULTS_EREKA_2021_OVERALL.pdf) 
  - This system is develop using tkinter python package to convert the code into windows execute below command is used:
```
pyinstaller --noupx --onedir --window --hidden-import=tensorflow --hidden-import=tensorflow.lite.python.lite -F --add-data "vf.png;." --add-data "mymodel.h5;." --add-data "eye_train;." vfgui.py
```
  
- The system GUI have 3 pages:
  * First page is introduction of steel defect industry (HOME PAGE)
  <p align="center">
    <img width="100%" height="100%" src= "https://github.com/masyitah-abu/Steel-defect-detection-using-transfer-learning/blob/main/GUI/page_example/Page_1.JPG">
  </p>

  * Second page is Menu page to enter the detection page
  <p align="center">
    <img width="100%" height="100%" src= "https://github.com/masyitah-abu/Steel-defect-detection-using-transfer-learning/blob/main/GUI/page_example/Page_2.JPG">
  </p>

  * Lastly is detection page  
  <p align="center">
    <img width="100%" height="100%" src= "https://github.com/masyitah-abu/Steel-defect-detection-using-transfer-learning/blob/main/GUI/page_example/Page_3.JPG">
  </p>

- The specification of this work is:
  - Python 3.6
  - Google Colab GPU environment 

- You can refer this paper, video and poster about this work
  - [CONFERENCE PAPER](https://iopscience.iop.org/article/10.1088/1742-6596/1755/1/012041/meta) 
  - [POSTER](https://github.com/masyitah-abu/Steel-defect-detection-using-transfer-learning/blob/main/GUI/EREKA%20Poster.pptx)
  - [VIDEO](https://youtu.be/66KFhL9oO6I)
