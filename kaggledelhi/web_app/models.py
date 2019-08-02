from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

# Volunteer Model

vol_status = (
    (0,"deactive"),
    (1,"active")
)

class Volunteer(models.Model):

    firstName = models.CharField(max_length=64)
    lastName = models.CharField(max_length=64)
    githubLink = models.URLField(max_length=2048,blank=True,unique=True)
    kaggleLink = models.URLField(max_length=2048,blank=True,unique=True)
    email = models.EmailField(blank=True,unique=True)
    contact = models.CharField(max_length=15)
    image = models.ImageField(upload_to='volunteer/',blank=True)
    vol_status = models.IntegerField(choices=vol_status, default=1)
    def __str__(self):
        return "{0} {1}".format(self.firstName,self.lastName)

class Role(models.Model):

    role = models.CharField(max_length=64)
    roleDescription = models.TextField()
    def __str__(self):
        return self.role

class HasRole(models.Model):
    volunteerId = models.ForeignKey(Volunteer, on_delete=models.CASCADE, related_name='volunteer_details')
    roleId = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='role_details')
    startTime = models.DateTimeField(auto_now=True)
    endTime =models.DateTimeField(blank=True,null=True)
    def __str__(self):
        return "{0} has {1}".format(self.volunteerId,self.roleId)


# Talk Model 

talk_status=(
    (0,"onSite"),
    (1,"onLine")
)

class RequirementType(models.Model):
    type_name = models.CharField(max_length=255)
    def __str__(self):
        return self.type_name


class Requirement(models.Model):
    name = models.CharField(max_length=255,blank=False)
    requirementTypeId = models.ForeignKey(RequirementType, on_delete=models.CASCADE, related_name='requirementType_details')
    def __str__(self):
        return self.name
    
class Meetup(models.Model):
    meetupName = models.CharField(max_length=64)
    meetupDescription = models.TextField()
    meetupLocation = models.TextField()# it has to pointfield by using geodjango
    starttime = models.DateField()
    endtime = models.DateField()
    def __str__(self):
        return self.meetupName

class Slide(models.Model):
    slideName = models.CharField(max_length=64)
    slideLink = models.URLField(max_length=2048,unique = True, blank=False)
    def __str__(self):
        return self.slideName

class Notebook(models.Model):
    NoteName = models.CharField(max_length=64)
    NoteLink = models.URLField(max_length=2048,unique = True, blank=False)
    def __str__(self):
        return self.NoteName

class Code(models.Model):
    CodeName = models.CharField(max_length=64)
    CodeLink = models.URLField(max_length=2048,unique = True, blank=False)
    def __str__(self):
        return self.CodeName

class Talk(models.Model):
    talkName = models.CharField(max_length=64)
    talkStatus = models.IntegerField(choices=talk_status,default=0)
    # talkRequirementId = models.ForeignKey(TalkRequirement,on_delete=models.CASCADE, related_name='talkRequirement_details')
    talkDescription = models.TextField()
    slideId = models.ForeignKey(Slide, on_delete=models.CASCADE, related_name='slide_details')
    noteId = models.ForeignKey(Notebook, on_delete=models.CASCADE, related_name='Notebook_details')
    codeId = models.ForeignKey(Code, on_delete=models.CASCADE, related_name='Code_details')
    startTime = models.TimeField()
    endTime =models.TimeField()
    meetupId = models.ForeignKey(Meetup, on_delete = models.CASCADE, related_name= 'Meetup_details')
    def __str__(self):
        return self.talkName

class TalkRequirement(models.Model):
    talkId = models.ForeignKey(Talk, on_delete=models.CASCADE, related_name='talk_details_for_TalkRequirement')
    requirementId = models.ForeignKey(Requirement, on_delete=models.CASCADE, related_name='requirement_details_for_TalkRequirement')
    quantity = models.IntegerField(blank=False)
    cost = models.DecimalField(max_digits=8,decimal_places=2,default=0.0)
    def __str__(self):
        return "{0} require {1}".format(self.talkId,self.requirementId)

class Engaged(models.Model):
    talkId = models.ForeignKey(Talk, on_delete=models.CASCADE, related_name='talk_details_for_Volunteer_Engaged' )
    hasRoleId = models.ForeignKey(HasRole, on_delete=models.CASCADE, related_name='has_role_detail')
    startTime = models.DateTimeField()
    endTime =models.DateTimeField(blank=True,null=True)

class Speaker(models.Model):
    firstName = models.CharField(max_length=64)
    lastName = models.CharField(max_length=64)
    about = models.CharField(max_length = 500)
    image = models.ImageField(upload_to='speaker/')
    def __str__(self):
        return "{0} {1}".format(self.firstName,self.lastName)

class Partcipate(models.Model):
    talkId = models.ForeignKey(Talk, on_delete=models.CASCADE, related_name='talk_details_for_Speaker_Partcipate')
    speakerId = models.ForeignKey(Speaker,on_delete=models.CASCADE, related_name='speaker_details_for_partcipate')
    startTime = models.TimeField()
    endTime=models.TimeField(blank=True)
    def __str__(self):
        return "{1} particpate in {0}".format(self.talkId,self.speakerId)

class FollowSpeaker(models.Model):
    speakerId = models.ForeignKey(Speaker,on_delete=models.CASCADE, related_name='speaker_details_for_follow_speaker')
    socialMediaHandleName = models.CharField(max_length=64)
    smhLink = models.URLField(max_length=2048,blank=False)

class Sponsor(models.Model):
    sponsorName = models.CharField(max_length=64)
    sponsorLink = models.URLField(max_length=2048, blank=False)
    sponsorLogo = models.ImageField(upload_to='sponsor/',blank=False)
    def __str__(self):
        return self.sponsorname

class SponsorRole(models.Model):
    role_name = models.CharField(max_length=64)
    role_description = models.TextField()
    def __str__(self):
        return self.role_name

class HasSponsor(models.Model):
    meetupId = models.ForeignKey(Meetup,on_delete=models.CASCADE, related_name='meetup_details')
    roleId = models.ForeignKey(SponsorRole,on_delete=models.CASCADE, related_name='sponsorrole_details')
    sponsorId = models.ForeignKey(Sponsor,on_delete=models.CASCADE, related_name='sponsor_details')






STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
 
class post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title