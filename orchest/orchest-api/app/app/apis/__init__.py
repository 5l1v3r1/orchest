from flask import Blueprint
from flask_restplus import Api

from app.apis.namespace_experiments import api as ns_experiments
from app.apis.namespace_sessions import api as ns_sessions
from app.apis.namespace_runs import api as ns_runs


blueprint = Blueprint('api', __name__)

api = Api(
    blueprint,
    title='Orchest API',
    version='1.0',
    description='Back-end API for Orchest'
)

api.add_namespace(ns_experiments)
api.add_namespace(ns_sessions)
api.add_namespace(ns_runs)
