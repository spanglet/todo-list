<template>
  
  <Transition tag="div">
    <BaseButton :class="currentClass" @click="onClick" :btnType="currentIcon" />
  </Transition>
  
</template>

<script>

  import BaseButton from "./BaseButton.vue"

  export default { 
    components: {
      BaseButton,
    },
    props: {
      // { 'plus' | 'minus' }
      icons: Array,
    },
    data() {
      return {
        iterator: this.icons.values(),
        currentIcon: this.icons[0],
      }
    },
    mounted() {
      this.iterator.next()
    },
    methods: {
      onClick() {
        var currItem = this.iterator.next()
        if (currItem.done) {
          this.iterator = this.icons.values()
          this.iterator.next()
          this.currentIcon = this.icons[0]
        }
        else {
          this.currentIcon = currItem.value
        }
      }
    },
    computed: {
      currentClass() {
        return this.currentIcon + "-button"
      },
    }
  }
</script>

<style>
  [class$="-button"] {
    box-shadow: 0 2px 2px 0;
  }
  .plus-button {
    background-color: lightgreen;
    border-radius: 8px;
  }
  .minus-button {
    background-color: limegreen;
    border-radius: 8px;
  }
  .xmark-button {
    background-color: red;
    border-radius: 5px;
  }
  .check-button {
    background-color: green;
    border-radius: 5px;
  }
  .v-enter-active,
  .v-leave-active {
    transition: all 0.5s ease;
  }
  .v-enter-from,
  .v-leave-to {
    opacity: 0;
  }
</style>
