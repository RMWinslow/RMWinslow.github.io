


document.write(`
<div class="rulesBlock"   style="background-color: hsl(0, 80%, 80%);">
    <center>
        <div id="flex-container">
            <div class="flex-item" >   <img src="imgs/mahjong.svg" >    </div>
            <div class="flex-item" >   <img src="imgs/mahjong.svg" >    </div>
            <div class="flex-title">    
                <h3 id="mahjong">    Mahjong    </h3> 
            </div>
            <div class="flex-item" >   <img src="imgs/mahjong.svg">    </div>
            <div class="flex-item" >   <img src="imgs/mahjong.svg" >    </div>
        </div>

        <p><i>  YET TO PLAY </i></p>
        <p>(2-4) Rummy. Mahjong tiles, dice, chips.</p>
    </center>
    <div class="rulesBody"  style="background-color: hsl(0, 100%, 95%)">
        <ul>
        <li>Use all tiles except the flowers and seasons in the basic game.</li>
        <li>Shuffle the tiles into a wall and deal 13 to each player.</li>
        <li>The goal is to collect patterns of tiles in your hand:</li>
            <ul>
            <li>A <b>Pair</b> consists of 2 identical tiles.</li>
            <li>A <b>Set</b> consists of either 3 identical tiles (called a <b>Pung</b> or <b>Triplet</b>) or a run of 3 sequential tiles from the same suit (called a <b>Chow</b>).</li>
            <li>A <b>Mahjong</b> consists of 1 pair and 4 sets, for a total of 14 tiles. Get a Mahjong to instantly win the round.</li>
            </ul>
        <li>Starting with the dealer as active player, players take turns:</li>
            <ul>
            <li>The active player draws a tile.</li>
            <li>If they have a mahjong, the round immediately ends.</li>
            <li>Otherwise they discard a tile face up to the middle of the table.</li>
            <li>Before the turn ends, players have a chance to claim the most recently discarded tile.</li>
                <ul>
                <li>If the tile completes a mahjong,  call out "Mahjong" and reveal your hand to claim the tile</li>
                <li>If the tile can be use to complete a triplet, call out "Pung" and reveal the other two matching tiles from your hand to claim the tile.</li>
                <li>If the tile could complete a run and <i> you are sitting immediately clockwise of the player who discarded that tile</i>, call out "chow" and reveal the other two tiles in the run to claim the tile.</li>
                <li>If multiple players claim the tile, precedence is Mahjong > Pung > Chow, with ties broken clockwise starting from the active player</li>
                </ul>
            <li>If a player claimed the discarded tile, the turn passes to them, but instead of drawing from the wall, they draw the discarded tile and place it face-up alongside the other pieces of the revealed pattern.  </li>
            <li>If no player claimed the discard tile, the turn passes clockwise.</li>
            </ul>

        <li>After a mahjong is formed, the round ends, and the player with the mahjong earns +1 point.</li>
        <li>It is traditional to play 16 rounds before tallying points.</li>
        <hr>
        <li>Regional scoring variants exist to give bonus points for a mahjong which contains a triplet of dragons or for getting a mahjong without claiming any discards, or ... </li>
        <li>Some games play with an extra set pattern called the <b>Kong</b>, which is a quadruplet of identical tiles. After claiming the discard to complete a Kong, draw one extra tile on your turn before discarding.</li>
        <li>If playing wih flower tiles, you may flip them and draw an extra tile as replacement.</li>
        <li>With fewer than 4 players, place a ghost player in between each actual player. The ghost simply draws and discards a random tile whenever they take a turn, and never claims a discarded tile.</li>
        
        <!--<hr>

        <li>In Zung Jung variant, there are two more patterns that can win the round, in addition to the Mahjong:</li>
            <ul>
            <li>Thirteen Terminals: The hand contains at least one of each dragon, one of each wind, and the ace and nine from all three suits. This makes thirteen tiles, and the fourteenth needs to be a copy of one of these. (Worth 160 points)</li>
            <li>Seven Pairs (30 points)</li>
        <li>Scoring is more complicated: https://www.zungjungmahjong.com/how-to-play-zj/</li>

        </ul>
    </div>
    <p class="cardAuthor">traditional game</p>
</div><br>
`)












