# Please Note
The majority of this project was developed at UC Berkeley, primarily by John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu). Within this project were several blank sections that needed to be filled in to complete major parts of the project. The parts of this project listed below were implemented by me and were of my own design (excluding the traditional algorithms, which I implemented but definitely did not create). These implementations include search algorithms, heuristics, and more.

The creators of this project requested that solutions not be shared or published, and I have attempted to honor this request by placing my solutions in this inconspicuously named repository. I have only made this repository public so that those who are reviewing my resume will be able to see my work. I am not attempting to give away any solutions. After receiving responses from the positions I have applied to this repository will be made private.

# My Implementations and Demos
### NOTE: Some demo commands will only work if you are using Python 3.6
The following are parts of this program that I implemented. These solutions were implemented by me and were of my own design (excluding the traditional algorithms, which I implemented but definitely did not create). Each "Demo Command" can be run in the terminal inside its respective project folder. For example: all of the demo commands under "Pacman Search" can be run in a terminal when inside the pacmanSearch directory.

## Pacman Search
  **search.py**\
    - Code: [Depth-first Search](https://github.com/CalDevC/AI-Portfolio-Project/blob/aa6cece2f691c15496020095f3220ae964da4e00/pacmanSearch/search.py#L76)\
    - Demo Command: `python pacman.py -l bigMaze -z .5 -p SearchAgent`\
    \
    - Code: [Breadth-first Search](https://github.com/CalDevC/AI-Portfolio-Project/blob/aa6cece2f691c15496020095f3220ae964da4e00/pacmanSearch/search.py#L137)\
    - Demo Command: `python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5`\
    \
    - Code: [Uniform-cost Search](https://github.com/CalDevC/AI-Portfolio-Project/blob/aa6cece2f691c15496020095f3220ae964da4e00/pacmanSearch/search.py#L194)\
    - Demo Command: `python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=ucs -z .5`\
    \
    - Code: [A* Search](https://github.com/CalDevC/AI-Portfolio-Project/blob/aa6cece2f691c15496020095f3220ae964da4e00/pacmanSearch/search.py#L265)\
    - Demo Command: `python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar -z .5`\
    \
  **searchAgents.py**\
    - Code: ['Find all corners' Search Problem](https://github.com/CalDevC/AI-Portfolio-Project/blob/aa6cece2f691c15496020095f3220ae964da4e00/pacmanSearch/searchAgents.py#L279)\
    - Demo Command: `python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem`\
    \
    - Code: ['Find all corners' Heuristic](https://github.com/CalDevC/AI-Portfolio-Project/blob/aa6cece2f691c15496020095f3220ae964da4e00/pacmanSearch/searchAgents.py#L370)\
    - Demo Command: `python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5`\
    \
    - Code: ['Eat all dots' Heuristic](https://github.com/CalDevC/AI-Portfolio-Project/blob/aa6cece2f691c15496020095f3220ae964da4e00/pacmanSearch/searchAgents.py#L474)\
    - Demo Command: `python pacman.py -l trickySearch -p AStarFoodSearchAgent`\
    

## Pacman Multi-agent
  **multiAgents.py**\
    - Code: [Reflex Agent](https://github.com/CalDevC/AI-Portfolio-Project/blob/97922af57d84059afc78f200a0565356c2084ff0/pacmanMultiAgent/multiAgents.py#L22)\
    - Demo Command: `python pacman.py -p ReflexAgent -l testClassic`\
    \
    - Code: [Minimax](https://github.com/CalDevC/AI-Portfolio-Project/blob/97922af57d84059afc78f200a0565356c2084ff0/pacmanMultiAgent/multiAgents.py#L140)\
    - Demo Command: `python pacman.py -p MinimaxAgent -l minimaxClassic -a depth=4`\
    \
    - Code: [Expectimax](https://github.com/CalDevC/AI-Portfolio-Project/blob/97922af57d84059afc78f200a0565356c2084ff0/pacmanMultiAgent/multiAgents.py#L260)\
    - Demo Command: `python pacman.py -p ExpectimaxAgent -l minimaxClassic -a depth=3`\
    \
    - Code: [Better Evaluation Function](https://github.com/CalDevC/AI-Portfolio-Project/blob/97922af57d84059afc78f200a0565356c2084ff0/pacmanMultiAgent/multiAgents.py#L353)\
    - Demo Command: `python autograder.py -q q5` (This command will play several games to completion)
    
