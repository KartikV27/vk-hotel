import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LanguageService } from '../../services/language.service';
import { TRANSLATIONS } from '../../data/translations';
import { RESTAURANT_CONFIG } from '../../data/restaurant-config';

@Component({
  selector: 'app-hero',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './hero.component.html',
  styleUrl: './hero.component.scss'
})
export class HeroComponent {
  readonly langService = inject(LanguageService);
  readonly config = RESTAURANT_CONFIG;

  get t() {
    return TRANSLATIONS[this.langService.currentLang()];
  }

  scrollToMenu(event: Event): void {
    event.preventDefault();
    const menuEl = document.getElementById('menu');
    if (menuEl) {
      const headerOffset = 80;
      const elementPosition = menuEl.getBoundingClientRect().top;
      const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
      window.scrollTo({
        top: offsetPosition,
        behavior: 'smooth'
      });
    }
  }
}
