export interface PageUrl {
	path: string;
	selectors: SelectorObject[];
}

export interface BlockPage {
	baseUrl: string;
	block: PageUrl[];
}

export interface SelectorObject {
	displayName: string;
	selector: string;
}