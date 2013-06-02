import FWCore.ParameterSet.Config as cms

process = cms.Process("SimpleCounter")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 10000
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(

	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_77_5_GQd.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_776_5_3ww.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_777_1_Nhl.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_778_6_Wcp.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_779_6_yxJ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_780_1_vts.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_781_5_Iy9.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_782_4_tiq.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_783_6_Q5Q.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_784_5_6GT.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_785_6_yre.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_78_5_wGu.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_786_6_wxp.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_787_5_IJE.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_788_5_ysd.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_789_5_a9B.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_790_5_4F6.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_791_5_K4V.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_792_5_POW.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_793_5_55r.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_794_5_duG.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_795_4_XXj.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_79_5_v0v.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_796_4_sv5.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_797_5_1pi.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_798_4_Cg5.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_799_3_1z9.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_800_3_Fsp.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_801_5_kH0.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_802_3_sP8.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_803_5_n8j.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_804_4_J45.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_805_6_rZ6.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_80_5_6xw.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_806_5_tLI.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_807_5_Y7v.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_808_6_qz3.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_809_5_tAJ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_810_6_mkh.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_811_5_2pp.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_812_5_j9E.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_813_4_nlp.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_814_3_ns8.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_815_2_wTk.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_81_5_8Al.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_816_5_P5A.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_817_6_HQy.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_818_5_Kba.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_819_5_XGr.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_820_6_Feq.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_821_5_7yE.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_822_5_lEz.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_823_5_fQY.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_824_5_CMs.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_82_5_2UY.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_825_6_Hfr.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_826_4_gEp.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_827_5_acs.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_828_3_xrz.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_829_7_yYe.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_830_3_vo5.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_831_6_AvZ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_832_6_xBN.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_833_2_t3V.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_834_6_8jZ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_835_3_fDr.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_83_5_yZY.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_836_3_wfv.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_837_3_Z1h.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_838_6_b7i.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_839_1_Mh1.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_8_3_IRn.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_840_2_RC9.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_841_2_I47.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_842_1_0Av.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_843_3_Tq1.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_844_6_ghT.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_845_3_K0y.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_84_5_5Yp.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_846_2_1tJ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_847_3_FEc.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_848_3_o8S.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_849_3_0YM.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_850_2_8hL.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_851_2_EMQ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_852_3_c04.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_853_3_2Ih.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_854_3_Ynr.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_855_3_TXY.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_85_5_oJg.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_856_1_YxD.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_857_3_ACQ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_858_1_tPj.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_859_1_tVu.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_860_3_ooH.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_86_5_oTy.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_87_4_VLO.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_88_5_VLW.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_89_3_fcx.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_90_5_DI3.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_91_5_0hY.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_9_1_lBb.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_92_4_bOh.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_93_5_U3C.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_94_5_GmS.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_95_5_60l.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_96_3_ehy.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_97_4_ECB.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_98_4_V8k.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_99_5_caW.root',

    )
)

process.TFileService = cms.Service("TFileService", fileName = cms.string(

	'/lustre/cms/store/user/calabria/Data/SKIMMING/ETT/DYToEE_mtt_HS/histo_DYToEE_mtt_HS_4.root'

))

process.demo = cms.EDAnalyzer('SimpleCounter'
)


process.p = cms.Path(process.demo)
