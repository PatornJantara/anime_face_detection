# anime_face_detection
## anime character face detection using self trained haar cascade

**Instruction to create your own Haar cascade**
<br /><br />Follow steps below to complete training your haar cascade
<br />1. Collect your interested object images in **/positive/rawdata** folder as .bmp file and unrelated images in **negative** folder. [The original source is here](http://www.mediafire.com/file/1aq02tpidk105fv/dasar_haartrain.rar/file) 
<br />2. Go to **/negative** folder then run create_list.bat
<br />3. Go to **/positive** folder then run objectmaker.exe then collect your ROI of rawdata (the program instruction is on header of window) 
<br />4. Run **01sample_creation.bat** 
<br />5. Open **02haarTraining.bat** using nodpad.Change the numper after -npos as number of your image in rawdata folder and -nneg as number of your image in negative folder then save and run (before running be sure that cascade folder is empty)
<br />6. Run **03 convert.bat** then you will recieve **myhaar.xml** as your haar cascade model. Now you can enjoy your object detection
<br />The efficiency of model will be depend on number of your positive and negative images
<br /><br /><br />**Here are results**
<br /><br />- images
<br /><br />![test2 jpg](https://user-images.githubusercontent.com/56642026/74905201-295d9500-53e0-11ea-9396-00cfd06e6f04.png)
<br /> ![test1 jpg](https://user-images.githubusercontent.com/56642026/74916869-320e9500-53f9-11ea-859c-666ded7a6a4e.png)
<br /><br />- Video
<br /><a href="https://imgflip.com/gif/3pqpsc"><img src="https://i.imgflip.com/3pqpsc.gif" title="made at imgflip.com"/></a>
<br /><br /> I think it's too hard for haar cascade method to classify face of anime characters or may be i have to add more images LOL  

