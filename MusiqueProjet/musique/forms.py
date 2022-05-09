from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class MusiqueForm(ModelForm):
    class Meta :
        model = models.Musique
        fields = ('titre', 'artiste','date_parution', 'min', 'sec', 'commentaire')
        labels = {
            'titre' : _('Titre'),
            'artiste' : _('Artiste'),
            'date_parution' : _('Date de parution'),
            'min' : _('Minutes'),
            'sec' : _('Secondes'),
            'commentaire' : _('Commentaire'),
        }

class AlbumForm(ModelForm):
    class Meta :
        model = models.Album
        fields = ('nom', 'artiste', 'date')
        labels = {
            'nom' : _('Nom'),
            'artiste' : _('Artiste'),
            'date' : _('Date de création'),
        }
