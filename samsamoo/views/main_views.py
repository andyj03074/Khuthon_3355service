from flask import Blueprint, url_for, request
from werkzeug.utils import redirect

from samsamoo.models import Funding, Company

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/home', methods=['GET'])
def home():
    data = {}
    if request.method == 'GET':
        new_company_list = Company.query.order_by(Company.date_created.desc()).limit(4)
        data = {
            'new_company1_name': new_company_list[0].company_name,
            'new_company1_data': new_company_list[0].company_short_data,
            'nem_company2_name': new_company_list[1].company_name,
            'new_company2_data': new_company_list[1].company_short_data,
            'new_company3_name': new_company_list[2].company_name,
            'new_company3_data': new_company_list[2].company_short_data,
            'new_company4_name': new_company_list[3].company_name,
            'new_company4_data': new_company_list[3].company_short_data
        }
    return data
