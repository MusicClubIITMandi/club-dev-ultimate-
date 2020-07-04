<template>
  <v-content>
    <v-container fluid fill-height>
      <v-layout>
        <v-flex xs12 sm12 md6 lg6 offset-md-1 offset-lg-1>
          <v-card class="elevation-12">
            <v-toolbar dark>
              <v-toolbar-title>IIT Mandi Music Society - Login</v-toolbar-title>
              <v-spacer />
            </v-toolbar>
            <v-card-text>
              <v-form ref="form" v-model="valid" lazy-validation>
                <v-container>
                  <v-text-field
                    v-model="credentials.username"
                    prepend-icon="person"
                    :counter="70"
                    label="Username"
                    :rules="rules.username"
                    maxlength="70"
                    required
                  />
                  <v-text-field
                    v-model="credentials.password"
                    prepend-icon="lock"
                    type="password"
                    :counter="20"
                    label="Password"
                    :rules="rules.password"
                    maxlength="20"
                    required
                  />
                </v-container>
              </v-form>
            </v-card-text>
            <v-card-actions>
              <v-spacer />
              <v-btn @click="login">Login</v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </v-content>
</template>

<script>
import axios from "axios";
import router from "../../router";

export default {
  name: "Auth",
  data: () => ({
    credentials: {},
    valid: true,
    loading: false,
    rules: {
      username: [
        v => !!v || "Username is required",
        v =>
          (v && v.length > 3) ||
          "A username must be more than 3 characters long",
        v =>
          /^[a-z0-9_]+$/.test(v) ||
          "A username can only contain letters and digits"
      ],
      password: [
        v => !!v || "Password is required",
        v =>
          (v && v.length > 7) || "The password must be longer than 7 characters"
      ]
    }
  }),
  methods: {
    login() {
      if (this.$refs.form.validate()) {
        this.loading = true;
        axios
          .post("http://localhost:8000/auth/", this.credentials)
          .then(res => {
            localStorage.setItem("token", res.data.token);
            const username = this.credentials.username.toString();
            localStorage.setItem("username", username);
            router.push("/");
            location.reload();
          })
          .catch(e => {
            this.loading = false;
            console.log(e);
          });
      }
    }
  }
};
</script>