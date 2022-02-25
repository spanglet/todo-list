<template>
  <div class="container">    
    <div class="col">
      <div>Name is {{name}}</div>
    </div>  
    <div class="col">
      <div>Description is {{description}}</div>
    </div>  
  </div>
</template>

<script>
  export default { 
    data() {
      return {
      }
    },
    props: {
      name: String,
      description: String
    }
  }
</script>
<style>

  .container {
    display: flex;
    justify-content: center;
    
    padding: 0;
    margin: 0;
    list-style: none;
    gap: 10px;
  }
  .col {
    display: flex;
    justify-content: center;
    align-items: center;
    background: tomato;
    height: 50px;
    width: 150px;
    text-align: center;
    border-radius: 25px;
  }


</style>
