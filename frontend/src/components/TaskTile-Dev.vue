<template> 
  <div class="task-tile" @click="isExpanded=!isExpanded" :class="{ 'expanded-tile': isExpanded, 'removed-tile': isRemoved}">
    <div class="task-row">
      <div class="task-name task-item">
        {{name}}
      </div>  
      <div class="task-date task-item">
        {{formattedDueDate}}
      </div>
      <div class="task-buttons task-item">
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
    <Transition name="description">
      <div v-show="isExpanded" class="task-description">
        <p class="tile-text"> {{description}} </p>
      </div>
    </Transition>
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
    emits: ['removeItem','taskCompleted'],
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

  .task-tile {
    border: 2px #b378cc solid;
    border-radius: 7px;
    background: #bb8fce;
    padding: 5px;
  }
  .task-row {
    display: flex;
    font-size: 2em;
  }
  .task-item {
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .task-name {
    flex: 5;
    justify-content: flex-start;
  }
  .task-date {
    flex: 2;
  }
  .task-buttons {
    flex: 1;
  }
  .task-description {
    border-top: 1px solid black;
    font-size: 1.2em;
    padding: 5px;
    transition: all 1s;
  }
  .description-enter-active,
  .description-leave-active {
    opacity: 0;
    transition: all 0.5s ease;
  }
  .description-enter-from,
  .description-leave-to {
    height: 0px;
    border-width: 0px;
    padding: 0px;
    opacity: 0;
  }

</style>
