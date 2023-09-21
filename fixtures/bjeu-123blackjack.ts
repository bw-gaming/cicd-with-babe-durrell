import { BlockPage, PageUrl } from "../entities/entities";

export const newsindex: PageUrl = {
    path:  '/news.html',
    selectors: [    
                 { displayName: 'News bloc', selector: '#alist'},
                 { displayName: 'Breadcrumb', selector: '#breadcrumb'},
                 { displayName: 'Read more button', selector: '.readmore'}                                      
               ]
};

export const homepage: PageUrl = {
    path: '/',
    selectors: [
                { displayName: '123BLACKJACK header', selector: '.header'},
                { displayName: 'Les meilleurs casinos en ligne évalués par nos experts', selector: '.casinos__header'},
                { displayName: 'Casinos toplist', selector: '.csinos__list'},
                { displayName: 'casino of the month', selector: '.casinos.casinos-monthly'},
                { displayName: 'payment options', selector: '.hpbanking'},
                { displayName: 'last news', selector: '#newhp'},
                { displayName: 'Age restriction +18', selector: '[src="https://www.123blackjack.eu/img/footers/~130/31/jeuresponsable.png"]'}
               ]
};


export const blockPage: BlockPage = {
    baseUrl: 'https://www.123blackjack.eu',
    block: [newsindex, homepage],
};
