import ROOT
from DataFormats.FWLite import Events,Handle
muonsLabel  = "selectedPatMuonsPFlow"
muonsHandle = Handle("vector<pat::Muon>")
muonsPtHist = ROOT.TH1D("muonsPtHist","muonsPtHist",200,0,200)
####
events = Events('/user/hoehle/CMSSW_5_3_16/FWLitePython/cmsswScripts/MultiJet-Run2012A_patTuple.root')
###
TrigResultslabel=("TriggerResults");TrigResultshandle=Handle("edm::TriggerResults") 
##
for i,event in enumerate(events):
  event.getByLabel(muonsLabel,muonsHandle)
  event.getByLabel((TrigResultslabel,"","HLT"),TrigResultshandle); TrigResults=TrigResultshandle.product()
  TriggerNames=event.object().triggerNames(TrigResults)
  ############### find correct trigger version
  triggerName = "HLT_IsoMu24_eta2p1_v"
  availTrigger=(" ".join([ tr for tr in TriggerNames.triggerNames() if triggerName in tr])).strip()
  ######################## check trigger
  print triggerName," found ",availTrigger," index ",TriggerNames.triggerIndex(availTrigger)
  if TrigResults[TriggerNames.triggerIndex(availTrigger)].accept():
    print availTrigger," was accepted"
  ################
  muons = muonsHandle.product()
  for muon in muons:
    muonsPtHist.Fill(muon.pt())
  if i%100 == 0:
    print "processed ",i+1," events"
##############
muonsPtHist.SaveAs(muonsPtHist.GetName()+'.root')
