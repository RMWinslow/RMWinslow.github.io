- Motivation
    - relatives sick
    - graph theory stuff is neato
    - Politicians and religious people got sick first
    - Transmission through networks
      - Percolation threshold
         - On random graphs and on graphs with a specific structure
         - Tells us whether an "outbreak" will become an "epidemic" and spread to an infinite number of nodes 
    - Not looking at:
      - the time path of how a disease spreads
        - (Sort of time invariant approach)
      - The mortality or costs involved.

- Model
    – Tranmission
        - always happens at rate r
        - If you have n outneighbors, its expected that your case will cause an additional n*r new cases
        - If there is a total population *I* of your type, then together you'll create Inr new cases.
        - If nr > 1, then on average cases will grow.
    - population structure
      - Split into types indexed by *i*
      - types are defined by  the number of connections is has to each other type.
      - infinite population of each type, so I'm not worrying about susceptibility and the like
      - parameters n_ij tell us the number of outdegrees from a type i node to a type j node
      - Suppose that each of these groups is very large and that the connections are chosen at random, save for the fact about which group they connect.
    - Obvious consequences
      - let \Phi_{i} be the portion of infectious people who are of type i. So \Phi_{i}\equiv\frac{I_{i}}{\sum_{k}I_{k}}.
      - expected number of new transmission events is \sum_{k}\left[I_{k}\sum_{j}rn_{kj}\right]
      - refer to latex notes for info about number of newly infected of each type

- Proposition 0: what happens with identity mapping among distribution
  - Any point is a fixed point
  - will technically be minor variations
  - but will stick around the initial outbreak point
  - epidemic will depend purely on whether n_ii > 1/r?

- Proposition 1: fixed point and convergence
  - Note that, holding the parameters \eta_{..} constant, the system of equations describing each \Phi_{i}^{\prime} is a mapping from a probability distribution to itself, which doesn't depend on the transmission rate r. 
  - In other words, I'm splitting up two questions about how the contagion spreads: how does the distribution of types amongst the infected evolve?, and does the incidence of the infection grow or shrink?
  - Because it's a continous mapping from a simplex to the same simplex, there must be at least one fixed point. 
  - This fixed point is not necessarily unique. 
  - If the connecton parameters \left\{ \eta\right\}  are chosen such that \eta_{ij}\neq0 for any i\neq j , then the fixed point must be in the interior of the probability. simplex.
  - In the latter case, subsequent generations of infectious will evolve to have a distribution of types which converges to the fixed distribution. 
  - Then the question of whether the contagion can spread to a large portion of the network depends on the average number of new tranmissions per person among this distribution of infectious people.
  - Then after the distribution evolves in a way determined by the structure of connections between types, the number of new transmissions per infectious person will be a weighted sum of the average number of transmissions per type of person \sum_{k}\left[\Phi_{k}\sum_{j}rn_{kj}\right]

-Continuous example with two types is in pdf

-exmaple with only two people

-note about endogenizing connections )pdf

-point about eigenvectors


[ ] What do checkmarks look like?