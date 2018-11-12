<template>
    <div id="home">
        <ImpactWelcome/>
        <ImpactDescription v-if="!$store.state.showingQuestions"/>
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
        created()
        {
            this.setTitle();
        }
	};
</script>

<style scoped>

</style>