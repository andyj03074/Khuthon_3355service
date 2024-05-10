from flask import Blueprint, request, session
from samsamoo import db
from samsamoo.models import Funding, Company
from datetime import datetime

bp = Blueprint('funding', __name__, url_prefix='/funding')


@bp.route('/', methods=['GET'])
def funding_list():
    funding_list = []
    for company in Company.query.all():
        funding_list.append({"name": company.company_name , "data": company.company_short_data})

    return funding_list


@bp.route('/<int:company_name>', methods=['GET'])
def funding_detail(company_name):
    data = {}
    if request.method == 'GET':
        company = Company.query.filter_by(company_name=company_name).first()
        data = {
            "name": company.company_name,
            "data": company.company_short_data,
        }
    return data




