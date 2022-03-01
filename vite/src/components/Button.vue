<template>
  <button @click="action">
    <font-awesome-icon class="icon" :icon="icon" />
  </button>
</template>

<script>
  export default { 
    data() {
      return {
      }
    },
    props: {
      action: Function,
      content: String,
      icon: String
    }
  }
</script>

<style>
  button {
    display: flex;
    border-radius: 9px;
    align-items: center;
    
  }

  .icon {
    margin: 2px;
    height: 100%;
    width: 100%
  }

</style>

