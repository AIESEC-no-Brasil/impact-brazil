<template>
    <div class="section" id="opportunities">
        <OpportunityInvite/>
        <OpportunityOptions/>
        <div id="opportunities-list">
            <OpportunityCard/>
            <OpportunityCard/>
        </div>
        <br><br><br><br>
        this is where oppportunities will occur
        Selection: {{potato.query}}
    </div>
</template>

<script>
	import OpportunityInvite from '../components/OpportunityInvite.vue';
	import OpportunityOptions from '../components/OpportunityOptions.vue';
	import OpportunityCard from '../components/OpportunityCard.vue';

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

