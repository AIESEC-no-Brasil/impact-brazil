<template>
    <div class="section">
        <i class="material-icons">contact_support</i>
        <div class="title">Contact Us</div>
        <div class="iframe">
            <iframe src="https://podio.com/webforms/21986117/1538640"></iframe>
        </div>
    </div>
</template>

<script>
	export default {
		name: "Contact",
		created()
		{
			this.setTitle("Contact");
		},
	};
</script>

<style scoped>
    .section
    {
        margin: 10vh 0 0 0;
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

    .iframe
    {
        width: 100%;
        text-align: center;
    }
    iframe
    {
        margin: auto;
        border: 0;
        width: 60%;
        height: 800px;
    }
</style>