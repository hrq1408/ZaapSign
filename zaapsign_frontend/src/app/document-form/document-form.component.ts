import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { DocumentService } from '../document.service';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule } from '@angular/forms';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';

@Component({
  selector: 'app-document-form',
  standalone: true, // Adicione esta linha
  imports: [CommonModule, ReactiveFormsModule, MatFormFieldModule, MatInputModule, MatButtonModule],
  templateUrl: './document-form.component.html',
  styleUrls: ['./document-form.component.css']
})
export class DocumentFormComponent {
  documentForm: FormGroup;

  constructor(private fb: FormBuilder, private documentService: DocumentService) {
    this.documentForm = this.fb.group({
      name: ['', Validators.required],
      signerName: ['', Validators.required],
      signerEmail: ['', [Validators.required, Validators.email]],
      pdfUrl: ['', Validators.required]
    });
  }

  onSubmit() {
    if (this.documentForm.valid) {
      const documentData = this.documentForm.value;

      this.documentService.createDocument(documentData)
        .subscribe({
          next: (response) => {
            console.log('Documento criado com sucesso:', response);
            // Lógica para exibir mensagem de sucesso, limpar o formulário e atualizar a lista de documentos
          },
          error: (error) => {
            console.error('Erro ao criar documento:', error);
            // Lógica para exibir mensagem de erro
          }
        });
    }
  }
}
