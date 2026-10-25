import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LanguageService } from '../../services/language.service';
import { TRANSLATIONS } from '../../data/translations';
import { RESTAURANT_CONFIG } from '../../data/restaurant-config';
import { MENU_CATEGORIES } from '../../data/menu-data';

@Component({
  selector: 'app-footer',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './footer.component.html',
  styleUrl: './footer.component.scss'
})
export class FooterComponent {
  readonly langService = inject(LanguageService);
  readonly config = RESTAURANT_CONFIG;
  readonly categories = MENU_CATEGORIES;
  readonly currentYear = new Date().getFullYear();

  get t() {
    return TRANSLATIONS[this.langService.currentLang()];
  }

  scrollToSection(sectionId: string, event?: Event): void {
    if (event) {
      event.preventDefault();
    }
    const el = document.getElementById(sectionId);
    if (el) {
      const headerOffset = 80;
      const elementPosition = el.getBoundingClientRect().top;
      const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
      window.scrollTo({
        top: offsetPosition,
        behavior: 'smooth'
      });
    }
  }

  scrollToTop(event: Event): void {
    event.preventDefault();
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  }
}
