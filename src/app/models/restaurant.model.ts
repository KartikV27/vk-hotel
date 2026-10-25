export type Language = 'ta' | 'en';

export type MenuCategoryKey = 'porotta' | 'dosai' | 'chapathi' | 'veg-sides' | 'nonveg-sides';

export interface MenuItem {
  id: string;
  category: MenuCategoryKey;
  nameEn: string;
  nameTa: string;
  descriptionEn: string;
  descriptionTa: string;
  isVeg: boolean;
  priceDisplayEn: string;
  priceDisplayTa: string;
  image: string;
  popular?: boolean;
  badgeEn?: string;
  badgeTa?: string;
}

export interface MenuCategory {
  key: MenuCategoryKey;
  titleEn: string;
  titleTa: string;
  descriptionEn: string;
  descriptionTa: string;
  icon: string;
}

export interface RestaurantConfig {
  nameEn: string;
  nameTa: string;
  shortNameEn: string;
  shortNameTa: string;
  taglineEn: string;
  taglineTa: string;
  descriptionEn: string;
  descriptionTa: string;
  serviceTypeEn: string;
  serviceTypeTa: string;
  operatingHoursEn: string;
  operatingHoursTa: string;
  serviceNoteEn: string;
  serviceNoteTa: string;
  location: {
    streetEn: string;
    streetTa: string;
    villageEn: string;
    villageTa: string;
    pincode: string;
    districtEn: string;
    districtTa: string;
    stateEn: string;
    stateTa: string;
    fullAddressEn: string;
    fullAddressTa: string;
    googleMapsUrl: string;
    latitude: number;
    longitude: number;
  };
  contact: {
    // Leave blank if unconfirmed. Buttons will automatically hide.
    phoneNumber: string;
    whatsappNumber: string;
    email: string;
  };
}
