# Buildbot

# workflow
## init
1. cloudformation deploy meta: gitlab, jenkins, scores page, health checkers teams meta dynamo
2. cloudformation deploy per team: team page, team dynamo, EKS, WAF container, webapp container
## prepare
3. team page display readme highlighting situation of vuln
## identify
4. team ssh to server inspect logs
## contain
5. team add WAF rules
6. checker lambda scores if vuln is blocked
## eradicate
7. team page display readme asking to clean site content
8. team removes malicious content
9. checker lambda scores if content is cleaned
## recovery
10. team page explains ci/cd pipeline
11. team fixes code and deploys new server
12. checker lambda scores if vuln is fixed
## lessons learned
13. team page explains ci/cd testing
14. team writes unit tests
15. jenkins pulls out tests and tests against hidden respository for regression and valid builds
