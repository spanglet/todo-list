import { defineStore } from 'pinia'
import { axios } from "../axios.js"

export const useLists = defineStore('lists', {
  state: () => ({
    _lists: [],
    currentListID: 0,
  }),
  getters: {
    currentList(state) {
      return state.currentListID
    },
    /**
     * @returns {{ text: string, id: number, isFinished: boolean }[]}
     */
    lists(state) {
      return this._lists
    },
  },
  actions: {
    async fetchLists() {
      try {
        var resp = await axios.get("lists/")
        this._lists = resp.data
        if (this.currentListID == 0) {
          this.currentListID = this._lists[0].id
        }
      }
      catch (error) {
        console.log(error)
      }
    },
    async deleteList(list_id) {
      var targetPath = "lists/" + String(list_id)
      var response = await axios.delete(targetPath)
      this.fetchLists()
    },
    async addList(list_name) {
        var results = await axios.post("lists/", {
            "name": list_name
          })
        this.fetchLists()
    },
  }
})

