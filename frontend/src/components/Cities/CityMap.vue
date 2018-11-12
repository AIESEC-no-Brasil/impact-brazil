<template>
    <div id="map">
        <div id="mapcontainer">
            <object id="brazilmap" type="image/svg+xml" data="/static/Brazil_Map.svg">
                Your browser does not support this map.
            </object>
        </div>
        <div class="citydesc" v-if="showingDesc" :style="descStyle" v-html="desc"></div>
    </div>
</template>

<script>
	import SVG from 'svgjs';
	import {config} from '../../config';

	export default {
		name:    "CityMap",
		data()
		{
			return {
				svg:         {},
				pt:          {},
				currentCity: 0,
				showingDesc: false,
				desc:        "",
				descStyle:   {
					top:  0,
					left: 0,
				}
			};
		},
		props:   {
			cities: Array
		},
		created()
		{
			let loadMap = () => {
				// Set the w/h of the SVG container after it's loaded (so it's correctly sized)
				let svgObj = document.querySelector('#brazilmap');
				svgObj.style.width = "100%";
				svgObj.style.height = "100%";

				// Find your root SVG element
				this.svg = document.querySelector('#brazilmap').contentDocument.querySelector('svg');

				// Create an SVGPoint for future math
				this.pt = this.svg.createSVGPoint();

				// Get point in global SVG space
				let cursorPoint = evt => {
					this.pt.x = evt.clientX;
					this.pt.y = evt.clientY;
					return this.pt.matrixTransform(this.svg.getScreenCTM().inverse());
				};

				this.svg.addEventListener('mousedown', function (evt) {
					let loc = cursorPoint(evt);
					//console.log(loc);
                    return loc;
				}, false);
			};

			document.querySelector('#brazilmap').addEventListener('load', loadMap);

			// Debug?
			if (this.cities.length > 0)
				this.plotCities();
		},
		methods: {
			plotCities()
			{
				if (this.svg.tagName !== "svg")
				{
					setTimeout(this.plotCities, 1000);
					return;
				}

				let svg = SVG.adopt(this.svg);
				//let circleRad = Math.max(document.documentElement.clientWidth, window.innerWidth || 0) > 768 ? 35 : 60;
				let circleRad = 15;

				this.cities.forEach(city => {
					svg
					.circle(circleRad)
					.fill(config.colors.ibPurple.dark)
					//.stroke('transparent')
					.move(city.mapX, city.mapY)
					.attr('class', 'city')
					.click(() => this.showCity(city.id))
					.mouseover((evt) => {
						evt.target.setAttribute('r', 20);
						this.showingDesc = true;
						this.desc = `<b>${city.name}</b><span class="subdesc"><br>${city.short_desc}</span>`;
						if (this.desc.length > 200)
							this.desc = this.desc.substr(0, 200) + "...";

						let offset = document.querySelector("#mapcontainer").getBoundingClientRect();
						this.descStyle.left = (offset.left + evt.clientX + 10) + 'px';
						this.descStyle.top = (offset.top + evt.clientY + 10) + 'px';
					})
					.mouseout((evt) => {
						evt.target.setAttribute('r', circleRad/2);
						this.showingDesc = false;
					});
				});
			},
			showCity(id)
			{
				this.currentCity = id;
				this.$emit('city-clicked', id);
			}
		},
		watch:   {
			cities(val)
			{
				if (val.length === 0)
					return;

				this.plotCities();
			}
		}
	};
</script>

<style scoped>
    #map
    {
        text-align: center;
    }

    #brazilmap
    {
        /*We do this in JS instead so it sizes properly when the page loads*/
        /*width: 100%;*/
        /*height: 100%;*/
        max-width: 90vw;
        max-height: 75vh;
        margin: auto;
    }

    .citydesc
    {
        display: block;
        border: 1px solid #000;
        background-color: #fff;
        font-family: PierSans, sans-serif;
        max-width: 300px;
        position: fixed;
        padding: 10px;
        text-align: justify;
        z-index: 100;
    }

    @media screen and (max-width: 767.98px)
    {
        /* Maybe? */
        #map >>> .citydesc
        {
            display: none;
        }

        #map >>> .subdesc
        {
            display: none;
        }
    }

    #mapcontainer
    {
        display: inline-block;
    }
</style>