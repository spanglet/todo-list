
<template>
  
  <TransitionGroup name="task-list" class="list-group" tag="div">

    <TaskTile
      v-for="task in tasks"
      :name="task.name"
      :key="task.id"
      :description="task.description"
      :dueDate="task.dueDate"
      @remove-item='store.deleteTask(task)'
      @task-completed='store.completeTask(task)'
    />

  </TransitionGroup>

</template>

<script setup>

  import TaskTile from './TaskTile.vue'
  import { computed } from 'vue'
  import { useTasks } from '../stores/tasks.js'

  const store = useTasks()

  const tasks = computed(() => {
    return store.filteredTasks
  })

</script>


<style>
  
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
    gap: .5em;
    position: relative;
  }

</style>
