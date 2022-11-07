<template>
  
  <Transition tag="div">
    <BaseButton :class="currentClass" @click.stop="onClick" :btnType="currentIcon">
      <slot />
    </BaseButton>
  </Transition>
  
</template>

<script>

  import BaseButton from "./BaseButton.vue"

  export default { 
    components: {
      BaseButton,
    },
    props: {
      // { 'plus' | 'minus' | 'xmark' | 'check'}
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
  }
  .plus-button {
    background-color: lightgreen;
  }
  .minus-button {
    background-color: limegreen;
  }
  .xmark-button {
    background-color: red;
  }
  .check-button {
    background-color: green;
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
