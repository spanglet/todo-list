<template> 
  <div class="tile" @click="isExpanded=!isExpanded" :class="{ 'expanded-tile': isExpanded, 'removed-tile': isRemoved}">
    <div class="col">
      {{name}}
    </div>  
    <div class="col description-col">
      <p class="tile-text"> {{description}} </p>
    </div>  
    <div class="col">
      {{formattedDueDate}}
    </div>  
    <div class="button-col">
      <SymbolButton
          class="tile-button del-button"
          @click="removeItem"
          :icons="['xmark']"
      />
      <SymbolButton
          class="tile-button done-button"
          @click="markTaskCompleted"
          :icons="['check']"
      />
    </div>  
  </div>
</template>


<script>

  import SymbolButton from "./SymbolButton.vue"
  
  var days = ['Sun','Mon','Tues','Wed','Thurs','Fri','Sat']
  var months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
      "Jul","Aug", "Sep", "Oct", "Nov", "Dec"]

  export default { 
    components: {
      SymbolButton
    },
    data() {
      return {
        isExpanded: false,
        isRemoved: false
      }
    },
    emits: ['removeItem'],
    props: {
      name: String,
      description: String,
      dueDate: String
    },
    methods: {
      // Emit delete event to App parent container
      removeItem() {
        this.isRemoved = true
        this.$emit('removeItem')
      },
      markTaskCompleted() {
        this.isRemoved = true
        this.$emit('taskCompleted')
      }
    },
    computed: {
      formattedDueDate() {
        var date = new Date(this.dueDate)
        return days[date.getDay()] + ", " +
            months[date.getMonth()] + " " +
            (date.getDate() + 1)
      },

    }
  }
</script>


<style>

  .tile {
    display: flex;
    align-items: stretch;
    justify-content: center;
    margin: 0;
    list-style: none;
    border: 2px #b378cc outset;
    border-radius: 8px;
    background: #bb8fce;
    gap: 5px;
    height: 3em;
    transition: all .5s;
  }
  .expanded-tile {
    height: 6em;
  }
  .expanded-tile .tile-text {
    white-space: normal;
  }
  .removed-tile {
    opacity: 0;
  }
  .col {
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    flex: 1;
  }
  .button-col {
    display: flex;
    justify-content: flex-end;
    align-items: stretch;
  }
  .tile-text {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .description-col {
    overflow: hidden;
  }
  .tile-button {
    margin: 2px; 
    width: 4em;
    max-height: 65px;
  }
  .del-button {
    background: darksalmon;
  }
  .done-button {
    background: lightgreen;
  }

</style>
