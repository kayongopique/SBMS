from flask import Blueprint
from app.models import Permission

main = Blueprint('main', __name__)

from . import views, errors

# Adding the Permission class to the template context 
@main.app_context_processor 
def inject_permissions():    
    return dict(Permission=Permission) 