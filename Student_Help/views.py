from django.shortcuts import render 
from django.http import HttpResponse
from .forms import RecommandationForm ,PosteForm,LogementForm , StageForm , EvènementForm , TransportForm, ContactForm,EditProfileForm,LikeForm
from django.shortcuts import HttpResponseRedirect
from .models import Reservation,FriendList,Notificationcr,Message,Invitation, Notificatione,  Notificationt, Notifications, Notificationl,Commentairee, Commentaires ,Commentairet, Commentairel, LikeEvent ,LikeTransport , LikeStage,Likelogement,User, Contact,Recommandation, Logement,Notification, Transport, Stage, EvenClub,Enseignant,Evènement,Poste,Like,Commentaire
from django.shortcuts import redirect
from .forms import  UserCreationForm ,LoginForm,UserRegistrationForm,CommentaireForm
from django.contrib.auth import login, authenticate , logout
from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseBadRequest
from django.utils import timezone
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User

@login_required
def list_message(request):
    # Récupérez tous les utilisateurs Django non connectés
    users = User.objects.exclude(pk=request.user.pk)# Passez les utilisateurs à votre modèle HTML
    return render(request, 'Student_Help/message.html', {'users': users})



@login_required
def invite_list(request):
    # Récupérer la liste d'amis de l'utilisateur connecté
    friend_list = FriendList.objects.get(user=request.user)
    friends = friend_list.friends.all()

    # Exclure l'utilisateur connecté et les amis de la liste des utilisateurs
    users = User.objects.exclude(pk=request.user.pk).exclude(pk__in=friends)

    # Passez les utilisateurs à votre modèle HTML
    return render(request, 'Student_Help/invite_list.html', {'users': users})


@login_required
def inbox(request):
    messages = Message.objects.all()
    users =User.objects.exclude(pk=request.user.pk)
    return render(request, 'Student_Help/message.html', {'messages': messages,'users':users})


@login_required
def send_message(request):
    if request.method == 'POST':
        body = request.POST.get('message_body')

        if body:
            sender = request.user
            
            # Créer un message avec l'utilisateur connecté comme expéditeur
            Message.objects.create(
                sender=sender,
                subject="",
                body=body,
                timestamp=timezone.now(),
            )
            
            return redirect('Student_Help:inbox')
        else:
            return HttpResponseBadRequest("Le champ du message est vide")
    
    return render(request, 'Student_Help/message.html')






def notification_list(request):
    # Récupérer toutes les notifications de l'utilisateur connecté
    notifications = Notification.objects.filter(user=request.user).order_by('-timestamp')

    return render(request, 'Student_Help/notif.html', {'notifications': notifications })

def notification_l(request):
    # Récupérer toutes les notifications de l'utilisateur connecté
    notifications = Notificationl.objects.filter(user=request.user).order_by('-timestamp')

    return render(request, 'Student_Help/notif.html', {'notifications': notifications })

def notification_s(request):
    # Récupérer toutes les notifications de l'utilisateur connecté
    notificationst = Notifications.objects.filter(user=request.user).order_by('-timestamp')

    return render(request, 'Student_Help/notif.html', {'notificationst': notificationst })

def notification_t(request):
    # Récupérer toutes les notifications de l'utilisateur connecté
    notifications = Notificationt.objects.filter(user=request.user).order_by('-timestamp')

    return render(request, 'Student_Help/notif.html', {'notifications': notifications })

def notification_e(request):
    # Récupérer toutes les notifications de l'utilisateur connecté
    notifications = Notificatione.objects.filter(user=request.user).order_by('-timestamp')

    return render(request, 'Student_Help/notif.html', {'notifications': notifications })


def notification_cr(request):
    # Récupérer toutes les notifications de l'utilisateur connecté
    notifications = Notificationcr.objects.filter(user=request.user).order_by('-timestamp')

    return render(request, 'Student_Help/notif.html', {'notifications': notifications })

@login_required
def like_recommandation(request, recommandation_id):
    if request.method == 'POST':
        recommandation = get_object_or_404(Recommandation, pk=recommandation_id)
        like, created = Like.objects.get_or_create(user=request.user, recommandation=recommandation)
        if not created:
            like.delete()  # Si le like existe déjà pour cet utilisateur et cette recommandation, le supprimer
        else:
            # Créez une notification associée à ce like
            Notification.objects.create(user=recommandation.user, like=like)
    return redirect('Student_Help:poste')

@login_required
def like_logement(request, logement_id):
    if request.method == 'POST':
        logement = get_object_or_404(Logement, pk=logement_id)
        like, created = Likelogement.objects.get_or_create(user=request.user, logement=logement)
        if not created:
            like.delete()  # Si le like existe déjà pour cet utilisateur et cette recommandation, le supprimer
        else:
            # Créez une notification associée à ce like
            Notificationl.objects.create(user=logement.user, like=like)
    return redirect('Student_Help:poste')


@login_required
def like_stage(request, stage_id):
    if request.method == 'POST':
        stage = get_object_or_404(Stage, pk=stage_id)
        like, created = LikeStage.objects.get_or_create(user=request.user, stage=stage)
        if not created:
            like.delete()  # Si le like existe déjà pour cet utilisateur et cette recommandation, le supprimer
        else:
            # Créez une notification associée à ce like
            Notifications.objects.create(user=stage.user, like=like)
    return redirect('Student_Help:poste')

@login_required
def like_transport(request, transport_id):
    if request.method == 'POST':
        transport = get_object_or_404(Transport, pk=transport_id)
        like, created = LikeTransport.objects.get_or_create(user=request.user, transport=transport)
        if not created:
            like.delete()  # Si le like existe déjà pour cet utilisateur et cette recommandation, le supprimer
        else:
            # Créez une notification associée à ce like
            Notificationt.objects.create(user=transport.user, like=like)
    return redirect('Student_Help:poste')

@login_required
def like_event(request, evenement_id):
    if request.method == 'POST':
        evenement = get_object_or_404(Evènement, pk=evenement_id)
        like, created = LikeEvent.objects.get_or_create(user=request.user, evenement=evenement)
        if not created:
            like.delete()  # Si le like existe déjà pour cet utilisateur et cette recommandation, le supprimer
        else:
            # Créez une notification associée à ce like
            Notificatione.objects.create(user=evenement.user, like=like)
    return redirect('Student_Help:poste')
# @login_required
# def like_recommandation(request, recommandation_id):
#     if request.method == 'POST':
#         recommandation = Recommandation.objects.get(pk=recommandation_id)
#         like, created = Like.objects.get_or_create(user=request.user, recommandation=recommandation)
#         if not created:
#             like.delete()  # Si le like existe déjà pour cet utilisateur et cette recommandation, le supprimer
#     return redirect('Student_Help:poste')

@login_required
def creer_commentaire(request, recommandation_id):
    recommendation = get_object_or_404(Recommandation, pk=recommandation_id)

    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        if comment_text: 
            Commentaire.objects.create(
                user=request.user,
                recommandation=recommendation, 
                texte=comment_text
            )
            messages.success(request, 'Commentaire ajouté avec succès.')
           
            return redirect(reverse('Student_Help:list_comments', kwargs={'publication_id': recommandation_id}))
        else:
            messages.error(request, 'Le commentaire ne peut pas être vide.')
        
  
    return redirect(reverse('Student_Help:poste', kwargs={'recommandation_id': recommandation_id}))

@login_required
def creer_commentairel(request, logement_id):
    logement = get_object_or_404(Logement, pk=logement_id)

    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        if comment_text:  # Check if comment is not empty
            comment = Commentairel.objects.create(
                user=request.user,
                logement=logement,  # Assign recommendation directly
                texte=comment_text
            )
            messages.success(request, 'Commentaire ajouté avec succès.')
        else:
            messages.error(request, 'Le commentaire ne peut pas être vide.')
        
        return render(request, 'student_help/list_posts.html', {'comment': logement})
    
    return render(request, 'student_help/list_posts.html', {'comment': logement})


@login_required
def creer_commentairet(request, transport_id):
    transport = get_object_or_404(Transport, pk=transport_id)

    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        if comment_text:  # Check if comment is not empty
            comment = Commentairet.objects.create(
                user=request.user,
                transport=transport,  # Assign recommendation directly
                texte=comment_text
            )
            messages.success(request, 'Commentaire ajouté avec succès.')
        else:
            messages.error(request, 'Le commentaire ne peut pas être vide.')
        
        return render(request, 'student_help/list_posts.html', {'comment': transport})
    
    return render(request, 'student_help/list_posts.html', {'comment': transport})

@login_required
def creer_commentaires(request, stage_id):
    stage = get_object_or_404(Stage, pk=stage_id)

    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        if comment_text:  # Check if comment is not empty
            comment = Commentaires.objects.create(
                user=request.user,
                stage=stage,  # Assign recommendation directly
                texte=comment_text
            )
            messages.success(request, 'Commentaire ajouté avec succès.')
        else:
            messages.error(request, 'Le commentaire ne peut pas être vide.')
        
        return render(request, 'student_help/list_posts.html', {'comment': stage})
    
    return render(request, 'student_help/list_posts.html', {'comment': stage})

@login_required
def creer_commentairee(request, evenement_id):
    evenement = get_object_or_404(Evènement, pk=evenement_id)

    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        if comment_text:  # Check if comment is not empty
            comment = Commentairee.objects.create(
                user=request.user,
                evenement=evenement,  # Assign recommendation directly
                texte=comment_text
            )
            messages.success(request, 'Commentaire ajouté avec succès.')
        else:
            messages.error(request, 'Le commentaire ne peut pas être vide.')
        
        return render(request, 'student_help/list_posts.html', {'comment': evenement})
    
    return render(request, 'student_help/list_posts.html', {'comment': evenement})

@login_required
def ajouter_commentaire(request, recommandation_id):
    if request.method == 'POST':
        recommandation = Recommandation.objects.get(pk=recommandation_id)
        texte_commentaire = request.POST.get('comment')  # Récupérer le texte du commentaire à partir du formulaire
        Commentaire.objects.create(user=request.user, recommandation=recommandation, texte=texte_commentaire)
    return redirect('Student_Help:poste')

def list_comments(request , publication_id):
    publication = get_object_or_404(Recommandation, pk=publication_id)

    comments = Commentaire.objects.filter(recommandation=publication).order_by('-date_creation')
   
    return render(request, 'Student_Help/list_comments.html', {'publication': publication, 'comments': comments})

def comments_l(request , publication_id):
    publication = get_object_or_404(Logement, pk=publication_id)

    comments = Commentairel.objects.filter(logement=publication).order_by('-date_creation')
   
    return render(request, 'Student_Help/list_comments.html', {'publication': publication,'comments': comments})

def comments_t(request, publication_id):
    publication = get_object_or_404(Transport, pk=publication_id)

    comments = Commentairet.objects.filter(transport=publication).order_by('-date_creation')
   
    return render(request, 'Student_Help/list_comments.html', {'publication': publication,'comments': comments})

def comments_s(request, publication_id):
    publication = get_object_or_404(Stage, pk=publication_id)

    comments = Commentaires.objects.filter(stage=publication).order_by('-date_creation')
   
    return render(request, 'Student_Help/list_comments.html', {'publication': publication,'comments': comments})

def comments_e(request, publication_id):
    publication = get_object_or_404(Evènement, pk=publication_id)

    comments = Commentairee.objects.filter(evenement=publication).order_by('-date_creation')
   
    return render(request, 'Student_Help/list_comments.html', {'publication': publication,'comments': comments})

class ModifierComment(UpdateView):
    model = Commentaire
    template_name = 'Student_Help/Modifier_comment.html'
    form_class = CommentaireForm 

    def get_success_url(self):
        return reverse_lazy('Student_Help:list_comments', kwargs={'publication_id': self.object.recommandation.pk})

class SupprimerComment(DeleteView):
    model = Commentaire
    template_name = 'Student_Help/Supprimer_comment.html'
    def get_success_url(self):
        return reverse_lazy('Student_Help:list_comments', kwargs={'publication_id': self.object.recommandation.pk})

class ModifierCommentl(UpdateView):
    model = Commentaire
    template_name = 'Student_Help/Modifier_comment.html'
    form_class = CommentaireForm 

    def get_success_url(self):
        return reverse_lazy('Student_Help:list_comments', kwargs={'publication_id': self.object.logement.pk})

class SupprimerCommentl(DeleteView):
    model = Commentaire
    template_name = 'Student_Help/Supprimer_comment.html'
    def get_success_url(self):
        return reverse_lazy('Student_Help:list_comments', kwargs={'publication_id': self.object.logement.pk})
    
class ModifierPost(UpdateView):
    model = Poste
    template_name = 'Student_Help/Modifier_post.html'
    form_class = PosteForm  
    success_url = reverse_lazy('Student_Help:poste')
class SupprimerPost(DeleteView):
    model = Poste
    template_name = 'Student_Help/Supprimer_post.html'
    success_url = reverse_lazy('Student_Help:poste') 

class UserEditView(LoginRequiredMixin, UpdateView):
    form_class = EditProfileForm
    template_name = "registration/edit_profile.html"
    success_url = '/Student_Help'  # Changer l'URL de redirection vers la page d'accueil

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        # Enregistrement du formulaire et redirection vers la page d'accueil
        form.save()
        return redirect('Student_Help:ind')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Rediriger vers une page après la connexion réussie
                return render(request, 'Student_Help/index.html')  # Remplacez  par l'URL de la page à rediriger
            else:
                # Si l'authentification échoue, afficher un message d'erreur
                error_message = "Nom d'utilisateur ou mot de passe incorrect."
                return render(request, 'registration/login.html', {'form': form, 'error_message': error_message})
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Ne pas enregistrer directement dans la base de données
            user.email = form.cleaned_data.get('email')  # Récupérer l'adresse e-mail depuis le formulaire
            user.save()  # Maintenant, enregistrez l'utilisateur avec l'e-mail
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Hello {username}, Your account has been created successfully!')
            return render(request, 'Student_Help/index.html')  # Redirigez l'utilisateur vers la page d'accueil après l'inscription
    else:
        form = UserRegistrationForm()
    
    return render(request, 'registration/register.html', {'form': form})

def logout_view(request):
    logout(request)
    # Rediriger vers une page de confirmation de déconnexion ou une autre page
    return render(request,'Student_Help/index.html')  # Remplacez 'page_accueil' par le nom de l'URL de la page d'accueil de votre application

def list_posts(request):
    recommandations = Recommandation.objects.all().order_by('-date')
    logements = Logement.objects.all().order_by('-date')
    transports = Transport.objects.all().order_by('-date')
    stages = Stage.objects.all().order_by('-date')
    evenements = Evènement.objects.all().order_by('-date')
    likes=Like.objects.all()
    return render(request, 'Student_Help/list_posts.html', {'recommandations': recommandations, 'logements': logements, 'transports': transports, 'stages': stages, 'evenements': evenements ,'likes':likes})

def list_Enseignant(request):
    query = request.GET.get('q')
    print("Query:", query)  # Ajoutez ce message de débogage pour voir ce qui est recherché
    list = Enseignant.objects.all()
    if query:
        list = list.filter(prenom__icontains=query)
    print("Results:", list)  # Ajoutez ce message de débogage pour voir les résultats de la recherche
    return render(request, 'Student_Help/list_Enseignant.html', {'list': list})

def send_email_to_enseignant(request, enseignant_email):
    subject = 'Sujet de l\'e-mail'  # Modify the subject of the email as needed
    message = 'Quelqu\'un a cliqué sur votre mail'  # Modify the content of the email as needed
    sender_email = 'mkaouar.chayma7@example.com'  # Modify the sender's email address
    recipient_email = enseignant_email  # Use the email of the teacher passed as a parameter

    send_mail(subject, message, sender_email, [recipient_email])
    return render(request, 'Student_Help/list_Enseignant.html')

def recPost(request):
    recommandations = Recommandation.objects.all()
    user = request.user
    context = {
        'recommandations': recommandations,
        'user': user,
    }
    return render(request, 'Student_Help/recommandations.html', context)

def logPost(request):
    logements = Logement.objects.all()
    user = request.user
    context = {
        'logements': logements,
        'user': user,
    }
    return render(request, 'Student_Help/logement.html', context)

def stgPost(request):
    stages = Stage.objects.all()
    user = request.user
    context = {
        'stages': stages,
        'user': user,
    }
    return render(request, 'Student_Help/stage.html', context)

def evPost(request):
    evenements = Evènement.objects.all()
    user = request.user
    context = {
        'evenements': evenements,
        'user': user,
    }
    return render(request, 'Student_Help/evenement.html', context)

def logTrans(request):
    transports = Transport.objects.all()
    user = request.user
    context = {
        'transports': transports,
        'user': user,
    }
    return render(request, 'Student_Help/transport.html', context)

def post(request):
    return render(request, 'Student_Help/post.html')

def index(request):
    return render(request, 'base.html')


def galerie(request):
    return render(request, 'Student_Help/galerie.html')



# def like_post(request):
#     if request.method == 'POST' and request.is_ajax():
#         post_id = request.POST.get('post_id')
#         action = request.POST.get('action')
#         if post_id and action in ['like', 'unlike']:
#             return JsonResponse({'success': True})
#         else:
#             return JsonResponse({'success': False, 'error': 'Invalid request'})
#     else:
#         return JsonResponse({'success': False, 'error': 'Invalid request'})

def plan(request):
    user = User.objects.all()
    context = {'User': user}
    return render(request, 'Student_Help/plan.html', context)

def org(request):
    user = User.objects.all()
    context = {'User': user}
    return render(request, 'Student_Help/organigramme.html', context)

def clubIset(request):
    return render(request, 'Student_Help/club.html')

def ind(request):
    user = User.objects.all()
    context = {'User': user}
    return render(request, 'Student_Help/index.html', context)

@login_required
def ajoutRec(request):
    if request.method == "POST":
        form = RecommandationForm(request.POST, request.FILES)
        if form.is_valid():
            rec = form.save(commit=False)
            rec.user = request.user  # Définir l'utilisateur connecté comme utilisateur de la recommandation
            rec.save()
            return render(request, 'Student_Help/list_posts.html')
    else:
        form = RecommandationForm(initial={'user': request.user})  # Passer l'utilisateur connecté comme initial
    return render(request, 'Student_Help/AjoutRec.html', {'form': form})


@login_required
def ajoutLogement(request):
    if request.method == "POST":
        form = LogementForm(request.POST, request.FILES)
        if form.is_valid():
            rec = form.save(commit=False)
            rec.user = request.user  # Définir l'utilisateur connecté comme utilisateur de la recommandation
            rec.save()
            return render(request, 'Student_Help/list_posts.html')
    else:
        form = LogementForm(initial={'user': request.user})  # Passer l'utilisateur connecté comme initial
        return render(request, 'Student_Help/ajoutLogement.html', {'form': form})
# def mesRec(request):
#     if request.method == "POST":
#         form = RecommandationForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/Student_Help')
#     else:
#         rec = Recommandation.objects.all()
#         return render(request, 'Student_Help/MesRec.html', {'rec': rec})
    
def mesRec(request):
    recommandations = Recommandation.objects.all()
    recommandations_with_like_count = []
    
    
    return render(request, 'Student_Help/MesRec.html', )
    

def ajoutTransport(request):
    if request.method == "POST":
        form = TransportForm(request.POST, request.FILES)
        if form.is_valid():
            rec = form.save(commit=False)
            rec.user = request.user  # Définir l'utilisateur connecté comme utilisateur de la recommandation
            rec.save()
            form.save()
        return HttpResponseRedirect('/Student_Help')
    else:
        form = TransportForm(initial={'user': request.user})
        return render(request, 'Student_Help/ajoutTransport.html', {'form': form})

def ajoutStage(request):
    if request.method == "POST":
        form = StageForm(request.POST, request.FILES)
        if form.is_valid():
            rec = form.save(commit=False)
            rec.user = request.user  # Définir l'utilisateur connecté comme utilisateur de la recommandation
            rec.save()
            form.save()
        return HttpResponseRedirect('/Student_Help')
    else:
        form = StageForm(initial={'user': request.user})
        return render(request, 'Student_Help/ajoutStage.html', {'form': form})
    
def ajoutEvenement(request):
    if request.method == "POST":
        form = EvènementForm(request.POST, request.FILES)
        if form.is_valid():
            rec = form.save(commit=False)
            rec.user = request.user  # Définir l'utilisateur connecté comme utilisateur de la recommandation
            rec.save()
            form.save()
        return HttpResponseRedirect('/Student_Help')
    else:
        form = EvènementForm()
        return render(request, 'Student_Help/ajoutEvenement.html', {'form': form})
    
def AjoutContact(request):
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/Student_Help')
    else:
        form = ContactForm()
        return render(request, 'Student_Help/Contact.html', {'form': form})
    

def send(request):
    if request.method == 'POST':
        nom = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        
        # Enregistrer les données dans la base de données
        contact_obj = Contact.objects.create(
            nom=nom,
            email=email,
            message=message
        )

        # Envoyer un email (en supposant que vous avez les imports nécessaires)
        send_mail(
            'Hey ' + nom,
            'Nous avons reçu votre message!\n\nVotre message: ' + message,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False
        )

    return render(request, 'Student_Help/index.html')

@login_required
def invite_user(request, username):
    try:
        # Trouver l'utilisateur par son nom d'utilisateur
        user = get_object_or_404(User, username=username)

        # Vérifier si une invitation existe déjà pour cet utilisateur
        if Invitation.objects.filter(email=user.email, invited_by=request.user).exists():
            messages.warning(request, f"An invitation to {user.username} has already been sent.")
        else:
            # Générer le code d'invitation
            code = get_random_string(20)

            # Créer l'invitation avec l'adresse e-mail
            invitation = Invitation.objects.create(
                email=user.email,
                code=code,
                invited_by=request.user
            )

            # Envoyer l'e-mail d'invitation
            send_mail(
                f'Hello',
                f'You have a new request from: {request.user}',
                'from@example.com',
                [user.email],  # Envoyer l'e-mail à l'adresse e-mail de l'utilisateur
                fail_silently=False,
            )

            messages.success(request, f"Invitation sent to {user.username} successfully.")

    except User.DoesNotExist:
        messages.error(request, "User does not exist.")
        return redirect('path_to_error_page')

    return redirect('Student_Help:invitation_sent')

def invitation_sent(request):
    return render(request, 'Student_Help/invitation_sent.html')

def invitation_list(request):
    invitations = Invitation.objects.filter(email=request.user.email)
    return render(request, 'Student_Help/invitation_list.html', {'invitations': invitations})

from django.shortcuts import redirect, get_object_or_404
from .models import Invitation, FriendList

def accept_invitation(request, invitation_id):
    invitation = get_object_or_404(Invitation, pk=invitation_id)
    
    # Ajouter l'expéditeur de l'invitation à la liste d'amis de l'utilisateur connecté
    friend_list_user = FriendList.objects.get_or_create(user=request.user)[0]
    friend_list_user.friends.add(invitation.invited_by)
    friend_list_user.save()
    
    # Ajouter l'utilisateur connecté à la liste d'amis de l'expéditeur de l'invitation
    friend_list_inviter = FriendList.objects.get_or_create(user=invitation.invited_by)[0]
    friend_list_inviter.friends.add(request.user)
    friend_list_inviter.save()
    
    # Supprimer l'invitation acceptée
    invitation.delete()
    
    return redirect('Student_Help:invitation_list')

def reject_invitation(request, invitation_id):
    invitation = get_object_or_404(Invitation, pk=invitation_id)
    # Logique pour refuser l'invitation
    # Par exemple : invitation.rejected = True
    # Supprimer l'invitation rejetée
    invitation.delete()
    return redirect('Student_Help:invitation_list')


@login_required
def view_friends(request):
    friend_list = FriendList.objects.filter(user=request.user).first()
    friends = friend_list.friends.all() if friend_list else []
    return render(request, 'Student_Help/view_friends.html', {'friends': friends})
    



def reserver_logement(request, logement_id):
    if not request.user.is_authenticated:
        messages.error(request, 'Vous devez être connecté pour réserver un logement.')
        return redirect('Student_Help:login')

    logement = get_object_or_404(Logement, pk=logement_id)
    user = request.user

    if Reservation.user_has_reservation_for_logement(user, logement):
        alert_reservation_exists = True
        return render(request, 'Student_Help/list_posts.html', {'alert_reservation_exists': alert_reservation_exists})

    # Créer une nouvelle réservation
    reservation = Reservation(user=user, logement=logement)
    reservation.save()


    # Envoyer un e-mail de confirmation de réservation
    subject = 'Confirmation de réservation'
    message = f"Bonjour {user.username},\n\nVous avez réservé le logement '{logement}' avec succès."
    sender = 'mkaouar.chayma7@email.com'
    recipient = [user.email]  # Adresse e-mail de l'utilisateur connecté
    send_mail(subject, message, sender, recipient)

    return redirect('Student_Help:LogRes', logement_id=logement_id)


def list_postsRes(request, logement_id=None):
    recommandations = Recommandation.objects.all().order_by('-date')
    logements = Logement.objects.all().order_by('-date')
    transports = Transport.objects.all().order_by('-date')
    stages = Stage.objects.all().order_by('-date')
    evenements = Evènement.objects.all().order_by('-date')
    likes = Like.objects.all()
    return render(request, 'Student_Help/list_posts.html', {'recommandations': recommandations, 'logements': logements, 'transports': transports, 'stages': stages, 'evenements': evenements ,'likes':likes})
