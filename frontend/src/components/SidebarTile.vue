
<template>

  <div class="sidebar-tile">

    <div class="sidebar-tile-header" @click="expand">
      {{ text }}
      <font-awesome-icon :icon="dropdownIcon" /> 
    </div>

    <TransitionGroup>
      <div class="sidebar-expanded-group" v-if="expanded">
        <div 
          class="sidebar-expanded-item"
          v-for="list in currentLists"
          :key="list.id"
          :class="{ 'active-list': isActiveList(list.id) }"
          @click="changeList(list.id)">

            {{ list.name }}

            <Button
              class="del-list-btn"
              btn-type="xmark"
              @click="this.$emit('listRemoved', list)"
            />

        </div>

        <div
          class="completed-list sidebar-expanded-item"
          @click="changeList(-1)"
          :class="{ 'active-list': isActiveList(-1) }"
        >
          Completed Tasks
        </div>

        <Button
          class="new-list-btn"
          v-if="expanded"
          btn-type="plus"
          @click="this.$emit('viewForm')"
        > New List </Button>
      </div>
    </TransitionGroup>

  </div>

</template>


<script>

  import Button from "./Button.vue"
  import { useTasks } from '../stores/tasks.js'

  export default {
    setup() {
      const store = useTasks()
      return {
        store,
      }
    },
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
      expand() {
        this.expanded = !this.expanded
      },
      // Emit the list change to the root (App) component for handling
      changeList (list_id) {
        this.store.currentListID = list_id
      },
      isActiveList (listID) {
        return (this.store.currentListID == listID)
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
  .sidebar-tile-header {
    display: flex;
    font-size: 20pt;
    justify-content: space-between;
    height: 30px;
    box-shadow: 0px 3px 9px -8px black;
    padding: 5px;
  }
  .sidebar-tile-header:hover {
    background: hsl(var(--hue-purple),100%,var(--lgt-2));
  }
  .new-list-btn {
    background: aquamarine;
    font-size: 18pt;
    justify-content: space-evenly;
  }
  .sidebar-expanded-group {
    display: flex;
    flex-flow: column nowrap;
    gap: 5px;
  }
  .sidebar-expanded-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 25px;
    font-size: 16pt;
    text-align: left;
    flex: 1;
  }
  .del-list-btn {
    background: salmon;
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
  .active-list {
    background-color: hsl(var(--hue-purple),100%,var(--lgt-2));
  }
  .completed-list {
    border-top: 2px solid black;
    box-shadow: 0px -3px 9px -5px black;
  }

</style>

