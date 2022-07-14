<template>
  <button class="button" :class="btnType" >
    <slot></slot>
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
    border: 1px black solid;
    font-weight: bold;
    font-size: 1em;
    padding: 0 10px 0 10px;
  }
  .icon {
    margin: 3px;
    min-height: 2em;
  }
  .button:hover {
    filter: brightness(.92);
  }
  .button:active {
    filter: brightness(.75);
  }

</style>

