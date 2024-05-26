from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser,Group,Permission
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User as DjangoUser
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
#Create your models here.
class User(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=10)
    email = models.EmailField(max_length=70)
    image = models.ImageField(upload_to='media/', blank=True, null=True)  # Champ pour l'image de l'utilisateur

    def __str__(self):
        return "Nom: " + self.nom + ", Prénom: " + self.prenom + ", Téléphone: " + self.telephone + ", Email: " + str(self.email)



class Invitation(models.Model):
    email = models.EmailField()
    code = models.CharField(max_length=20)
    invited_by = models.ForeignKey(DjangoUser, on_delete=models.CASCADE)
    


    def __str__(self):
        return f"Invitation for {self.email}"

class FriendList(models.Model):
    user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE, related_name='friend_list')
    friends = models.ManyToManyField(DjangoUser, related_name='friends')

    def __str__(self):
        return f"Friend list for {self.user.username}"


class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to='profile_photos', blank=True, null=True)
    
    # Ajouter l'argument related_name aux champs de groupe et de permission
    groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True, related_name='customuser_set')
    user_permissions = models.ManyToManyField(Permission, verbose_name=_('user permissions'), blank=True, related_name='customuser_set')


class Poste (models.Model):
    image=models.ImageField(blank=True)
    TYPE_CHOICES=[
        (0,'offre'),
        (1,'demande')
    ]
    type=models.IntegerField(choices=TYPE_CHOICES)
    date=models.DateField(default=date.today)
    user = models.ForeignKey(DjangoUser, on_delete=models.CASCADE, default=None)  # Ajout de `default=None`
    
    @property
    def likes_count(self):
        return self.likes.count()
    def __str__(self):
        return"type:"+str(self.type)+", date:"+str(self.date)

    
class Recommandation(Poste):
    texte = models.CharField(max_length=200)

    def __str__(self):
        return "texte: " + str(self.texte) + super().__str__()

    @property
    def likes_count(self):
        return self.likes.count()

    


class Transport(Poste):
    départ=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)
    heure_dep=models.TimeField()
    nbre_siège=models.IntegerField()
    contactinfo=models.CharField(max_length=100)
    def __str__(self):
        return "départ :"+self.départ+", destination :"+self.destination+", heure départ :"+str(self.heure_dep)+", nombre siège:"+str(self.nbre_siège)+", contact info:"+self.contactinfo+super().__str__()
    @property
    def likes_count(self):
        return self.likes.count()
    
class Logement(Poste):
    localisation=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    contactinfo=models.CharField(max_length=100)
    places_disponibles = models.IntegerField(default=0)  # Ajout du champ pour les places disponibles

    def __str__ (self):
        return "Localisation :"+self.localisation+", description :"+self.description+", contact info:"+self.contactinfo+super().__str__()
    @property
    def likes_count(self):
        return self.likes.count()
  
    

class Stage(Poste):
    TYPE_CHOICES=[
        (1,'ouvrier'),
        (2,'technicien'),
        (3,'PFE')
    ]
    typeStg=models.IntegerField(choices=TYPE_CHOICES)
    société=models.CharField(max_length=100)
    durée=models.IntegerField()
    sujet=models.CharField(max_length=100)
    contactinfo=models.CharField(max_length=100)
    spécialité=models.CharField(max_length=100)
    def __str__(self):
        return "Type de stage:"+str(self.typeStg)+", societé :"+self.société+", durée :"+str(self.durée)+", sujet"+self.sujet+", contact info"+self.contactinfo+", spécialité"+self.spécialité+super().__str__()

    @property
    def likes_count(self):
        return self.likes.count()



class Evènement(Poste):
    intitulé=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    lieu=models.CharField(max_length=100)
    contactInfo=models.CharField(max_length=100)
    def __str__(self):
        return "Intitulé: "+self.intitulé+", description: "+self.description+", lieu"+self.lieu+", contact info"+self.contactInfo+super().__str__()
    @property
    def likes_count(self):
        return self.likes.count()
    
class EvenClub(Evènement):
    club=models.CharField(max_length=100)
    def __str__ (self):
        return "Club:"+self.club+super().__str__()
    
class EvenSocial(Evènement):
    prix=models.FloatField()
    def __str__ (self):
        return "Prix:"+str(self.prix)+super().__str__()

class Enseignant(models.Model):
    nom=models.CharField(max_length=100)
    prenom=models.CharField(max_length=100)
    email=models.EmailField(max_length=70)
    image=models.ImageField(blank=True)

    def __str__(self):
        return "Image:"+str(self.image)+", Nom:"+self.nom+", Prenom:"+self.prenom+", email:"+str(self.email)

class Contact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(max_length=70)
    message = models.TextField()

    def __str__(self):
        return f"Nom: {self.nom}, Email: {self.email}, Message: {self.message}"



    
class Like(models.Model):
    user = models.ForeignKey(DjangoUser, on_delete=models.CASCADE)
    recommandation = models.ForeignKey(Recommandation, on_delete=models.CASCADE, related_name='likes', default=None)

    def __str__(self):
        return f"Like by {self.user.username} on post {self.recommandation.id}"
    
class Likelogement(models.Model):
    user = models.ForeignKey(DjangoUser, on_delete=models.CASCADE)
    logement = models.ForeignKey(Logement,on_delete=models.CASCADE, related_name='likes', default=None)

    def __str__(self):
        return f"Like by {self.user.username} on post {self.logement.id}"

class LikeStage(models.Model):
    user = models.ForeignKey(DjangoUser, on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage,on_delete=models.CASCADE, related_name='likes', default=None)

    def __str__(self):
        return f"Like by {self.user.username} on post {self.stage.id}"

class LikeTransport(models.Model):
    user = models.ForeignKey(DjangoUser, on_delete=models.CASCADE)
    transport = models.ForeignKey(Transport,on_delete=models.CASCADE, related_name='likes', default=None)

    def __str__(self):
        return f"Like by {self.user.username} on post {self.transport.id}"
    
class LikeEvent(models.Model):
    user = models.ForeignKey(DjangoUser, on_delete=models.CASCADE)
    evenement = models.ForeignKey(Evènement,on_delete=models.CASCADE, related_name='likes', default=None)

    def __str__(self):
        return f"Like by {self.user.username} on post {self.evenement.id}"

class Notification(models.Model):
    like = models.OneToOneField(Like, on_delete=models.CASCADE )
    user = models.ForeignKey(DjangoUser, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username} for like {self.like.id} "



class Notificationl(models.Model):
    like = models.OneToOneField(Likelogement, on_delete=models.CASCADE )
    user = models.ForeignKey(DjangoUser, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username} for like {self.like.id} "

class Notifications(models.Model):
    like = models.OneToOneField(LikeStage, on_delete=models.CASCADE )
    user = models.ForeignKey(DjangoUser, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username} for like {self.like.id} "


class Notificationt(models.Model):
    like = models.OneToOneField(LikeTransport, on_delete=models.CASCADE )
    user = models.ForeignKey(DjangoUser, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username} for like {self.like.id} "

class Notificatione(models.Model):
    like = models.OneToOneField(LikeEvent, on_delete=models.CASCADE )
    user = models.ForeignKey(DjangoUser, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username} for like {self.like.id} "


class Commentaire(models.Model):
    user = models.ForeignKey(DjangoUser, on_delete=models.CASCADE)
    recommandation = models.ForeignKey(Recommandation, on_delete=models.CASCADE, related_name='commentaires', default=None)
    texte = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commentaire: {self.texte} - Recommandation: {self.recommandation.texte} - Utilisateur: {self.user.username}"
    
class Notificationcr(models.Model):
    commentaire = models.OneToOneField(Commentaire, on_delete=models.CASCADE )
    user = models.ForeignKey(DjangoUser, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username} for like {self.commentaire.id} "
    


class Commentairel(models.Model):
    user = models.ForeignKey(DjangoUser, on_delete=models.CASCADE)
    logement = models.ForeignKey(Logement, on_delete=models.CASCADE, related_name='commentaires', default=None)
    texte = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commentaire: {self.texte} - Logement: {self.logement.texte} - Utilisateur: {self.user.username}"
    
class Commentairet(models.Model):
    user = models.ForeignKey(DjangoUser, on_delete=models.CASCADE)
    transport = models.ForeignKey(Transport, on_delete=models.CASCADE, related_name='commentaires', default=None)
    texte = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commentaire: {self.texte} - Transport: {self.transport.texte} - Utilisateur: {self.user.username}"

class Commentaires(models.Model):
    user = models.ForeignKey(DjangoUser, on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE, related_name='commentaires', default=None)
    texte = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commentaire: {self.texte} - Stage: {self.stage.texte} - Utilisateur: {self.user.username}"
    
class Commentairee(models.Model):
    user = models.ForeignKey(DjangoUser, on_delete=models.CASCADE)
    evenement = models.ForeignKey(Evènement, on_delete=models.CASCADE, related_name='commentaires', default=None)
    texte = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commentaire: {self.texte} - Evènement: {self.evenement.texte} - Utilisateur: {self.user.username}"
    

class Message(models.Model):
    sender = models.ForeignKey(DjangoUser, related_name='sent_messages', on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)


class Reservation(models.Model):
    user = models.ForeignKey(DjangoUser, on_delete=models.CASCADE)
    logement = models.ForeignKey(Logement, on_delete=models.CASCADE)
    date_reservation = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('user', 'logement')  # Assure que chaque utilisateur ne peut réserver un logement qu'une seule fois

    def __str__(self):
        return f"Réservation de {self.user.username} pour {self.logement}"
    @staticmethod
    def user_has_reservation_for_logement(user, logement):
        return Reservation.objects.filter(user=user, logement=logement).exists()
    
@receiver(post_save, sender=Reservation)
def update_places_disponibles(sender, instance, created, **kwargs):
    if created:
        logement = instance.logement
        logement.places_disponibles -= 1  # Décrémenter le nombre de places disponibles
        if logement.places_disponibles <= 0:
            logement.delete()
        else:
            logement.save()
    
