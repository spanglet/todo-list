
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
      <input name="username" v-model="form.username" required>
      <div class="input-warning" v-if="form.username.length < 4">
        Username must contain at least 4 characters
      </div>

      <label for="password">Password</label>
      <input type="password" v-model="form.password" name="password" required>
      <div class="input-warning" v-if="form.password.length < 8">
      	Password must contain at least 8 characters
      </div>

      <button class="register-submit-btn" @click="register"> Submit </button>
    </div>
  </div>

</template>


<script setup>

  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  import Fetch from './fetch.js'

  const router = useRouter()

  const form = $ref({
    username: "",
    password: '',
  })

  //Send form to registration endpoint on backend
  async function register() {
    if (form.password.length < 8 || form.username.length < 4) {
      // show error message as ref
      return
    } 
    const json = await Fetch.post("auth/register", form)
    if (json.data) {
      router.push("/login")
    }
    else {
      alert(json.error.message)
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

