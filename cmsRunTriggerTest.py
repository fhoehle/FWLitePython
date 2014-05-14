import FWCore.ParameterSet.Config as cms
import sys

process = cms.Process("TrigTest")


process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 10000
 
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)
process.source = cms.Source("PoolSource",
    noEventSort = cms.untracked.bool(True),
    skipEvents = cms.untracked.uint32(0),
    duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
    fileNames = cms.untracked.vstring('file:/user/Samples/Data_Run2012A_MultiJet/0036C47E-0B74-E211-B992-00266CF32684.root')
)
 
process.triggerCheck = cms.EDFilter("TriggerResultsFilter",
    l1tIgnoreMask = cms.bool(False),
    l1tResults = cms.InputTag(""),
    l1techIgnorePrescales = cms.bool(False),
    hltResults = cms.InputTag("TriggerResults","","HLT"),
    triggerConditions = cms.vstring('HLT_Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*'),
    throw = cms.bool(False),
    daqPartitions = cms.uint32(1)
)

process.testPath = cms.Path(process.triggerCheck)

if not 'crab' in sys.argv[0]:
  from FWCore.ParameterSet.VarParsing import VarParsing
  options = VarParsing ('analysis')
  options.parseArguments()
  if options.inputFiles != cms.untracked.vstring():
    process.source.fileNames=options.inputFiles

