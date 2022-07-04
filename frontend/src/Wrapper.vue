
<template>

  <div class="wrapper">

    <router-view></router-view>

  </div>

</template>


<script>


  export default {
    data() {
      return {
        title: "Flax"
      }
    },
    created () {
      // Check if a user is active in the backend session
      // Routes to login page if no active user returned
      this.axios.get("auth/login")
	      .then((res) => {
          if (res.data["activeSession"]) {
            //this.$router.push('/app')
            this.$router.push('/app/calendar')
          }
          else {
            this.$router.push('/login')
          }
        })
    }
  }

</script>


<style>

  .wrapper {

    height: 100vh;
  
  }

</style>

