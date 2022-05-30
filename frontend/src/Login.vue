
<template>

  <div class="login">
    <h1>Login</h1>
    <div class="login-form">
      <label for="username">Username</label>
      <input name="username" v-model="username" required>
      <label for="password">Password</label>
      <input type="password" v-model="password" name="password" required>
      <button class="login-submit-btn" @click="authenticate"> Submit </button>
      <router-link to="/register" class="create-account-btn">Create a New Account</router-link>
    </div>
    

  </div>

</template>


<script>


  var config = {
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Credentials': "true",
        'Access-Control-Allow-Origin': 'http://127.0.0.1:5000'
      }
    }
  
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

        var url = "users/login"
        axios.post(url, {
            "username": this.username,
            "password": this.password
          }, config).then((res) => { 
            // Render application if login is successful
            if (res.data['loginSuccess']) {
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
    background: lightgrey;
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
    color: white;
  }
  .login-submit-btn {
    font-size: 20pt;
  }
  .create-account-btn {
    display: flex;
    justify-content: center;
    border-radius: 18px;
    font-size: 18pt; 
    color: black;
    text-decoration: none;
    background: lightgrey;
  }

</style>

