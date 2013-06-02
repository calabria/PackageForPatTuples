import FWCore.ParameterSet.Config as cms

process = cms.Process("SimpleCounter")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 10000
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(

	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_135_MTT_LepDecay/patTuple_10_0_9B4.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_135_MTT_LepDecay/patTuple_11_0_tK2.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_135_MTT_LepDecay/patTuple_1_1_AjR.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_135_MTT_LepDecay/patTuple_12_0_g5o.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_135_MTT_LepDecay/patTuple_13_0_AkK.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_135_MTT_LepDecay/patTuple_14_0_LDS.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_135_MTT_LepDecay/patTuple_15_0_tkL.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_135_MTT_LepDecay/patTuple_16_0_NYy.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_135_MTT_LepDecay/patTuple_17_0_YZ3.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_135_MTT_LepDecay/patTuple_18_0_uwE.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_135_MTT_LepDecay/patTuple_19_0_3Sr.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_135_MTT_LepDecay/patTuple_20_0_Kwm.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_135_MTT_LepDecay/patTuple_2_3_BcH.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_135_MTT_LepDecay/patTuple_3_1_4aP.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_135_MTT_LepDecay/patTuple_4_1_VBt.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_135_MTT_LepDecay/patTuple_5_1_bb4.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_135_MTT_LepDecay/patTuple_6_2_JQM.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_135_MTT_LepDecay/patTuple_7_0_uv0.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_135_MTT_LepDecay/patTuple_8_0_zgx.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/WH_135_MTT_LepDecay/patTuple_9_0_Ckd.root',

    )
)

process.TFileService = cms.Service("TFileService", fileName = cms.string(

	'/lustre/cms/store/user/calabria/Data/SKIMMING/ETT/WH_135_mtt_LepDecay/histo_WH_135_mtt_LepDecay_1.root'

))

process.demo = cms.EDAnalyzer('SimpleCounter'
)


process.p = cms.Path(process.demo)
