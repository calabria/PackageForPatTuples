import FWCore.ParameterSet.Config as cms

process = cms.Process("SimpleCounter")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 10000
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(

	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_776_2_38A.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_777_6_df2.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_778_4_Gmx.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_779_1_LND.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_780_5_uOn.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_781_2_IMV.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_782_2_3kA.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_78_2_FOX.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_783_4_HCk.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_784_6_YZB.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_785_4_XT4.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_786_5_xl3.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_787_4_QCq.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_788_2_F7T.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_789_2_tkE.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_790_4_177.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_791_3_jeA.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_792_3_hSi.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_793_2_Lt2.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_79_3_t4S.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_794_5_H2M.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_795_4_SV5.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_796_2_QMF.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_797_4_bzK.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_798_2_aH5.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_799_4_Soj.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_800_1_9k0.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_801_5_7p1.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_802_7_UYP.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_803_2_Trf.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_804_4_sfX.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_80_4_Yfd.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_805_5_qZb.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_806_5_kdB.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_807_4_FJY.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_808_2_JFc.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_809_1_pVS.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_810_2_C2c.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_811_3_bk4.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_81_1_a3L.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_812_1_GcT.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_813_4_1pG.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_814_3_mpo.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_815_2_Gqw.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_816_4_4au.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_817_1_kmN.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_818_4_oX5.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_819_4_6Pc.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_820_3_hOE.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_821_3_9jX.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_82_1_DuW.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_822_2_ftc.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_823_4_Z1z.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_824_2_G7m.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_825_4_e2l.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_826_4_RYL.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_827_4_OLq.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_828_5_xNK.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_829_4_EF9.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_830_4_qkY.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_831_4_gJR.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_83_2_1hF.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_832_3_fJ6.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_833_3_Igf.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_834_1_eCP.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_835_3_RIy.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_836_1_i4D.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_837_4_3RR.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_838_1_cHj.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_839_5_g2p.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_840_2_SGM.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_841_1_9ye.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_84_1_dag.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_842_5_tG4.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_843_2_YxX.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_844_1_JVw.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_845_4_zbF.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_846_5_vvB.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_847_5_EYZ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_848_1_QlP.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_849_5_5hf.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_850_1_sza.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_851_4_1yI.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_852_3_loq.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_853_4_03a.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_85_4_2Qd.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_854_3_Z1S.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_855_5_dRX.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_856_1_rz1.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_857_5_fC7.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_858_1_8gP.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_859_4_8d9.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_860_1_gd2.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_86_2_6yt.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_87_1_KoS.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_8_7_Ueh.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_88_2_QKq.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_89_3_urK.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_90_4_IvK.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_91_1_gAS.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_92_1_178.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_93_2_4GS.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_94_1_25H.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_95_4_EoS.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_96_3_BsQ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_9_6_aYF.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_97_4_BaJ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_98_5_t3S.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_99_5_4QR.root',

    )
)

process.TFileService = cms.Service("TFileService", fileName = cms.string(

	'/lustre/cms/store/user/calabria/Data/SKIMMING/ETT/DYToEE_ett_HS/histo_DYToEE_ett_HS_4.root'

))

process.demo = cms.EDAnalyzer('SimpleCounter'
)


process.p = cms.Path(process.demo)
