<template>
  <v-card flat>
    <v-toolbar
      dark
      extended
      flat
      overflow: hidden
    >
    </v-toolbar>

    <v-card dark>
      <v-toolbar flat>
        <v-toolbar-title>Get Song Recommendations</v-toolbar-title>
        <v-spacer />
      </v-toolbar>
      <v-divider></v-divider>
        
      <v-card-text>
          <v-select
            v-model="genre"
            :items="allGenres"
            label="Select an option">
          </v-select>
          <v-spacer></v-spacer>
          <v-btn color="teal" @click="getRecommendations()" :disabled="disableBtn">
            Get Songs
            <v-icon dark right>headset</v-icon>
          </v-btn><br><br>
          <h3 class="cap" v-for ="(item, i) in info" :key="i" v-on:click="link(item)">
            {{ item.recommendation_song_name }} by {{ item.recommendation_song_artist}}
          </h3>
              
      </v-card-text>
    </v-card>
  </v-card>
</template>


<script>
import axios from 'axios';

export default {
    name: "GetSongRecommendation",
    data: () => {
      return ({
        info: [],
        allGenres: ["rock","metal","pop"],
        genre: "",
        claims: "",
        disableBtn: false
      });
    },
    computed: {
      allSongs() { 
        return this.$store.getters.getAllSongRecommendations;
      },
    },
    created () { 
      axios.defaults.headers.common["Authorization"] =
          "Token " + this.$session.get("token");

      if (this.allSongs == null) {
        this.disableBtn = true;
        this.getAllRecommendations();
      }
    },
    methods: {

      getAllRecommendations() {
        axios.get("http://localhost:8000/songsapp/recommendation/").then(res => {
          this.disableBtn = false;
          this.$store.dispatch("changeAllSongRecommendations", res.data);
          this.allSongs = res.data;
        });
      },

      link: function (item) {
        const ref = `https://www.youtube.com/results?search_query=${item.recommendation_song_name} by ${item.recommendation_song_artist}`;
        window.open(ref);
      },

      getRecommendations() {
        const shuffledSongs = this.allSongs.sort(() => 0.5 - Math.random()).filter(song => song.recommendation_song_genre == this.genre);
        this.info = shuffledSongs.slice(0, Math.min(3, shuffledSongs.length));
      },
    }
}
</script>

<style scoped>
  v-card {
    overflow: hidden;
  }
  .cap {
    text-transform: capitalize;
    font-family: sans-serif;
    
  }
  .cap:hover {
    cursor: pointer;
    color: purple;
  }
</style>