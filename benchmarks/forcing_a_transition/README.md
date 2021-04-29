

# motivation
I want to enforce that after visiting stop x the tour must continue to stop y. 

# details
- transit cost between nodes is constant at 1
- problem generator:
    - transitions are picked at random
    - solution time out is 10 seconds

# links
## next var
- https://github.com/google/or-tools/issues/224#issuecomment-787049151

## locks
- manual: https://acrogenesis.com/or-tools/documentation/user_manual/manual/vrp/partial_routes.html
- reference: https://developers.google.com/optimization/reference/python/constraint_solver/pywrapcp#applylocks
- **are locks always at the beginning of tours?**