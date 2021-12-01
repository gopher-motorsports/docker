from django.db import models
from cms.models.fields import PlaceholderField

#CMS Models for each of the pages

#Home page - CMS for the rank line as well as the first three paragraphs
class HomePage(models.Model):
    rank = PlaceholderField('rank', related_name='rankplaceholder')
    firstphead = PlaceholderField('firstphead', related_name='firstpheadplaceholder')
    firstp1 = PlaceholderField('firstp1', related_name='firstp1placeholder')
    firstp2 = PlaceholderField('firstp2', related_name='firstp2placeholder')
    firstp3 = PlaceholderField('firstp3', related_name='firstp3placeholder')
    secondphead = PlaceholderField('secondphead', related_name='secondpheadplaceholder')
    secondp1 = PlaceholderField('secondp1', related_name='secondp1placeholder')
    secondp2 = PlaceholderField('secondp2', related_name='secondp2placeholder')
    thirdphead = PlaceholderField('thirdphead', related_name='thirdpheadplaceholder')
    thirdp1 = PlaceholderField('thirdp1', related_name='thirdp1placeholder')
    thirdp2 = PlaceholderField('thirdp2', related_name='thirdp2placeholder')

#Competition page - CMS for the rank line and the as of [year] line
class CompetitionPage(models.Model):
    rank = PlaceholderField('rank', related_name='comprankplaceholder')
    year = PlaceholderField('year', related_name='yearplaceholder')

#Cars page - CMS for the paragraph head and the paragraph itself
class CarsPage(models.Model):
    carshead = PlaceholderField('carshead', related_name='carsheadplaceholder')
    carsp1 = PlaceholderField('carsp1', related_name='carsp1placeholder')
    carsp2 = PlaceholderField('carsp2', related_name='carsp2placeholder')

#Teams page - CMS for the alumni section and the images section
class TeamPage(models.Model):
    #Officer section
    president = PlaceholderField('president', related_name='presidentplaceholder')
    president_image = PlaceholderField('president_image', related_name='president_imageplaceholder')
    chief_engineer = PlaceholderField('chief_engineer', related_name='chief_engineerplaceholder')
    chief_engineer_image = PlaceholderField('chief_engineer_image', related_name='chief_engineer_imageplaceholder')
    project_manager = PlaceholderField('project_manager', related_name='project_managerplaceholder')
    project_manager_image = PlaceholderField('project_manager_image', related_name='project_manager_imageplaceholder')
    aerodynamics = PlaceholderField('aerodynamics', related_name='aerodynamicsplaceholder')
    aerodynamics_image = PlaceholderField('aerodynamics_image', related_name='aerodynamics_imageplaceholder')
    electrical = PlaceholderField('electrical', related_name='electricalplaceholder')
    electrical_image = PlaceholderField('electrical_image', related_name='electrical_imageplaceholder')
    engine_drivetrain = PlaceholderField('engine_drivetrain', related_name='engine_drivetrainplaceholder')
    engine_drivetrain_image = PlaceholderField('engine_drivetrain_image', related_name='engine_drivetrain_imageplaceholder')
    ergonomics = PlaceholderField('ergonomics', related_name='ergonomicsplaceholder')
    ergonomics_image = PlaceholderField('ergonomics_image', related_name='ergonomics_imageplaceholder')
    frame_suspension = PlaceholderField('frame_suspension', related_name='frame_suspensionplaceholder')
    frame_suspension_image = PlaceholderField('frame_suspension_image', related_name='frame_suspension_imageplaceholder')
    business = PlaceholderField('business', related_name='businessplaceholder')
    business_image = PlaceholderField('business_image', related_name='business_imageplaceholder')

    #Alumni section
    alumni1 = PlaceholderField('alumni1', related_name='alumni1placeholder')
    alumni2 = PlaceholderField('alumni2', related_name='alumni2placeholder')
    alumni3 = PlaceholderField('alumni3', related_name='alumni3placeholder')

#Join the Team page - CMS for the join the team paragraph and the meeting time
class JoinTeamPage(models.Model):
    jointeam = PlaceholderField('jointeam', related_name='jointeamplaceholder')
    meetingtime = PlaceholderField('meetingtime', related_name='meetingtimeplaceholder')

#Subteam pages - CMS for everything (main paragraph, the image and the subteam leader info)
class SubteamPage(models.Model):
    subteam = models.CharField(max_length=50, null=True, blank=True)
    mainp = PlaceholderField('mainp', related_name='mainpplaceholder')
    subteam_image = PlaceholderField('subteam_image', related_name='subteam_imageplaceholder')
    subteam_leader = PlaceholderField('subteam_leader', related_name='subteam_leaderplaceholder')

#Donate page - CMS for the donate paragraph
class DonatePage(models.Model):
    donatep = PlaceholderField('donatep', related_name='donatepplaceholder')