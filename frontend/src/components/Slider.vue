

<template>

  <Transition>
    
  <div class="slider-container">
    <div
      @click="onClick"
      class="slider-main"
    >
      <div
        :class=" { 'clicked-slider-mover': clicked }"
        class="slider-mover"
      >
      </div>
      <div class="slider-text">
        {{ text }}
      </div>
    </div>
  </div>

  </Transition>

</template>


<script>

  import { useTasks } from '../stores/tasks.js'

  export default {
    setup() {
      const store = useTasks()
      return {
        store,
      }
    },
    emits: ["clicked"],
    props: ["width"],
    data() {
      return {
        clicked: false,
      }
    },
    methods: {
      onClick() {
        this.$emit("clicked")
        this.clicked = !this.clicked
      }
    },
    computed: {
      text() {
        return this.clicked ? "No" : "Yes"
      }
    }
  }

</script>

<style>
.slider-container {
	display: flex;
	justify-content: center;
	align-items: stretch;
	flex-flow: column;
  width: 100%
}
.slider-main {
	display: flex;
	border: 3px black solid;
	border-radius: v-bind(width);
	flex-flow: column;
	justify-content: center;
  width: v-bind(width);
}
.clicked-slider-mover {
  transform: translate(calc(v-bind(width) - v-bind(width) / 6 - 2px));
}
.slider-text {
  position: absolute;
  width: v-bind(width);
  display: flex;
  justify-content: center;
}
.slider-mover {
	background-color: black;
	border-radius: 50%;
	border: 1px solid black;
	transition: all .8s;
	transition-timing-function: ease-in-out;
	width: calc(v-bind(width) / 6);
  height: calc(v-bind(width) / 6);
  box-shadow: 0 0 0 1px black;
}
  .v-enter-active,
  .v-leave-active {
    transition: opacity 0.5s ease;
  }
  .v-enter-from,
  .v-leave-to {
    opacity: 0;
  }

</style>

