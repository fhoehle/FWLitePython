import ROOT
from DataFormats.FWLite import Events,Handle
muonsLabel  = "selectedPatMuonsPFlow"
muonsHandle = Handle("vector<pat::Muon>")
muonsPtHist = ROOT.TH1D("muonsPtHist","muonsPtHist",200,0,200)
jetsLabel = "selectedPatJetsPFlow"
jetsHandle = Handle("vector<pat::Jet>")
####
#events = Events('/user/hoehle/CMSSW_5_3_16/FWLitePython/cmsswScripts/MultiJet-Run2012A_patTuple.root')
#events = Events('dcap://grid-dcap-extern.physik.rwth-aachen.de/pnfs/physik.rwth-aachen.de/cms/store/user/hoehle/SingleMu/BScSkim_SingleMuData/bd22b76fe02f0bcf6d005e3433b8e12b/MultiJet-Run2012A_patTuple_SingleMu__Run2012A-22Jan2013-v1__AOD_120_1_t6S.root')
events = Events('dcap://grid-dcap-extern.physik.rwth-aachen.de/pnfs/physik.rwth-aachen.de/cms/store/user/fhohle/TTJets_SemiLeptMGDecays_8TeV-madgraph-tauola/BScSkim_TTJets_semiLep_2014-06-02_11-12-02/6eea63ca40c7f36421b750ebc0e3ead7/TTTT_TuneZ2star_8TeV-madgraph-tauola_patTuple_TTJets_SemiLeptMGDecays_8TeV-madgraph-tauola__Summer12_DR53X-PU_S10_START53_V7C-v1__AODSIM_10_3_7rD.root')
###
#
maxEvents=100
eventsPassSoftJetSel = 0
eventsPassHardJetSel = 0
for i,event in enumerate(events):
  if maxEvents <= i:
    break
  #event.getByLabel(muonsLabel,muonsHandle)
  #muons = muonsHandle.product()
  #for muon in muons:
  #  muonsPtHist.Fill(muon.pt())
  event.getByLabel(jetsLabel,jetsHandle);jets = jetsHandle.product()
  softJets = 0; hardJets = 0;
  for jet in jets:
    if jet.pt() > 15:
      softJets += 1
    if jet.pt() > 20:
      hardJets += 1
  if softJets >= 4:
    eventsPassSoftJetSel += 1
  if hardJets >= 5:
    eventsPassHardJetSel += 1
  if i%100 == 0:
    print "processed ",i+1," events"
##############
print "totalevents ",i," eventsPassSoftJetSel ",eventsPassSoftJetSel," eventsPassHardJetSel ", eventsPassHardJetSel
#muonsPtHist.SaveAs(muonsPtHist.GetName()+'.root')
