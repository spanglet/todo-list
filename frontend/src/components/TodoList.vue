<template>
  <div class="todo-main">
    <ListHeader class="todo-header" />
    <TaskList class="list-area" />
    <TaskForm
      @click.stop=''
      @submitted="setFormVisibility(false)"
      class="task-form"
    />
  </div>

</template>

<script>

  import ListHeader from './ListHeader.vue'
  import TaskList from './TaskList.vue'
  import TaskForm from './TaskForm.vue'
  import { useTasks } from '../stores/tasks.js'

  export default {
    setup() {
      const store = useTasks()
      return {
        store,
      }
    },
    components: {
      TaskList,
      TaskForm,
      ListHeader,
    },
    data() {
      return {
        
      }
    },
    methods: {
      setFormVisibility(visible) {
        this.store.taskFormActive = visible
      },
    },
  }

</script>

<style>

  .todo-header {
    grid-area: app-header;
    align-self: stretch;
  }
  .list-area {
    grid-area: app-main / app-main / app-main / app-main-right;
  }
  .task-form {
    grid-area: app-main-right;
    height: auto;
    box-shadow: 0px 0px 50px 2px black;
  }

</style>
