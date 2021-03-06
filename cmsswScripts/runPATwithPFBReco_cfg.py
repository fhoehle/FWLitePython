import FWCore.ParameterSet.Config as cms
import sys
from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing ('analysis')
options.register ('eventsToProcess',
                   '',
                   VarParsing.multiplicity.list,
                   VarParsing.varType.string,
                   "Events to process")
options.register('runOnData',False,VarParsing.multiplicity.singleton,VarParsing.varType.bool,'runOnData')
options.register('runRange','',VarParsing.multiplicity.singleton,VarParsing.varType.string,'runRange used for running on data to estimate trigger')
print "args ",sys.argv
options.parseArguments()
import re
reRunRange = re.match('^([0-9]+)-([0-9]+)$',options.runRange)
print "options.runRange",options.runRange
minRun = None ; maxRun = None
if options.runOnData:
  if not reRunRange or len(reRunRange.groups()) != 2 :
    sys.exit('runRange wrong should be 123-234')
  minRun=int(reRunRange.group(1));maxRun=int(reRunRange.group(2))
process = cms.Process("PAT")

## MessageLogger
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100

## Options and Output Report
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

## Source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/mc/Summer12_DR53X/TTTT_TuneZ2star_8TeV-madgraph-tauola/AODSIM/PU_S10_START53_V7A-v1/00000/7083D246-AA0A-E211-ADA5-001E67397F26.root')
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
process.load("PhysicsTools.PatAlgos.patSequences_cff")

## Output Module Configuration (expects a path 'p')
from PhysicsTools.PatAlgos.patEventContent_cff import patEventContent
process.out = cms.OutputModule("PoolOutputModule",
                               fileName = cms.untracked.string('TTTT_TuneZ2star_8TeV-madgraph-tauola_patTuple.root'),
                               # save only events passing the full path
                               SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
                               # save PAT Layer 1 output; you need a '*' to
                               # unpack the list of commands 'patEventContent'
                               outputCommands = cms.untracked.vstring('drop *', *patEventContent )
                               )

process.outpath = cms.EndPath(process.out)
# load the PAT config
process.load("PhysicsTools.PatAlgos.patSequences_cff")
if options.runOnData:
  process.source.fileNames = cms.untracked.vstring('/store/data/Run2012A/MultiJet/AOD/22Jan2013-v1/20000/0036C47E-0B74-E211-B992-00266CF32684.root')
  process.out.fileName=cms.untracked.string('MultiJet-Run2012A_patTuple.root')
# Configure PAT to use PF2PAT instead of AOD sources
# this function will modify the PAT sequences.
from PhysicsTools.PatAlgos.tools.pfTools import *

postfix = "PFlow"
jetAlgo="AK5"
usePF2PAT(process,runPF2PAT=True, jetAlgo=jetAlgo, runOnMC=(not options.runOnData), postfix=postfix,jetCorrections=('AK5PFchs', ['L1FastJet','L2Relative','L3Absolute']) if not options.runOnData else ('AK5PFchs', ['L1FastJet','L2Relative','L3Absolute','L2L3Residual']) )

if options.runOnData:
  from PhysicsTools.PatAlgos.tools.coreTools import runOnData # replaced by usePF2PAT with runOnMC
  runOnData(process, names = [ 'PFAll' ] , postfix = postfix )


# to turn on type-1 MET corrections, use the following call
#usePF2PAT(process,runPF2PAT=True, jetAlgo=jetAlgo, runOnMC=True, postfix=postfix, typeIMetCorrections=True)

# to run second PF2PAT+PAT with different postfix uncomment the following lines
# and add the corresponding sequence to the path
#postfix2 = "PFlow2"
#jetAlgo2="AK7"
#usePF2PAT(process,runPF2PAT=True, jetAlgo=jetAlgo2, runOnMC=True, postfix=postfix2)

# to use tau-cleaned jet collection uncomment the following:
#getattr(process,"pfNoTau"+postfix).enable = True

# to switch default tau (HPS) to old default tau (shrinking cone) uncomment
# the following:
# note: in current default taus are not preselected i.e. you have to apply
# selection yourself at analysis level!
#adaptPFTaus(process,"shrinkingConePFTau",postfix=postfix)

# to use GsfElectrons instead of PF electrons
# useGsfElectrons(process,postfix)

# Let it run
process.p = cms.Path(
#    process.patDefaultSequence  
    getattr(process,"patPF2PATSequence"+postfix)
#    second PF2PAT
#    + getattr(process,"patPF2PATSequence"+postfix2)
)



# Add PF2PAT output to the created file
from PhysicsTools.PatAlgos.patEventContent_cff import patEventContentNoCleaning,patExtraAodEventContent
#process.load("CommonTools.ParticleFlow.PF2PAT_EventContent_cff")
#process.out.outputCommands =  cms.untracked.vstring('drop *')
process.out.outputCommands = cms.untracked.vstring('drop *',
                                                   'keep recoPFCandidates_particleFlow_*_*',
                                                   *(patEventContentNoCleaning+patExtraAodEventContent ))

#########################################################
#########################################################
########### configuration
#########################################################
#########################################################
# top projections in PF2PAT:
getattr(process,"pfNoPileUp"+postfix).enable = True
getattr(process,"pfNoMuon"+postfix).enable = True
getattr(process,"pfNoElectron"+postfix).enable = True
getattr(process,"pfNoTau"+postfix).enable = False
getattr(process,"pfNoJet"+postfix).enable = True

# verbose flags for the PF2PAT modules
getattr(process,"pfNoMuon"+postfix).verbose = False

# enable delta beta correction for muon selection in PF2PAT?
getattr(process,"pfIsolatedMuons"+postfix).doDeltaBetaCorrection = False

process.options.wantSummary = True
