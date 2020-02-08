


document.write(`
<div class="rulesBlock"   style="background-color: hsl(330, 80%, 85%);">
    
    <center>

    <div id="flex-container">
        <div class="flex-item">   <img src="imgs/twemojiDNA.svg" >    </div>
        <div class="flex-item">   <img src="imgs/twemojiDNA.svg" >    </div>
        <div class="flex-item">   <img src="imgs/twemojiDNA.svg" >    </div>
        <div class="flex-title">    
            <h4 id="lamarckian">    Lamarckian Poker    </h4> 
            <p><i>  Dad is freakishly good at this. </i></p>
        </div>
        <div class="flex-item">   <img src="imgs/twemojiDNA.svg">    </div>
        <div class="flex-item">   <img src="imgs/twemojiDNA.svg" >    </div>
        <div class="flex-item">   <img src="imgs/twemojiDNA.svg" >    </div>
    </div>

    <p>(3-6) <a href="poker.html">Poker Hands</a>. Poker deck, no jokers.</p>

    </center>
    <div class="rulesBody"  style="background-color: hsl(240, 100%, 95%)">
        <ul>
        <li>Deal 4 cards to each player.</li>
        <li>Each turn:</li>
            <ul>
            <li>Flip four cards from the deck into a pool.</li>
            <li>Each player plays a card from their hand, face down, and reveals simultaneously.</li>
            <li>In order from highest played card to lowest, each player:</li>
                <ul>
                <li>Takes all cards from the pool that match the rank or suit of their card.</li>
                <li>Places their card into the pool.</li>
                </ul>
            <li>All cards left in the pool are discarded.</li>
            </ul>
        <li>Turns continue until the deck runs out.</li>
        <li>Players use the cards in their hand to form a single poker hand of 5 cards.</li>
        </ul>
    </div>
    <p class="cardAuthor">by James Ernest and Dave Howel</p>
</div><br>
`)






