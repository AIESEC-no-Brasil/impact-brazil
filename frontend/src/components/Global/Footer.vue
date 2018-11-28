<template>
    <div id="footer" style="">
        <img src="../../assets/aiesec-logo.png" class="logo"/>
        <div class="social">
            <a href="https://aiesec.org"
               rel="noopener"
               target="_blank">
                <img src="../../assets/social/internet.png"/>
            </a>
            <a href="https://www.facebook.com/AIESECinBrazil/"
               rel="noopener"
               target="_blank">
                <img src="../../assets/social/facebook.png"/>
            </a>
            <a href="https://instagram.com/aiesecnobrasil"
               rel="noopener"
               target="_blank">
                <img src="../../assets/social/instagram.png"/>
            </a>
            <a href="https://twitter.com/AIESECBrasil"
               rel="noopener"
               target="_blank">
                <img src="../../assets/social/twitter.png"/>
            </a>
            <a href="https://www.youtube.com/user/AIESECinBrazil/"
               rel="noopener"
               target="_blank">
                <img src="../../assets/social/youtube.png"/>
            </a>
        </div>
        <div class="legal">
            <a rel="noopener" href="https://aiesec.org/assets/AIESEC%20Privacy%20Policy.pdf">Terms & Privacy</a> &middot;
            This website does not use cookies.
        </div>
        <div class="copyright">
            &copy; AIESEC in Brazil {{ new Date().getFullYear() }}
        </div>
        <div class="credit">
            Website developed by <a rel="noopener" href="https://raitech.org">Raihan Navroze</a>.
        </div>
    </div>
</template>

<script>
	export default {
		name: "Footer"
	};
</script>

<style lang="scss" scoped>
    @import "../../assets/colors";

    #footer
    {
        margin-top: 40px;
        padding: 16px;
        font-family: PierSans, sans-serif;
        background-color: $ib-blue-dk;
        color: #fff;
        text-align: center;

        .logo
        {
            width: 200px;
        }

        .social a
        {
            margin: 0 8px;
        }

        a:not(.social)
        {
            text-decoration: underline;
            color: #fff;
        }

        .social, .legal, .copyright
        {
            margin-top: 16px;
        }

        .legal, .credit
        {
            font-size: 10px;
        }

        .credit
        {
            margin-bottom: 40px;
        }
    }
</style>