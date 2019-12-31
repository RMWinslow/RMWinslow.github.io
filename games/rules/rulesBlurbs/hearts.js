


document.write(`
<div class="rulesBlock"   style="background-color: hsl(0, 80%, 80%);">
    <div style="float:left;"></div>
    <center>
        <img src="imgs/heart.svg" class="lch">
        <img src="imgs/heart.svg" class="lch">
        <img src="imgs/heart.svg" class="rch">
        <img src="imgs/heart.svg" class="rch">
        <h4 id="hearts">Hearts</h4> 
        <p><i>YET TO PLAY</i></p>
        <p>(2) <a href="tricktaking.html">Trick-Taking</a>. Standard Deck, no Jokers.</p>
    </center>
    <div class="rulesBody"  style="background-color: hsl(0, 100%, 95%)">
        <ul>
        <li>There is no trump suit.</li>
        <li>Each hand, the entire deck is dealt out. 13 cards to each player.</li>
        <li>Each player passes three cards to their left/right/opposite/no-pass. The direction changes each hand.</li>
        <li>Within a hand, hearts cannot be played as lead suit until at least one heart has already been played.</li>
        <li>End-of-hand:</li>
            <ul>
            <li>Earn +1 point for each <b><span style="color:red">♥&#xFE0E;</span></b> card you have taken.
            <li>Earn +13 points for taking <img src="imgs/QS.svg" class="ilc">
            <li><b>Shooting the moon:</b> If you took all 13 <b><span style="color:red">♥&#xFE0E;</span></b>s and the <b><span style="color:black">[Q♠]</span></b>, then instead:
                <ul>
                <li>Earn -26 points, OR</li>
                <li>Give <i>each</i> other player +26 points.</li>
                </ul>
            <li>Game ends if a player now has 100+ points. </li>
            </ul>
        <li>Player with the <i>fewest</i> points wins.</li>
        </ul>
    </div>
</div><br>
`)