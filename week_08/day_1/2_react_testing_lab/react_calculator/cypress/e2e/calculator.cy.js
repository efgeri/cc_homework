describe("Calculator", () => {
  beforeEach(() => {
    cy.visit("http://localhost:3000");
  })

  it('should have working number buttons', () => {
    cy.get('#number2').click();
    cy.get('.display').should('contain', '2')
  })

  it('The number buttons should update the display of the running total', () => {
    cy.get('#number2').click();
    cy.get('#number8').click();
    cy.get('#number1').click();
    cy.get('.display').should('contain', '281')
  })
  
  it('The arithmetical operations should update the display with the result of the operation', () => {
    cy.get('#number2').click();
    cy.get('#number8').click();
    cy.get('#operator-divide').click();
    cy.get('#number4').click();
    cy.get('#operator-equals').click();
    cy.get('.display').should('contain', '7')
  })
  
  it('Should be able to chain multiple operations together', () => {
    cy.get('#number2').click();
    cy.get('#number8').click();
    cy.get('#operator-divide').click();
    cy.get('#number4').click();
    cy.get('#operator_add').click();
    cy.get('#number9').click();
    cy.get('#operator-equals').click();
    cy.get('.display').should('contain', '16')
  })
  
  it('The output should show as expected for positive numbers', () => {
    cy.get('#number2').click();
    cy.get('#operator_add').click();
    cy.get('#number8').click();
    cy.get('#operator-equals').click();
    cy.get('.display').should('contain', '10')
  })

  it('The output should show as expected for negative numbers', () => {
    cy.get('#number2').click();
    cy.get('#operator-subtract').click();
    cy.get('#number8').click();
    cy.get('#operator-equals').click();
    cy.get('.display').should('contain', '-6')
  })

  it('The output should show as expected for decimal numbers', () => {
    cy.get('#number5').click();
    cy.get('#operator-divide').click();
    cy.get('#number2').click();
    cy.get('#operator-equals').click();
    cy.get('.display').should('contain', '2.5')
  })

  it('The output should show as expected for very large numbers', () => {
    cy.get('#number5').click();
    cy.get('#number4').click();
    cy.get('#number1').click();
    cy.get('#number7').click();
    cy.get('#number3').click();
    cy.get('#number2').click();
    cy.get('#number5').click();
    cy.get('#number4').click();
    cy.get('#number1').click();
    cy.get('#number7').click();
    cy.get('#number3').click();
    cy.get('#number2').click();
    cy.get('#operator-multiply').click();
    cy.get('#number2').click();
    cy.get('#number8').click();
    cy.get('#number1').click();
    cy.get('#number3').click();
    cy.get('#number2').click();
    cy.get('#number8').click();
    cy.get('#number1').click();
    cy.get('#number3').click();
    cy.get('#number2').click();
    cy.get('#number8').click();
    cy.get('#number1').click();
    cy.get('#number3').click();
    cy.get('#operator-equals').click();
    cy.get('.display').should('contain', '1.5240460444950414e+23')
  })

  it('Should be able to show error when dividing by zero', () => {
    cy.get('#number8').click();
    cy.get('#operator-divide').click();
    cy.get('#number0').click();
    cy.get('#operator-equals').click();
    cy.get('.display').should('contain', "Error: Can't divide by zero")
  })
  
})