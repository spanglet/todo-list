
<template>

  <div class="cal-week">
    <div class="cal-week-group cal-week-header">
      <div class="cal-header" v-for="dayName in daysInWeek">
        {{ dayName }} 
      </div>
    </div>
    <div class="cal-week-group cal-week-days" >
      <CalendarTile
        v-for="n in 7"
        :date="new Date(year, month, startDate + n - 1)"
        class='cal-week-day'
      />
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
      startDate() {
        var currDate = (new Date()).getDate()
        var dayOfWeek = (new Date()).getDay()

        return currDate - dayOfWeek 
      }
    },
  }
</script>

<style>

  .cal-week {
    display: flex;
    flex-flow: column nowrap;
    align-items: stretch;
    justify-content: flex-start;
    height: 100%;
    margin: 5px;
  }
  .cal-header {
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: bold;
  }
  .cal-week-header {
    background: skyblue;
    border-radius: 8px;
  }
  .cal-week-group {
    display: flex;
    flex-flow: row nowrap;
    align-items: stretch;
    justify-content: space-around;
    font-size: 1.5em;
  }
  .cal-week-group > * {
    flex: 1;
  }
  .cal-week-days {
    flex: .8;
  }
  .cal-week-day {
    border: 2px solid black;
    border-radius: 5px;
    box-shadow: 0px 0px 1px 1px grey;
    margin: 5px;
  }

</style>
