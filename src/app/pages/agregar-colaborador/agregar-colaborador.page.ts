import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import {IonButton, IonContent, IonHeader, IonIcon, IonInput, IonLabel, IonSelect, IonSelectOption, IonTitle, IonToolbar, AlertController } from '@ionic/angular';
import { personCircleOutline, camera } from 'ionicons/icons';
import { addIcons } from 'ionicons';

@Component({
  selector: 'app-agregar-colaborador',
  templateUrl: './agregar-colaborador.page.html',
  styleUrls: ['./agregar-colaborador.page.scss'],
  imports: [IonIcon, IonInput, IonLabel, IonSelect, IonSelectOption, IonButton, IonContent, IonHeader, IonTitle, IonToolbar, CommonModule, FormsModule
  ]
})
export class AgregarColaboradorPage implements OnInit {

  nombre = '';
  correo = '';
  telefono = '';
  puesto = '';
  departamento = '';
  fechaIngreso = '';

  constructor(private alertController: AlertController) {
    addIcons({
    'person-circle-outline': personCircleOutline, 'camera':camera
    });
  }

  ngOnInit() {
  }

  async guardarColaborador() {
    const alerta = await this.alertController.create({
      header: 'Colaborador agregado',
      message: 'Los datos de ' + this.nombre +
        ' se han capturado correctamente.',
      buttons: ['Aceptar']
    });

    await alerta.present();
  }

}
