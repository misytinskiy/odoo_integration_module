from odoo import models, fields, api, _
from odoo.exceptions import UserError
import requests
import json

class FormTemplate(models.Model):
    _name = 'form.template'
    _description = 'Form Template'

    name = fields.Char(string='Template Name')
    author = fields.Char(string='Author')
    questions = fields.Text(string='Questions')
    number_of_answers = fields.Integer(string='Number of Answers')
    aggregated_results = fields.Text(string='Aggregated Results')
    api_token = fields.Char(string='API Token')

    def action_import_data(self):
        for record in self:
            if not record.api_token:
                raise UserError(_('API Token не указан.'))

            url = 'http://localhost:3000/api/aggregated-results'
            headers = {
                'api-token': record.api_token,
            }

            try:
                response = requests.get(url, headers=headers)
                response.raise_for_status()
                data = response.json()

                for result in data['results']:
                    if result['title'] == record.name:
                        record.number_of_answers = result.get('numberOfAnswers', 0)
                        record.aggregated_results = json.dumps(result.get('aggregatedResults', {}), ensure_ascii=False, indent=2)
                        record.questions = json.dumps(result.get('questions', []), ensure_ascii=False, indent=2)
                        break
                else:
                    raise UserError(_('Данные для данного шаблона не найдены.'))

            except requests.exceptions.RequestException as e:
                raise UserError(_('Ошибка при запросе данных: %s') % str(e))
