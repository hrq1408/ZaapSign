import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

interface Document {
  id: number;
  name: string;
  status: string;
  signerName: string;
  signerEmail: string;
  pdfUrl: string;

}

@Injectable({
  providedIn: 'root'
})
export class DocumentService {
  private apiUrl = 'http://localhost:8000/api/documents/';

  constructor(private http: HttpClient) { }

  getDocuments(): Observable<Document[]> {
    return this.http.get<Document[]>(this.apiUrl);
  }

  createDocument(documentData: any): Observable<Document> {
    return this.http.post<Document>(this.apiUrl, documentData, {
      headers: {
        'Content-Type': 'application/json'
      }
    });
  }


  updateDocument(id: number, documentData: any): Observable<Document> {
    return this.http.put<Document>(`${this.apiUrl}${id}/`, documentData);
  }

  deleteDocument(id: number): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}${id}/`);
  }
}
