
<template>
  
  <div class="cal-month">
    <div class='cal-header' v-for="dayName in daysInWeek">
      {{ dayName }} 
    </div>
    <div v-for="i in startDay" class="inactive-day">
      <div>{{ i }} </div>
    </div>
    <div v-for="day in days" class="day">
      <CalendarTile :date="new Date(year, month, day)" />
    </div>
  </div>

</template>

<script>
  
  import CalendarTile from "./CalendarTile.vue"

  export default {

    components: {
      CalendarTile,
    },
    data() {
      return {
        year: new Date().getFullYear(),
        month: new Date().getMonth(),
        daysInWeek: ['Sunday', 'Monday', 'Tuesday',
          'Wednesday', 'Thursday', 'Friday', 'Saturday'],
      }
    },
    computed: {
      days() {
        var numDays = (new Date(this.year, this.month, 0)).getDate()
        return Array.from({length: numDays}, (_, i) => i + 1)
      },
      startDay() {
        return (new Date(this.year, this.month, 1)).getDay()
      },
    }
  }

</script>

<style>

  .cal-month {
    display: grid;
    grid-template-columns:
      repeat(7, minmax(60px, 1fr)) [col-end];
    grid-template-rows:
      minmax(25px, 1fr) 
      repeat(5, minmax(60px, 1fr)) [row-end];
    height: 100%;  
    font-size: 1.5em;
    font-weight: bold;
    gap: 3px;
  }
  .day {
    border: 3px solid black;
    border-radius: 5px;
  }
  .inactive-day {
    background-color: lightgrey;
    opacity: .3;
  }

</style>
