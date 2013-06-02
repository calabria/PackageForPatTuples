import FWCore.ParameterSet.Config as cms

process = cms.Process("SimpleCounter")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 10000
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(

	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_115_MTT_LepDecay/patTuple_10_0_Ex7.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_115_MTT_LepDecay/patTuple_11_0_bKV.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_115_MTT_LepDecay/patTuple_1_1_1n7.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_115_MTT_LepDecay/patTuple_12_1_x9C.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_115_MTT_LepDecay/patTuple_13_0_4ef.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_115_MTT_LepDecay/patTuple_14_0_qkd.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_115_MTT_LepDecay/patTuple_15_0_4UE.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_115_MTT_LepDecay/patTuple_16_0_dgg.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_115_MTT_LepDecay/patTuple_17_0_TyF.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_115_MTT_LepDecay/patTuple_18_0_XKW.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_115_MTT_LepDecay/patTuple_19_0_GnX.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_115_MTT_LepDecay/patTuple_20_0_1uf.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_115_MTT_LepDecay/patTuple_21_0_3uH.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_115_MTT_LepDecay/patTuple_2_2_EBD.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_115_MTT_LepDecay/patTuple_3_1_XX6.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_115_MTT_LepDecay/patTuple_4_2_0fE.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_115_MTT_LepDecay/patTuple_5_3_XEC.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_115_MTT_LepDecay/patTuple_6_0_RX9.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_115_MTT_LepDecay/patTuple_7_0_v5u.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_115_MTT_LepDecay/patTuple_8_0_eM2.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_115_MTT_LepDecay/patTuple_9_0_Cv7.root',

    )
)

process.TFileService = cms.Service("TFileService", fileName = cms.string(

	'/lustre/cms/store/user/calabria/Data/SKIMMING/ETT/WH_115_mtt_LepDecay/histo_WH_115_mtt_LepDecay_1.root'

))

process.demo = cms.EDAnalyzer('SimpleCounter'
)


process.p = cms.Path(process.demo)
