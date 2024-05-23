#!/bin/sh
export SCRAM_ARCH=el8_amd64_gcc11
cd /afs/cern.ch/user/y/yilun/CMSSW_13_0_3/src 
#cmsenv
eval `scramv1 runtime -sh`

#path="/afs/cern.ch/user/t/tuos/work/private/Glauber2016/version3/code/v31/pbpb/default/5360"
#jbi=default
#cd $path/$jbi 
cd /afs/cern.ch/user/y/yilun/GlauberModel/default

$ROOTSYS/bin/root -l -b <<EOF
{
  gSystem->Load("libMathMore");
  gROOT->ProcessLine(".L /afs/cern.ch/user/y/yilun/GlauberModel/default/runglauber_v3.1.C+");
  runAndSaveNtuple(1000000,"Pbpnrw","Pbpnrw",68.0,-1,0.4,-1,-1,"glauber_PbpnrwPbpnrw_default_1M.root");
}
EOF

echo "Done!"



