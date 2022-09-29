import { defineStore, acceptHMRUpdate } from 'pinia'
import { axios } from "../axios.js"

export const useAuth = defineStore('auth', {
  state: () => ({
    username: [],
  }),
  getters: {
  },
  actions: {
    async loginUser() {
      try {
        var resp = await axios.get("/")
      }
      catch (error) {
        console.log(error)
      }
    },
    async loginUser() {
      try {
        var resp = await axios.get("/")
      }
      catch (error) {
        console.log(error)
      }
    },
  }
})

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useTasks, import.meta.hot))
}
