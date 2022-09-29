
<template>

  <div class="login">
    <h1>Create a New Account</h1>
    <div class="register-form">
      <div class="input-row">
        <div>
          <label for="firstName">First Name</label>
          <input name="firstName" v-model="fname" required>
        </div>
        <div>
          <label for="lastName">Last Name</label>
          <input name="lastName" v-model="lname" required>
        </div>
      </div>
      <label for="username">Username</label>
      <input name="username" v-model="username" required>
      <div class="input-warning" v-if="username.length < 4">
        Username must contain at least 4 characters
      </div>

      <label for="password">Password</label>
      <input type="password" v-model="password" name="password" required>
      <div class="input-warning" v-if="password.length < 8">
      	Password must contain at least 8 characters
      </div>

      <button class="register-submit-btn" @click="register"> Submit </button>
    </div>
  </div>

</template>


<script>

  export default {
    data() {
      return {
        username: "",
        password: '',
        fname: "",
        lname: ""
      }
    },
    methods: {
      // User info sent to Flask backend for authentication
      register() {
        
        // User inputs validated to ensure correct registration request is sent
        if (this.password.length < 8) {
          alert("Password must contain at least 8 characters")
          
        } 
        else if (this.username.length < 4) {
          alert("Username must contain at least 4 characters")
        } 
        else {
          this.axios.post("auth/register", {
              "username": this.username,
              "password": this.password
            })
            .then((res) => { 
              // Render application if login is successful
              if (res.status == 200) {
                this.$router.push("/login")
              }
            })
        }
      }
    }
  }

</script>


<style>

  .login {
    height: 100vh;
    width: 100vw;
    display: flex;
    align-items: center;
    justify-content: center;
    background: lightgrey;
  }
  .register-form {
    display: flex;
    flex-flow: column nowrap;
    gap: 10px;
    padding: 10px;
    width: 500px;
    height: 400px; 
    background: hsl(var(--hue-purple), 100%, var(--lgt-4));
    border: 3px solid black;
    border-radius: 10px;
    color: #efefef;
    box-shadow: 5px 6px 15px 3px gray;
  }
  .register-submit-btn {
    font-size: 20pt;
  }
  .input-row {
    display: flex;
  }
  .input-warning {
   font-size: .8em;
   font-weight: bold;
   text-align: center;
  }	

</style>

