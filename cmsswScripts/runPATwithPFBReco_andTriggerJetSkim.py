### Generated by ConfigEditor ###
import sys
import os.path
sys.path.append(os.path.abspath(os.path.expandvars(os.path.join('$CMSSW_BASE','FWLitePython/cmsswScripts'))))
sys.path.append(os.path.abspath(os.path.expandvars(os.path.join('$CMSSW_RELEASE_BASE','FWLitePython/cmsswScripts'))))
### ------------------------- ###

from runPATwithPFBReco_cfg import *

### Generated by ConfigEditor ###
if hasattr(process,'resetHistory'): process.resetHistory()
### ------------------------- ###
#################################
#################################
process.source.fileNames = ['/store/data/Run2012B/SingleMu/AOD/22Jan2013-v1/110000/0C57EA77-AEE3-E211-8DCA-00259073E4D4.root']
###############################
#################################
import runPATwithPFBReco_andTriggerSkim 
triggersUsedForAnalysis = runPATwithPFBReco_andTriggerSkim.triggersUsedForAnalysis
process.triggerCheck = runPATwithPFBReco_andTriggerSkim.triggerCheck
process.p.insert(0,process.triggerCheck)
import softJetSkim_cfg
process.mySoftJets = softJetSkim_cfg.mySoftJets
process.softJetsCounter =  softJetSkim_cfg.softJetsCounter
process.p += process.mySoftJets
process.p += process.softJetsCounter


