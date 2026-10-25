import { Injectable, signal, computed } from '@angular/core';
import { Language } from '../models/restaurant.model';

@Injectable({
  providedIn: 'root'
})
export class LanguageService {
  private readonly STORAGE_KEY = 'vk_hotel_lang';

  // Default to Tamil ('ta') as primary local language, with instant switch to 'en'
  readonly currentLang = signal<Language>(this.getInitialLanguage());

  readonly isTamil = computed(() => this.currentLang() === 'ta');
  readonly isEnglish = computed(() => this.currentLang() === 'en');

  private getInitialLanguage(): Language {
    if (typeof window !== 'undefined') {
      try {
        const urlParams = new URLSearchParams(window.location.search);
        const queryLang = urlParams.get('lang');
        if (queryLang === 'ta' || queryLang === 'en') {
          return queryLang as Language;
        }
      } catch {}

      if (window.localStorage) {
        const saved = localStorage.getItem(this.STORAGE_KEY) as Language;
        if (saved === 'ta' || saved === 'en') {
          return saved;
        }
      }
    }
    return 'en'; // Default to English on first visit
  }

  constructor() {
    this.updateDocumentAttributes(this.currentLang());
  }

  private updateDocumentAttributes(lang: Language): void {
    if (typeof document !== 'undefined') {
      document.documentElement.lang = lang;
      document.title = lang === 'ta'
        ? 'வி.கே ஹோட்டல் — கரடிசித்தூர் | மாலை & இரவு டிபன்'
        : 'V.K Hotel — Karadichittur | Evening & Night Tiffin';
    }
  }

  setLanguage(lang: Language): void {
    this.currentLang.set(lang);
    if (typeof window !== 'undefined' && window.localStorage) {
      localStorage.setItem(this.STORAGE_KEY, lang);
    }
    this.updateDocumentAttributes(lang);
  }

  toggleLanguage(): void {
    const nextLang: Language = this.currentLang() === 'ta' ? 'en' : 'ta';
    this.setLanguage(nextLang);
  }
}
