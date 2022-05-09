
<template>

  <div class="wrapper">

    <router-view></router-view>

  </div>

</template>


<script>

  var config = { headers: {'Access-Control-Allow-Origin': '*' } }

  var url = "http://127.0.0.1:5000/users/active"

  export default {
    data() {
      return {
        title: "Flax"
      }
    },
    created () {
      // Check if a user is active in the backend session
      // Routes to login page if no active user returned
      axios.get(url, config
	      ).then((res) => {
          if (res.status == 200 && res.data["user"]) {
            this.$router.push('/app')
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
  
  }

</style>

