**aminoacidProfiler** for Linux

**How to clone the repository**

Clone the repository by using the command ```git clone https://github.com/ABUSHEIKHSP/aminoacidProfiler.git``` in your Terminal.

If you want to clone the repository using ssh you can do so.

The downloaded repository will have the name **aminoacidProfiler**.


**How to install aminoacidProfiler**

In Terminal navigate to the aminoacidProfiler directory by using the command ``cd``.

Enter ```ls``` to view the files such as aaP.py, page2.py,refracted.py, script.py and setup.py.

If you are not able to view the files, you are on the wrong directory.

Install the necessary requirements by running the command ```pip install requirements.txt``` or ```pip3 install requirements.txt```.

In the Terminal run setup file by using the command ```python3 setup.py```.

Setup will complete all the installations.


**How to start aminoacidProfiler**

Close all the existing Terminal windows.

Open a new Terminal and run the command ```aaP``` to start the **aminoacidProfiler** application.

Restart the System if required.


**How to utilise aminoacidProfiler to it's best**

Create a new folder (optional).

![image](https://user-images.githubusercontent.com/96288958/207559108-48a00852-2abb-43f6-82d2-29548024c2da.png)


Download required protein sequecnes in the **FASTA** format.

If you need geographical location to be mentioned in the result, name the folder that geographical location. (Ex: Folder named Asia)

![image](https://user-images.githubusercontent.com/96288958/207559359-783729de-b02e-42b9-a80d-f32cbaa657b0.png)


Inside the folder you can add subfolders too. (Ex: Asia/Malaysia)

![image](https://user-images.githubusercontent.com/96288958/207559879-a63f6e6b-ddf4-487f-8071-1259bb320c48.png)


Add FASTA files specific to that folder.

![image](https://user-images.githubusercontent.com/96288958/207560448-fb5a3e8f-a0b9-4aad-8ecd-da69b910cf09.png)


Now start the **aminoacidProfiler** by running the command ```aaP``` in the Terminal.

Click the **select folder** button, and select the Folder.

**aminoacidProfiler** will automatically detect all the **.fasta** files, from the main folder and it's subfolder.

The result will be saved as **result.csv** in the folder you have selected early, and can also be directly visualized using **aminoacidProfiler**



