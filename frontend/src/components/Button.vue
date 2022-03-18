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
    border-radius: 9px;
    align-items: center;
    justify-content: center;
    
  }

  .icon {
    margin: 1px;
    height: 100%;
  }

</style>

