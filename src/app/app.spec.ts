import { TestBed } from '@angular/core/testing';
import { App } from './app';
import { LanguageService } from './services/language.service';

describe('App', () => {
  beforeEach(async () => {
    localStorage.clear();
    await TestBed.configureTestingModule({
      imports: [App],
    }).compileComponents();
  });

  afterEach(() => {
    localStorage.clear();
  });

  it('should create the app', () => {
    const fixture = TestBed.createComponent(App);
    const app = fixture.componentInstance;
    expect(app).toBeTruthy();
  });

  it('should render hero headline in English by default on first visit', () => {
    const fixture = TestBed.createComponent(App);
    fixture.detectChanges();
    const compiled = fixture.nativeElement as HTMLElement;
    expect(compiled.querySelector('h1')?.textContent).toContain('Hot Tiffin. Homestyle Taste.');
  });

  it('should render hero headline in Tamil when switched to Tamil', () => {
    const fixture = TestBed.createComponent(App);
    const langService = TestBed.inject(LanguageService);
    langService.setLanguage('ta');
    fixture.detectChanges();
    const compiled = fixture.nativeElement as HTMLElement;
    expect(compiled.querySelector('h1')?.textContent).toContain('சூடான டிபன்');
  });
});
