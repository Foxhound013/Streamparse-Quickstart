# Streamparse-Quickstart
This repository is intended to serve as an Apache Storm streamparse quickstart guide and resource repository. Many of the "tutorials" currently out there do not address many specifics and the streamparse quickstart may leave someone wondering how everything fits together. This repository is intended to help solve that. This repository will include a description of how to get set up and going with a local development environment (this guide reflects my experiences setting things up on a mac running High Sierra) and a detailed explanation of the files in the streamparse quickstart guide.

Some useful resources for reference are listed below.

  * [Github repository for Apache Storm](https://github.com/apache/storm)
  * [Github repository for Steamparse](https://github.com/Parsely/streamparse)
  * [Documentation for streamparse](https://streamparse.readthedocs.io/en/stable/)  
    * [In Depth streamparse documentation](https://media.readthedocs.org/pdf/streamparse/stable/streamparse.pdf)


## Getting Started
To get started using streamparse, you'll need to get your environment set up.
  
  1. Make sure you have the latest Java Development Kit (JDK), at the time of writing, this was [JDK 8](https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)  
     * Check if the JDK was installed using *java -version* from the terminal.
     
  2. Install leiningen, an extremely useful guide to this can be found [here](http://www.wisdomofjim.com/blog/setting-up-leiningen-on-mac-os)   
     * In case that link ever dies, the steps are reproduced below.
     1. Verify if you have java with *java -version* (We completed this step already)
     2. Go to your /usr/local/bin directory *cd /usr/local/bin*
     3. Get the Lein file by running *sudo curl -O https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein*
     4. Allow the Lein file to be executed by running *sudo chmod a+x /usr/loacl/bin/lein*
     5. You'll need to make sure that /usr/local/bin is in your path, you can check by running echo $PATH
        * If it isn't, edit your bash profile as follows, run the command *vi ~/.bash_profile* and add the following lines. It would be good to add a comment above your addition for future reference.
            
            PATH="/usr/local/bin:${PATH}"
            
            export PATH
     6. While inside of /usr/local/bin, run *lein* to get all of the necessary extras installed
     7. run *lein version* to ensure that everything is good to go!
     
  3. Now we can get the Apache Storm dev environment installed.
     1. You can find the latest files [here](http://storm.apache.org/downloads.html). I just downloaded the tar.gz (for 1.2.2 at the time of writing this)
     2. The tar file will be placed in your downloads folder, I unpacked it there by double clicking it in your downloads and then ran *mv apache-storm-1.2.2 /usr/local/bin* to move it to my /usr/local/bin directory.
     3. Run *sudo chmod a+x /usr/local/bin/apache-storm-1.2.2/bin/storm* to make storm executable.
     4. Just like lein, storm needs to be added to your PATH.
        * edit your bash profile to include the following
        
          PATH="/usr/local/bin/apache-storm-1.2.2/bin:${PATH}"
          
          export PATH
   
   4. We can finally install streamparse! *I'm assuming you already have python installed, if not go get it installed from [python.org](python.org). Run *pip install streamparse* to get it set up.
       * Note: If you run into an issue with thriftpy building, you may need to run *xcode-select --install* on mac. This resolved the issue for me.
       
   5. Now that everything is installed, you can navigate to wherever you would like your storm project to be and run *sparse quickstart wordcount*, streamparse will then set up the quickstart project for you.
      * Before you can run the quickstart example, you'll need to update the project.clj file in the example directory. Inside of this file you need to update the storm version to the version that you are using.
   
   6. cd into the wordcount directory and run the command *sparse run*. The local dev environment for starm will start up shortly and begin running the example.
   
   7. Celebrate your new found streaming powers! :squirrel:
   
## What's next?
Take a look at the Spout, Bolt, and Topology files in this repository. My version of these files are heavily commented to help even the newest of people to understand what is happening in Storm.

## Updates to come?
As I learn more about Storm and Streamparse myself, I'll continually update this repository. Some things to come . . .

  * A flowchart of how the peices fit together, specifically in the context of the wordcount example.
  * Instructions for moving from the local dev environment to production.
  * A more intensive example utilizing weather data from the High-Resolution Rapid Refresh Weather Model (HRRR)
