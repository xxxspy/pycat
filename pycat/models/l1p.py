#encoding:utf8
from model_base import Model
'''
 * The One-Paramter Logistic (Rasch) IRT model:
 * P(X=1|theta) = 1/1+exp[-(sum_i theta_i -b + sum_j d_j covariate_j)],
 * where b is the item difficulty.
 * Distance is defined as: abs(sum_i theta_i - b + sum_j d_j covariate_j).
'''
class ModelL1p(Model):
	def get_max(self):
		return 1
	def P(self):
