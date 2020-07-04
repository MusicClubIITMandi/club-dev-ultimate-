<template>
  <v-card dark>
    <v-toolbar>
      <v-toolbar-title>Add a Song to Your Song Recommendations</v-toolbar-title>
      <v-spacer />
    </v-toolbar>
    <v-card-text>
      <v-form ref="form" v-model="valid" lazy-validation>
        <v-container>
          <v-text-field
            v-model="song_details.recommendation_song_name"
            prepend-icon="headset"
            :counter="70"
            label="Song"
            :rules="rules.Song"
            maxlength="70"
            required
          />
          <v-text-field
            v-model="song_details.recommendation_song_artist"
            prepend-icon="person"
            :counter="70"
            label="Artist"
            :rules="rules.Artist"
            maxlength="70"
            required
          />
          <v-select
            v-model="song_details.recommendation_song_genre"
            prepend-icon="headset"
            :counter="70"
            label="Genre"
            :items="genre_items"
            :rules="rules.Genre"
            maxlength="70"
            required
          />
        </v-container>
      </v-form>
    </v-card-text>
    <v-card-actions>
      <v-spacer />
      <v-btn color="teal" @click="addSong()" :loading="loading">
        Add
        <v-icon dark right>mdi-checkbox-marked-circle</v-icon>
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import axios from "axios";
import swal from "sweetalert2";
import router from "../../router";

export default {
  name: "AddSong",
  data: () => ({
    drawer: null,
    loading: 0,
    items: [
      { title: "Home", icon: "house" },
      { title: "Get Songs", icon: "headset" },
      { title: "LogOut", icon: "mdi-export" }
    ],
    song_details: {},
    name: sessionStorage.getItem("username"),
    valid: true,
    loading: false,
    rules: {
      Song: [
        v => !!v || "Required",
        v =>
          /^[A-Z a-z 0-9_ ']+$/.test(v) ||
          "Name can only contain letters and digits"
      ],
      Artist: [v => !!v || "Required"],
      Genre: [
        v => !!v || "Required",
        v => /^[a-z 0-9_]+$/.test(v) || "Genre can only contain small letters"
      ]
    },
    genre_items: ["rock", "metal", "pop"]
  }),

  created() {
    this.checkLoggedIn();
  },

  methods: {
    checkLoggedIn() {
      if (!localStorage.getItem("token")) {
        router.push("/auth");
      }
    },

    LinkTo: function(item) {
      var ref = "";
      if (item.title == "Home") {
        ref = "http://localhost:8080/";
      } else if (item.title == "Get Songs") {
        ref = "http://localhost:8080/getsong/";
      } else if (item.title == "LogOut") {
        this.$session.destroy();
        ref = "http://localhost:8080/auth";
      }
      window.location.href = ref;
    },

    addSong() {
      if (this.$refs.form.validate()) {
        this.loading = true;
        this.loading = true;

        this.song_details.song_name = this.song_details.recommendation_song_name.toLowerCase();
        this.song_details.song_artist = this.song_details.recommendation_song_artist.toLowerCase();

        axios.defaults.headers.common["Authorization"] =
          "Token " + localStorage.getItem("token");

        axios
          .post("http://localhost:8000/auth/verify/", {
            token: localStorage.getItem("token")
          })
          .then(() => {
            axios
              .post(
                "http://localhost:8000/songsapp/recommendation/",
                this.song_details
              )
              .then(res => {
                this.loading = false;
                alert("Your Song has been added.");
                location.reload();
              })
              .catch(error => {
                this.loading = false;
                if (error.response.status == 400) {
                  alert("This Song has already been added.");
                  location.reload();
                }
              });
          })
          .catch(error => {
            this.loading = false;
            console.log(error);
          });
      }
    }
  }
};
</script>

<style scoped>
</style>