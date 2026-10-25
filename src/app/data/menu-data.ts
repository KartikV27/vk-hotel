import { MenuCategory, MenuItem } from '../models/restaurant.model';

/**
 * VK HOTEL — MENU DATA
 *
 * Standardized Indian English food terms:
 * - Porotta
 * - Dosai
 * - Chapathi
 * - Salna
 * - Kothu Porotta
 *
 * FACTUAL ACCURACY:
 * - Unconfirmed dishes use standard evening tiffin preparations.
 * - All prices remain clearly marked as "Price on request" until confirmed.
 */

export const MENU_CATEGORIES: MenuCategory[] = [
  {
    key: 'porotta',
    titleEn: 'Porotta Varieties',
    titleTa: 'பரோட்டா வகைகள்',
    descriptionEn: 'Freshly made layered and kothu porottas served with spiced tiffin salna.',
    descriptionTa: 'கை பக்குவத்தில் சுடச்சுட அடிக்கப்பட்டு, மொறுமொறு அடுக்குடன் மணக்கும் சால்னாவுடன் பரிமாறப்படும் பரோட்டா.',
    icon: 'flaky'
  },
  {
    key: 'dosai',
    titleEn: 'Dosai Varieties',
    titleTa: 'தோசை வகைகள்',
    descriptionEn: 'Crisp roast dosais and soft kal dosais cooked fresh on the iron tawa.',
    descriptionTa: 'சூடான இரும்பு கல்லில் ஊற்றி மொறுமொறுப்பாகவும், மெத்தென்ற கல் தோசையாகவும் சுடப்படும் தோசை வகைகள்.',
    icon: 'dosa'
  },
  {
    key: 'chapathi',
    titleEn: 'Chapathi',
    titleTa: 'சப்பாத்தி',
    descriptionEn: 'Soft whole-wheat flatbreads served with vegetable kurma or salna.',
    descriptionTa: 'மென்மையான கோதுமை சப்பாத்தி, சால்னா மற்றும் சுவையான குருமாவோடு சாப்பிடுவதற்கு ஏற்றது.',
    icon: 'flatbread'
  },
  {
    key: 'veg-sides',
    titleEn: 'Vegetarian Side Dishes',
    titleTa: 'சைவ கறி வகைகள்',
    descriptionEn: 'Coconut vegetable kurma, lentil sambar, and freshly ground chutneys.',
    descriptionTa: 'அசல் நாட்டு சுவையில் மணக்கும் வெள்ளை குருமா, சாம்பார் மற்றும் கார சட்னி வகைகள்.',
    icon: 'leaf'
  },
  {
    key: 'nonveg-sides',
    titleEn: 'Non-Vegetarian Side Dishes',
    titleTa: 'அசைவ கறி வகைகள்',
    descriptionEn: 'Traditional chicken chukka, spiced tiffin salna, and egg preparations.',
    descriptionTa: 'நாட்டு பாணியில் காரசாரமாக தயாரிக்கப்படும் சால்னா மற்றும் சுவையான அசைவ கறி வகைகள்.',
    icon: 'meat'
  }
];

export const MENU_ITEMS: MenuItem[] = [
  // --- POROTTA VARIETIES ---
  {
    id: 'parotta-salna',
    category: 'porotta',
    nameEn: 'Layered Porotta with Salna',
    nameTa: 'அடுக்கு பரோட்டா (சால்னாவுடன்)',
    descriptionEn: 'Freshly made layered porotta served warm with spiced tiffin salna.',
    descriptionTa: 'சுடச்சுட அடிக்கப்பட்ட மொறுமொறு அடுக்கு பரோட்டா, மணக்கும் சால்னாவுடன்.',
    isVeg: true,
    priceDisplayEn: 'Price on request',
    priceDisplayTa: 'விலை விவரம் அறிய',
    image: 'images/porotta.jpg',
    popular: true,
    badgeEn: 'House Specialty',
    badgeTa: 'சிறப்பு உணவு'
  },
  {
    id: 'kothu-parotta',
    category: 'porotta',
    nameEn: 'Kothu Porotta',
    nameTa: 'கொத்து பரோட்டா',
    descriptionEn: 'Shredded porotta tossed on a hot iron tawa with eggs, onions, green chillies, and spiced gravy.',
    descriptionTa: 'இரும்பு கல்லில் சூடாக கொத்தி வெங்காயம், பச்சை மிளகாய், மசாலா கலந்து தயாரிக்கப்படும் சுவையான கொத்து பரோட்டா.',
    isVeg: false,
    priceDisplayEn: 'Price on request',
    priceDisplayTa: 'விலை விவரம் அறிய',
    image: 'images/kothu-parotta.jpg',
    popular: true,
    badgeEn: 'Popular Choice',
    badgeTa: 'விருப்ப உணவு'
  },
  {
    id: 'egg-parotta',
    category: 'porotta',
    nameEn: 'Egg Porotta (Veechu)',
    nameTa: 'முட்டை பரோட்டா / வீச்சு',
    descriptionEn: 'Thinly stretched porotta folded with seasoned beaten egg and roasted on the tawa.',
    descriptionTa: 'மெல்லிய வீச்சு பரோட்டாவில் முட்டை மசாலா சேர்த்து கல்லில் மொறுமொறுப்பாக சுடப்பட்டது.',
    isVeg: false,
    priceDisplayEn: 'Price on request',
    priceDisplayTa: 'விலை விவரம் அறிய',
    image: 'images/hero-feast.jpg'
  },

  // --- DOSAI VARIETIES ---
  {
    id: 'ghee-roast-dosa',
    category: 'dosai',
    nameEn: 'Ghee Roast Dosai',
    nameTa: 'நெய் ரோஸ்ட் தோசை',
    descriptionEn: 'Crisp, golden dosai roasted with ghee and served with fresh chutneys and sambar.',
    descriptionTa: 'சுவையான நெய் மணம் கமழ பொன்னிறமாக சுடப்பட்ட மொறுமொறு நெய் ரோஸ்ட் தோசை.',
    isVeg: true,
    priceDisplayEn: 'Price on request',
    priceDisplayTa: 'விலை விவரம் அறிய',
    image: 'images/dosa.jpg',
    popular: true,
    badgeEn: 'Crispy',
    badgeTa: 'பொன்னிற மொறுமொறு'
  },
  {
    id: 'kal-dosai',
    category: 'dosai',
    nameEn: 'Kal Dosai (Set)',
    nameTa: 'மெதுவான கல் தோசை',
    descriptionEn: 'Thick, soft homestyle dosais cooked on the tawa, served with salna and chutney.',
    descriptionTa: 'பஞ்சு போன்ற மென்மையான கிராமத்து கல் தோசை, சால்னா ஊற்றி சாப்பிட உகந்தது.',
    isVeg: true,
    priceDisplayEn: 'Price on request',
    priceDisplayTa: 'விலை விவரம் அறிய',
    image: 'images/dosa.jpg'
  },
  {
    id: 'egg-dosai',
    category: 'dosai',
    nameEn: 'Egg Dosai (Muttai Dosai)',
    nameTa: 'முட்டை தோசை',
    descriptionEn: 'Traditional dosai topped with beaten egg, ground black pepper, and curry leaves.',
    descriptionTa: 'தோசையின் மேல் நாட்டு முட்டை, மிளகுத்தூள் தூவி சுடப்படும் சுவையான முட்டை தோசை.',
    isVeg: false,
    priceDisplayEn: 'Price on request',
    priceDisplayTa: 'விலை விவரம் அறிய',
    image: 'images/hero-feast.jpg',
    badgeEn: 'Popular Choice',
    badgeTa: 'விருப்ப உணவு'
  },
  {
    id: 'onion-roast-dosa',
    category: 'dosai',
    nameEn: 'Onion Roast Dosai',
    nameTa: 'வெங்காய ரோஸ்ட் தோசை',
    descriptionEn: 'Crisp dosai roasted on the tawa with finely chopped onions and curry leaves.',
    descriptionTa: 'பொடியாக நறுக்கிய வெங்காயம் தூவி பொன்னிறமாக சுடப்பட்ட மொறுமொறு வெங்காய தோசை.',
    isVeg: true,
    priceDisplayEn: 'Price on request',
    priceDisplayTa: 'விலை விவரம் அறிய',
    image: 'images/dosa.jpg'
  },

  // --- CHAPATHI ---
  {
    id: 'soft-chapathi',
    category: 'chapathi',
    nameEn: 'Chapathi (Set)',
    nameTa: 'மெதுவான கோதுமை சப்பாத்தி',
    descriptionEn: 'Soft whole-wheat flatbreads served warm with vegetable kurma or salna.',
    descriptionTa: 'சூடான மெல்லிய வீட்டு முறை கோதுமை சப்பாத்தி, சால்னா அல்லது குருமாவோடு பரிமாறப்படுகிறது.',
    isVeg: true,
    priceDisplayEn: 'Price on request',
    priceDisplayTa: 'விலை விவரம் அறிய',
    image: 'images/chapathi.jpg',
    popular: true,
    badgeEn: 'Homestyle',
    badgeTa: 'வீட்டு சுவை'
  },

  // --- VEGETARIAN SIDE DISHES ---
  {
    id: 'veg-vellai-kurma',
    category: 'veg-sides',
    nameEn: 'Vegetable Kurma (Vellai Kurma)',
    nameTa: 'நாட்டு வெள்ளை குருமா / சைவ குருமா',
    descriptionEn: 'Mildly spiced coconut and vegetable gravy prepared for porotta and chapathi.',
    descriptionTa: 'தேங்காய், முந்திரி மற்றும் காய்கறிகள் சேர்த்து பக்குவமாக தயாரிக்கப்பட்ட சுவையான வெள்ளை குருமா.',
    isVeg: true,
    priceDisplayEn: 'Price on request',
    priceDisplayTa: 'விலை விவரம் அறிய',
    image: 'images/veg-sides.jpg',
    popular: true,
    badgeEn: 'Vegetarian',
    badgeTa: 'சுத்த சைவம்'
  },
  {
    id: 'kadamba-sambar-chutney',
    category: 'veg-sides',
    nameEn: 'Sambar and Chutneys',
    nameTa: 'கிராமத்து சாம்பார் & இரட்டை சட்னி',
    descriptionEn: 'Lentil sambar served with freshly ground coconut chutney and spicy tomato chutney.',
    descriptionTa: 'மணமணக்கும் பருப்பு சாம்பார், தேங்காய் சட்னி மற்றும் காரசாரமான தக்காளி சட்னி காம்போ.',
    isVeg: true,
    priceDisplayEn: 'Price on request',
    priceDisplayTa: 'விலை விவரம் அறிய',
    image: 'images/veg-sides.jpg'
  },

  // --- NON-VEGETARIAN SIDE DISHES ---
  {
    id: 'tiffin-salna',
    category: 'nonveg-sides',
    nameEn: 'Tiffin Salna (Gravy)',
    nameTa: 'மணக்கும் டிபன் சால்னா (குழம்பு)',
    descriptionEn: 'Traditional spiced gravy slow-simmered with aromatic whole spices, served with porotta and dosai.',
    descriptionTa: 'பரோட்டாவிற்கு பிரத்யேகமாக பட்டை, கிராம்பு, ஏலக்காய் மணத்துடன் கொதிக்க வைக்கப்பட்ட அசல் கிராமத்து சால்னா.',
    isVeg: false,
    priceDisplayEn: 'Price on request',
    priceDisplayTa: 'விலை விவரம் அறிய',
    image: 'images/porotta.jpg',
    popular: true,
    badgeEn: 'Signature Gravy',
    badgeTa: 'தனித்துவ சால்னா'
  },
  {
    id: 'chicken-chukka',
    category: 'nonveg-sides',
    nameEn: 'Chicken Chukka',
    nameTa: 'கிராமத்து சிக்கன் சுக்கா',
    descriptionEn: 'Tender chicken pieces pan-roasted with shallots, curry leaves, and black pepper.',
    descriptionTa: 'சின்ன வெங்காயம், கறிவேப்பிலை, இடித்த மிளகு சேர்த்து சுடச்சுட வறுக்கப்பட்ட கிராமத்து சிக்கன் சுக்கா.',
    isVeg: false,
    priceDisplayEn: 'Price on request',
    priceDisplayTa: 'விலை விவரம் அறிய',
    image: 'images/chicken-chukka.jpg',
    popular: true,
    badgeEn: 'Spicy',
    badgeTa: 'காரசார விருந்து'
  },
  {
    id: 'muttai-kalakki',
    category: 'nonveg-sides',
    nameEn: 'Muttai Kalakki',
    nameTa: 'முட்டை கலக்கி',
    descriptionEn: 'Soft-cooked egg prepared on the tawa with a splash of hot salna gravy.',
    descriptionTa: 'சூடான தோசைக் கல்லில் சால்னா குழம்பு சேர்த்து மென்மையாக வறுத்து எடுக்கப்படும் பாரம்பரிய முட்டை கலக்கி.',
    isVeg: false,
    priceDisplayEn: 'Price on request',
    priceDisplayTa: 'விலை விவரம் அறிய',
    image: 'images/hero-feast.jpg'
  }
];
