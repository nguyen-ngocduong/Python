{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Hàm tính toán kết quả dự báo\n",
    "from sklearn.metrics import classification_report, confusion_matrix\n",
    "from sklearn.metrics import precision_score, recall_score, f1_score\n",
    "from sklearn.metrics import accuracy_score\n",
    "def Static_score_model_class(y, y_pred,aver = 'macro'):\n",
    "    accuracy = accuracy_score(y, y_pred)\n",
    "    precision = precision_score(y,y_pred, average = aver)\n",
    "    recall = recall_score(y,y_pred, average = aver)\n",
    "    f1 = f1_score(y, y_pred, average = aver)\n",
    "    return accuracy, precision, recall, f1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import time\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.model_selection import cross_val_score\n",
    "def Average_Score_Model(model, X, y, size = 0.2, cv =10):\n",
    "    score_train = []\n",
    "    score_test = []\n",
    "    duration = []\n",
    "    for i in range(cv) :\n",
    "        start_time = time.time()\n",
    "        X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=size)\n",
    "        model.fit(X_train, y_train)\n",
    "        acc_train, _ , _ , _ = Static_score_model_class(y_train, model.predict(X_train))\n",
    "        acc_test, _ , _ , _ = Static_score_model_class(y_test, model.predict(X_test))\n",
    "        score_train.append(acc_train)\n",
    "        score_test.append(acc_test)\n",
    "\n",
    "    #   score_test.append(cross_val_score(model, X_test, y_test, scoring = 'accuracy'))\n",
    "        duration.append(time.time()-start_time)\n",
    "    return np.array(score_train).mean(), np.array(score_test).mean(), np.array(duration).mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Trực quan hóa confusion matrix\n",
    "def Visualize_confusion_matrix(y, y_pred):\n",
    "    cm = confusion_matrix(y,y_pred)\n",
    "    cm_df = pd.Dataframe()\n",
    "    plt.figure(figsize = (6,5))\n",
    "    sns.heatmap(cm_df, annot = True, cmap = 'Reds')\n",
    "    plt.title('AccuracyL {0:.3f}'.format(accuracy_score(y,y_pred)))\n",
    "    plt.xlabel('True values')\n",
    "    plt.ylabel('Predict values')\n",
    "    plt.show()\n",
    "    return "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "def Visualize_data(X1,X2,y,title) :\n",
    "    plt.figure(figsize = (6,5))\n",
    "    sns.scatterplot(X1, X2, hue = y, cmap = 'Sequential')\n",
    "    plt.title(title)\n",
    "    plt.show()\n",
    "    return"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "# ROC_AUC:\n",
    "from sklearn.metrics import roc_curve, roc_auc_score\n",
    "def ROC_AUC(y,y_prob):\n",
    "    # tính roc curves\n",
    "    fqr, tqr, threshold = roc_curve(y, y_prob)\n",
    "    # Tính scores\n",
    "    model_auc = roc_auc_score(y, y_prob)\n",
    "    # hình vẽ:\n",
    "    plt.plot([0,1], [0,1], linestyle = '--', label = 'No Skill')\n",
    "    plt.plot(fqr,tqr, marker = '.', label = 'Model - AUC = %.3f' % (model_auc))\n",
    "    #Show axis labels and the legend\n",
    "    plt.xlabel('False Positive Rate')\n",
    "    plt.ylabel('True Positive Rate')\n",
    "    plt.legend()\n",
    "    plt.show(block = False)\n",
    "    return"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import precision_recall_curve, auc\n",
    "def Precision_Recall_AUC(y, y_prob):\n",
    "    # Tính ROC curves\n",
    "    precision, recall, threshold = precision_recall_curve(y, y_prob)\n",
    "    # Tính Scores\n",
    "    model_auc = auc(precision, recall)\n",
    "    #hình vẽ:\n",
    "    ns = len(y[y==1]) / len(y)\n",
    "    plt.plot([0,1],[ns,ns], marker = '--', label = 'No Skill')\n",
    "    plt.plot(recall, precision, marker = '.', label = 'Model - AUC = %.3f' % (model_auc))\n",
    "    # Show on the plot\n",
    "    plt.xlabel('Recall')\n",
    "    plt.ylabel('Precision')\n",
    "    plt.legend()\n",
    "    plt.show()\n",
    "    return"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
