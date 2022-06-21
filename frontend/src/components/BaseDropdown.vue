
<template>

  <div class="dropdown">
  
    <div class="dropdown-header" @click="expand">
      {{ headerText }}
      <font-awesome-icon :icon="dropdownIcon" /> 
    </div>

    <TransitionGroup>
      <div class="expanded-group" v-if="expanded">
        <div
          v-for="item in dropdownItems"
          :key="list"
          class="expanded-item"
        > {{ item }}
        </div>
      </div>
    </TransitionGroup>

  </div>

</template>


<script>

  import Button from "./Button.vue"

  export default {
    components: {
      Button
    },
    props: ["headerText"],
    data() {
      return {
        expanded: false,
        dropdownItems: ["Logout", "Account Info"]
      }
    },
    computed: {
      dropdownIcon() {
        return this.expanded ? 'angle-up' : 'angle-down'
      }
    },
    methods: {
      // Expand or shrink when title is clicked
      expand: function () {
        this.expanded = !this.expanded
      },
      // Emit the list change to the root (App) component for handling
      changeList: function(list) {
        this.$emit('listChanged', list)
      }
    }
  }

</script>


<style>

  .dropdown {
    display: flex;
    flex-flow: column nowrap;
    align-items: flex-end;
    margin: 5px;
    gap: 10px;
    
  }

  .dropdown-header {
    display: flex;
    font-size: 20pt;
    justify-content: space-between;
    height: 30px;
    gap: 6px;
    
  }
  .dropdown-header:hover {
    background: hsl(var(--hue-purple),100%,var(--lgt-2));
  }
  .expanded-group {
    display: flex;
    flex-flow: column nowrap;
    gap: 5px;
    margin: 10px;
    position: absolute;
    top: 3em;
    color: white;
    background: hsl(var(--hue-purple),100%,var(--lgt-3));
    border-radius: 0px 0px 5px 5px;
    border: 2px hsl(var(--hue-purple),100%,var(--lgt-5));
  }
  .expanded-item {
    display: flex;
    justify-content: space-between;
    height: 25px;
    font-size: 16pt;
    text-align: left;
    flex: 1;
  }
  .v-enter-active,
  .v-leave-active {
    transition: all .5s ease;
  }
  .v-leave-to,
  .v-enter-from {
    opacity: 0;
  }
  .expanded-content:hover {
    background-color: grey;
  }
  

</style>

