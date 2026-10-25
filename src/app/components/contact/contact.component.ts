import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LanguageService } from '../../services/language.service';
import { TRANSLATIONS } from '../../data/translations';
import { RESTAURANT_CONFIG } from '../../data/restaurant-config';

@Component({
  selector: 'app-contact',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './contact.component.html',
  styleUrl: './contact.component.scss'
})
export class ContactComponent {
  readonly langService = inject(LanguageService);
  readonly config = RESTAURANT_CONFIG;

  get t() {
    return TRANSLATIONS[this.langService.currentLang()];
  }
}
