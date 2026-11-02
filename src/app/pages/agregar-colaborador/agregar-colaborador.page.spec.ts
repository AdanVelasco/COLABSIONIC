import { ComponentFixture, TestBed } from '@angular/core/testing';
import { AgregarColaboradorPage } from './agregar-colaborador.page';

describe('AgregarColaboradorPage', () => {
  let component: AgregarColaboradorPage;
  let fixture: ComponentFixture<AgregarColaboradorPage>;

  beforeEach(() => {
    fixture = TestBed.createComponent(AgregarColaboradorPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
