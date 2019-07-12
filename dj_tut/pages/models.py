from django.db import models

class Participant(models.Model):
	dataset = models.ForeignKey('Dataset', on_delete=models.CASCADE)
	participant_id = models.TextField()

	def __str__(self):
		return self.participant_id

class Dataset(models.Model):
	dataset_title = models.TextField()
	url = models.TextField()
	description = models.TextField()

	def __str__(self):
		return self.dataset_title

class Session(models.Model):
	session_id = models.TextField()
	description = models.TextField()

	def __str__(self):
		return self.session_id

class Site(models.Model):
	site_id = models.TextField()
	description = models.TextField()

	def __str__(self):
		return self.site_id

class Phenotype(models.Model):
	dataset = models.ForeignKey('Dataset', on_delete=models.CASCADE)
	participant_id = models.ForeignKey('Participant', on_delete=models.CASCADE)
	site = models.ForeignKey('Site', on_delete=models.CASCADE, null=True, blank=True)
	session = models.ForeignKey('Session', on_delete=models.CASCADE, null=True, blank=True)
	measure_name = models.TextField()
	measure_value = models.TextField()

	def __str__(self):
		return self.measure_name

class Scan(models.Model):
	dataset = models.ForeignKey('Dataset', on_delete=models.CASCADE)
	participant_id = models.ForeignKey('Participant', on_delete=models.CASCADE)
	session = models.ForeignKey('Session', on_delete=models.CASCADE)
	site = models.ForeignKey('Site', on_delete=models.CASCADE)
	#protocol name
	protocol_name = models.TextField()
	scan_type = models.TextField()
	run_number = models.TextField()
	#s3 path
	url = models.TextField()


	def __str__(self):
		return self.participant_id.participant_id+'_'+self.session.session_id

	def add_scan():
		return

class Protocol(models.Model):
	protocol_name = models.TextField()
	measure_name = models.TextField()
	measure_value = models.TextField()

	def __str__(self):
		return self.protocol_name+'_'+self.measure_name

