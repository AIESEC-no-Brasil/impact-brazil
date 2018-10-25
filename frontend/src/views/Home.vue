<template>
    <div id="home">
        <ImpactWelcome @showing-questions="showingQuestions = true"
                       @not-showing-questions="showingQuestions = false"/>
        <ImpactDescription v-show="!showingQuestions"/>
    </div>
</template>

<script>
	import ImpactWelcome from '../components/Home/ImpactWelcome.vue';
	import ImpactDescription from '../components/Home/ImpactDescription.vue';

	export default {
		name:       "Home",
		components: {
			ImpactWelcome,
			ImpactDescription
		},
		data()
		{
			return {
				showingQuestions: false
			};
		}
	};
</script>

<style scoped>

</style>