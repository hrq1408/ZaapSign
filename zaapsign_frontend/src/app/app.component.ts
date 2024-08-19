import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { DocumentFormComponent } from './document-form/document-form.component';
import { DocumentListComponent } from './document-list/document-list.component';
import { DocumentService } from './document.service';

@Component({
  selector: 'app-root',
  standalone: true, // Mova esta linha para cima
  imports: [CommonModule, DocumentFormComponent, DocumentListComponent],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [DocumentService]
})
export class AppComponent {
  name = 'ZaapSign';
}
