import ROOT

work1 = ROOT.TFile('sig_bg_output.root', 'RECREATE')
fact = ROOT.TMVA.Factory('TMVAClassification',work1,'V:Color:Correlations:!Silent:DrawProgressBar:AnalysisType=Classification')
#create data DataLoader
data = ROOT.TMVA.DataLoader('dataset')

signalWeight = 1.0
backgroundWeight = 1.0
#open signal file
f = ROOT.TFile( 'sig_30000_0.0_0.1.root', 'READ' )
#get tree
treesig = f.Get('t1')
#open bg file
g = ROOT.TFile( 'bg_30000_0.0_0.1.root', 'READ' )
#get tree
treebg = g.Get('t2')

#add variables to MVA
data.AddVariable("x",'F')
data.AddVariable("y",'F')

#adding signal and bg tree
data.AddSignalTree(treesig,signalWeight)
data.AddBackgroundTree(treebg,backgroundWeight)

#cuts sg and bg
sigCut = ROOT.TCut("truth > 0.5")
bgCut = ROOT.TCut("truth <= 0.5")
#training and testing
data.PrepareTrainingAndTestTree(sigCut,bgCut,'random') #random choose randomly the events
fact.BookMethod(data,ROOT.TMVA.Types.kBDT,'BDT','NTrees=100:Maxdepth=10')
#meth = fact.BookMethod(data,ROOT.TMVA.Types.kBDT, "BDTG",":".join(["!H","!V","NTrees=850","nEventsMin=150","MaxDepth=3","BoostType=AdaBoost","AdaBoostBeta=0.5","SeparationType=GiniIndex","nCuts=20","PruneMethod=NoPruning",]))
#method = fact.BookMethod( ROOT.TMVA.Types.kSVM, "SVM", "C=1.0:Gamma=0.005:Tol=0.001:VarTransform=None" )
#fact.BookMethod(ROOT.TMVA.Types.kNN,'NN','NTrees=100:Maxdepth=5') another method
fact.TrainAllMethods()
fact.TestAllMethods()
fact.EvaluateAllMethods()
