import { RestaurantConfig } from '../models/restaurant.model';

/**
 * VK HOTEL — CENTRAL CONFIGURATION
 *
 * Edit this single file to update restaurant details, location coordinates,
 * Google Maps link, and contact details.
 *
 * FACTUAL ACCURACY NOTICE:
 * - Call and WhatsApp buttons are automatically HIDDEN when `phoneNumber`
 *   or `whatsappNumber` is empty ("").
 * - Operating hours are listed as unconfirmed general evening/night tiffin
 *   without stating an unverified start time.
 */
export const RESTAURANT_CONFIG: RestaurantConfig = {
  nameEn: 'V.K Hotel',
  nameTa: 'வி.கே ஹோட்டல்',
  shortNameEn: 'VK Hotel',
  shortNameTa: 'வி.கே ஹோட்டல்',
  taglineEn: 'Hot Tiffin. Homestyle Taste.',
  taglineTa: 'சூடான டிபன் • வீட்டு சுவை',
  descriptionEn: 'A local village restaurant on Karadichittur Main Road serving freshly made South Indian evening and night tiffin, including porotta, dosai, chapathi, and homestyle salna.',
  descriptionTa: 'கரடிசித்தூர் மெயின் ரோட்டில் அமைந்துள்ள கிராமத்து மாலை மற்றும் இரவு நேர டிபன் உணவகம். சுடச்சுட பரோட்டா, தோசை, சப்பாத்தி மற்றும் மணக்கும் சால்னாவுடன் அசல் வீட்டு சுவை.',
  serviceTypeEn: 'Evening & Night Tiffin',
  serviceTypeTa: 'மாலை மற்றும் இரவு டிபன்',
  operatingHoursEn: 'Evening and night tiffin',
  operatingHoursTa: 'மாலை மற்றும் இரவு டிபன்',
  serviceNoteEn: 'Serving evening and night tiffin. Daily timings and dish availability depend on fresh preparation. Walk-ins welcome.',
  serviceNoteTa: 'மாலை மற்றும் இரவு நேர டிபன். தினசரி தயாரிப்புக்கு ஏற்ப நேரம் மற்றும் உணவு இருப்பு அமையும். அனைவரும் வருக.',
  location: {
    streetEn: 'Karadichittur Main Road',
    streetTa: 'கரடிசித்தூர் மெயின் ரோடு',
    villageEn: 'Karadichittur',
    villageTa: 'கரடிசித்தூர்',
    pincode: '606207',
    districtEn: 'Kallakurichi District, Tamil Nadu',
    districtTa: 'கள்ளக்குறிச்சி மாவட்டம், தமிழ்நாடு',
    stateEn: 'India',
    stateTa: 'இந்தியா',
    fullAddressEn: 'Karadichittur Main Road, Karadichittur, Tamil Nadu 606207, India',
    fullAddressTa: 'கரடிசித்தூர் மெயின் ரோடு, கரடிசித்தூர், தமிழ்நாடு 606207, இந்தியா',
    googleMapsUrl: 'https://www.google.com/maps/place/V.k+Hotel/@11.8260004,78.8742624,16.75z/data=!4m6!3m5!1s0x3bab63cd567cae63:0xf87362ce2d673c6f!8m2!3d11.8285938!4d78.8757887',
    latitude: 11.8285938,
    longitude: 78.8757887
  },
  contact: {
    // Keep empty until confirmed by the hotel owner. Buttons remain hidden.
    phoneNumber: '',
    whatsappNumber: '',
    email: ''
  }
};
