#!/bin/sh
export SCRAM_ARCH=el8_amd64_gcc11
cd /location/of/any/CMSSW/version/you/have/on/lxplus/src
#cmsenv
eval `scramv1 runtime -sh`

cd /current/directory/where/you/put/this/glauber/code

$ROOTSYS/bin/root -l -b <<EOF
{
  gSystem->Load("libMathMore");
  gROOT->ProcessLine(".L /current/directory/where/you/put/this/glauber/code/runglauber_v3.1.C+");
  runAndSaveNtuple(1000000,"Pbpnrw","Pbpnrw",68.0,-1,0.4,-1,-1,"glauber_PbpnrwPbpnrw_default_1M.root");
}
EOF

echo "Done!"



