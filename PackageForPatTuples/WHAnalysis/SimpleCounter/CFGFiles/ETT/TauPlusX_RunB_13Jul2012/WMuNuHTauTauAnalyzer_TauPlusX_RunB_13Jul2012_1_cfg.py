import FWCore.ParameterSet.Config as cms

process = cms.Process("SimpleCounter")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 10000
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(

	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_1000_1_MXa.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_100_1_bnd.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_101_2_Mry.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_10_1_KGR.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_102_1_hyq.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_103_1_0iK.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_104_1_ny6.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_105_1_jH0.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_106_1_15S.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_107_1_lii.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_108_1_93M.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_109_1_HAF.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_110_1_0Ro.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_111_1_d5Y.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_11_1_GvO.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_112_1_NvZ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_113_1_fyS.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_114_1_yre.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_115_1_ZZE.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_116_1_hyB.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_117_1_Civ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_118_1_05N.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_119_1_Mwn.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_1_1_aaj.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_120_1_QXZ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_121_1_Ojc.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_12_1_7Av.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_122_1_m3N.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_123_1_7GJ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_124_1_Yl7.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_125_1_D9w.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_126_1_2kH.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_127_1_qTv.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_128_1_pA6.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_129_1_48C.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_130_1_fLX.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_131_1_pjt.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_13_1_fss.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_132_1_wUq.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_133_1_quL.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_134_1_Sfp.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_135_1_Tmy.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_136_1_dkq.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_137_1_FGM.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_138_1_m83.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_139_1_AVO.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_140_1_Wi4.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_141_1_ajO.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_14_1_Ax3.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_142_1_hC2.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_143_1_9pJ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_144_1_MxR.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_145_1_Zuv.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_146_2_85R.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_147_2_g6m.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_148_1_W6v.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_149_1_1iP.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_150_1_1Km.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_151_1_v0g.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_152_1_oXM.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_15_2_oIW.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_153_1_WWh.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_154_1_iHL.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_155_1_DLk.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_156_1_kkF.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_157_1_9Pi.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_158_1_EFj.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_159_1_WRS.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_160_1_f2q.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_161_1_798.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_162_1_qgq.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_16_2_2wE.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_163_1_gzJ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_164_1_vSm.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_165_1_zha.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_166_1_oD3.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_167_2_iBx.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_168_1_g8t.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_169_4_eav.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_170_1_h5b.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_171_1_8mv.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_17_1_mzb.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_172_1_om5.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_173_1_nbj.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_174_1_0o6.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_175_1_aNX.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_176_1_yb1.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_177_1_Sir.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_178_1_O7v.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_179_1_0jW.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_180_1_tmr.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_181_1_su5.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_18_1_dcu.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_182_1_pHs.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_183_2_mOn.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_184_1_s9h.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_185_1_ZiU.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_186_1_Msn.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_187_1_AAL.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_188_1_XEt.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_189_1_J9N.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_190_1_R7y.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_191_3_qas.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_19_1_4Bs.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_192_1_HGo.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_193_1_z2h.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_194_1_Git.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_195_1_VYV.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_196_1_Ntf.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_197_1_aNS.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_198_1_0WZ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_199_1_WpJ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_200_1_0KT.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_201_1_sGh.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_202_1_QzH.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_20_2_Fz5.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_203_2_HIc.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_204_1_QOO.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_205_1_ywD.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_206_1_i8d.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_207_1_q7H.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_208_1_Bsl.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_209_1_CNV.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_210_1_WVf.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_211_1_BLy.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_21_1_vyj.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_212_1_6wh.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_213_1_F2O.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_214_1_IjK.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_215_1_73p.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_216_1_fY6.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_217_1_N0S.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_218_1_LKN.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_219_2_9IF.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_2_1_SPO.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_220_1_Yv5.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_221_2_D5m.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_22_1_48M.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_222_1_vWG.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_223_1_QBT.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_224_1_zQA.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_225_1_6Ny.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_226_1_xDk.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_227_1_Rxd.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_228_1_Gvg.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_229_1_MbV.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_230_1_HuA.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_231_1_W5r.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_23_1_62F.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_232_1_oJK.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_233_1_BRd.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_234_1_bLm.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_235_2_ejl.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_236_1_pB9.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_237_1_dZ2.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_238_1_vQr.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_239_1_5E8.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_240_1_Yg7.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_241_1_qMU.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_24_1_LKf.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_242_1_DuI.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_243_1_1GV.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_244_1_xZp.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_245_1_7EV.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_246_1_oXN.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_247_1_ruz.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_248_1_V0v.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_249_3_4Ip.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_250_1_b2p.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_251_1_18z.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_25_1_WZV.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_252_1_6fK.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_253_1_1Id.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_254_1_cHL.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_255_1_Pxh.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_256_1_fPz.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_257_1_fr3.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_258_1_mvK.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_259_1_hQW.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_260_1_SBz.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_261_1_J0i.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_26_1_pQw.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_262_1_JQk.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_263_1_hLO.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_264_1_YVm.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_265_1_vOP.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_266_1_uKM.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_267_1_332.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_268_2_d0Q.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_269_1_cQ5.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_270_1_Ikz.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_271_1_ALe.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_27_1_Nma.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_272_1_t4H.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_273_1_j7u.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_274_1_zSy.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_275_1_3Iq.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_276_1_4HM.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_277_1_daC.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_278_1_fTI.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_279_1_RuE.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_280_1_zko.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_281_1_J39.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_28_1_3vK.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_282_1_Kqb.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_283_1_Ufx.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_284_1_c9i.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_285_1_pZY.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_286_1_DbG.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_287_1_qwT.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_288_1_Qo2.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_289_1_iie.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_290_1_oQi.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_291_1_u0E.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_29_1_jhp.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_292_1_gbq.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_293_1_aGp.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_294_1_R1y.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_295_1_sCF.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_296_1_4EL.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_297_1_tMf.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_298_1_AbS.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_299_2_ND2.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_300_1_L2n.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_301_1_n19.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_30_1_26Z.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_302_1_PF2.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_303_1_H88.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_304_1_IBl.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_305_1_vpK.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_306_1_E1h.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_307_1_Nsp.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_308_1_1zG.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_309_1_6Fu.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_310_1_3kG.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_311_1_cYZ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_31_1_63J.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_312_1_v5A.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_313_1_k8s.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_314_1_q1e.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_315_1_Mh1.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_316_1_TTl.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_317_1_Ekh.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_318_2_g20.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_319_1_d7Y.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_3_1_LEb.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_320_1_KBG.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_32_1_27U.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_321_2_WfV.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunB_13Jul2012/patTuple_322_1_6AH.root',

    )
)

process.TFileService = cms.Service("TFileService", fileName = cms.string(

	'/lustre/cms/store/user/calabria/Data/SKIMMING/ETT/TauPlusX_RunB_13Jul2012/histo_TauPlusX_RunB_13Jul2012_1.root'

))

process.demo = cms.EDAnalyzer('SimpleCounter'
)


process.p = cms.Path(process.demo)
