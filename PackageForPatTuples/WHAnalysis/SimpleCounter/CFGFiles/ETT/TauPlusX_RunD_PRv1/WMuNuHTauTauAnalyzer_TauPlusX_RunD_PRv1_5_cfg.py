import FWCore.ParameterSet.Config as cms

process = cms.Process("SimpleCounter")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 10000
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(

	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_489_2_sXz.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_490_2_w48.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_491_2_iSl.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_49_1_C21.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_492_2_8ZH.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_493_2_vTK.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_494_2_RwV.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_495_2_del.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_496_2_xd8.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_497_3_O8c.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_498_2_O4h.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_499_2_Hcl.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_500_2_D2G.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_501_2_MgE.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_50_1_v4X.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_502_2_BRl.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_503_2_0nw.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_504_2_aDX.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_505_2_a6X.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_506_2_5hH.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_507_2_ve9.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_508_2_Zdj.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_509_2_wLr.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_510_2_b8w.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_511_2_7lU.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_51_1_KZo.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_512_2_jpj.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_513_2_cKv.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_514_2_jz7.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_515_7_e3Y.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_516_2_1NB.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_517_6_yHW.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_518_2_Iqz.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_519_2_xFC.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_5_1_O82.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_520_2_Tkj.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_521_2_Qzm.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_52_1_Uue.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_522_2_JTq.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_523_2_AkU.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_524_2_PlV.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_525_2_shN.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_526_2_hau.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_527_4_tot.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_528_2_yyW.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_529_2_cNa.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_530_2_Uxq.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_53_1_1iM.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_531_2_8RE.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_532_2_cpo.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_533_2_nm8.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_534_2_7g7.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_535_2_nCf.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_536_2_gNT.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_537_3_zkY.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_538_2_cJa.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_539_2_NSX.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_540_2_hXU.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_541_2_xyk.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_54_1_PW3.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_542_2_Jh1.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_543_2_hMR.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_544_2_BxS.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_545_3_8lo.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_546_2_00Y.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_547_2_W70.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_548_2_FIR.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_549_2_1JX.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_550_2_cjw.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_551_3_SzG.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_55_1_bXH.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_552_2_07v.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_553_2_zwS.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_554_2_Bqd.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_555_2_P9e.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_556_2_QhH.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_557_2_bvm.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_558_2_wRU.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_559_2_U1U.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_560_2_laM.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_561_2_23U.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_56_1_qnh.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_562_2_ccx.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_563_2_OVf.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_564_3_grd.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_565_2_MRO.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_566_2_pqQ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_567_2_g9t.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_568_2_cx4.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_569_2_Lvu.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_570_2_Q2V.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_571_2_64R.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_57_1_dUV.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_572_2_zPg.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_573_2_cJ0.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_574_2_zkP.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_575_2_9ir.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_576_2_JUQ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_577_2_gMt.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_578_2_1z4.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_579_2_DdS.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_580_2_z9O.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_581_2_FqM.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_58_1_Sgs.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_582_2_5XT.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_583_2_3he.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_584_2_V1n.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_585_2_sIL.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_586_2_IPu.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_587_3_Sby.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_588_2_iKm.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_589_2_mGP.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_590_2_qpI.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_591_2_9mN.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_59_1_AaU.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_592_2_xXN.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_593_2_w0B.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_594_2_ODC.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_595_2_NKP.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_596_2_Ucc.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_597_2_P9e.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_598_2_tdf.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_599_2_cjT.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_600_2_YaO.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_601_2_QCy.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_60_1_Ew2.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_602_1_Po5.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_603_1_gYA.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_604_1_tTP.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_605_1_vkk.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_606_1_Pln.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_607_1_TTf.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_608_1_sLp.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_609_1_8Th.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_610_1_uE3.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_611_1_WB2.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_612_1_uuL.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_61_2_l64.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_613_1_EXJ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_614_1_fqO.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_615_1_w1A.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_616_1_v4j.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_617_1_Mm0.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_618_1_emC.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_619_1_BKK.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_6_1_WYb.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_620_1_7Qn.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_621_1_t4C.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_62_1_icS.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_622_1_W4U.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_623_1_u3l.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_624_1_wrJ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_625_1_SVL.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_626_1_0yR.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_627_1_rea.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_628_1_NcK.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_629_1_A4d.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_630_1_vbg.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_631_1_3M6.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_63_1_QTv.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_632_1_TpU.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_633_1_EUW.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_634_1_pM6.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_635_1_doI.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_636_1_IlQ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_637_1_ReJ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_638_1_uWD.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_639_1_K8J.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_640_1_yg6.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_641_1_qCZ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_64_1_5zC.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_642_2_rGZ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_643_2_QSM.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_644_1_JpK.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_645_1_BvW.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_646_1_sr7.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_647_1_11Z.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_648_1_30E.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_649_1_zFB.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_650_1_ZiB.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_651_1_b7T.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_65_1_2lS.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_652_1_eWc.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_653_1_CLS.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_654_1_MV6.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_655_1_ZlH.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_656_1_Vun.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_657_1_UHR.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_658_1_HKu.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_659_1_aFn.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_660_1_nyC.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_661_1_qRI.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_66_1_opm.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_662_1_a61.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_663_1_0ft.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_664_1_bA8.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_665_1_Y3y.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_666_1_mej.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_667_1_c7m.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_668_1_uCi.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_669_1_fUH.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_670_1_lNY.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_671_1_Qd8.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_67_1_809.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_672_1_HIC.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_673_1_wRB.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_674_1_cnu.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_675_1_DyK.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_676_1_AS8.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_677_1_EJO.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_678_1_abj.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_679_1_Ocz.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_680_1_ffW.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_681_2_XM4.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_68_1_t9d.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_682_1_drp.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_683_1_UX4.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_684_1_SA7.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_685_1_9ZW.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_686_1_L0h.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_687_1_fIS.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_688_1_5GC.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_689_1_esm.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_690_1_7TZ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_691_1_CjR.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_69_1_T4A.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_692_1_jOP.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_693_3_whx.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_694_1_p8P.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_695_1_4iD.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_696_1_OL5.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_697_1_RMW.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_698_3_pHx.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_699_2_H1C.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_700_2_HZb.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_701_1_VxK.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_70_1_d6R.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_702_1_9t1.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_703_2_vdV.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_704_1_3qY.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_705_1_C3P.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_706_2_bWA.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_707_1_pHl.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_708_2_5eg.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_709_1_pWh.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_710_1_GmA.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_711_1_qJv.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_71_1_dgV.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_712_1_1mD.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_713_1_VQG.root',

    )
)

process.TFileService = cms.Service("TFileService", fileName = cms.string(

	'/lustre/cms/store/user/calabria/Data/SKIMMING/ETT/TauPlusX_RunD_PRv1/histo_TauPlusX_RunD_PRv1_5.root'

))

process.demo = cms.EDAnalyzer('SimpleCounter'
)


process.p = cms.Path(process.demo)
