import FWCore.ParameterSet.Config as cms
import sys
from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing ('analysis')
print "args ",sys.argv
options.parseArguments()
process = cms.Process("JetSkim")

## MessageLogger
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100

## Options and Output Report
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

## Source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/user/hoehle/SingleMu/BScSkim_SingleMuData/bd22b76fe02f0bcf6d005e3433b8e12b/MultiJet-Run2012A_patTuple_SingleMu__Run2012A-22Jan2013-v1__AOD_120_1_t6S.root')
)
## Maximal Number of Events
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

## Geometry and Detector Conditions (needed for a few patTuple production steps)
process.load("Configuration.Geometry.GeometryIdeal_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
#from Configuration.AlCa.autoCond import autoCond
#process.GlobalTag.globaltag = cms.string( autoCond[ 'startup' ] )
process.GlobalTag.globaltag = cms.string( 'START53_V27::All' )
process.load("Configuration.StandardSequences.MagneticField_cff")

## Standard PAT Configuration File
process.out = cms.OutputModule("PoolOutputModule",
                               fileName = cms.untracked.string('softJetSkim.root'),
                               # save only events passing the full path
                               SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
                               # save PAT Layer 1 output; you need a '*' to
                               # unpack the list of commands 'patEventContent'
                               outputCommands = cms.untracked.vstring('keep *')
                               )
process.outpath = cms.EndPath(process.out)
#############
process.mySoftJets = cms.EDFilter("PATJetSelector",
    src = cms.InputTag("selectedPatJetsPFlow"),
    cut = cms.string("pt > 15")
) 
process.softJetsCounter =  cms.EDFilter("PATCandViewCountFilter",
     minNumber = cms.uint32(4),     maxNumber = cms.uint32(999999),
     src = cms.InputTag("mySoftJets")
 )
# load the PAT config
# Let it run
process.p = cms.Path(
    process.mySoftJets*process.softJetsCounter  
)


process.options.wantSummary = True
