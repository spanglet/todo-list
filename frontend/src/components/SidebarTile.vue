
<template>

  <div class="sidebar-tile">

    <div class="sidebar-tile-header sidebar-tile-item" @click="expand">
      {{ name }}
      <font-awesome-icon :icon="dropdownIcon" v-if="routes"/> 
    </div>

    <TransitionGroup>
      <div class="sidebar-expanded-group" v-if="expanded && routes">

        <div 
          class="sidebar-expanded-item sidebar-tile-item"
          v-for="route in routes"
          :key="route.id"
          :class="{ 'active-route': isActiveRoute(route.id) }"
          @click="routeTo(route.id)"
        >
          <div>
            {{ route.name }}
          </div>
          <div
            v-if='hasButton'
            @click.stop='onClick(route.id)'
          >
            <slot name='sidebar-tile-button' />
          </div>
        </div>
        
        <div v-if="hasFooter" class="sidebar-expanded-item footer-item">
          <slot name='sidebar-tile-footer' /> 
        </div>

      </div>
    </TransitionGroup>

  </div>

</template>

<script>

  import { useTasks } from '../stores/tasks.js'

  export default {
    setup() {
      const store = useTasks()
      return {
        store,
      }
    },
    emit: ['clicked'],
    props: {
      name: {
        type: String,
        required: true
      },
      path: {
        type: String,
        required: true
      },
      routes: Array,
      footer: Boolean,
      tileButton: Boolean,
    },
    data() {
      return {
        expanded: false,
        hasFooter: this.footer,
        hasButton: this.footer,
      }
    },
    computed: {
      dropdownIcon() {
        return this.expanded ? 'angle-up' : 'angle-down'
      },
      basePath() {
        return '/app/' + this.path
      },
    },
    methods: {
      // Expand or shrink when title is clicked
      expand() {
        if (this.routes) {
          this.expanded = !this.expanded
        }
        else {
          this.$router.push(this.basePath)
        }
      },
      routeTo(id) {
        this.$router.push(this.basePath + id.toString() )
      },
      isActiveRoute(id) {
        return this.$route.path === (this.basePath + id)
      },
      onClick(id) {
        this.$emit('clicked',id)
      },
    }
  }

</script>


<style>

  .sidebar-tile {
    display: flex;
    flex-flow: column nowrap;
    align-items: stretch;
    gap: 10px;
  }
  .sidebar-tile-header {
    display: flex;
    font-size: 1.75em;
    justify-content: space-between;
    align-items: center;
    height: 30px;
    box-shadow: 0px 3px 5px 1px black;
    padding: 5px;
  }
  .sidebar-expanded-group {
    display: flex;
    flex-flow: column nowrap;
    gap: 1px;
  }
  .sidebar-expanded-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 25px;
    font-size: 18pt;
    border-radius: 2px;
    text-align: left;
    flex: 1;
    padding: 5px;
    border-bottom: 1px solid #3c0e97;
  }
  .footer-item {
    border: 4px dashed black;
    background: green;
    border-radius: 12px;
  }
  .v-enter-active,
  .v-leave-active {
    transition: all .5s ease;
  }
  .v-leave-to,
  .v-enter-from {
    opacity: 0;
  }
  .active-route {
    background-color: hsl(var(--hue-purple),100%,var(--lgt-2));
  }
  .sidebar-tile-item:hover {
    background: hsl(var(--hue-purple),100%,var(--lgt-2));
  }
  .sidebar-tile-item {
    display: flex;
    justify-content: space-between; 
  }

</style>

