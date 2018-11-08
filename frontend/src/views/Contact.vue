<template>
    <div class="section">
        <i class="material-icons">contact_support</i>
        <div class="title">Contact Us</div>
        <div class="text-center">
            Drop us a mail at <a href='mailto:impact.brazil@aiesec.net' target='_blank'>impact.brazil@aiesec.net</a>
            to get in touch with us!
        </div>
    </div>
</template>

<script>
	export default {
		name: "Contact"
	};
</script>

<style scoped>
    .section
    {
        margin: 10vh 0 45vh 0;
    }

    .title
    {
        text-align: center;
        margin: 10px 0;
        font-size: 36px;
        font-family: PierSansBold, sans-serif;
    }

    i
    {
        font-size: 64px;
        margin: auto;
        display: block;
        text-align: center;
    }
</style>