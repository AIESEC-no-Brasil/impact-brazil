const config = {
	api:             "http://32478bb8.ngrok.io/api/",//"http://localhost:8000/api/",
	ipApiURI:        "http://ip-api.com/json",
	defaultVideoURI: "https://www.youtube.com/embed/CckIMe0VT2k?enablejsapi=1",
	videos:          {
		lcThumbDir:                "/static/videothumbs/lcs/",
		defaultLCThumb:            "default_lc_thumb.jpg",
		entiyPartnerThumbDir:      "/static/videothumbs/entity_partners/",
		defaultEntityPartnerThumb: "default_ep_thumb.jpg",
	},
	logos:           {
		products:      "/static/images/products/",
		subproductsGT: "/static/images/subproducts/",
		subproductsGE: "/static/images/subproducts/",
		sdgs:          "/static/images/sdgs/"
	},
	endpoints:       {
		entities:      "entities.json",
		products:      "products.json",
		sdgs:          "sdgs.json",
		subproductsGT: "subproducts.json?product=2",
		subproductsGE: "subproducts.json?product=5",
		entityPartner: (id) => `entity_partners/${id}.json`,
		opportunities: "opportunities.json",
	},
	colors:          {
		ibBlue:   {
			dark:  "#188cff",
			light: "#18c2f4",
		},
		ibOrange: {
			dark:  "#ff8c01",
			light: "#ff6d00",
		},
		ibGreen:  {
			dark:  "#3be33d",
			light: "#97e04a",
		},
		ibPurple: {
			dark:  "#ff3b98",
			light: "#ff5eba",
		},
		ibYellow: {
			dark:  "#ffdd00",
			light: "#ffb200",
		},
		ibPink:   {
			dark:  "#d12354",
			light: "#ff3b54",
		},
	},
};

export {config};