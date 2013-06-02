import FWCore.ParameterSet.Config as cms

process = cms.Process("SimpleCounter")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 10000
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(

	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_130_MTT_LepDecay/patTuple_10_0_iRM.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_130_MTT_LepDecay/patTuple_11_0_oLp.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_130_MTT_LepDecay/patTuple_12_0_TGT.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_130_MTT_LepDecay/patTuple_1_2_Yht.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_130_MTT_LepDecay/patTuple_13_0_rtE.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_130_MTT_LepDecay/patTuple_14_0_lkB.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_130_MTT_LepDecay/patTuple_15_0_SQj.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_130_MTT_LepDecay/patTuple_16_0_l8g.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_130_MTT_LepDecay/patTuple_17_0_bZi.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_130_MTT_LepDecay/patTuple_18_0_aWx.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_130_MTT_LepDecay/patTuple_19_0_E0J.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_130_MTT_LepDecay/patTuple_20_0_9AS.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_130_MTT_LepDecay/patTuple_21_0_T8d.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_130_MTT_LepDecay/patTuple_2_1_4Cw.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_130_MTT_LepDecay/patTuple_3_0_maa.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_130_MTT_LepDecay/patTuple_4_0_xXK.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_130_MTT_LepDecay/patTuple_5_0_n7U.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_130_MTT_LepDecay/patTuple_6_0_yRe.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_130_MTT_LepDecay/patTuple_7_0_pCg.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_130_MTT_LepDecay/patTuple_8_0_xHI.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_130_MTT_LepDecay/patTuple_9_0_Ds1.root',

    )
)

process.TFileService = cms.Service("TFileService", fileName = cms.string(

	'/lustre/cms/store/user/calabria/Data/SKIMMING/ETT/WH_130_mtt_LepDecay/histo_WH_130_mtt_LepDecay_1.root'

))

process.demo = cms.EDAnalyzer('SimpleCounter'
)


process.p = cms.Path(process.demo)
