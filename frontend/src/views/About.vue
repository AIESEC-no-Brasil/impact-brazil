<template>
    <div id="about">
        <ImpactDescription/>
    </div>
</template>

<script>
	import ImpactDescription from '../components/Home/ImpactDescription.vue';

	export default {
		name:       "About",
		components: {
			ImpactDescription
		},
		created()
		{
			this.setTitle("About");
		}
	};
</script>

<style scoped>
    #about
    {
        padding-top: 40px;
    }
</style>