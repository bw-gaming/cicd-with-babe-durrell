import { BlockPage, PageUrl } from "../entities/entities";

export const pronostics: PageUrl = {
    path:  '/pronostico-final-champions.html',
    selectors: [    
                 { displayName: 'pronostic block', selector: '.inner.pronostics.maintext'},
                 { displayName: 'Title', selector: '.title01'},
                 { displayName: 'Pronostic Image', selector: '[src="https://www.apostarperu.pe/img/site/~650/365/pronostico-final-champions.jpg"]'},                                      
                 { displayName: 'CTA Link: APOSTAR EN LEGEND PLAY SPORTS', selector: '[href="/go/LegendPlay-Sports.html?p=pro"]'}
               ]
};

export const review: PageUrl = {
    path:  '/casino/',
    selectors: [
                 { displayName: 'Header', selector: '#header'},
                 { displayName: 'Casino Vertical', selector: '[href="https://www.apostarperu.pe/casino/"]'},                                      
               ]
};

export const homepage: PageUrl = {
    path: '/',
    selectors: [
                { displayName: 'Bookmaker Vertical', selector: '[href="https://www.apostarperu.pe/"]'},
                { displayName: 'Top casinos', selector: '.top-block.homepage-block'},
                { displayName: 'toplists', selector: '.t-table'},
                { displayName: 'casino Du Mois', selector: '.h-month-top.h-promo.homepage-block'},
                { displayName: 'newsletter', selector: '.h-form__content'},
                { displayName: 'Age restriction +18', selector: '.disclaimer-div'}
               ]
};

export const blockPage: BlockPage = {
    baseUrl: 'https://www.apostarperu.pe',
    block: [pronostics, review, homepage],
};