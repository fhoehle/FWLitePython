import os,sys
sys.path.append(os.getenv('CMSSW_BASE')+'/MyCMSSWAnalysisTools')
import Tools.datasetTools as datasetTools
ttbar = [
 '/DoubleMu/Run2011A-05Aug2011-v1/AOD'
]

ttbarFiles =   datasetTools.createDatasampleFile(os.getenv('CMSSW_BASE')+'/FWLitePython/cmsswScripts/Production/ttbarDatasetsata.py')
##############
for ds in ttbar:
  ttbarFiles.addDataset(ds)
ttbarFiles.createFile()

