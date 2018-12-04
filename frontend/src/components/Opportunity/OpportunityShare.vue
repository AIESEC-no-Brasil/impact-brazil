<template>
    <social-sharing :url="`https://impactbrazil.org/opportunity/${opportunity.id}`"
                    :title="`${opportunity.title} - Impact Brazil`"
                    :description="opportunity.description.length > 203 ? opportunity.description.substr(0, 200) + '...' : opportunity.description"
                    :quote="opportunity.description.length > 203 ? opportunity.description.substr(0, 200) + '...' : opportunity.description"
                    hashtags="brazil,opportunity,internship,professional,volunteering,entrepreneurship,aiesec"
                    inline-template>
        <div>
            <network network="whatsapp">
                <img src="../../assets/social/whatsapp.png"/>
            </network>
            <network network="facebook">
                <img src="../../assets/social/facebook.png"/>
            </network>
            <network network="twitter">
                <img src="../../assets/social/twitter.png"/>
            </network>
            <network network="linkedin">
                <img src="../../assets/social/linkedin.png"/>
            </network>
            <network network="googleplus">
                <img src="../../assets/social/googleplus.png"/>
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
    img
    {
        cursor: pointer;
    }
</style>