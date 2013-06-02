import FWCore.ParameterSet.Config as cms

process = cms.Process("SimpleCounter")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 10000
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(

	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_939_2_6GE.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_940_2_vrb.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_941_2_8Ox.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_94_1_y7Z.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_942_2_MiX.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_943_2_ssn.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_944_2_H4A.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_945_2_TvP.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_946_2_74C.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_947_2_k96.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_948_2_9wi.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_949_2_Xdd.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_950_2_sFF.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_951_2_Sb6.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_95_1_XgH.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_952_2_AOL.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_953_2_sbH.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_954_2_1tw.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_955_6_i6R.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_956_2_srM.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_957_2_fT7.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_958_2_e5u.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_959_2_tKN.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_960_2_GFo.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_961_2_1W8.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_96_1_zIH.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_962_2_c3w.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_963_2_ejc.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_964_2_o19.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_965_2_GF6.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_966_2_sJE.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_967_2_xBH.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_968_2_E7u.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_969_2_jkI.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_970_2_b4R.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_971_2_xWM.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_97_1_V48.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_972_2_mmy.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_973_2_3Oy.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_974_2_Mdc.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_975_2_VQq.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_976_2_22A.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_977_2_c6f.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_978_2_s6B.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_979_2_7yG.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_980_6_tQ9.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_981_2_r6o.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_98_1_cu4.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_982_6_Jkt.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_983_2_OoT.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_984_2_dSM.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_985_6_mxw.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_986_2_A5D.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_987_3_Pu3.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_988_2_PtQ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_989_2_Fgo.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_990_2_4Lt.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_991_2_0av.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_99_1_8LL.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_992_2_BVH.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_993_2_3bT.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_994_4_e2O.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_995_3_1dI.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_996_2_Z6Y.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_997_2_Ggg.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_998_2_B7q.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_999_2_o4t.root',

    )
)

process.TFileService = cms.Service("TFileService", fileName = cms.string(

	'/lustre/cms/store/user/calabria/Data/SKIMMING/ETT/TauPlusX_RunD_PRv1/histo_TauPlusX_RunD_PRv1_7.root'

))

process.demo = cms.EDAnalyzer('SimpleCounter'
)


process.p = cms.Path(process.demo)
