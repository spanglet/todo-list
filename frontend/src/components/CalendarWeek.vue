
<template>

  <div class="cal-week">
    <div class="cal-week-group cal-week-header">
      <div  v-for="dayName in daysInWeek">
        {{ dayName }} 
      </div>
    </div>
    <div class="cal-week-group" >
      <CalendarTile
        v-for="n in 7"
        :date="new Date(year, month, startDate + n - 1)"
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
    justify-content: center;
  }
  .cal-week-group {
    display: flex;
    flex-flow: row nowrap;
    align-items: stretch;
    justify-content: space-around;
    gap: 3px;
  }
  .cal-week-group > * {
    flex: 1;
  }

</style>
