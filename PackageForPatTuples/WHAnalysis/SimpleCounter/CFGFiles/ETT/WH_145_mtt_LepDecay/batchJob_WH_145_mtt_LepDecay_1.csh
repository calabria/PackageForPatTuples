#!/bin/csh
setenv VO_CMS_SW_DIR /opt/exp_soft/cms
source $VO_CMS_SW_DIR/cmsset_default.csh
limit vmem unlim
mkdir /lustre/cms/store/user/calabria/Data/SKIMMING/ETT/WH_145_mtt_LepDecay

cd /cmshome/calabria/Code_53X_TauIdDec2012/CMSSW_5_3_7_patch4/src/WHAnalysis/SimpleCounter/
setenv SCRAM_ARCH slc5_amd64_gcc462
eval `scramv1 runtime -csh`
cd -
cmsRun /cmshome/calabria/Code_53X_TauIdDec2012/CMSSW_5_3_7_patch4/src/WHAnalysis/SimpleCounter/CFGFiles/ETT/WH_145_mtt_LepDecay/WMuNuHTauTauAnalyzer_WH_145_mtt_LepDecay_1_cfg.py
