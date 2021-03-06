import FWCore.ParameterSet.Config as cms

process = cms.Process("SimpleCounter")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 10000
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(

	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_100_4_llw.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_101_1_AP6.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_10_1_b6G.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_102_5_k1w.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_103_4_15z.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_104_5_JVb.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_105_5_ao0.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_106_6_ppD.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_107_5_HbK.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_108_5_fRD.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_109_5_J86.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_110_4_HRC.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_111_4_NVn.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_11_1_mKp.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_112_5_49t.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_113_5_zBq.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_114_5_m6X.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_115_3_hkI.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_116_1_Zue.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_117_3_Ud9.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_118_5_OGG.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_119_5_eC9.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_1_1_XqD.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_120_5_paQ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_121_4_qnT.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_122_5_aqO.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_12_2_ITO.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_123_5_Xj4.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_124_4_slY.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_125_5_3Nq.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_126_4_88F.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_127_6_O2s.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_128_4_M5K.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_129_4_C2F.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_130_4_4KW.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_131_4_7A6.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_132_5_F05.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_133_4_QrD.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_13_3_iUN.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_134_5_2as.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_135_5_PYX.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_136_1_eeI.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_137_5_GmX.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_138_5_qrs.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_139_5_ljv.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_140_5_1to.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_141_3_4qz.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_142_6_VjJ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_143_4_Vz2.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_14_3_FGT.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_144_5_aGy.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_145_4_55Y.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_146_5_Yo2.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_147_5_tkM.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_148_5_Hew.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_149_5_BG5.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_150_5_kL0.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_151_5_lXg.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_152_1_5yU.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_153_4_4g2.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_15_3_K1A.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_154_4_IlG.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_155_5_mg9.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_156_3_Ahb.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_157_6_lmY.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_158_4_vts.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_159_4_kfM.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_160_6_rp7.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_161_5_a7F.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_16_1_pXh.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_162_5_doB.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_163_5_wAl.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_164_6_hHW.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_165_5_bOT.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_166_3_j0G.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_167_6_Mpb.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_168_5_NGq.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_169_4_GTF.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_170_4_L2k.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_171_5_jX8.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_17_1_mWq.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_172_5_puD.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_173_5_K4L.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_174_5_Tgy.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_175_5_mGI.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_176_5_Hg6.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_177_5_C0I.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_178_5_ZdL.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_179_4_F7e.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_180_5_Qc8.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_181_5_ZSs.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_182_4_OEg.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_18_2_ox8.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_183_4_dd3.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_184_5_6C7.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_185_4_2We.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_186_4_1kx.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_187_5_73Q.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_188_5_k5s.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_189_4_Qva.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_190_5_stz.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_191_5_B0m.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_192_5_GSB.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_193_5_aXo.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_194_5_QrN.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_195_1_GwO.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_19_5_fyh.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_196_4_Rh1.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_197_4_kfC.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_198_3_Yy8.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_199_3_LV4.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_200_4_GCj.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_201_3_xjy.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_202_1_d20.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_20_2_Vcu.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_203_1_mur.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_204_1_E1n.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_205_1_eXl.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_206_1_FAH.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_207_3_Zko.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_208_1_2Wa.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_209_2_BtW.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_210_4_7Px.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_211_2_eHv.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_21_1_fiq.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_212_2_bXF.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_213_1_SCS.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_214_1_9cY.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_215_2_ucO.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_216_3_b3J.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_217_4_uku.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_218_1_PVj.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_219_1_jNp.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_220_3_Zkh.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_221_2_dOm.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_222_2_5pH.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_22_2_5G5.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_223_2_baZ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_224_3_MEU.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_225_1_v3G.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_226_1_U04.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_227_1_Irf.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_228_3_8A9.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_229_3_Vu3.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_230_2_rgp.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_23_1_06G.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_231_3_WDZ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_232_1_y5O.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_233_3_Tsx.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_234_4_MZ4.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_235_1_Mh9.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_236_4_wsn.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_237_1_J4s.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_238_3_qiy.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_239_4_QPB.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_240_3_QLW.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_241_2_bma.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_242_3_w4F.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_243_1_hWP.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_24_3_dWN.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_244_7_Wmp.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_245_4_u20.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_246_3_FjL.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_247_3_6Vo.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_248_2_Ax3.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_249_1_HdQ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_250_3_FGs.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_251_2_H9e.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_252_3_lPq.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_25_2_Duz.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_253_2_8Zc.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_254_3_KOd.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_255_4_UGn.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_256_3_DuS.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_257_1_YcS.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_258_5_KA5.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_259_1_3HL.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_2_5_IxF.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_260_1_PtC.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_261_1_Nto.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_262_1_CKq.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_263_5_rAI.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_26_3_yQQ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_264_3_eD8.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_265_1_p93.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_266_5_d8E.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_267_3_baQ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_268_3_i24.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_269_5_oEU.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_270_5_wjt.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_271_1_rmV.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_272_1_dFE.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_273_4_IKs.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_274_3_ewE.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_275_3_V5U.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_27_5_hzD.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_276_2_KNK.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_277_2_iv9.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_278_5_6nS.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_279_3_VhC.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_280_3_EVY.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_281_2_qFJ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_282_5_ny7.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_283_4_igK.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_28_3_eXV.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_284_5_fvW.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_285_5_9AS.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_286_5_upT.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_287_3_xgZ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_288_3_2lm.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_289_2_pPc.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_290_2_swR.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_291_3_UxW.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_292_5_EIL.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_293_5_Wc9.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_29_3_ZUA.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_294_2_qCW.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_295_5_VBt.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_296_2_6Dl.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_297_3_j2n.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_298_5_CiW.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_299_3_pBZ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_300_1_q8W.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_301_1_L92.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_302_1_nuJ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_303_3_M7T.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_30_3_hU7.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_304_5_jXl.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_305_3_sd3.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_306_3_rXf.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_307_1_Vb1.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_308_3_6rP.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_309_3_rOE.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_310_3_dlc.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_311_3_qKU.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_312_2_V6F.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_313_3_oUv.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_31_3_afn.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_314_5_YOG.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_315_3_DRj.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_316_5_evI.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_317_4_2tx.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_318_3_cNr.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_319_2_9GM.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_320_1_hMB.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_321_2_3kx.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_322_2_I2B.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_323_3_6cS.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_324_2_MCB.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToEE_MTT_HS/patTuple_325_3_sJ9.root',

    )
)

process.TFileService = cms.Service("TFileService", fileName = cms.string(

	'/lustre/cms/store/user/calabria/Data/SKIMMING/ETT/DYToEE_mtt_HS/histo_DYToEE_mtt_HS_1.root'

))

process.demo = cms.EDAnalyzer('SimpleCounter'
)


process.p = cms.Path(process.demo)
