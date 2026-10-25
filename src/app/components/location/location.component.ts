import { Component, inject, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { DomSanitizer, SafeResourceUrl } from '@angular/platform-browser';
import { LanguageService } from '../../services/language.service';
import { TRANSLATIONS } from '../../data/translations';
import { RESTAURANT_CONFIG } from '../../data/restaurant-config';

@Component({
  selector: 'app-location',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './location.component.html',
  styleUrl: './location.component.scss'
})
export class LocationComponent {
  readonly langService = inject(LanguageService);
  readonly config = RESTAURANT_CONFIG;
  private readonly sanitizer = inject(DomSanitizer);

  readonly copied = signal<boolean>(false);

  // Safe Google Maps Embed URL using exact coordinates
  readonly mapEmbedUrl: SafeResourceUrl = this.sanitizer.bypassSecurityTrustResourceUrl(
    `https://maps.google.com/maps?q=${this.config.location.latitude},${this.config.location.longitude}&hl=${this.langService.currentLang()}&z=16&output=embed`
  );

  get t() {
    return TRANSLATIONS[this.langService.currentLang()];
  }

  copyAddress(): void {
    const textToCopy = this.langService.isTamil()
      ? this.config.location.fullAddressTa
      : this.config.location.fullAddressEn;

    if (navigator.clipboard) {
      navigator.clipboard.writeText(textToCopy).then(() => {
        this.copied.set(true);
        setTimeout(() => this.copied.set(false), 2500);
      });
    }
  }
}
