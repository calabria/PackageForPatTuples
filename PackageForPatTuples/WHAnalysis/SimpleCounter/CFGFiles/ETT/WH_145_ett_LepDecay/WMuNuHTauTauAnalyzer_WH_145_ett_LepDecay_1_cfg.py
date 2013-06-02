import FWCore.ParameterSet.Config as cms

process = cms.Process("SimpleCounter")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 10000
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(

	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_145_ETT_LepDecay/patTuple_10_1_fxs.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_145_ETT_LepDecay/patTuple_11_2_EqI.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_145_ETT_LepDecay/patTuple_12_1_9vJ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_145_ETT_LepDecay/patTuple_1_2_Es5.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_145_ETT_LepDecay/patTuple_13_2_3Dq.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_145_ETT_LepDecay/patTuple_14_1_xzE.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_145_ETT_LepDecay/patTuple_15_1_Se9.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_145_ETT_LepDecay/patTuple_16_1_1b0.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_145_ETT_LepDecay/patTuple_17_1_tv9.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_145_ETT_LepDecay/patTuple_18_1_H1m.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_145_ETT_LepDecay/patTuple_19_2_yWR.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_145_ETT_LepDecay/patTuple_20_2_RVR.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_145_ETT_LepDecay/patTuple_2_2_rD3.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_145_ETT_LepDecay/patTuple_3_1_ZVt.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_145_ETT_LepDecay/patTuple_4_2_DqL.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_145_ETT_LepDecay/patTuple_5_1_7Uj.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_145_ETT_LepDecay/patTuple_6_1_OVT.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_145_ETT_LepDecay/patTuple_7_1_Tci.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_145_ETT_LepDecay/patTuple_8_1_E52.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_145_ETT_LepDecay/patTuple_9_2_ytj.root',

    )
)

process.TFileService = cms.Service("TFileService", fileName = cms.string(

	'/lustre/cms/store/user/calabria/Data/SKIMMING/ETT/WH_145_ett_LepDecay/histo_WH_145_ett_LepDecay_1.root'

))

process.demo = cms.EDAnalyzer('SimpleCounter'
)


process.p = cms.Path(process.demo)
