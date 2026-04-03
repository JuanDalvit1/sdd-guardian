# Deploy

## Release flow

1. Update the repository locally
2. Run local validation
3. Commit and push to `main`
4. Let GitHub Actions validate structure and scripts
5. Pull on other machines and run `bootstrap\\sync.ps1`

## Rollback

- Revert the offending commit
- Push the revert
- Run `bootstrap\\sync.ps1` on affected machines if install or snippet behavior changed

