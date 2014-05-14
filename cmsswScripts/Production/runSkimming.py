#!/usr/bin/env python
# run cmssw analysis
import FWCore.ParameterSet.Config as cms
import os
import sys
sys.path.append(os.getenv('CMSSW_BASE')+'/MyCMSSWAnalysisTools/Tools')
import  cmsswAnalysisTools
import samples
print "executing "," ".join(sys.argv)
cfg = os.getenv('CMSSW_BASE')+'/FWLitePython/cmsswScripts/runPATwithPFBReco_Skim.py'
myAnalysis = cmsswAnalysisTools.cmsswAnalysis(samples.files,cfg)
myAnalysis.readOpts()
myAnalysis.startAnalysis()

