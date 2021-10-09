export default {
  oidc: {
    clientId: '0oa260t6nxLw9hKwP5d7',
    issuer: 'https://dev-67344502.okta.com',
    redirectUri: 'https://61614b8cda02ec0008942f85--determined-swirles-94cfa3.netlify.app/',
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
