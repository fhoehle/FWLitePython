import ROOT,os
files = {
  "MultiJet__Run2012A-22Jan2013-v1__AOD": {
    "localFile": ['/store/data/Run2012A/MultiJet/AOD/22Jan2013-v1/20000/0036C47E-0B74-E211-B992-00266CF32684.root']    ,"backupLocalFile":"/user/hoehle/CMSSW/TEMP/Samples/0051A2ED-482A-E111-9863-0026189438F7.root", "label":"MultiJetData"
    ,"datasetName":'/MultiJet/Run2012A-22Jan2013-v1/AOD'
    ,"xSec":1
    ,"color":ROOT.kBlack+1
    ,"addOptions":"runOnData=True"
    ,"crabConfig":{
          "CMSSW":{"lumis_per_job":5,"total_number_of_lumis" : -1,"lumi_mask":os.getenv('CMSSW_BASE')+'/FWLitePython/cmsswScripts/Production/jsonFiles/'+'GoldenJSON_MultiJetsRunA2012_JSON.txt'}
          #"CMSSW":{"number_of_jobs":1500}
          #"GRID":{"se_white_list":"T2_DE_RWTH"}
          #https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions12/8TeV/Reprocessing/Cert_190456-208686_8TeV_22Jan2013ReReco_Collisions12_JSON.txt
          ,'USER':{"publish_data": 1,"publish_data_name" : "BScSkim_MultiJetData"}
    }
  }
  ,"TTTT_TuneZ2star_8TeV-madgraph-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM":{
    "label":"TTTTJets"
    ,"localFile":['/store/mc/Summer12_DR53X/TTTT_TuneZ2star_8TeV-madgraph-tauola/AODSIM/PU_S10_START53_V7A-v1/00000/7083D246-AA0A-E211-ADA5-001E67397F26.root']
    ,"datasetName":'/TTTT_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'
    ,"xSec":1
    ,"color":ROOT.kGreen+1
    #,"addOptions":""
    ,"crabConfig":{
          #"CMSSW":{"number_of_jobs":1500}
          #"GRID":{"se_white_list":"T2_DE_RWTH"}
          'USER':{"publish_data": 1,"publish_data_name" : "BScSkim_TTTTJets"}
    }
  }
  ,'TTJets_TuneZ2star_8TeV-madgraph-tauola__Summer12-PU_S8_START52_V9-v1__AODSIM':{
    'label':"TTJets"
    ,"localFile":['/store/mc/Summer12/TTJets_TuneZ2star_8TeV-madgraph-tauola/AODSIM/PU_S8_START52_V9-v1/0000/00069C6C-77C3-E111-8C84-0030486790A0.root']
    ,"datasetName":'/TTJets_TuneZ2star_8TeV-madgraph-tauola/Summer12-PU_S8_START52_V9-v1/AODSIM'
    ,"xSec":1
    ,"color":ROOT.kRed+1
    #,"addOptions":""
    ,"crabConfig":{
          #"CMSSW":{"number_of_jobs":1500}
          #"GRID":{"se_white_list":"T2_DE_RWTH"}
          'USER':{"publish_data": 1,"publish_data_name" : "BScSkim_TTJets"}
    }
  }
}
