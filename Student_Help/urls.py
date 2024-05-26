from django.urls import path
from . import views
from .views import UserEditView,ModifierPost,SupprimerPost,ModifierComment,SupprimerComment,ModifierCommentl,SupprimerCommentl

app_name = 'Student_Help'

urlpatterns = [
    path('', views.ind, name="ind"),
    path('ajoutRec/', views.ajoutRec, name="ajoutRec"),
    path('rec/', views.mesRec, name='rec'),
    path('list_posts/', views.list_posts, name='poste'),
    path('ajoutLogement/', views.ajoutLogement, name='ajoutLogement'),
    path('ajoutTransport/', views.ajoutTransport, name='ajoutTransport'),
    path('ajoutStage/', views.ajoutStage, name='ajoutStage'),
    path('ajoutEvenement/', views.ajoutEvenement, name='ajoutEvenement'),
    path('register/',views.register, name = 'register'),
    path('list_Enseignant/',views.list_Enseignant , name="list_Enseignant"),
    path('plan/',views.plan , name="plan"),
    path('organigramme/',views.org , name="org"),
    path('clubIset/',views.clubIset , name="clubIset"),
    path('galerie/',views.galerie , name="galerie"),
    path('contact/',views.AjoutContact , name="contact"),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.user_login, name='login'),
    path('notif/', views.notification_list, name='notif'),
    path('post/', views.post, name='post'),
    path('recpost/', views.recPost, name='recpost'),
    path('logPost/', views.logPost, name='logPost'),
    path('logTrans/', views.logTrans, name='logTrans'),
    path('stgPost/', views.stgPost, name='stgPost'),
    path('evPost/', views.evPost, name='evPost'),
    path("edit-profile/", UserEditView.as_view(), name="edit_profile"),
    path('<int:pk>/modifier/', ModifierPost.as_view(), name='modifier_post'),  
    path('<int:pk>/supprimer/', SupprimerPost.as_view(), name='supprimer_post'),
    path('recommandation/<int:recommandation_id>/commentaire/ajouter/', views.ajouter_commentaire, name='ajouter_commentaire'),
    path('like/recommandation/<int:recommandation_id>/', views.like_recommandation, name='like_recommandation'),
    path('recommandation/<int:recommandation_id>/commentaires/creer/', views.creer_commentaire, name='creer_commentaire'),
    path('send/',views.send , name='send'),
    path('like/logement/<int:logement_id>/', views.like_logement, name='like_logement'),
    path('like/stage/<int:stage_id>/', views.like_stage, name='like_stage'),
    path('like/transport/<int:transport_id>/', views.like_transport, name='like_transport'),
    path('like/event/<int:evenement_id>/', views.like_event, name='like_event'),

    path('list_comments/<int:publication_id>/', views.list_comments, name='list_comments'),
    path('<int:pk>/modifiercomment/', ModifierComment.as_view(), name='Modifier_comment'),  
    path('<int:pk>/supprimercomment/', SupprimerComment.as_view(), name='Supprimer_comment'),

    path('logement/<int:logement_id>/commentaires/creer/', views.creer_commentairel, name='creer_commentairel'),
    path('comments_logement/<int:publication_id>/', views.comments_l, name='comments_logement'),
    path('<int:pk>/modifiercommentl/', ModifierCommentl.as_view(), name='Modifier_commentl'),  
    path('<int:pk>/supprimercommentl/', SupprimerCommentl.as_view(), name='Supprimer_commentl'),

    path('transport/<int:transport_id>/commentaires/creer/', views.creer_commentairet, name='creer_commentairet'),
    path('comments_transport/<int:publication_id>/', views.comments_t, name='comments_transport'),

    path('stage/<int:stage_id>/commentaires/creer/', views.creer_commentaires, name='creer_commentaires'),
    path('comments_stage/<int:publication_id>/', views.comments_s, name='comments_stage'),

    path('event/<int:evenement_id>/commentaires/creer/', views.creer_commentairee, name='creer_commentairee'),
    path('comments_event/<int:publication_id>/', views.comments_e, name='comments_event'),

    path('notif/', views.notification_l, name='notif'),
    path('notif/', views.notification_s, name='notifs'),
    path('notif/', views.notification_t, name='notif'),
    path('notif/', views.notification_e, name='notif'),
    path('notif/', views.notification_cr, name='notif'),


    path('inbox/', views.inbox, name='inbox'),
    path('sendMessage/', views.send_message, name='send_message'),
    path('list_message/', views.list_message, name='list_message'),

    path('invitation-sent/', views.invitation_sent, name='invitation_sent'),
    path('invite_list/', views.invite_list, name='invite_list'),
    path('invite-user/<str:username>/', views.invite_user, name='invite_user'),

    path('invitations/', views.invitation_list, name='invitation_list'),
    path('invitations/<int:invitation_id>/accept/', views.accept_invitation, name='accept_invitation'),
    path('invitations/<int:invitation_id>/reject/', views.reject_invitation, name='reject_invitation'),

    path('friends/', views.view_friends, name='view_friends'),


path('reserver/<int:logement_id>/', views.reserver_logement, name='reserver_logement'),

path('list_posts/<int:logement_id>/', views.list_postsRes, name='LogRes'),
path('sendMailEns/<str:enseignant_email>/', views.send_email_to_enseignant, name='send_email_to_enseignant')

]
