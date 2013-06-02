import FWCore.ParameterSet.Config as cms

process = cms.Process("SimpleCounter")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 10000
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(

	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunA_06Aug2012/patTuple_10_1_aii.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunA_06Aug2012/patTuple_11_1_XcB.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunA_06Aug2012/patTuple_1_1_wBB.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunA_06Aug2012/patTuple_12_1_pOA.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunA_06Aug2012/patTuple_13_1_0Sv.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunA_06Aug2012/patTuple_14_1_30g.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunA_06Aug2012/patTuple_15_1_Kkf.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunA_06Aug2012/patTuple_16_1_BZR.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunA_06Aug2012/patTuple_17_1_g4V.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunA_06Aug2012/patTuple_18_1_wnY.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunA_06Aug2012/patTuple_19_1_ruu.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunA_06Aug2012/patTuple_20_1_qcF.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunA_06Aug2012/patTuple_2_1_0fK.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunA_06Aug2012/patTuple_21_1_Fb3.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunA_06Aug2012/patTuple_22_1_DJ4.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunA_06Aug2012/patTuple_23_1_5sl.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunA_06Aug2012/patTuple_24_1_Fsy.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunA_06Aug2012/patTuple_25_1_l1t.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunA_06Aug2012/patTuple_26_1_H5u.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunA_06Aug2012/patTuple_27_1_Y0D.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunA_06Aug2012/patTuple_28_1_4zd.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunA_06Aug2012/patTuple_29_1_usC.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunA_06Aug2012/patTuple_30_1_I8R.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunA_06Aug2012/patTuple_31_1_l6X.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunA_06Aug2012/patTuple_3_1_Zsy.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunA_06Aug2012/patTuple_32_1_7YG.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunA_06Aug2012/patTuple_33_1_8pk.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunA_06Aug2012/patTuple_34_1_zlp.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunA_06Aug2012/patTuple_4_1_z4q.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunA_06Aug2012/patTuple_5_1_QqJ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunA_06Aug2012/patTuple_6_1_Txa.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunA_06Aug2012/patTuple_7_1_4UL.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunA_06Aug2012/patTuple_8_1_huo.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunA_06Aug2012/patTuple_9_1_1W3.root',

    )
)

process.TFileService = cms.Service("TFileService", fileName = cms.string(

	'/lustre/cms/store/user/calabria/Data/SKIMMING/ETT/TauPlusX_RunA_06Aug2012/histo_TauPlusX_RunA_06Aug2012_1.root'

))

process.demo = cms.EDAnalyzer('SimpleCounter'
)


process.p = cms.Path(process.demo)
