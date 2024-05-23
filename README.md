# Compile the Glauber model code
We need to use some library from CMSSW, so compile any CMSSW version you have first and go to the Glauber model directory:
```
cd /location/of/any/CMSSW/version/you/have/on/lxplus/src
cmsenv
cd /current/directory/where/you/put/this/glauber/code
```
Load the CMS library and compile the Glauber model code `runglauber_v3.1.C+`: 
```
$ root -l
root [0] gSystem->Load("libMathMore")
(int)0
root [1] .L runglauber_v3.1.C+
```
# Run the Glauber model to generate Glauber events
Below line is the example of running line. Input parameters meaning: 

runAndSaveNtuple(number of generated events,"Pbpnrw","Pbpnrw",Sigma NN Inelastic,-1,d_node,-1,-1,"Output.root")
```
root [2] runAndSaveNtuple(10000,"Pbpnrw","Pbpnrw",67.6,-1,0.4,-1,-1,"glauber_PbpnrwPbpnrw_default_10k.root")
```
Other input parmeters, like "Nuclear Radius for proton", "Skin Depth for proton", "Nuclear Radius for neutron" and "Skin Depth for neutron" are changed inside the C code. We can run 10k events without submitting jobs for testing. 

# Use Condor to submit the batch jobs
To run 1 million Glauber events, `sub_glauber.sub` is used to submit the job, it calls the bash file `exeJob.sh` to actually run the Glauber code. In `exeJob.sh`, remember to change the location of CMSSW and Glauber model directory. 

Condor commands:  `condor_submit sub_glauber.sub`. To check the job stuatus, use `condor_q`. 
