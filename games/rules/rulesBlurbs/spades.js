
document.write(`
<div class="rulesBlock"   style="background-color: hsl(0, 0%, 50%);">
    <center>
        <img src="imgs/S.svg" class="lch">
        <img src="imgs/S.svg" class="lch">
        <img src="imgs/S.svg" class="rch">
        <img src="imgs/S.svg" class="rch">
        <h4 id="spades">Spades</h4> 
        <p><i>Brother's favorite card game.</i></p>
        <p>(4) <a href="tricktaking.html">Trick-Taking</a>. Standard Deck, no Jokers.</p>
    </center>
    <div class="rulesBody"  style="background-color: hsl(0, 0%, 80%)">
        <ul>
        <li>2 teams of 2. Each person sits across from their teammate.</li>
        <li>Spades are always the trump suit.</li>
        <li>Each hand, the entire deck is dealt out. 13 cards to each player.</li>
        <li>Each player bids how many tricks they think they will take. Teammate's bids are combined.</li>
        <li>Within a hand, spades cannot be played as lead suit until at least one spade has already been played.</li>
        <li>End-of-hand scoring:</li>
            <ul>
            <li>If team's bid is met or exceeded: +10×[bid]</li>
            <li>If team's bid is not met: -10×[bid]</li>
            <li>For each trick taken in excess of team bid: +1 point and +1 <b>bag</b>:</li>
                <ul>
                <li>Bags accumulate across hands.</li>
                <li>Every 7th bag results in -100 points.</li>
                </ul>
            <li>Special case: If a player bids 0</li>
                <ul>
                    <li>Any tricks that player earns are counted as bags instead of contributing to their teams total.</li>
                    <li>If that player takes exactly 0 tricks, their team earns +100 points</li>
                </ul>
            <li>Special Case: <b>Shooting the Moon.</b> If a team bids 13 and succeeds, they earn +200 points instead of +130</li>
            </ul>
        <li>First team to 300 points wins.</li> 
        </ul>
    </div>
</div><br>
`)

