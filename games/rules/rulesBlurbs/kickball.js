


document.write(`
<div class="rulesBlock"   style="background-color: hsl(0, 100%, 80%);">
    <center>
        <h3 id="kickball">Kickball</h3> 
        <p><i>Symetric Do Dizhu.</i></p>
        <p>(4) Climbing Game. Poker Deck, no Jokers.</p>
    </center>
    <div class="rulesBody"  style="">
        <ul>
        <li>Teammates sit across from each other.</li>
        <li>Deal 13 cards to each player.</li>
        <li>After dealing, a player can <b>boast</b> that they will go out first.</li> 
        <li>Person with <span class="cC">3♣&#xFE0E;</span> leads first.</li>
        <li>Scoring at the end of each hand:</li>
            <ul>
            <li>+100 points for a sucessful boast. -100 for a failed boast.</li>
            <li>If both members of a team went out before either member of the other, </li>
                <ul><li>then +200 points for that team.</li></ul>
            <li>Otherwise, </li>
                <ul>
                <li>The last to go out gives the rest of their hand to the other team.</li>
                <li>The last to go out gives their <i>taken</i> cards to the first to go out.</li>
                <li>Each team scores +5 points for each taken <span class="card">5</span>, +10 for each <span class="card">10</span>, and +10 for each <span class="card">K</span>.
                </ul>
            </ul>

    </div>
    <p class="cardAuthor">variant with scoring taken from "Tichu", by Urs Hostettler</p>
</div><br>
`)