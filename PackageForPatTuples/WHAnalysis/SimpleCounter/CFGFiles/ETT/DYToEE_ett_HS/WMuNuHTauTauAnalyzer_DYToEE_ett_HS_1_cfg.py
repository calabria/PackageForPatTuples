import FWCore.ParameterSet.Config as cms

process = cms.Process("SimpleCounter")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 10000
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(

	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_100_3_fnE.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_101_1_4od.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_102_5_BH4.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_103_1_n2L.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_104_1_xtO.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_105_3_keu.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_106_4_XZx.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_10_6_aTp.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_107_2_rL1.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_108_1_8FB.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_109_2_O1M.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_110_4_hGw.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_111_4_Gv4.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_112_1_Zmt.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_113_1_4RJ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_11_3_SQN.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_114_1_SGg.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_115_1_4Gd.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_116_4_0xL.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_117_3_WTV.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_118_3_2Zy.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_119_3_NJr.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_120_1_GNQ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_121_3_OPR.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_12_1_EcG.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_122_4_Cq2.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_123_5_jUv.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_124_1_7po.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_125_5_4iM.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_126_5_S4h.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_127_1_DWf.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_128_3_TWs.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_129_3_qIK.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_130_3_OuQ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_131_3_vIn.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_132_3_2Z3.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_133_3_Kwn.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_134_3_9f0.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_135_1_yRh.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_13_5_6Qp.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_136_3_c8E.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_137_3_KkT.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_138_1_UUS.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_139_4_56k.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_140_2_TDi.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_141_3_KOK.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_14_1_nnT.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_142_6_qth.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_143_5_dY6.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_144_4_NAS.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_145_6_cAe.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_146_1_b0K.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_147_3_6Ql.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_148_4_hhN.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_149_4_MVR.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_1_4_tJz.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_150_3_yzO.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_151_6_jSc.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_152_6_P9K.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_153_5_a0N.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_154_4_Zhr.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_155_1_yFY.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_15_5_kXJ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_156_4_Ql0.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_157_4_R8P.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_158_5_g3Q.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_159_3_0sy.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_160_6_P8J.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_161_3_6rJ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_162_4_DBX.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_163_4_h1T.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_164_4_UCT.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_16_4_eIY.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_165_4_R3Y.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_166_1_Amu.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_167_3_SfB.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_168_4_bws.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_169_5_olk.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_170_4_aQ0.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_171_3_coR.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_172_4_1M9.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_173_5_Fa3.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_174_5_I5i.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_175_4_QvP.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_17_5_ELI.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_176_4_vdb.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_177_4_sp7.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_178_1_eBl.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_179_3_GOk.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_180_7_vnc.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_181_1_zRJ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_182_3_kbg.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_183_2_Upe.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_18_3_9Fo.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_184_3_MoG.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_185_3_wp7.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_186_5_9Xz.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_187_3_On6.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_188_4_9JT.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_189_4_xrZ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_190_3_YcJ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_191_4_R03.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_192_4_MVG.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_193_4_kS2.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_19_4_2Nc.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_194_4_eF4.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_195_5_j5e.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_196_1_WcC.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_197_4_CI5.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_198_6_QQf.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_199_4_Mni.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_200_1_SnS.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_201_4_1aH.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_20_1_Lmo.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_202_3_Eyf.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_203_3_mrE.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_204_1_Csf.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_205_2_82U.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_206_2_VfU.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_207_2_H5B.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_208_3_oIC.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_209_1_vUd.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_210_1_3fd.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_211_2_Xim.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_212_3_a0y.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_21_2_3He.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_213_2_Fv2.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_214_2_g4X.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_215_3_zs8.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_216_2_9oc.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_217_3_B4Q.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_218_3_ef2.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_219_5_Nvw.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_220_2_g7X.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_221_2_peF.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_22_2_1Vx.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_222_3_pVO.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_223_3_NHp.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_224_3_D3B.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_225_3_jcr.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_226_3_UY0.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_227_2_X2B.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_228_3_dzm.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_229_2_8xG.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_230_2_DOC.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_231_2_O9R.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_23_1_DXZ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_232_3_DH2.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_233_3_K4N.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_234_3_QF1.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_235_3_DSO.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_236_2_VfF.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_237_3_RNF.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_238_3_PFr.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_239_3_YXU.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_240_2_rWa.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_241_2_GCK.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_242_3_7Kl.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_243_2_aet.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_244_3_mS2.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_245_3_Yse.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_246_3_Lor.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_24_6_z3i.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_247_2_Tj0.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_248_2_6zS.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_249_4_hKN.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_2_4_ztx.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_250_3_Syo.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_251_2_gLI.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_25_1_JiA.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_252_6_Cq5.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_253_3_HuA.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_254_4_sO7.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_255_3_v1f.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_256_2_dPT.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_257_4_j1v.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_258_3_DiG.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_259_3_3yK.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_260_3_Xw8.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_261_2_RFe.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_262_5_fF7.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_263_1_KgW.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_264_5_xKJ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_26_4_Vbv.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_265_1_7AH.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_266_3_ru3.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_267_5_Grq.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_268_2_2TF.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_269_3_RsJ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_270_6_FXH.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_271_4_cbt.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_272_2_rlI.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_273_2_DHK.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_27_3_yOQ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_274_4_tts.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_275_4_7u4.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_276_7_Xbx.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_277_6_fFe.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_278_4_MNz.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_279_3_5AG.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_280_5_9xv.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_281_5_JF7.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_282_5_8QJ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_283_4_ycL.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_284_4_NAi.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_285_4_AHI.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_286_1_gT1.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_28_6_o5O.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_287_5_ZiR.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_288_1_1Lo.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_289_1_KuN.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_290_4_tL2.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_291_4_nTK.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_292_1_dcR.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_293_2_C3x.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_294_1_Fg7.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_29_4_CcT.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_295_4_RiJ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_296_2_IlN.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_297_5_Wxt.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_298_4_YS8.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_299_5_hFt.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_300_2_G52.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_301_4_vEc.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_302_3_pty.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_303_5_paI.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_30_3_9aI.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_304_6_WAw.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_305_4_zEz.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_306_3_NcX.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_307_4_Dzg.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_308_5_Suq.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_309_4_ZBJ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_310_4_Emr.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_311_3_9rV.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_312_4_U8q.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_313_2_rX1.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_314_5_nAW.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_315_3_4bq.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_31_5_Ym5.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_316_3_8Up.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_317_3_x7U.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_318_3_Bb1.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_319_2_A0i.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_320_3_4rt.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_321_4_Bdu.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_322_3_91g.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_323_1_i8u.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_324_2_gxa.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_ETT_HS/patTuple_32_4_l9t.root',

    )
)

process.TFileService = cms.Service("TFileService", fileName = cms.string(

	'/lustre/cms/store/user/calabria/Data/SKIMMING/ETT/DYToEE_ett_HS/histo_DYToEE_ett_HS_1.root'

))

process.demo = cms.EDAnalyzer('SimpleCounter'
)


process.p = cms.Path(process.demo)
