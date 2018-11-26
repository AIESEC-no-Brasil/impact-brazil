const config = {
	websiteName:        "Impact Brazil",
	api:                window.webpackHotUpdate
		                    ? "http://localhost:8000/api/"
		                    : "http://impactbrazil.raitech.org/api/api/",
	gisPublicAPI:       "https://gis-api.aiesec.org/graphql?access_token=e316ebe109dd84ed16734e5161a2d236d0a7e6daf499941f7c110078e3c75493",
	gisTokenAPI:        token => `https://gis-api.aiesec.org/graphql?access_token=${token}`,
	youtubeURL:         url => `https://www.youtube.com/embed/${url}?enablejsapi=1`,
	defaultVideoURL:    "https://www.youtube.com/embed/CckIMe0VT2k?enablejsapi=1",
	gisBrazilID:        1606,
	defaultMonthOffset: 6,
	videos:             {
		lcThumbDir:                "/static/videothumbs/lcs/",
		defaultLCThumb:            "default_lc_thumb.jpg",
		entiyPartnerThumbDir:      "/static/videothumbs/entity_partners/",
		defaultEntityPartnerThumb: "default_ep_thumb.jpg",
		projectThumbDir:           "/static/videothumbs/projects/",
		defaultProjectThumb:       "default_project_thumb.jpg",
	},
	logos:              {
		products:      "/static/images/products/",
		subproductsGT: "/static/images/subproducts/",
		subproductsGE: "/static/images/subproducts/",
		sdgs:          "/static/images/sdgs/"
	},
	logosHD:            {
		products:      "/static/images/products/hd/",
		subproductsGT: "/static/images/subproducts/hd/",
		subproductsGE: "/static/images/subproducts/hd/",
		sdgs:          "/static/images/sdgs/hd/"
	},
	endpoints:          {
		entities:      "entities.json",
		products:      "products.json",
		sdgs:          "sdgs.json",
		subproductsGT: "subproducts.json?product=2",
		subproductsGE: "subproducts.json?product=5",
		entityPartner: id => `entity_partners/${id}.json`,
		sdg:           id => `sdg/${id}.json`,
		subproduct:    id => `subproduct/${id}.json`,
		projects:      "projects.json",
		project:       id => `project/${id}.json`,
		opportunities: "opportunities.json",
		opportunity:   id => `opportunity/${id}.json`,
		lcs:           "lcs.json",
		lc:            id => `lcs/${id}.json`,
		cities:        "cities.json",
		city:          name => `city/${name}.json`,
		login:         "login.json",
		apply:         "apply.json",
		ip:            "ip.json",
	},
	colors:             {
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