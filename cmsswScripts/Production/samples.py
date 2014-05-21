import ROOT,os
files = {
  "SingleMu__hoehle-BScSkim_SingleMuData-bd22b76fe02f0bcf6d005e3433b8e12b__USER":{
    "label":"SingleMu_Trigger_SoftJetSim"
    ,"datasetName":"/SingleMu/hoehle-BScSkim_SingleMuData-bd22b76fe02f0bcf6d005e3433b8e12b/USER" 
    ,"localFile":['/store/user/hoehle/SingleMu/BScSkim_SingleMuData/bd22b76fe02f0bcf6d005e3433b8e12b/MultiJet-Run2012A_patTuple_SingleMu__Run2012A-22Jan2013-v1__AOD_120_1_t6S.root']
    ,"xSec":1
    ,"color":ROOT.kBlack+1
    #,"addOptions":"runOnData=True"
    ,"crabConfig":{
          "CMSSW":{ 'dbs_url':'phys03',"lumis_per_job":35,"total_number_of_lumis" : -1 }
          #"CMSSW":{"number_of_jobs":1500}
          #"GRID":{"se_white_list":"T2_DE_RWTH"}
          ,'USER':{"publish_data": 1,"publish_data_name" : "SoftJetSkim"}
    }
  }
  ,"SingleMu__Run2012A-22Jan2013-v1__AOD":{
    "label":"SingleMuData"
    ,"localFile": ['/store/data/Run2012A/SingleMu/AOD/22Jan2013-v1/20000/002F5062-346F-E211-BF00-1CC1DE04DF20.root'], "label":"SingleMuRunAData"
    ,"datasetName":'/SingleMu/Run2012A-22Jan2013-v1/AOD'
    ,"xSec":1
    ,"color":ROOT.kBlack+1
    ,"addOptions":"runOnData=True"
    ,"crabConfig":{
          "CMSSW":{"lumis_per_job":5,"total_number_of_lumis" : -1,"lumi_mask":os.getenv('CMSSW_BASE')+'/FWLitePython/cmsswScripts/Production/jsonFiles/'+'SingleMu__Run2012A-22Jan2013-v1__AOD__AND__Cert_190456-208686_8TeV_22Jan2013ReReco_Collisions12_JSON.txt'}
          #"CMSSW":{"number_of_jobs":1500}
          #"GRID":{"se_white_list":"T2_DE_RWTH"}
          #https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions12/8TeV/Reprocessing/Cert_190456-208686_8TeV_22Jan2013ReReco_Collisions12_JSON.txt
          ,'USER':{"publish_data": 1,"publish_data_name" : "BScSkim_SingleMuData"}
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
  ,'TTJets_TuneZ2star_8TeV-madgraph-tauola__fhohle-BScSkim_TTJets-10916883f87702ed6d1a4822bbfe7433__USER':{
    'label':"TTJetsTrigSkim"
    ,"localFile":['/store/user/fhohle/TTJets_TuneZ2star_8TeV-madgraph-tauola/BScSkim_TTJets/10916883f87702ed6d1a4822bbfe7433/TTTT_TuneZ2star_8TeV-madgraph-tauola_patTuple_TTJets_TuneZ2star_8TeV-madgraph-tauola__Summer12-PU_S8_START52_V9-v1__AODSIM_100_1_7nl.root']
    ,"datasetName":'/TTJets_TuneZ2star_8TeV-madgraph-tauola/fhohle-BScSkim_TTJets-10916883f87702ed6d1a4822bbfe7433/USER'
    ,"xSec":1
    ,"color":ROOT.kRed+1
    #,"addOptions":""
    ,"crabConfig":{
          "CMSSW":{ 'dbs_url':'phys03'}
          #"GRID":{"se_white_list":"T2_DE_RWTH"}
          ,'USER':{"publish_data": 1,"publish_data_name" : "BScSkim_TTJetsTrigSkim"}
    }
  }
}
