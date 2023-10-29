from odoo import api, fields, models


class ManagementSekolah(models.Model):
    _name = 'management.sekolah'
    _description = 'Management Sekolah'

    name = fields.Char(string='Kelas', required=True)
    tanggal = fields.Date('Tanggal',required=True)
    status = fields.Selection([
        ('mul','Mulai'),('sel','Selesai')
    ], string='Status', default='ren')
    res_id = fields.Many2one('res.partner', string='Guru',required=True)
    matpel = fields.Char('Mata Pelajaran')
    siswa_ids = fields.One2many('siswa.sekolah', 'sekolah_id', string='Siswa')

    def action_mulai(self):
        self.write({'status':'mul'})

    def action_sel(self):
        self.write({'status':'sel'})



class SiswaSekolah(models.Model):
    _name ="siswa.sekolah"

    sekolah_id = fields.Many2one('management.sekolah', string='Sekolah', invisible=True)
    res_id = fields.Many2one('res.partner', string='Siswa')
    absen = fields.Selection([
        ('absen', 'Absen'),('sakit','Sakit'),('izin','Izin')
    ], string='Absen')
    nilai = fields.Float('Nilai')    
    