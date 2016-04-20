#encoding:utf8
class Model(object):
	space=None# space of test
	ndims=None# number of dimensions
	nparams=None#number of parameters
	ncova=None# number of covariates
	dims=None #dimensions
	params=None #parameters
	names=None
	covariates=None
	def __init__(self):
		pass
	def get_max(self):
		'''Returns: the maximum valid response category for this model'''
		raise NotImplementedError('get_max')
	def P(self,resp,theta,covariates):
		'''
		 @resp: the examinee response value
		 @theta: the #GGslVector parameter value
		 @covariates: (allow-none): the values for covariates
		 
		 Calculates the probability of response @resp, given latent ability @theta.
		 Returns: the computed probability
		'''
		raise NotImplementedError('get_max')
	def distance(self):
		'''
		 * oscats_model_distance:
		 * @theta: the #GGslVector parameter value
		 * @covariates: (allow-none): the values of covariates
		 *
		 * Calculates a distance metric between the model and the given latent
		 * ability.  Metric definition is implementation specific.  Note:
		 * model implementations are not required to provide oscats_model_distance().
		 * Refer to specific implementation documentation for details.
		 *
		 * Returns: the distance metric
		'''
		raise NotImplementedError('get_max')
	def logLik_dtheta(self):
		'''
		/**
		 * oscats_model_logLik_dtheta:
		 * @model: an #OscatsModel
		 * @resp: the examinee response value 
		 * @theta: the value of the latent variables
		 * @covariates: (allow-none): the value of covariates
		 * @grad: (inout) (allow-none): a #GGslVector for returning the gradient
		 * @hes: (inout) (allow-none): a #GGslMatrix for returning the Hessian
		 * 
		 * Calculates the derivative of the log-likelihood with respect to the 
		 * latent ability @theta, given the examinee response @resp,
		 * evaluated at @theta.  If given, the graident is <emphasis>added</emphasis>
		 * to @grad, and the Hessian (second derivatives) to @hes.  The vectors and
		 * matrix must have dimension @model->dims->size.
		 *
		 * Not all model implementations support oscats_model_logLik_dtheta().
		 * Generally, only models on continuous latent sub-spaces will provide
		 * derivatives.  Refer to model implementation documentation for details.
		 */
		 '''
		raise NotImplementedError('get_max')
	def logLik_dparam(self):
		'''
		/**
		 * oscats_model_logLik_dparam:
		 * @model: an #OscatsModel
		 * @resp: the examinee response value 
		 * @theta: the point in latent space
		 * @covariates: (allow-none): the values of covariates
		 * @grad: (inout) (allow-none): a #GGslVector for returning the gradient
		 * @hes: (inout) (allow-none): a #GGslMatrix for returning the Hessian
		 * 
		 * Calculates the derivative of the log-likelihood with respect to the
		 * parameters, given the examinee response @resp, latent variables @theta,
		 * and covariates @covariates.  If given, the graident is
		 * <emphasis>added</emphasis> to @grad, and the Hessian (second partial
		 * derivatives) to @hes.  The gradient and Hessian must have dimension
		 * @model->Np, and the latent ability @theta must be compatible with
		 * #OscatsModel:space for @model.
		 *
		 * Note: Not all model implementations support oscats_model_logLik_dparam().
		 * Refer to model implementation documentation for details.
		 */
		'''
		raise NotImplementedError('get_max')
	def fisher_inf(self):
		'''
		/**
		 * oscats_model_fisher_inf:
		 * @model: an #OscatsModel
		 * @theta: the #OscatsPoint latent point
		 * @covariates: (allow-none): the value of covariates
		 * @I: a #GGslMatrix for returning the Fisher Information
		 * 
		 * Calculates the Fisher Information at @theta, given @covariates:
		 * I = E_{X|theta}[-d^2/dtheta dtheta' log(P(X))].
		 * The information is <emphasis>added</emphasis> to @I.
		 * The matrix must have dimension @model->space->num_cont.
		 */
		 '''
		 raise NotImplementedError('fisher_inf')
	