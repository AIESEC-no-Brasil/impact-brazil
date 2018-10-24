<template>
    <div class="section" id="opportunities">
        <div id="invite">Inviting <span>India</span> to Impact Brazil</div>
        <div id="ey-banner">
            <div></div>
        </div>
        <div id="options-left">
            Showing <b>IT</b> opportunities for <b>Global Talent</b>
        </div>
        <div id="options-right">
            <b-dropdown id="timespan" variant="transparent" right size="sm" text="January 2019">
                <b-dropdown-item>Global Volunteer</b-dropdown-item>
                <b-dropdown-item>Global Talent</b-dropdown-item>
                <b-dropdown-item>Global Entrepreneur</b-dropdown-item>
            </b-dropdown>
            <b-dropdown id="prog" variant="transparent" right size="sm" text="Global Talent">
                <b-dropdown-item>Global Volunteer</b-dropdown-item>
                <b-dropdown-item>Global Talent</b-dropdown-item>
                <b-dropdown-item>Global Entrepreneur</b-dropdown-item>
            </b-dropdown>
            <b-dropdown id="subproductOrSdg" variant="transparent" right size="sm" text="IT">
                <b-dropdown-item>Global Volunteer</b-dropdown-item>
                <b-dropdown-item>Global Talent</b-dropdown-item>
                <b-dropdown-item>Global Entrepreneur</b-dropdown-item>
            </b-dropdown>
        </div>

        <div id="opportunities-list">
            <div class="opportunity">
                <div class="opportunity-image">
                    <b-img src="../assets/videothumbs/sample_city.jpg" fluid-grow/>
                </div>
                <div class="opportunity-desc-l">

                </div>
            </div>
        </div>
        <br><br><br><br>
        this is where oppportunities will occur
        Selection: {{potato.query}}

        <br><br><br><br>
        <div>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Id illum libero nobis reprehenderit tempora!
            Error harum itaque voluptas! Consequatur impedit nostrum nulla numquam qui soluta. Doloribus molestias
            quaerat repudiandae voluptatum?
        </div>
        <div>Aliquid nobis quos reprehenderit. Ab aut cumque, ducimus error ipsa nemo non optio provident, quae quam
            quod repudiandae soluta ut? At consectetur doloribus, eius facilis fuga itaque minus nobis porro.
        </div>
        <div>Ipsum odit repudiandae sapiente veritatis? Accusantium delectus, doloribus iste itaque mollitia nostrum
            officiis similique unde ut velit. Aut quis repellendus reprehenderit sit suscipit! Architecto dolor ipsa
            mollitia perspiciatis placeat! Voluptate.
        </div>
        <div>Alias autem dolorum eaque eveniet minima mollitia nulla omnis sit veniam voluptatum. Accusamus at
            ducimus eligendi exercitationem ipsa molestiae, mollitia necessitatibus nisi quaerat quia quibusdam,
            recusandae rerum sint suscipit ut!
        </div>
        <div>Aut consequuntur cum delectus deleniti dignissimos dolores ducimus earum eius eligendi enim expedita
            fuga harum inventore iusto maxime minima nihil nobis officia omnis quibusdam quidem quos rerum tempora
            ullam, voluptate.
        </div>
        <div>Accusantium autem ea, eaque eligendi facilis fugiat illo inventore ipsa laudantium minus nam non
            possimus ratione, repellat, similique sint suscipit? Aperiam dicta incidunt ipsa nam nemo quia quod
            soluta sunt?
        </div>
        <div>Ab accusamus accusantium commodi et eum ex fugit impedit inventore ipsam iure laboriosam maxime minus
            nesciunt nobis quae quia, repellat velit veniam vitae voluptates? Asperiores eligendi ipsa modi nostrum
            voluptatem?
        </div>
        <div>A ab corporis cum, cupiditate doloribus id illo illum impedit iusto labore laboriosam laudantium
            mollitia necessitatibus nisi ratione repellendus veniam. Amet asperiores assumenda commodi error,
            officia perferendis quia quidem similique.
        </div>
        <div>Ab adipisci alias aperiam atque beatae consectetur, cum deleniti dolore eius eligendi eveniet fugiat
            illum in ipsam itaque laboriosam, natus necessitatibus quis quod repellat, sit suscipit unde veritatis
            vero voluptatem!
        </div>
        <div>Ab adipisci amet consectetur consequuntur culpa cum cumque dignissimos dolore earum, et fuga fugiat
            incidunt inventore ipsa iste maiores molestiae nemo porro possimus provident quasi quo ratione
            repellendus sint, veniam!
        </div>
        <div>Alias consequuntur facilis molestias, omnis possimus quae quia quidem quo recusandae voluptatum. Ab
            accusantium obcaecati placeat quia. Eos excepturi illo in inventore minima nobis perferendis porro.
            Accusantium animi, inventore. Assumenda?
        </div>
        <div>Ad alias ducimus facilis iusto modi, praesentium sapiente. A alias assumenda, consectetur dolores ex
            expedita facere illum laudantium molestias mollitia omnis perferendis provident quas saepe sit sunt
            tempore totam unde!
        </div>
        <div>Ab aliquam corporis debitis doloremque ea excepturi expedita facilis hic, id minima, modi molestias
            perspiciatis possimus quaerat quam quis sequi sunt vel vero voluptatem. Culpa ducimus omnis repellat
            voluptate voluptatibus.
        </div>
        <div>Ad aliquam amet atque autem corporis culpa cum debitis delectus dolore doloribus ea esse eveniet
            expedita facilis magni maiores minus odio provident quia quo repudiandae, similique sit suscipit tenetur
            voluptas.
        </div>
        <div>Assumenda atque aut autem consectetur culpa cumque dolor dolore eaque, eos incidunt ipsa iste
            laudantium maxime molestiae mollitia nam natus nesciunt non, odit praesentium quisquam, sapiente unde ut
            voluptas voluptatum.
        </div>
    </div>
</template>

<script>
	import bDropdown from 'bootstrap-vue/es/components/dropdown/dropdown';
	import bDropdownItem from 'bootstrap-vue/es/components/dropdown/dropdown-item';
	import bImg from 'bootstrap-vue/es/components/image/img';

	export default {
		name:       "Opportunities",
		components: {
			bDropdown,
			bDropdownItem,
			bImg,
		},
		data()
		{
			return {
				potato: this.$route
			};
		}
	};
</script>

<style lang="scss" scoped>
    #invite
    {
        padding-top: 12px;
        text-align: center;

        span
        {
            font-size: 3em;
            padding: 0 4px;
            font-family: PierSansBold, sans-serif;
        }
    }

    #ey-banner
    {
        width: calc(100% + 48px);
        height: 300px;
        margin: 12px 0 24px -24px;
        padding: 0;

        cursor: pointer;

        background-attachment: fixed;
        background-position: center;
        background-repeat: no-repeat;
        background-size: cover;

        background-image: url('../assets/videothumbs/sample_ep.jpg');

        div
        {
            background-image: url('../assets/play-button.png');
            width: 150px;
            height: 150px;
            background-size: 100%;
            position: relative;
            top: 75px;
            margin: auto;
        }
    }

    #options-left
    {
        float: left;
    }

    #options-right
    {
        float: right;
    }

    #options-right /deep/
    {
        button
        {
            margin-left: 8px;
        }
    }

</style>