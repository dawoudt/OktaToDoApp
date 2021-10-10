export default {
  oidc: {
    clientId: '0oa26c3o1mbzUY1tC5d7',
    issuer: 'https://dev-73746063.okta.com/oauth2/default',
    redirectUri: 'http://localhost:8080/login/callback',
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
