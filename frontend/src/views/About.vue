<template>
    <div id="about">
        <ImpactDescription v-show="!showingQuestions"/>
    </div>
</template>

<script>
	import ImpactDescription from '../components/Home/ImpactDescription.vue';

	export default {
		name:       "About",
		components: {
			ImpactDescription
		},
	};
</script>

<style scoped>
    #about
    {
        padding-top: 40px;
    }
</style>