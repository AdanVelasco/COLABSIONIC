import { Component } from '@angular/core';
import { IonFabButton, IonFab ,IonItem, IonLabel, IonAvatar, IonList, IonHeader, IonToolbar, IonTitle, IonContent, IonSearchbar, IonButton, IonIcon } from '@ionic/angular';
import { peopleSharp } from 'ionicons/icons';
import { addIcons } from 'ionicons';
import { add } from 'ionicons/icons';
import { Router } from '@angular/router';


@Component({
  selector: 'app-tab1',
  templateUrl: 'tab1.page.html',
  styleUrls: ['tab1.page.scss'],
  imports: [IonFabButton, IonFab, IonLabel, IonAvatar, IonList, IonHeader, IonToolbar, IonTitle, IonContent, IonSearchbar, IonButton, IonIcon, IonItem],
})

export class Tab1Page {
  sihay=true;
  constructor(private router: Router) {
    addIcons({
      'people-sharp': peopleSharp
    });
    addIcons({ add });

  }

  Agregar_Colaboradores(){
    this.router.navigate(['agregar-colaborador']);  
  }

}
