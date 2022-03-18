<template>

  <div class="container">
    <div class="header-item"> To-Do List </div>
  </div>

</template>


<script>

  export default {
    data() {
       return {
       }
    }
  }

</script>


<style>

  .container {
    display: flex;
    flex-flow: row nowrap;
    justify-content: center;
    align-items: center;
    background: hsl(var(--hue-purple), 100%, var(--lgt-2));
    color: white;
    border: solid;
    border-width: 1px;
    border-color: darkgrey;
  }

  .header-item {
    text-align: center;
    padding: 10px;
    font-size: 29px;
    
  }

</style>

