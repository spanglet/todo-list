<template>

  <div class="app-header">
    <div class="header-item invisible" />
    <div class="header-item header-title"> To-Do List </div>
      <BaseDropdown 
        header-text="My Account"
        class="header-item header-menu"
      />
  </div>

</template>

<script>

  import BaseDropdown from "./BaseDropdown.vue"

  export default {
    components: {
      "BaseDropdown": BaseDropdown
    },
    data() {
       return {
        menuExpanded: false
       }
    },
    methods: {

      expandAccountMenu () {
        this.menuExpanded = !this.menuExpanded
      },
      logout () {
        var url = this.HOST_URL + "users/logout/"
        this.axios.get(url, this.REQ_CONFIG
          ).then((res) => {
            if (res.status == 200) {
              this.$router.push('/login')
            }
          })
      }
    }
  }

</script>


<style>

  .app-header {
    display: flex;
    flex-flow: row nowrap;
    justify-content: center;
    align-items: center;
    background: hsl(var(--hue-purple), 100%, var(--lgt-2));
    color: white;
    position: relative;
  }
  .app-header > * {
    flex: 1;
  }
  .header-title {
    display: flex;
    justify-content: center;
    font-size: 30px;
  }
  .header-menu {
    display: flex;
    justify-content: flex-end;
    gap: 10px;
  }
  .header-menu-item:hover {
    background: lightgrey; 
  }
  .invisible {
    visibility: hidden;
  }

</style>

