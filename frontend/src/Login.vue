
<template>

  <div class="login">
    <h1>Login</h1>
    <div class="login-form">
      <label for="username">Username</label>
      <input name="username" v-model="username" required>
      <label for="password">Password</label>
      <input type="password" v-model="password" name="password" required>
      <button class="login-submit-btn" @click="authenticate"> Submit </button>
      <router-link to="/register" class="create-account-btn">
        Create a New Account
      </router-link>
    </div>
  </div>

</template>


<script>

  export default {
    data() {
       return {
         username: "",
         password: ''
       }
    },
    methods: {
      // User info sent to Flask backend for authentication
      authenticate() {

        this.axios.post("auth/login", {
            "username": this.username,
            "password": this.password
          })
          .then((res) => { 
            // Render application if login is successful
            if (res.data['OK']) {
              this.$router.push("/app")
            }
            else {
              alert("Username or password is incorrect")
            }
          })
      }
    }
  }
</script>

<style>

  .login {
    height: 100vh;
    width: 100vw;
    display: flex;
    flex-flow: column nowrap;
    align-items: center;
    justify-content: center;
    font-size: 18pt;
    border-radius: 10px;
    background: hsl(var(--hue-blue), 100%, var(--lgt-6));
  }
  .login-form {
    display: flex;
    flex-flow: column nowrap;
    gap: 10px;
    padding: 10px;
    width: 400px;
    height: 350px; 
    background: hsl(var(--hue-purple), 100%, var(--lgt-4));
    border: 3px solid black;
    border-radius: 10px;
    color: #efefef;
    box-shadow: 5px 6px 15px 3px gray;
  }
  .login-submit-btn {
    font-size: 20pt;
    border: 1px black solid;
    border-radius: 15px;
  }
  .create-account-btn {
    display: flex;
    justify-content: center;
    border-radius: 18px;
    font-size: 18pt; 
    color: black;
    text-decoration: none;
    background: lightgrey;
    border: 1px black solid;
  }

</style>

