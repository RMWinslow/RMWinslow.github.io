
document.write(`
<div class="rulesBlock"   style="background-color: hsl(240, 100%, 85%);">
    <center>
        <img src="imgs/D.svg" class="lch">
        <img src="imgs/D.svg" class="lch">
        <img src="imgs/D.svg" class="rch">
        <img src="imgs/D.svg" class="rch">
        <h4 id="diamonds">Diamonds</h4> 
        <p><i>Yet to play. </i></p>
        <p>(3-5) <a href="tricktaking.html">Trick-Taking</a>. <br>Standard Deck, no Jokers, chips, and a bag or cup for each player.</p>
    </center>
    <div class="rulesBody"  style="background-color: hsl(240, 100%, 95%)">
        <ul>
        <li>No trump suit</li>
        <li>Give three chips to each player.</li>
        <li>Each Hand:</li>
            <ul>
            <li>Deal 10 cards to each player.</li>
            <li>Dealer chooses 1/2/3. Each players passes that many cards to their left.</li>
            <li>If a player cannot follow suit, they take a <b>Suit Action</b></li>
            <li>The winner of each trick plays a <b>Suit Action</b></li>
            <li>At the end of the Hand:</li>
                <ul>
                <li>For each suit, the player with the most cards of that suit plays a <b>Suit Action</b>. <i>Ties get no action.</i></li>
                <li>If a player has taken no tricks, they play two <span class="cD">♦&#xFE0E;</span> <b>Suit Actions</b></li>
                </ul>
            </ul>
        <li>Suit Actions are based on the card played:</li>
            <ul>
            <li><span class="cD">♦&#xFE0E;</span>: Place a chip from the supply into your bag.</li>
            <li><span class="cH">♥&#xFE0E;</span>: Take a chip from the supply.</li>
            <li><span class="cS">♠&#xFE0E;</span>: Place one of your chips in your bag.</li>
            <li><span class="cC">♣&#xFE0E;</span>: Steal a chip. <i>(You can't steal bagged chips.)</i></li>
            </ul>
        <li>After a predetermined number of rounds (4/5/6), most chips wins.</li>
        <li>Chips in the bag count as doubled.</li>
        </ul>
    </div>
    <p class="cardAuthor">by Mike Fitzgerald</p>
</div><br>
`)

