<template>
    <div id="footer" style="">
        <img src="../../assets/aiesec-logo.png" class="logo"/>
        <div class="social">
            <a href="https://aiesec.org"
               rel="noopener"
               target="_blank">
                <span class="socicon socicon-internet"></span>
            </a>
            <a href="https://www.facebook.com/impactbrazil/"
               rel="noopener"
               target="_blank">
                <span class="socicon socicon-facebook"></span>
            </a>
            <a href="https://instagram.com/aiesecnobrasil"
               rel="noopener"
               target="_blank">
                <span class="socicon socicon-instagram"></span>
            </a>
            <a href="https://twitter.com/AIESECBrasil"
               rel="noopener"
               target="_blank">
                <span class="socicon socicon-twitter"></span>
            </a>
            <a href="https://www.youtube.com/user/AIESECinBrazil/"
               rel="noopener"
               target="_blank">
                <span class="socicon socicon-youtube"></span>
            </a>
        </div>
        <div class="legal">
            This website uses cookies. &middot;
            <a rel="noopener" href="/static/Privacy.pdf">Terms & Privacy</a> &middot;
            <a rel="noopener" href="/static/Cookies.pdf">Cookie Policy</a>
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
		name: "Footer",
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
            margin: 0 12px;
            font-size: 24px;
            text-decoration: none !important;
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