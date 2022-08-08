
<template>
  
  <TransitionGroup name="task-list" class="list-group" tag="div">
    <div v-for="task in tasks" :key="task">

      <TaskTile class="list-group-item"
        :name="task.name"
        :description="task.description"
        :dueDate="task.trueDueDate"
        @remove-item='deleteTask(task)'
        @task-completed='sendTaskCompletion(task)'
      />

    </div>
  </TransitionGroup>

</template>

<script>

  import TaskTile from './TaskTile-Dev.vue'
  import { computed } from 'vue'
  import { useTasks } from '../stores/tasks.js'

  export default { 
    setup() {
      const store = useTasks()
      return {
        store,
      }
    },
    props: ["listID"],
    components: {
      TaskTile,
    },
    data() {
      return {
        // ...
      }
    },
    methods: {

      deleteTask(task) {
        const i = this.store.tasks.indexOf(task)
        this.store.tasks.splice(i, 1);
        this.store.deleteTask(task.id)
      },
      sendTaskCompletion(task) {
        const i = this.store.tasks.indexOf(task)
        this.store.tasks[i].completed = true
        this.store.completeTask(task.id)
      },
    },
    computed: {
      tasks() {
        return this.store.filteredTasks
      }
    },
  }

</script>


<style>
  
  .task-list {
    background: hsl(var(--hue-purple), 100%, var(--lgt-6));
    min-width: 0;
  }
  .task-list > * {
    margin: 0 
  }
  .task-list-move,
  .task-list-enter-active,
  .task-list-leave-active {
    transition: all 0.5s ease;
  }
  .task-list-leave-active {
    position: relative;
  }
  .task-list-enter-from,
  .task-list-leave-to {
    opacity: 0;
  }
  .list-group {
    display: flex;
    flex-flow: column nowrap;
    gap: 3px;
    position: relative;
  }
  .list-group-item {
    width: 100%;
  }

</style>
