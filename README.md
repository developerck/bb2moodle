
> Step-by-Step guide for migrating courses from the Blackboard standard version to moodle version > 1.9.

#### Black Board Categorisation :

For the purpose of course migration to Moodle, Blackboard can be categorised into 3 different systems, each with a different migration procedure.  

-   CE 4.0/CE 4.1  (rebranded WebCT) [ can use the webctimport tool with the “IMS Content Migration Utility”]
-   **Standard Blackboard (5.5, 6, 7, 8, 9, 9.1)**  **[ Follow the mentioned Process in this article]**
-   Vista3/Vista4/Vista8 and CE 6/CE 8  (rebranded WebCT) [ backup files are encrypted so can not import that ]

> **“_The following process tested on a standard blackboard 9.1 Q4 course export file and importing that into moodle 2.7 LTS after following below steps”_**

### **Objective** :

Migrating courses from  **blackboard Standard 9.1 Q4**  version to Moodle 2.7, via exporting from Blackboard and importing that into Moodle.  

****** The reason to say  **moodle version > 1.9** is , all the versions utilise the moodle2 process to import and before moodle 2.0 (i.e moodle 1.9 and before) the process was different. However “ > moodle 2.0” was supplied with an inbuilt converter, which supports but upto a limit and without any assurity.

### **Solution :**

To achieve the target , you need to follow the below steps:

1 . Setup the Conversion Tool  [#step-1](https://developerck.com/blackboard-course-migration-to-moodle/#step-1)

2. Convert the exported BB (blackboard file) to Moodle 1.9 zip file via conversion tool  [#step-2](https://developerck.com/blackboard-course-migration-to-moodle/#step-2)

3 . Make some mentioned changes in moodle code and DB for moodle version > 1.9  [#step-3](https://developerck.com/blackboard-course-migration-to-moodle/#step-3)

Or

You can import it in moodle 1.9 and then upgrade moodle to 2.0 and export it to moodle 2 compatible import

4 . Import the Converted file into Moodle version > 1.9  [#step-4](https://developerck.com/blackboard-course-migration-to-moodle/#step-4)

#### **Step-1 : –**

Conversion Tool can be  [download from here](https://developerck.com/wp-content/uploads/2020/02/reteach.zip) or  [https://github.com/adamzap/reteach](https://github.com/adamzap/reteach)

or update version is available at :  [https://github.com/developerck/bb2moodle](https://github.com/developerck/bb2moodle)  (just replace reteach by bb2moodle)
Assuming that you are using linux environment.

-   **Pre-requisite : python2 and pip is installed**

**If not**  , then install python 2 and pip first, steps are –

Check for python

`>>> python --version`

If python not found :  [https://www.python.org/downloads/](https://www.python.org/downloads/)

Install pip and setup tools

`>>> sudo apt-get install python-setuptools`

For PIP

`>>> curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`

`>>> python get-pip.py`  

Now you have installed Python and pip and I assume that you have downloaded the conversion tool zip file. Let’s say you are under the directory  **/var/www/html**  and conversion tool is present at  **/var/www/html/retach.zip**  

-   Unzip that file , the directory  **reteach**  should be created.
-   Go inside that directory , location /var/www/html/retach
-   Setup.py file will be there
-   Run following command `**>>>**  **pip install .**`
-   Package has been installed, you can cross check via typing reteach **`>>> reteach`**
-   If reteach is not found than please try python reteach and try after running following command `**export PATH=$PATH:~/.local/bin**`

![](https://developerck.com/wp-content/uploads/2020/02/retach.png)

reatech

#### **Step-2 :**

You just need to run this command

`>>> reteach bb-sample.zip -o moodle-file.zip`

_bb-sample.zip is then name of bb course zip file name . I assume that you are currently present under the directory where bb-sample.zip is present_

_moodle-file.zip will be converted zip file that will be used to import in moodle.  
_

![](https://developerck.com/wp-content/uploads/2020/02/conversion.png)

#### **Step-3 : –**

If you are utilising moodle > 1.9, Update the following code

Line number 1257 File: backup/converter/moodle1/handlerlib.php

  
_// replay the upgrade step 2011060301 – Rename field defaultgrade on table question to defaultmark  
$data[‘defaultmark’] = $data[‘defaultgrade’];_

```

       // code to add for for blackboard course
        $data['generalfeedbackformat'] = '1';
        $data['createdby'] = '2'; // can be change
        $data['modifiedby'] = '2'; // can be change
// END
```

**And run the query:**  ``ALTER TABLE `mdl_qtype_match_subquestions` CHANGE `answertext` `answertext` TEXT CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL;``  

#### **Step -4 :**

Import that moodle-file.zip into Moodle setup , and you are done.  

![](https://developerck.com/wp-content/uploads/2020/02/import.png)

[https://developerck.com/blackboard-course-migration-to-moodle/](https://developerck.com/blackboard-course-migration-to-moodle/)
