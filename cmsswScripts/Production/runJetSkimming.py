#!/usr/bin/env python
# run cmssw analysis
import FWCore.ParameterSet.Config as cms
import os
import sys
sys.path.append(os.getenv('CMSSW_BASE')+'/MyCMSSWAnalysisTools/Tools')
import  cmsswAnalysisTools
import samples
print "executing "," ".join(sys.argv)
cfg = os.getenv('CMSSW_BASE')+'/FWLitePython/cmsswScripts/softJetSkim_cfg.py'
if not 'SingleMu__hoehle-BScSkim_SingleMuData-bd22b76fe02f0bcf6d005e3433b8e12b__USER' in sys.argv:
  print "use -specificSample SingleMu__hoehle-BScSkim_SingleMuData-bd22b76fe02f0bcf6d005e3433b8e12b__USER for this script"
  sys.exit(1)
myAnalysis = cmsswAnalysisTools.cmsswAnalysis(samples.files,cfg)

myAnalysis.readOpts()
myAnalysis.startAnalysis()

