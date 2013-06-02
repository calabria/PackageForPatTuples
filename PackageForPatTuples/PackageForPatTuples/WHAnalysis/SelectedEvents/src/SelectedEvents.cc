// -*- C++ -*-
//
// Package:    SelectedEvents
// Class:      SelectedEvents
// 
/**\class SelectedEvents SelectedEvents.cc WHAnalysis/SelectedEvents/src/SelectedEvents.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cesare Calabria
//         Created:  Sun Jul 10 18:27:48 CEST 2011
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Tau.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/MuonReco/interface/MuonSelectors.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "DataFormats/Common/interface/Ref.h"
#include "DataFormats/METReco/interface/PFMET.h"
#include "DataFormats/METReco/interface/PFMETFwd.h"
#include "DataFormats/PatCandidates/interface/MET.h"


#include <fstream>
#include <sstream>
//
// class declaration
//

class SelectedEvents : public edm::EDAnalyzer {
   public:
      explicit SelectedEvents(const edm::ParameterSet&);
      ~SelectedEvents();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() ;
      virtual void analyze(const edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;

      virtual void beginRun(edm::Run const&, edm::EventSetup const&);
      virtual void endRun(edm::Run const&, edm::EventSetup const&);
      virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
      virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);

      std::string path_;
      edm::InputTag muonSrc_;
      edm::InputTag eleSrc_;
      edm::InputTag tauSrc_;
      edm::InputTag jetSrc_;
      edm::InputTag PFMetTag_;

      // ----------member data ---------------------------
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
SelectedEvents::SelectedEvents(const edm::ParameterSet& iConfig):
	path_(iConfig.getUntrackedParameter<std::string>("path","/cmshome/calabria/")),
      	muonSrc_(iConfig.getUntrackedParameter<edm::InputTag>("muonSrc")),
      	eleSrc_(iConfig.getUntrackedParameter<edm::InputTag>("eleSrc")),
      	tauSrc_(iConfig.getUntrackedParameter<edm::InputTag>("tauSrc")),
  	jetSrc_(iConfig.getUntrackedParameter<edm::InputTag>("jetSrc")),
  	PFMetTag_(iConfig.getUntrackedParameter<edm::InputTag> ("PFMetTag"))
{
   //now do what ever initialization is needed

}


SelectedEvents::~SelectedEvents()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
SelectedEvents::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;

  std::ofstream selEvents;
  std::stringstream txtName;
  int run = iEvent.id().run();
  int event = iEvent.id().event();
  txtName<<path_<<"run_"<<run<<"__event_"<<event<<".txt";
  std::string txt = txtName.str();
  selEvents.open(txt.c_str());
  std::cout<<iEvent.id()<<std::endl;
  selEvents<<iEvent.id()<<std::endl;

  edm::Handle<pat::METCollection> pfmet;
  iEvent.getByLabel(PFMetTag_, pfmet);

  double met = pfmet->front().et();

  std::cout<<"mva met: "<<met<<std::endl;

  edm::Handle<edm::View<pat::Muon> > muons;
  iEvent.getByLabel(muonSrc_,muons);
  for(edm::View<pat::Muon>::const_iterator muon=muons->begin(); muon!=muons->end(); ++muon){

	double muonpt = muon->pt();
	//double muonphi = muon->phi();
	double muoneta = muon->eta();
	double muoniso = muon->userFloat("PFRelIsoDB04v2");
	double iso2 = (muon->chargedHadronIso() + std::max(0.0, muon->neutralHadronIso() + muon->photonIso() - 0.5 * muon->puChargedHadronIso()))/muon->pt();
	//std::cout<<"muon pt: "<<muonpt<<" muon eta: "<<muoneta<<" muon iso: "<<muoniso<<" iso pat: "<<iso2<<std::endl;

  }

  edm::Handle<edm::View<pat::Electron> > electrons;
  iEvent.getByLabel(eleSrc_,electrons);
  for(edm::View<pat::Electron>::const_iterator electron=electrons->begin(); electron!=electrons->end(); ++electron){

	double elept = electron->pt();
	//double elephi = electron->phi();
	double eleeta = electron->eta();
	double eleiso = electron->userFloat("PFRelIsoDB04");
	double mva1 = electron->userFloat("mvaPOGNonTrig");
	double mva2 = electron->electronID("mvaNonTrigV0");
	double iso2 = (electron->chargedHadronIso() + std::max(0.0, electron->neutralHadronIso() + electron->photonIso() - 0.5 * electron->puChargedHadronIso()))/electron->pt();
	//std::cout<<"electron pt: "<<elept<<" electron eta: "<<eleeta<<" electron iso: "<<eleiso<<" iso pat: "<<iso2<<std::endl;
	//std::cout<<"electron pt: "<<elept<<" electron eta: "<<eleeta<<" mva: "<<mva1<<" mva pat: "<<mva2<<std::endl;

  }

  edm::Handle<edm::View<pat::Tau> > taus;
  iEvent.getByLabel(tauSrc_,taus);
  for(edm::View<pat::Tau>::const_iterator patTau=taus->begin(); patTau!=taus->end(); ++patTau){

	double taupt = patTau->pt();
	//double tauphi = patTau->phi();
	double taueta = patTau->eta();
	int tauiso = patTau->tauID("byLooseIsolation");
	int tauIsoLooseDB = patTau->tauID("byLooseCombinedIsolationDeltaBetaCorr");
	int tauIsoMediumDB = patTau->tauID("byMediumCombinedIsolationDeltaBetaCorr");
	int tauIsoTightDB = patTau->tauID("byTightCombinedIsolationDeltaBetaCorr");
	int tauID = patTau->tauID("decayModeFinding");
	//std::cout<<"Tau pt: "<<taupt<<" Tau eta: "<<taueta<<" ID: "<<tauID<<" Tau isoLoose: "<<tauIsoLooseDB<<" Tau isoMedium: "<<tauIsoMediumDB<<" Tau isoTight "<<tauIsoTightDB<<std::endl;
	//selEvents<<"Tau pt: "<<taupt<<" Tau eta: "<<taueta<<" ID: "<<tauID<<" Tau isoLoose: "<<tauIsoLooseDB<<" Tau isoMedium: "<<tauIsoMediumDB<<" Tau isoTight "<<tauIsoTightDB<<std::endl;


  }

  edm::Handle<pat::JetCollection> patJets;
  iEvent.getByLabel(jetSrc_, patJets);
  for(std::vector<pat::Jet>::const_iterator patJet = patJets->begin(); patJet != patJets->end(); ++patJet){

	//selEvents<<"Jet Pt: "<<patJet->pt()<<" Jet Et: "<<patJet->et()<<" Jet eta: "<<patJet->eta()<<" BTag: "<<patJet->bDiscriminator("combinedSecondaryVertexBJetTags")<<std::endl;

  }

  selEvents.close();

}


// ------------ method called once each job just before starting event loop  ------------
void 
SelectedEvents::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
SelectedEvents::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
void 
SelectedEvents::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
SelectedEvents::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
SelectedEvents::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
SelectedEvents::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
SelectedEvents::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(SelectedEvents);
