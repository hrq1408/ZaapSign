import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { provideHttpClient } from '@angular/common/http';




@NgModule({
  declarations: [
  ],
  imports: [
    BrowserModule,


    BrowserAnimationsModule
  ],
  providers: [provideHttpClient()],
  exports: [
  ]
})
export class AppModule { }
