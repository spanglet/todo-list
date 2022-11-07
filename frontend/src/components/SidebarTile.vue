
<template>

  <div class="sidebar-item">

    <div class="sidebar-group-header" @click="expand">
      {{ name }}
    </div>

      <div class="sidebar-group">

        <div 
          class="sidebar-tile"
          v-for="route in routes"
          :key="route.id"
          :class="{ 'active-route': isActiveRoute(route.id) }"
          @click="routeTo(route.id)"
        >
          <div>
            {{ route.name }}
          </div>

          <div @click.stop='onClick(route)'>

            <slot name='sidebar-tile-button'/>

          </div>
        </div>
        
        <div v-if="hasFooter" class="sidebar-tile footer-item">
          <slot name='sidebar-tile-footer' /> 
        </div>

      </div>

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
      onClick(route) {
        this.$emit('clicked', route)
      },
    }
  }

</script>


<style>

  .sidebar-item {
    display: flex;
    flex-flow: column nowrap;
    align-items: stretch;
    gap: 10px;
  }
  .sidebar-group-header {
    display: flex;
    font-size: 1.75em;
    justify-content: space-between;
    align-items: center;
    height: 30px;
    box-shadow: 0px 3px 5px 1px black;
    padding: 5px;
  }
  .sidebar-group {
    display: flex;
    flex-flow: column nowrap;
    gap: 3px;
    margin: 5px;
  }
  .sidebar-tile {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 18pt;
    text-align: left;
    flex: 1;
    padding: 5px;
    border: 3px solid #1a1a1a;
    border-radius: 10px;
    background: hsl(var(--hue-purple),100%,var(--lgt-4))
  }
  .footer-item {
    border: 2px solid black;
    border-radius: 12px;
    background: green;
  }
  .active-route {
    border: 5px solid black;
    background: hsl(var(--hue-purple),70%,var(--lgt-4));
  }
  .sidebar-tile:hover, .sidebar-tile-header:hover {
    filter: brightness(.92);
  }

</style>

