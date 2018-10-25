const config = {
	api:       "http://32478bb8.ngrok.io/api/",//"http://localhost:8000/api/",
	ipApiURI:  "http://ip-api.com/json",
	endpoints: {
		entities:      "entities.json",
		products:      "products.json",
		sdgs:          "sdgs.json",
		subproductsGT: "subproducts.json?product=2",
		subproductsGE: "subproducts.json?product=5",
		entityPartner: (id) => `entity_partners/${id}.json`,
	},
	colors:    {
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