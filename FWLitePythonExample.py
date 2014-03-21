import ROOT
from DataFormats.FWLite import Events,Handle
muonsLabel  = "selectedPatMuonsPFlow"
muonsHandle = Handle("vector<pat::Muon>")
muonsPtHist = ROOT.TH1D("muonsPtHist","muonsPtHist",200,0,200)
####
events = Events('/user/hoehle/CMSSW_5_3_16/FWLitePython/cmsswScripts/MultiJet-Run2012A_patTuple.root')
###
for i,event in enumerate(events):
  event.getByLabel(muonsLabel,muonsHandle)
  muons = muonsHandle.product()
  for muon in muons:
    muonsPtHist.Fill(muon.pt())
  if i%100 == 0:
    print "processed ",i+1," events"
##############
muonsPtHist.SaveAs(muonsPtHist.GetName()+'.root')
