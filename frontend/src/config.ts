export default {
  oidc: {
    clientId: process.env.VUE_APP_OKTA_CLIENT_ID,
    issuer: `https://${process.env.VUE_APP_OKTA_DOMAIN}/oauth2/default`,
    redirectUri: `http://${process.env.VUE_APP_OKTA_BASE_URL}/login/callback`,
    scopes: ['openid', 'profile', 'email'],
    pkce: true,
    testing: {
      disableHttpsCheck: true
    }
  },
  resourceServer: {
    messagesUrl: 'http://localhost:8000/api/messages'
  },
  app: {
    basename: 'Dawouds Okta'
  }
}
