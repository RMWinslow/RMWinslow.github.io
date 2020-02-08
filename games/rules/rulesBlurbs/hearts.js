


document.write(`
<div class="rulesBlock"   style="background-color: hsl(0, 80%, 80%);">
    <center>
        <div id="flex-container">
            <div class="flex-item" >   <img src="imgs/H.svg" >    </div>
            <div class="flex-item" >   <img src="imgs/H.svg" >    </div>
            <div class="flex-title">    
                <h3 id="hearts">    Hearts    </h3> 
            </div>
            <div class="flex-item" >   <img src="imgs/H.svg">    </div>
            <div class="flex-item" >   <img src="imgs/H.svg" >    </div>
        </div>

        <p><i>  YET TO PLAY </i></p>
        <p>(4) <a href="tricktaking.html">Trick-Taking</a>. Poker Deck, no Jokers.</p>
    </center>
    <div class="rulesBody"  style="background-color: hsl(0, 100%, 95%)">
        <ul>
        <li>There is no trump suit.</li>
        <li>Each hand, the entire deck is dealt out. 13 cards to each player.</li>
        <li>Each player passes three cards to their left/right/opposite/no-pass. The direction changes each hand.</li>
        <li>Within a hand, hearts cannot be played as lead suit until at least one heart has already been played.</li>
        <li>End-of-hand:</li>
            <ul>
            <li>Earn +1 point for each <span class="cH">♥&#xFE0E;</span> card you have taken.
            <li>Earn +13 points for taking <span class="cS">Q♠&#xFE0E;</span>
            <li><b>Shooting the moon:</b> If you took all 13 <span class="cH">♥&#xFE0E;</span>s and the 
            <span class="cS">Q♠&#xFE0E;</span>, then instead:
                <ul>
                <li>Earn -26 points, OR</li>
                <li>Give <i>each</i> other player +26 points.</li>
                </ul>
            <li>Game ends if a player now has 100+ points. </li>
            </ul>
        <li>Player with the <i>fewest</i> points wins.</li>
        </ul>
    </div>
    <p class="cardAuthor">traditional game</p>
</div><br>
`)












