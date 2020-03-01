


document.write(`
<div class="rulesBlock"   style="background-color: hsl(0, 80%, 80%);">
    <center>
        <div id="flex-container">
            <div class="flex-item" >   <img src="imgs/dragon.svg" >    </div>
            <div class="flex-item" >   <img src="imgs/mahjong.svg" >    </div>
            <div class="flex-title">    
                <h3 id="dragoncastle">    Dragon Castle    </h3> 
            </div>
            <div class="flex-item" >   <img src="imgs/mahjong.svg">    </div>
            <div class="flex-item" >   <img src="imgs/dragon.svg" >    </div>
        </div>

        <p><i>  YET TO PLAY </i></p>
        <p>(2-4) Matching. Mahjong tiles, pyramids, chips.</p>
    </center>
    <div class="rulesBody"  style="background-color: hsl(0, 100%, 95%)">
        <ul>
        <li>Use the Dragons, Winds, and Suits 1-7 to build a face-up dragon's castle with three floors in the middle of the table.</li>
        <li>A tile is <b>available</b> if at least one of its long edges is free.</li>
        <li>On your turn</li>
            <ol>
            <li><b>TAKE:</b> Take an <b>available</b> tile from the top floor of the Dragon's Castle.</li>
                <ul>
                <li>After taking a tile, also do exactly one of the following three actions:</li>
                    <ul>
                    <li>Take an second, identical, available tile from any floor.</li>
                    <li>Take a pyramid from the pool and put it in your reserve.</li>
                    <li>Discard that tile you took, and earn +1 point.</li>
                    </ul>
                <li>Alternatively, you may forgoe the above to Summon the Elder Dragon and earn +2 points. (You can only do this if the Dragon's castle is down to its bottom floor.)</li>
                </ul> 
            <li><b>BUILD:</b> Place any tiles you just collected face-up into your own castle. A tile may be placed:      
                <ul>
                <li>On top of a face-down tile.</li>
                <li>On the ground diagonally or orthogonally adjacent to a tile in your castle.</li>
                </ul>           
                But may not be placed:
                <ul>
                <li>On top of a face-up tile.</li>
                <li>On top of a pyramid.</li>
                </ul></li>
            <li><b>FLIP:</b> If there is any group of more than 4 connected tiles of the same type, <b>Consolidate</b> those groups:</li>
                <ul>
                <li>Tiles are connected via orthogonal adjacencies. Height doesn't matter.</li>
                <li>Types are coins, strings of coins, myriads, winds, and dragons.</li>
                <li>To consolidate the tiles, flip them all face down.</li>
                <li>This is not optional.</li>      
                <li>Earn points for each set of tiles consolidated:</li>
                    <ul>
                    <li>4 tiles: +2 points.</li>
                    <li>5 tiles: +3 points.</li>
                    <li>6 tiles: +5 points.</li>
                    <li>7 tiles: +6 points.</li>
                    <li>8 tiles: +8 points.</li>
                    <li>For a consolidated group of dragons, Earn +1 bonus point.</li>
                    </ul>
                </ul>  
            <li><b>PYRAMID!:</b> Optionally, you may build pyramids from your reserve on top of tiles you just consolidated:</li>
                <ul>
                <li>The pyramids must be placed on tiles that were consolidated this turn.</li>
                <li>On a consolidated group of coins, strings, or myriads, you may only build one pyramid.</li>
                <li>On a consolidated group of winds or dragons, you may build up to two pyramids.</li>
                <li>When you build a pyramid, earn +1 point if it's on top of the first floor of your castle, +2 points if it's on the second floor, and +3 points if it's on the third floor or higher.</li>
                </ul>
            </ol>

        <li>The game end is triggered after player's have collectively chosen to Summon the Elder Dragon a number of times equal to the number of players. Continue playing until the last play in turn order has gone.</li>
        <li>Most points wins. As a reminder, points are earned by discarding tiles, Summoning the Elder Dragon, consolidating tiles, and building pyramids.</li>
        <li>Ties go to the player with the most stacks which are topped by a face-down tile. After that, ties are broken by the number of pyramids in your castle.</li>
    </div>
    <p class="cardAuthor">traditional game</p>
</div><br>
`)












