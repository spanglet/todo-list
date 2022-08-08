
<template>

  <div class='calendar-main'>
    <CalendarMonth v-if="calView == 'month'"/>
    <CalendarWeek v-else />
  </div>

</template>

<script>

  import { computed } from 'vue'

  import CalendarMonth from "./CalendarMonth.vue"
  import CalendarWeek from "./CalendarWeek.vue"
  import { useTasks } from "../stores/tasks.js"

  export default { 
    setup() {
      const store = useTasks()
      return {
        store,
      }
    },
    components: {
      CalendarWeek,
      CalendarMonth,
    }, 
    props: ['calView'],
    data() {
      return {
      }
    },
    mounted() {
      this.store.fetchTasks()
    },
  }
</script>

<style>

  .calendar-main {
    padding: 5px;
  }

</style>
