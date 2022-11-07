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
  
  const days = ['Sun','Mon','Tues','Wed','Thurs','Fri','Sat']
  const months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
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
    border-radius: 7px;
    max-height: 55px;
    transition: all .5s;
    width: 100%;
  }
  .task-row {
    display: flex;
    font-size: 2em;
    border-radius: 7px;
    background: #bb8fce;
    padding: .25em .5em;
    border: 2px #b378cc solid;
    position: relative;
    z-index: 2;
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
    padding: 10px 1em .25em 1em;
    position: relative;
    z-index: 1;
    font-size: 1.2em;
    top: -5px;
    background: #acaaaa;
    border: 2px #b266bb solid;
    border-radius: 0 0 10px 10px;
  }
  .description-enter-active,
  .description-leave-active {
    transition: all .5s ease;
  }
  .description-enter-from,
  .description-leave-to {
    transform: translateY(-42px);
  }
  .expanded-tile {
    max-height: 100px;
    
  }

</style>
