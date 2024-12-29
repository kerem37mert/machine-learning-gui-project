# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, uic
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier

import result
from ML.evaluation import evaluation
from ML.get_info_dataset import get_info_dataset
from ML.hold_out import hold_out
from ML.kfold import kfold


class Ui_ModelMenu(QtWidgets.QDialog):
    def __init__(self, main_window, dataset, title):
        super(Ui_ModelMenu, self).__init__()

        # Ana pencere referansı alınıyor
        self.main_window = main_window

        #dataseti alma
        self.dataset = dataset
        #print(self.dataset)

        # Load the UI file
        uic.loadUi('ModelMenu.ui', self)

        dataset_info = get_info_dataset(self.dataset)
        self.datasetInfo.setText(f"Veri setindedeki\n1 sınıfına ait örnek sayısı: {dataset_info[0]}\n0 sınıfına ait örnek sayısı: {dataset_info[1]}")

        self.button1.clicked.connect(lambda: self.go_to_result(self.useKNN))
        self.button2.clicked.connect(lambda: self.go_to_result(self.useDecisionTree))
        self.button3.clicked.connect(lambda: self.go_to_result(self.useMLP))
        self.button4.clicked.connect(lambda: self.go_to_result(self.useBest))
        self.backButton.clicked.connect(self.go_back)

    def useKNN(self):
        model = KNeighborsClassifier(n_neighbors=3)

        if(self.checkBox.isChecked()):
            cm = kfold(self.dataset, model)
        else:
            cm = hold_out(self.dataset, model)
        return cm, "KNN"

    def useDecisionTree(self):
        model = DecisionTreeClassifier()

        if (self.checkBox.isChecked()):
            cm = kfold(self.dataset, model)
        else:
            cm = hold_out(self.dataset, model)
        return cm, "Decision Tree"

    def useMLP(self):
        model = MLPClassifier()

        if (self.checkBox.isChecked()):
            cm = kfold(self.dataset, model)
        else:
            cm = hold_out(self.dataset, model)
        return cm, "MLP"

    def useBest(self):
        cm_knn =  self.useKNN()[0]
        cm_decisionTree = self.useDecisionTree()[0]
        cm_mlp = self.useMLP()[0]

        acc_knn = evaluation(cm_knn)
        acc_decision_tree = evaluation(cm_decisionTree)
        acc_mlp = evaluation(cm_mlp)

        if acc_knn >= acc_decision_tree and acc_knn >= acc_mlp:
            return cm_knn, "KNN En İyi Model"
        elif acc_decision_tree >= acc_knn and acc_decision_tree >= acc_mlp:
            return cm_decisionTree, "Decision Tree - En İyi Model"
        else:
            return cm_mlp, "MLP - En İyi Model"


    def go_to_result(self, useModel):
        cm, title = useModel() # modeli çalıştır.
        self.result_window = result.Ui_Result(self, cm)
        self.result_window.setWindowTitle(title)
        self.result_window.show()
        self.hide()  # Ana pencereyi gizle

    def go_back(self):
        # Ana pencereye geri dön
        self.main_window.show()
        self.close()
