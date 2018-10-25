<template>
    <div class="section" id="opportunities">
        <OpportunityInvite/>
        <OpportunityList/>
    </div>
</template>

<script>
	import OpportunityInvite from '../components/Opportunities/OpportunityInvite.vue';
	import OpportunityList from '../components/Opportunities/OpportunityList.vue';

	export default {
		name:       "Opportunities",
		components: {
			OpportunityInvite,
			OpportunityList,
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

</style>

