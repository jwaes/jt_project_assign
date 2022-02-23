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
        _logger.info("stage changed to %s ", self.stage_id.name)
        _logger.info("assigned users are %s", self.user_ids)
        if self.stage_id.auto_assign_user_id:
            _logger.info("found a assigned user for this stage: %s, self.stage_id.auto_assign_user_id.name")
            self.user_ids = self.stage_id.auto_assign_user_id
            _logger.info("assigned users are %s", self.user_ids)