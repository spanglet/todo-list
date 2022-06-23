<template>
  <button class="button" :class="btnType" @click="action">
    <font-awesome-icon class="icon" :icon="btnType" />
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
      btnType: String
    }
  }
</script>

<style>
  .button {
    display: flex;
    border-radius: 8px;
    align-items: center;
    justify-content: center;
    border: 1px black solid;
    
  }

  .icon {
    margin: 1px;
    height: 90%;
  }

</style>

