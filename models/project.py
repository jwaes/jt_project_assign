import logging
from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class ProjectTaskType(models.Model):
    _inherit = "project.task.type"

    auto_assign_user_id = fields.Many2one('res.users', 'Auto assign user')

class Task(models.Model):
    _inherit = "project.task"

    @api.onchange('stage_id')
    def _onchange_stage_id(self):
    # if self.stage_id and self.stage_id.name == 'Estimation':
    #     # do your code
        _logger.debug("stage changed to %s ", self.stage_id.name)
        _logger.debug("assigned users are %s", self.user_ids)
        if self.stage_id.auto_assign_user_id:
            _logger.debug("found a assigned user for this stage: %s, self.stage_id.auto_assign_user_id.name")
            self.user_ids = self.stage_id.auto_assign_user_id
            _logger.debug("assigned users are %s", self.user_ids)

class Task(models.Model):
    _inherit = 'project.task'

    @api.model
    def default_get(self, default_fields):
        stage_id = self._get_default_stage_id()
        task = self.env['project.task'].search([('stage_id', '=', stage_id)])

        vals = super(Task, self).default_get(default_fields)

        if task.stage_id.auto_assign_user_id:
            user = task.stage_id.auto_assign_user_id
            vals['user_ids'] = [user.id]
            
        return vals