#!/usr/bin/env python
# run cmssw analysis
import FWCore.ParameterSet.Config as cms
import os
import sys
sys.path.append(os.getenv('CMSSW_BASE')+'/MyCMSSWAnalysisTools/Tools')
import  cmsswAnalysisTools
import samples
print "executing "," ".join(sys.argv)
cfg = os.getenv('CMSSW_BASE')+'/FWLitePython/cmsswScripts/runPATwithPFBReco_andTriggerJetSkim.py'
myAnalysis = cmsswAnalysisTools.cmsswAnalysis(samples.files,cfg)
dataSamples = [ "SingleMu__Run2012A-22Jan2013-v1__AOD" , "SingleMu__Run2012B-22Jan2013-v1__AOD"]
if sum( [dS in sys.argv for dS in dataSamples] ) >0:
  sys.argv.append('--runOnData')
myAnalysis.readOpts()
myAnalysis.startAnalysis()

