import FWCore.ParameterSet.Config as cms

process = cms.Process("SimpleCounter")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 10000
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(

	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_110_ETT_LepDecay/patTuple_10_2_gMz.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_110_ETT_LepDecay/patTuple_11_2_6yX.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_110_ETT_LepDecay/patTuple_1_1_5Rq.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_110_ETT_LepDecay/patTuple_12_1_1NM.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_110_ETT_LepDecay/patTuple_13_1_CDz.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_110_ETT_LepDecay/patTuple_14_2_vAJ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_110_ETT_LepDecay/patTuple_15_1_9YX.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_110_ETT_LepDecay/patTuple_16_1_NPx.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_110_ETT_LepDecay/patTuple_17_2_IKK.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_110_ETT_LepDecay/patTuple_18_1_lya.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_110_ETT_LepDecay/patTuple_19_2_TRN.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_110_ETT_LepDecay/patTuple_20_1_Vs4.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_110_ETT_LepDecay/patTuple_21_1_qmK.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_110_ETT_LepDecay/patTuple_2_1_JGD.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_110_ETT_LepDecay/patTuple_3_1_XEK.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_110_ETT_LepDecay/patTuple_4_1_xQ0.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_110_ETT_LepDecay/patTuple_5_1_wEt.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_110_ETT_LepDecay/patTuple_6_1_6hS.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_110_ETT_LepDecay/patTuple_7_3_2sE.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_110_ETT_LepDecay/patTuple_8_1_4Zf.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_110_ETT_LepDecay/patTuple_9_2_UbM.root',

    )
)

process.TFileService = cms.Service("TFileService", fileName = cms.string(

	'/lustre/cms/store/user/calabria/Data/SKIMMING/ETT/WH_110_ett_LepDecay/histo_WH_110_ett_LepDecay_1.root'

))

process.demo = cms.EDAnalyzer('SimpleCounter'
)


process.p = cms.Path(process.demo)
