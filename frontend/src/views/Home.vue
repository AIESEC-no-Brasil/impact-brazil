<template>
    <div id="home">
        <ImpactWelcome/>
        <ImpactDescription/>
    </div>
</template>

<script>
    import ImpactWelcome from '@/components/ImpactWelcome.vue';
    import ImpactDescription from '@/components/ImpactDescription.vue';

	export default {
		name: "Home",
        components: {
			ImpactWelcome,
            ImpactDescription
        }
	};
</script>

<style scoped>

</style>