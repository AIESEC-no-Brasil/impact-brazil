<template>
    <router-link :to="`/opportunity/${id}`" class="shiny-btn">Apply &raquo;</router-link>
</template>

<script>
	export default {
		name:  "OpportunityApplyButton",
		props: {
			id: Number,
		}
	};
</script>

<style lang="scss" scoped>
    @import "../../../node_modules/bootstrap/scss/functions";
    @import "../../../node_modules/bootstrap/scss/variables";
    @import "../../../node_modules/bootstrap/scss/mixins/breakpoints";
    @import "../../assets/colors";

    .shiny-btn
    {
        color: white;
        display: block;
        text-align: center;
        font-size: 36px;
        text-decoration: none;
        padding: 4px 12px;
        transition: transform 500ms cubic-bezier(0.68, -0.55, 0.265, 1.55), background-position 800ms cubic-bezier(0.68, -0.55, 0.265, 1.55), box-shadow 500ms linear;
        background: $ib-pink-dk url('data:image/svg+xml;utf8,<?xml version="1.0" encoding="utf-8"?><svg version="1.1" id="Livello_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"   width="1296px" height="768px" viewBox="0 0 1296 768" enable-background="new 0 0 1296 768" xml:space="preserve"><g><polygon fill="%23FF2355" points="766.6,1.2 -0.2,768 200.7,768 967.5,1.2   "/></g><g><polygon fill="%23FF2355" points="1094.8,1.2 328,768 528.9,768 1295.7,1.2   "/></g></svg>') no-repeat -200px center;
        background-size: contain;

        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.24);

        @include media-breakpoint-up(md)
        {
            font-size: 36px;
            margin: 32px 0;
        }
        @include media-breakpoint-down(md)
        {
            font-size: 20px;
            margin: 14px 0;
        }
    }

    .shiny-btn:hover
    {
        transform: scale(1.1);
        background-position: -40px;
        box-shadow: 0 3px 6px rgba(0, 0, 0, 0.16), 0 3px 6px rgba(0, 0, 0, 0.23);
    }

    .shiny-btn:focus, .shiny-btn:active
    {
        transform: scale(1);
        background-position: 500px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.24);
    }
</style>