#!/bin/csh
setenv VO_CMS_SW_DIR /opt/exp_soft/cms
source $VO_CMS_SW_DIR/cmsset_default.csh
limit vmem unlim
mkdir /lustre/cms/store/user/calabria/Data/SKIMMING/ETT/TauPlusX_RunC_PRv2

cd /cmshome/calabria/Code_53X_TauIdDec2012/CMSSW_5_3_7_patch4/src/WHAnalysis/SimpleCounter/
setenv SCRAM_ARCH slc5_amd64_gcc462
eval `scramv1 runtime -csh`
cd -
cmsRun /cmshome/calabria/Code_53X_TauIdDec2012/CMSSW_5_3_7_patch4/src/WHAnalysis/SimpleCounter/CFGFiles/ETT/TauPlusX_RunC_PRv2/WMuNuHTauTauAnalyzer_TauPlusX_RunC_PRv2_6_cfg.py
