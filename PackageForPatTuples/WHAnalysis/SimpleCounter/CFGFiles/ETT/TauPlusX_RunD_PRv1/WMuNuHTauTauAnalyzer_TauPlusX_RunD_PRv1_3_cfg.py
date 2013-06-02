import FWCore.ParameterSet.Config as cms

process = cms.Process("SimpleCounter")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 10000
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(

	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1449_1_ChL.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1450_1_AOp.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1451_1_QvG.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_145_1_Wc0.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1452_1_jYF.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1453_1_T2v.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1454_1_bwS.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1455_1_j0G.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1456_1_8lN.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1457_1_JUa.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1458_1_vRa.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1459_1_3cF.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1460_1_bgO.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1461_2_Krb.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_146_1_uGS.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1462_1_NJQ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1463_1_sre.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1464_3_5Ip.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1465_1_ucK.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1466_1_EAE.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1467_1_0iE.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1468_1_CDo.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1469_1_6aD.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1470_1_rif.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1471_2_cKp.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_147_1_HBA.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1472_1_WND.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1473_1_zby.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1474_1_tOx.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1475_1_qYB.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1476_2_7UO.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1477_1_Ezd.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1478_1_RIL.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1479_1_RIG.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1480_1_E9S.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1481_1_0SG.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_148_1_WMe.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1482_1_18G.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1483_1_Pic.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1484_2_XA5.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1485_1_K9O.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1486_1_L40.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1487_1_T9I.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1488_1_p3F.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1489_1_gWZ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1490_1_hud.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1491_1_CJg.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_149_1_bpo.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1492_1_bCZ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1493_1_DpD.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1494_1_EHq.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1495_1_fkE.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1496_1_Zku.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1497_1_eMA.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1498_1_Ctu.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1499_1_M0b.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1500_1_7cD.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1501_1_cRR.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_150_1_BzQ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1502_1_LRT.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1503_1_mC0.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1504_1_ygW.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1505_1_HgA.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1506_1_gKm.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1507_1_GES.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1508_1_3EC.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1509_2_SPU.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1510_2_bxz.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1511_1_tnT.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_151_1_XCF.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1512_1_rP2.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1513_1_wYm.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1514_1_uHn.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1515_1_2Hm.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1516_1_gE4.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1517_2_u3P.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1518_1_eBY.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1519_1_AOH.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_15_1_Pd6.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1520_1_2sg.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1521_1_KWL.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_152_1_CFZ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1522_1_i98.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1523_1_EGg.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1524_3_apO.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1525_1_s0f.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1526_1_H9T.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1527_1_k8z.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1528_2_AMR.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1529_1_Pin.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1530_2_jA4.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1531_1_uWR.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_153_1_j3w.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1532_1_5qk.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1533_1_RoM.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1534_1_kNB.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1535_1_Jx0.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1536_1_CSd.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1537_1_agF.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1538_1_nvK.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1539_1_UPG.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1540_1_8wb.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1541_1_5iI.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_154_1_oYj.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1542_1_Kmc.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1543_1_s1H.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1544_0_GRu.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1545_0_DSi.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1546_0_HsK.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1547_0_l5g.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1548_0_M2N.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1549_0_9bn.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1550_0_OvX.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1551_0_Jsw.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_155_1_Rt1.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1552_0_WdX.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1553_0_WKB.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1554_0_49e.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1555_0_KEL.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1556_0_k98.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1557_0_Quw.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1558_0_v3b.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1559_0_kyb.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1560_0_UAB.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1561_0_KXV.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_156_1_JQk.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1562_0_T5K.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1563_0_Ppo.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1564_0_LQM.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1565_0_G74.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1566_0_qdc.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_1567_0_2F1.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_157_1_NWm.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_158_1_X9a.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_159_1_1U7.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_160_1_oWd.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_161_1_LLi.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_16_1_B86.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_162_1_Sk2.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_163_1_quK.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_164_1_E3w.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_165_1_vs5.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_166_1_0fi.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_167_1_4VB.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_168_1_gMO.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_169_1_xsT.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_170_1_kWH.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_171_1_VV2.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_17_1_kpG.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_172_1_tC4.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_173_1_wD5.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_174_1_gwx.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_175_1_zCO.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_176_1_tx6.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_177_1_n8q.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_178_1_swz.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_179_1_0B7.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_180_1_VAi.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_181_1_5v6.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_18_1_oQv.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_182_1_t2i.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_183_1_4fh.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_184_1_vhr.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_185_1_TdZ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_186_1_1No.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_187_1_ZWI.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_188_1_PFD.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_189_1_B0j.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_190_1_tyw.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_191_1_Qbj.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_19_1_xRJ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_192_1_BP8.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_193_1_jkf.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_194_1_Kse.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_195_1_Ak2.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_196_2_Jc6.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_197_1_VIo.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_198_1_B4V.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_199_1_xMz.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_200_1_VBT.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_20_1_18s.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_201_2_0Xp.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_202_1_2D3.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_203_1_SyC.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_204_1_e0n.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_205_2_R0Z.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_206_1_sMu.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_207_1_0tc.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_208_1_dHl.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_209_2_Ksk.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_210_1_oue.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_211_1_a8i.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_21_1_z2Q.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_212_1_UXI.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_213_1_vJ0.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_214_1_cKa.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_215_1_ICU.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_216_1_gTS.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_217_1_29p.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_218_1_alD.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_219_1_Td5.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_2_1_Bby.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_220_1_4Ch.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_221_1_ShU.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_22_1_nUb.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_222_1_Mk9.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_223_1_kGZ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_224_1_cbt.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_225_1_5ih.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_226_1_jH5.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_227_1_Faz.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_228_1_ihG.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_229_1_rQE.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_230_1_cg0.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_231_1_6jo.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_23_1_Yuh.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_232_1_TMG.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_233_1_kfc.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_234_1_AHP.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_235_1_crZ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_236_1_Jbq.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_237_1_B73.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_238_1_WHe.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_239_1_cTG.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_240_1_1j3.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_241_1_lI9.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_24_1_lkL.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_242_1_rTR.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_243_2_S06.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_244_1_PSA.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_245_1_GHF.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_246_1_45D.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_247_1_SV6.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_248_1_2yj.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_249_1_Cu0.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_250_1_3WP.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_251_1_jGf.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_25_1_uul.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_252_1_hP9.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_253_1_eWw.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_254_1_WqJ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_255_1_vqx.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_256_1_5qH.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_257_1_DWZ.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_258_1_GBH.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_259_1_bzR.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_260_1_usE.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_261_1_5UM.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_26_1_puy.root',
	'file:/lustre/cms/store/user/calabria/Data/PatTuples_WH_3Jan2013_Data/TauPlusX_RunD_PRv1/patTuple_262_1_YR5.root',

    )
)

process.TFileService = cms.Service("TFileService", fileName = cms.string(

	'/lustre/cms/store/user/calabria/Data/SKIMMING/ETT/TauPlusX_RunD_PRv1/histo_TauPlusX_RunD_PRv1_3.root'

))

process.demo = cms.EDAnalyzer('SimpleCounter'
)


process.p = cms.Path(process.demo)
