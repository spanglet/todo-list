
<template>

  <div class="login">
    <form method="post" class="login-form">
      <label for="username">Username</label>
      <input name="username" v-model="username" required>
      <label for="password">Password</label>
      <input type="password" v-model="password" name="password" required>
      <button @click="authenticate"> Submit </button>
    </form>
  </div>

</template>


<script>

  var config = {
          headers: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
          }
        }
  
  var auth_url = "http://127.0.0.1:5000/users"

  export default {
    data() {
       return {
         icon: ""
       }
    },
    methods {
      // Navigate to app after authentication
      onLogin() {
        this.$router.go("/")
      },
      // User info sent to Flask backend for authentication
      authenticate() {
        axios.post(url, {
            "username": this.username,
            "password": this.password,
          }, config).then((res) => { 
            // Render application if login is successful
            if (res == 200) {
              this.$router.go("/")
            }
          })
      }
    }
  }

</script>


<style>

  .login {
    width: 500px;
    height: 450px; 
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .login-form {
    display: flex;
    flex-flow: column nowrap;
    gap: 10px;
    background: hsl(var(--hue-purple), 100%, var(--lgt-3));
    border: 3px solid darkgrey;
    border-radius: 10px;
  }

</style>

