
<template>
  
  <TransitionGroup name="task-list" tag="div">
    <div v-for="task in tasks"  class="list-group" :key="task">

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

  import TaskTile from './TaskTile.vue'
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
    mounted() {
      this.store.currentListID = parseInt(this.listID)
    },
    methods: {

      deleteTask(task) {
        const i = this.store.tasks.indexOf(task)
        this.store.tasks.splice(i, 1);
        this.store.deleteTask(task.id)
      },
      sendTaskCompletion(task_id) {
        const i = this.store.tasks.indexOf(task_id)
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
  .task-list-move,
  .task-list-enter-active,
  .task-list-leave-active {
    transition: all 0.5s ease;
  }
  .task-list-leave-active {
    position: absolute;
  }
  .task-list-enter-from,
  .task-list-leave-to {
    opacity: 0;
  }
  .list-group {
    display: flex;
    flex-flow: column nowrap;
    gap: 3px;
    margin: .5em;
    position: relative;
  }
  .list-group-item {
    width: 100%;
  }

</style>
