<template>
    <social-sharing :url="`https://impactbrazil.org/opportunity/${opportunity.id}`"
                    :title="`${opportunity.title} - Impact Brazil`"
                    :description="opportunity.description.length > 203 ? opportunity.description.substr(0, 200) + '...' : opportunity.description"
                    :quote="opportunity.description.length > 203 ? opportunity.description.substr(0, 200) + '...' : opportunity.description"
                    hashtags="brazil,opportunity,internship,professional,volunteering,entrepreneurship,aiesec"
                    inline-template>
        <div class="social-icons">
            <network network="whatsapp">
                <span class="socicon socicon-whatsapp"></span>
            </network>
            <network network="facebook">
                <span class="socicon socicon-facebook"></span>
            </network>
            <network network="twitter">
                <span class="socicon socicon-twitter"></span>
            </network>
            <network network="linkedin">
                <span class="socicon socicon-linkedin"></span>
            </network>
            <network network="googleplus">
                <span class="socicon socicon-googleplus"></span>
            </network>
        </div>
    </social-sharing>
</template>

<script>
	import SocialSharing from 'vue-social-sharing';

	export default {
		name:       "OpportunityShare",
		components: {
			SocialSharing,
		},
		props:      {
			opportunity: Object,
		},
		created()
		{
			this.$root.$on('social_shares_open', function (network, url) {
				this.$ga.event('Share', network, url);
			});
		}
	};
</script>

<style scoped>
    .social-icons >>> span
    {
        font-size: 20px;
        margin: 0 4px;
        cursor: pointer;
    }
</style>