module.exports = {
	lintOnSave:       false,
	configureWebpack: {
		devServer: {
			allowedHosts: [
				'.ngrok.io'
			]
		}
	}
};
