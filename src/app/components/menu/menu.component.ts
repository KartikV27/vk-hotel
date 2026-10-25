import { Component, inject, signal, computed } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LanguageService } from '../../services/language.service';
import { TRANSLATIONS } from '../../data/translations';
import { MENU_CATEGORIES, MENU_ITEMS } from '../../data/menu-data';
import { MenuCategoryKey, MenuItem } from '../../models/restaurant.model';

@Component({
  selector: 'app-menu',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './menu.component.html',
  styleUrl: './menu.component.scss'
})
export class MenuComponent {
  readonly langService = inject(LanguageService);
  readonly categories = MENU_CATEGORIES;
  readonly allItems = MENU_ITEMS;

  readonly selectedCategory = signal<MenuCategoryKey | 'all'>('all');
  readonly vegOnlyFilter = signal<boolean>(false);

  get t() {
    return TRANSLATIONS[this.langService.currentLang()];
  }

  readonly filteredItems = computed(() => {
    const category = this.selectedCategory();
    const vegOnly = this.vegOnlyFilter();

    return this.allItems.filter(item => {
      const matchCat = category === 'all' || item.category === category;
      const matchVeg = !vegOnly || item.isVeg;
      return matchCat && matchVeg;
    });
  });

  selectCategory(categoryKey: MenuCategoryKey | 'all'): void {
    this.selectedCategory.set(categoryKey);
  }

  toggleVegFilter(): void {
    this.vegOnlyFilter.update(v => !v);
  }

  getCategoryTitle(key: MenuCategoryKey): string {
    const cat = this.categories.find(c => c.key === key);
    if (!cat) return '';
    return this.langService.isTamil() ? cat.titleTa : cat.titleEn;
  }
}
