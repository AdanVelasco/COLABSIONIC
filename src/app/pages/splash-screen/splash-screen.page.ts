import { Component, OnInit, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { IonContent, IonHeader, IonTitle, IonToolbar, IonIcon, IonButton,  LoadingController } from '@ionic/angular';
import { peopleSharp } from 'ionicons/icons';
import { addIcons } from 'ionicons';
import { Router } from '@angular/router';

@Component({
selector: 'app-splash-screen',
templateUrl: './splash-screen.page.html',
styleUrls: ['./splash-screen.page.scss'],
imports: [IonContent, IonHeader, IonTitle, IonToolbar, CommonModule, FormsModule, IonIcon, IonButton]
})
export class SplashScreenPage implements OnInit {
   // private router = signal(Router);

   

constructor(private router: Router,
     private loadingCtrl: LoadingController
) {
addIcons({
'people-sharp': peopleSharp
});
}

ngOnInit() {
    
}

   async showLoading() {
    const loading = await this.loadingCtrl.create({
      message: 'Cargando colaboradores...',
      duration: 3000,
      spinner: 'crescent'
    });

    await loading.present();
    await loading.onDidDismiss();
  }

  async colaboradores() {
    await this.showLoading();
    this.router.navigate(['/tabs/tab1']);
  }

}
