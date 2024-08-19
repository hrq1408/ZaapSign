import { bootstrapApplication } from '@angular/platform-browser';
import { AppComponent } from './app/app.component';
import { importProvidersFrom } from '@angular/core';
import { provideHttpClient } from '@angular/common/http';
import { AppModule } from './app/app.module';

bootstrapApplication(AppComponent, {
  providers: [
    importProvidersFrom(AppModule),
    provideHttpClient()
  ]
}).catch(err => console.error(err));
