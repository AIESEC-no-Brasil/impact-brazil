<template>
    <div class="text-center section">
        <i class="material-icons">error</i><br>
        This page was not found.<br>
        Please use one of the links in the navigation above to find what you're looking for.
    </div>
</template>

<script>
	export default {
		name: "Error404",
        created()
        {
            this.setTitle("Error");
        }
	};
</script>

<style scoped>
    .section
    {
        height: 80vh;
    }
    .material-icons
    {
        margin-top: 200px;
        font-size: 96px;
    }
</style>