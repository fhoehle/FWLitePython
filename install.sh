
if [[ ! "$CMSSW_BASE" =~ "CMSSW_5_3" ]]; then
  echo "missing CMSSW_BASE cmsenv"
  exit 1
fi
cd $CMSSW_BASE
if [ ! -d "$CMSSW_BASE/src/.git" ]; then
  git cms-init
fi
git clone git@github.com:fhoehle/MyCMSSWAnalysisTools.git
cd MyCMSSWAnalysisTools
./install.sh
cd $CMSSW_BASE
 
