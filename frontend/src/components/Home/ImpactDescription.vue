<template>
    <div class="section" id="description">
        <div class="title">How will you choose to develop yourself?</div>

        <b-container class="blocks">
            <b-row>
                <b-col cols="12" md="4">
                    <div class="prod gv">
                        <img src="/static/images/products/hd/gv-logo.png"
                             title="Global Volunteer"
                             alt="Global Volunteer">
                        Ambitious enough to believe you can make a positive impact in Brazil? Well, we believe you
                        can, through volunteering towards the UN Global Goals!
                        <div class="subtitle">DURATION</div>
                        6-12 weeks
                        <div class="subtitle">ORGANIZATION</div>
                        NGO
                        <div class="subtitle">COMPENSATION</div>
                        No
                        <a href="https://aiesec.org/global-volunteer"
                           target="_blank">
                            Read More
                        </a>
                    </div>
                </b-col>
                <b-col cols="12" md="4">
                    <div class="prod gt">
                        <img src="/static/images/products/hd/gt-logo.png"
                             title="Global Talent"
                             alt="Global Talent">
                        Searching for the next opportunity to level yourself up and gain professional experience?
                        Differentiate yourself through an international internship in Brazil.
                        <div class="subtitle">DURATION</div>
                        6-78 weeks
                        <div class="subtitle">ORGANIZATION</div>
                        Company
                        <div class="subtitle">COMPENSATION</div>
                        Yes
                        <a href="https://aiesec.org/global-talent"
                           target="_blank">
                            Read More
                        </a>
                    </div>
                </b-col>
                <b-col cols="12" md="4">
                    <div class="prod ge">
                        <img src="/static/images/products/hd/ge-logo.png"
                             title="Global Entrepreneur"
                             alt="Global Entrepreneur">
                        Does a dynamic, fast-paced work environment excite you? Begin your entrepreneurial journey with an internship at a startup in Brazil!
                        <div class="subtitle">DURATION</div>
                        6-12 weeks
                        <div class="subtitle">ORGANIZATION</div>
                        Startup
                        <div class="subtitle">COMPENSATION</div>
                        No
                        <a href="https://aiesec.org/global-entrepreneur"
                           target="_blank">
                            Read More
                        </a>
                    </div>
                </b-col>
            </b-row>
        </b-container>
    </div>
</template>

<script>
	import bContainer from 'bootstrap-vue/es/components/layout/container';
	import bCol from 'bootstrap-vue/es/components/layout/col';
	import bRow from 'bootstrap-vue/es/components/layout/row';


	export default {
		name:       "ImpactDescription",
		components: {
			bContainer,
			bCol,
			bRow
		}
	};
</script>

<style lang="scss" scoped>
    $gv-color: #f85a40;
    $gt-color: #008ea1;
    $ge-color: #00ce9f;

    #description
    {
        .title
        {
            font-size: 32px;
            text-align: center;
        }

        .prod
        {
            // box-shadow: offset-x offset-y blur spread color position
            box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.2);
            padding: 16px;
            text-align: center;
            border-radius: 2px;
            margin-top: 24px;
            background-color: #fff;

            img
            {
                width: 80%;
                margin: 16px auto;
                display: block;
            }
            .subtitle
            {
                font-size: 12px;
                color: #777;
                text-transform: capitalize;
                margin-top: 12px;
            }

            a
            {
                display: block;
                margin-top: 12px;
                font-size: 20px;
            }
        }
        .gv
        {
            border-top: 6px solid $gv-color;
            a
            {
                color: $gv-color;
            }
        }
        .gt
        {
            border-top: 6px solid $gt-color;
            a
            {
                color: $gt-color;
            }
        }
        .ge
        {
            border-top: 6px solid $ge-color;
            a
            {
                color: $ge-color;
            }
        }
    }
</style>