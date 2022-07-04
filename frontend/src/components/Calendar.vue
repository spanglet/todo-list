
<template>

  <div class='calendar-main'>
    <div class="cal-header" v-for="dayName in daysInWeek">
      {{ dayName }} 
    </div>
    <div v-for="day in days" class="day">
      <CalendarTile :date="new Date(year, month, day)">
        {{ day }} 
      </CalendarTile>
    </div>
  </div>

</template>

<script>

  import { computed } from 'vue'

  import CalendarTile from "./CalendarTile.vue"
  import { useTasks } from "../stores/tasks.js"

  export default { 
    setup() {
      const store = useTasks()
      return {
        store,
      }
    },
    components: {
      CalendarTile
    }, 
    data() {
      return {
        days: Array.from({length: 30}, (_, i) => i + 1),
        month: new Date().getMonth(),
        year: new Date().getFullYear(),
        daysInWeek: ['Sunday', 'Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday']
      }
    },
    mounted() {
      this.store.fetchTasks()
    },
    methods: {

    }
  }
</script>


<style>

  .calendar-main {
    display: grid;
    grid-template-columns:
      repeat(7, minmax(60px, 1fr)) [col-end];
    grid-template-rows:
      minmax(25px, 1fr) 
      repeat(5, minmax(60px, 2fr)) [row-end];
    height: 100%;  
    font-size: 1.5em;
    font-weight: bold;
  }
  .cal-header {
    grid-area: 0 / 0 / 1 / col-end;
    align-self: center;
    justify-self: center;
  }
  .day {
    grid-area: 1 / 0 / row-end / col-end;
    border: 3px solid black;
    border-radius: 5px;
    background-color: lightgrey;
  }

</style>
