<template>
    <div class="section" id="opportunities">
        <OpportunityInvite/>
        <OpportunityOptions/>
        <div id="opportunities-list">
            <OpportunityCard/>
            <OpportunityCard/>
        </div>
    </div>
</template>

<script>
	import OpportunityInvite from '../components/Opportunities/OpportunityInvite.vue';
	import OpportunityOptions from '../components/Opportunities/OpportunityOptions.vue';
	import OpportunityCard from '../components/Opportunities/OpportunityCard.vue';

	export default {
		name:       "Opportunities",
		components: {
			OpportunityInvite,
			OpportunityOptions,
			OpportunityCard,
		},
		data()
		{
			return {
				potato: this.$route
			};
		}
	};
</script>

<style lang="scss" scoped>
    #opportunities-list
    {
        margin-top: 24px;
    }
</style>

