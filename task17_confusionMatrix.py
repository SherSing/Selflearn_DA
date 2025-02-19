# confusion matrix

import matplotlib.pyplot as plt
import numpy
from sklearn import metrics

actual = numpy.random.binomial(1,.9,size = 1000)
predicted = numpy.random.binomial(1,.9,size = 1000)

print("actual is",actual, "\n\n")

print("actual is",predicted, "\n\n")

confusion_matrix = metrics.confusion_matrix(actual, predicted)

cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [0, 1])

Accuracy = metrics.accuracy_score(actual, predicted)
Precision = metrics.precision_score(actual, predicted)
Sensitivity_recall = metrics.recall_score(actual, predicted)
Specificity = metrics.recall_score(actual, predicted, pos_label=0)
F1_score = metrics.f1_score(actual, predicted)

print("True Positives:",confusion_matrix[1,1])
print("True Negatives:",confusion_matrix[1,0])
print("False Positives:",confusion_matrix[0,1])
print("False Negatives:",confusion_matrix[0,0])

print("Accuracy:\t",Accuracy,"\n",
      "Precision:\t",Precision,"\n",
      "Sensitivity_recall:\t",Sensitivity_recall,"\n",
      "Specificity:\t",Specificity,"\n",
      "F1_score:\t",F1_score)




cm_display.plot()
plt.show()

