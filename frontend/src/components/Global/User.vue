<template>
    <div id="user">
        <SweetModal title="Login"
                    overlay-theme="dark"
                    modal-theme="light"
                    ref="login">
            <b-form @submit.prevent="performLogin" v-show="!loggingIn">
                <div class="title">
                    Log in with your <a href="http://aiesec.org" target="_blank">aiesec.org</a> account
                    credentials.<br>
                    Don't have an account? <strong><a href="#" @click="registerForm">Sign up here</a>!</strong>
                </div>
                <div class="title" style="color: red" v-if="loginError">
                    Invalid username or password. Please try again.
                </div>
                <b-form-group id="username-group"
                              label="Email address"
                              label-for="username">
                    <b-form-input id="username"
                                  v-model="username"
                                  type="email"
                                  required
                                  placeholder="Enter email"/>
                </b-form-group>
                <b-form-group id="password-group"
                              label="Password"
                              label-for="password"
                              description="We do not store your password.">
                    <b-form-input id="password"
                                  v-model="password"
                                  type="password"
                                  required></b-form-input>
                </b-form-group>
                <b-button type="submit" variant="success">Login</b-button>
            </b-form>
            <Loading v-if="loggingIn && !loggedIn" dark center/>
            <div class="title" v-if="loggedIn">Logged in successfully.</div>
        </SweetModal>
        <SweetModal title="Sign Up"
                    overlay-theme="dark"
                    modal-theme="light"
                    ref="register">
            <div class="title">
                When you click the Sign Up button below, you will be taken to the sign up page for AIESEC in a new
                window. Please register your account on the form that shows up, then <strong>close that window and click
                the Login button below</strong> to login with your newly registered account.
            </div>
            <b-button variant="primary" size="lg" @click="showSignUpForm">Sign Up</b-button>&nbsp; &nbsp;
            <b-button variant="success" size="lg" @click="loginForm">Login</b-button>
        </SweetModal>
        <SweetModal title="Complete your profile"
                    overlay-theme="dark"
                    modal-theme="light"
                    ref="completeprofile">
            <div class="title">
                Before you can apply to an opportunity, you need to make sure that your profile is completed on <a
                    href="http://aiesec.org" target="_blank">aiesec.org</a>. Click the Profile button below to open your
                profile so you can fill in all your details, then <strong>close that window and click on Try Again
                below</strong> to apply again.
            </div>
            <b-button variant="primary" size="lg" @click="showProfileForm">Complete Profile</b-button>&nbsp; &nbsp;
            <b-button variant="success" size="lg" @click="retry">Try Again</b-button>
        </SweetModal>
    </div>
</template>

<script>
	import {SweetModal} from 'sweet-modal-vue';
	import bForm from 'bootstrap-vue/es/components/form/form';
	import bFormGroup from 'bootstrap-vue/es/components/form-group/form-group';
	import bFormInput from 'bootstrap-vue/es/components/form-input/form-input';
	import bButton from 'bootstrap-vue/es/components/button/button';
	import Loading from '../Loading.vue';
	import axios from 'axios';
	import {config} from '../../config';

	export default {
		name:       "User",
		components: {
			SweetModal,
			bForm,
			bFormGroup,
			bFormInput,
			bButton,
			Loading
		},
		data()
		{
			return {
				loginError: false,
				loggingIn:  false,
				loggedIn:   false,
				username:   '',
				password:   '',
			};
		},
		created()
		{
			this.$root.$on('login', () => {
				if (this.$refs.login)
					this.$refs.login.open();
			});
			this.$root.$on('profile', () => {
				if (this.$refs.completeprofile)
					this.$refs.completeprofile.open();
			});
		},
		methods:    {
			registerForm()
			{
				this.$refs.login.close();
				this.$refs.register.open();
			},
			loginForm()
			{
				this.$refs.register.close();
				this.$refs.login.open();
			},
			showSignUpForm()
			{
				window.open("https://auth.aiesec.org/users/sign_in#signup", "AIESEC_Form", "menubar=no,location=no,width=450,left=100,top=100");
			},
			showProfileForm()
			{
				window.open("https://aiesec.org/profile/edit", "AIESEC_Form", "menubar=no,location=no,width=450,left=100,top=100");
			},
			retry()
			{
				window.location.reload();
			},
			async performLogin()
			{
				this.loggingIn = true;
				if (this.username === "" || this.password === "")
				{
					this.loggingIn = false;
					return; // This is just safety, we should never reach here anyway
				}

				let tokenData;
				try
				{
					tokenData = await axios.post(config.api + config.endpoints.login, {
						username: this.username.trim(),
						password: this.password,
					});
				}
				catch (err)
				{
					if (err.response && (err.response.status === 400 || err.response.status === 401))
						this.loginError = true;
					else
					{
						console.error(err);
						this.$root.$emit('error');
					}

					this.loggingIn = false;
					return;
				}
				this.$session.set('loggedIn', true);
				// TODO: Refresh access token after 4hrs
				this.$session.set('accessToken', tokenData.data.access_token);
				this.loggedIn = true;

				setTimeout(() => window.location.reload(), 1000);
			}
		}
	};
</script>

<style scoped>
    .title
    {
        font-size: 18px;
        margin-bottom: 8px;
    }
</style>