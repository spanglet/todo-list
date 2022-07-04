<template>
  <button class="button" :class="btnType" @click.stop="action">
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
    border: 1px black solid;
    font-weight: bold;
  }

  .icon {
    margin: 3px;
    min-height: 2.5em;

  }
  .button:hover {
    filter: brightness(.95);
  }
  .button:active {
    filter: brightness(.75);
  }

</style>

