<template>

  <button class="button" :class="btnType" >
    <slot></slot>
    <font-awesome-icon class="icon" :icon="btnType" />
  </button>

</template>

<script setup>

  const props = defineProps({
      btnType: String
  })

</script>

<style>

  .button {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: .1em;
    font-weight: bold;
    font-size: 1em;
    box-shadow: 0 2px 2px 0;
    border-radius: 8px;
    border: 1px black solid;
  }
  .button:hover {
    filter: brightness(.90);
  }
  .button:active {
    filter: brightness(.74);
  }
  .icon {
    height: 1.25em;
    width: 1.25em;
  }

</style>

