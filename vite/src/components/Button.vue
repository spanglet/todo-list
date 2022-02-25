<template>
  <button @click="action"></button>
  <span class="icon"></span>
</template>

<script>
  export default { 
    data() {
      return {
      }
    },
    props: {
      action: Function,
      color: String,
    }
  }
</script>

<style>
  button {
    color: v-bind(color);
    
  }
  .icon {
   content: '\002B' 
  }
</style>

