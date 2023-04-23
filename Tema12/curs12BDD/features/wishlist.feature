Feature: Test the functionality of the Wishlist page

  #Scenariul 1 - Verificam ca nu avem nici un produs in Wishlist
  Scenario: Check that the Wishlist is empty
    Given I am on the Wishlist page
    Then The Wishlist text is displayed
    Then The Wishlist text contains "The wishlist is empty!"

    #Scenariul 2 - Adaugam un telefon in Wishlist si verificam ca a aparut mesajul de confirmare a adaugarii
  Scenario: Check that the "The product has been added to your wishlist" message is displayed when adding a product to Wishlist
    Given I am on the Cell-Phones page
    Then I add to Wishlist the "HTC One Mini Blue"
    Then The successful adding to Wishlist message is displayed
    Then The successful message contains "The product has been added to your wishlist"

    #Scenariul 3 - Adaugam in telefon in Wishlist si verificam ca el se afla in pagina de Wishlist
  Scenario: Check that a product which was added to Wishlist is actually in the Wishlist
    Given I am on the Cell-Phones page
    Then I add to Wishlist the "HTC One Mini Blue"
    Then I click on "Wishlist" button
    Then I actually am on "https://demo.nopcommerce.com/wishlist"
    Then The "HTC One Mini Blue" is actually in the Wishlist