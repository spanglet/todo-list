

<template>

  <Transition>
    <BaseForm class="task-form" v-show="store.taskFormActive" />
  </Transition>

</template>


<script>

  import BaseForm from "./BaseForm.vue"
  import { useTasks } from '../stores/tasks.js'

  export default {
    setup() {
      const store = useTasks()
      return {
        store,
      }
    },
    components: {
      BaseForm,
    },
    data() {
      return {
      } 
    }
  }


</script>

<style>
  .task-form {
    align-self: start;
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

