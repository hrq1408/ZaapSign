import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { DocumentService } from '../document.service';
import { MatTableModule } from '@angular/material/table';
import { HttpClient, HttpHandler, HttpXhrBackend } from '@angular/common/http';
import { HttpClientModule } from '@angular/common/http';


@Component({
  selector: 'app-document-list',
  standalone: true,
  imports: [CommonModule, MatTableModule, HttpClientModule],
  templateUrl: './document-list.component.html',
  styleUrls: ['./document-list.component.css'],
  providers: [{
    provide: DocumentService,
    useFactory: (handler: HttpHandler) => new DocumentService(new HttpClient(handler)), // Injete o HttpHandler
    deps: [HttpXhrBackend] // Declare a dependência do HttpXhrBackend
  }]
})
export class DocumentListComponent implements OnInit {
  displayedColumns: string[] = ['name', 'status', 'signerName', 'signerEmail'];
  dataSource: any[] = [];

  constructor(private documentService: DocumentService) { }

  ngOnInit(): void {
    this.loadDocuments();
  }

  loadDocuments(): void {
    this.documentService.getDocuments()
      .subscribe(
        (documents) => {
          this.dataSource = documents;
        },
        (error) => {
          console.error('Erro ao carregar documentos:', error);
          // Lógica para tratamento de erro (exibir mensagem, etc.)
        }
      );
  }
}
