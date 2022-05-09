
<template>

  <div class="sidebar-tile">

    <div class="sidebar-tile-header" @click="expand">
      {{ text }}
      <font-awesome-icon :icon="dropdownIcon" /> 
    </div>

    <TransitionGroup>
      <div class="sidebar-expanded-group" v-if="expanded">
        <div class="sidebar-expanded-item" v-for="list in currentLists" :key="list" @click="changeList(list.id)">
            {{ list.name }}
            <Button class="del-list-btn" btn-type="xmark" @click="this.$emit('listRemoved', list)" />
        </div>
        <Button class="new-list-btn" v-if="expanded" btn-type="plus" @click="this.$emit('viewForm')" />
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
    inject: ['currentLists'],
    props: ["text"],
    data() {
      return {
        expanded: false,
        lists: this.currentLists
      }
    },
    emits: ['viewForm','listChanged', "listRemoved"],
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

  .sidebar-tile {
    display: flex;
    flex-flow: column nowrap;
    align-items: stretch;
    margin: 5px;
    gap: 10px;
    
  }
  .sidebar-tile > * {
  }

  .sidebar-tile-header {
    display: flex;
    font-size: 20pt;
    justify-content: space-between;
    height: 30px;
  }
  .sidebar-tile-header:hover {
    background: hsl(var(--hue-purple),100%,var(--lgt-2));
  }
  .new-list-btn {
    height: 30px;
    width: 150px;
  }
  .sidebar-expanded-group {
    display: flex;
    flex-flow: column nowrap;
    gap: 5px;
  }
  .sidebar-expanded-item {
    display: flex;
    justify-content: space-between;
    height: 25px;
    font-size: 16pt;
    text-align: left;
    flex: 1;
  }
  .del-list-btn {
    width: 25px;
    background: red;
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

