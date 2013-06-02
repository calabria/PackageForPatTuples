import FWCore.ParameterSet.Config as cms

process = cms.Process("SimpleCounter")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 10000
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(

	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_550_2_xhy.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_551_2_74k.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_552_2_vrs.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_55_2_HCY.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_553_2_F8a.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_554_2_68H.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_555_2_99N.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_556_2_osk.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_557_2_i4q.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_558_2_Nzn.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_559_2_bI7.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_560_2_fE6.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_561_2_yK1.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_562_2_50U.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_56_2_K9R.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_563_3_Fb5.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_564_2_0vM.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_565_2_ofB.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_566_2_AsE.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_567_2_VQG.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_568_2_xJj.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_569_2_J3P.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_570_2_gMi.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_571_2_FFi.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_572_2_Fhm.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_57_2_a22.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_573_2_amD.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_574_2_1BR.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_575_2_Syz.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_576_2_861.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_577_2_z5h.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_578_2_dUh.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_579_2_dU6.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_580_2_Zsz.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_581_2_Ryr.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_582_2_X7A.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_58_2_HdB.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_583_2_Otd.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_584_2_0KT.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_585_2_mQq.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_586_3_Jzb.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_587_3_53F.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_588_3_2Xe.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_589_3_ZTR.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_590_2_Q9c.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_591_3_Fdf.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_592_3_JAH.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_59_2_wqv.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_593_4_lBK.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_594_3_jjz.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_595_3_6c2.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_596_3_PlL.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_597_3_ktr.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_598_3_nCJ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_599_3_fiR.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_600_2_566.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_601_3_2n6.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_602_3_9Qy.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_60_2_MJV.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_603_2_oum.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_604_2_Pdb.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_605_2_c0q.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_606_2_Kck.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_607_2_1JL.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_608_2_0d2.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_609_2_nmP.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_610_2_Tyi.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_611_2_Wln.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_612_2_mYH.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_61_2_TXZ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_613_2_ryW.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_614_2_vPX.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_615_2_jdt.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_616_2_zuv.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_617_2_R1A.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_618_2_v0T.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_619_2_noB.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_620_2_dhQ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_621_2_b0g.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_622_2_ezU.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_62_2_TZ8.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_623_2_Ew4.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_624_2_DMW.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_625_2_Jyf.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_626_2_aQw.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_627_2_iVy.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_628_2_X4u.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_629_2_aMN.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_630_2_ykK.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_631_2_vUn.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_632_2_NWj.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_63_2_TUP.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_633_2_OEz.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_634_2_p4c.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_635_2_obb.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_636_2_TP3.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_637_2_56q.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_638_2_ysG.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_639_2_0aQ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_640_2_lQ6.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_641_2_tzc.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_642_2_wvD.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_64_2_94b.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_643_3_yVS.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_644_2_OgI.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_645_2_wKA.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_646_2_Kkn.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_647_2_nij.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_648_2_yPP.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_649_2_MWi.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_6_4_Zij.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_650_2_6oA.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_651_2_s9U.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_652_2_gC4.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_65_2_A6O.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_653_2_Rz5.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_654_2_kM7.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_655_2_VSa.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_656_2_xlb.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_657_2_OEt.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_658_2_Y8K.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_659_2_cNB.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_660_2_nxk.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_661_2_EXc.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_662_2_hIL.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_66_2_mys.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_663_2_SSm.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_664_2_bqC.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_665_2_QWL.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_666_2_EBK.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_667_2_Y9i.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_668_2_3lX.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_669_2_1Hm.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_670_2_f6N.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_671_3_3uL.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_672_2_Ys3.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_67_2_sZp.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_673_2_5k2.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_674_2_PTl.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_675_3_nKi.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_676_2_pvU.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_677_3_rtB.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_678_3_KRc.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_679_3_8jS.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_680_2_CaO.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_681_3_YfI.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_682_3_VMW.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_68_2_Uvk.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_683_3_Tzm.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_684_3_MQS.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_685_3_RrK.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_686_3_1do.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_687_4_qcz.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_688_3_4fD.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_689_4_EzZ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_690_3_nIJ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_691_3_nYG.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_69_2_2E8.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_692_4_aNI.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_693_3_sRg.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_694_4_QOg.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_695_4_s4F.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_696_4_JHb.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_697_3_5rB.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_698_3_7DQ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_699_3_eh4.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_700_2_jR9.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_701_2_0T9.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_702_2_YwJ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_70_2_r8u.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_703_2_b35.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_704_2_Qhw.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_705_2_xaJ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_706_2_zjR.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_707_2_UW6.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_708_3_UAu.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_709_2_G3V.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_710_2_wRq.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_711_2_Xlr.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_712_2_YNw.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_71_2_EY4.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_713_2_kNP.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_714_2_I9O.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_715_2_wOg.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_716_2_4dZ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_717_2_VPo.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_718_2_K8z.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_719_2_Kc9.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_720_2_BPs.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_721_2_3OW.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_722_2_i3O.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_72_2_5Km.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_723_2_uj8.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_724_2_azK.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_725_2_JL9.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_726_3_HFF.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_727_3_7dB.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_728_3_oDq.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_729_3_RDO.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_730_2_jgV.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_731_3_j2t.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_732_3_evj.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_73_2_fZ8.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_733_3_Swt.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_734_3_9dV.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_735_3_bdg.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_736_4_4f3.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_737_3_RUb.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_738_4_PFo.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_739_4_Ooy.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_7_3_Anz.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_740_4_R5s.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_741_4_ME0.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_742_3_0ZH.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_74_2_kct.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_743_4_r5h.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_744_4_cIw.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_745_3_l6k.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_746_3_2jY.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_747_3_A9o.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_748_3_who.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_749_3_giq.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_750_3_dK4.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_751_4_nBz.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_752_3_XQ1.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_75_2_WjU.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_753_3_rBz.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_754_3_lHw.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_755_3_swM.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_756_3_Kco.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_757_3_9S6.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_758_4_8sx.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_759_3_QYg.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_760_3_SbF.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_761_3_RWD.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_762_3_jkl.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_76_2_c4B.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_763_3_PwP.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_764_3_StI.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_765_3_zfe.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_766_3_otQ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_767_3_DW9.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_768_3_Rv9.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_769_3_xmQ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_770_3_cjx.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_771_3_iSN.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_772_3_FHs.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_77_2_RTb.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_773_3_iwg.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_MC/DYToTauTau_MTT_HS/patTuple_774_3_vyY.root',

    )
)

process.TFileService = cms.Service("TFileService", fileName = cms.string(

	'/lustre/cms/store/user/calabria/Data/SKIMMING/ETT/DYToTauTau_mtt_HS/histo_DYToTauTau_mtt_HS_3.root'

))

process.demo = cms.EDAnalyzer('SimpleCounter'
)


process.p = cms.Path(process.demo)
