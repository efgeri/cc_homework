import React from 'react';
import Calculator from '../containers/Calculator';
import {render, fireEvent} from '@testing-library/react';

describe('Calculator', () => {
  let container;
  let addButton
  let button1
  let button2
  let button3
  let button5
  let button4
  let button7
  let equalButton
  let subtractButton
  let multiplyButton
  let divideButton
  let runningTotal
  let clearButton
  beforeEach(() => {
    container = render(<Calculator/>)
    addButton = container.getByTestId('operator-add');
    button1 = container.getByTestId('number1');
    button2 = container.getByTestId('number2');
    button3 = container.getByTestId('number3');
    button5 = container.getByTestId('number5');
    button4 = container.getByTestId('number4');
    button7 = container.getByTestId('number7');
    equalButton = container.getByTestId('operator-equals');
    subtractButton = container.getByTestId('operator-subtract');
    multiplyButton = container.getByTestId('operator-multiply');
    divideButton = container.getByTestId('operator-divide');
    runningTotal = container.getByTestId('running-total');
    clearButton = container.getByTestId('clear');
  })

  it('should change running total on number enter', () => {
    fireEvent.click(button4);
    expect(runningTotal.textContent).toEqual('4');
  })

  it('should be able to add two numbers together', () => {
    fireEvent.click(button1);
    fireEvent.click(addButton);
    fireEvent.click(button4);
    fireEvent.click(equalButton);
    expect(runningTotal.textContent).toEqual('5');
  })

  it('should be able to subtract', () => {
    fireEvent.click(button7);
    fireEvent.click(subtractButton);
    fireEvent.click(button4);
    fireEvent.click(equalButton);
    expect(runningTotal.textContent).toEqual('3');
  })

  it('should be able to multiply', () => {
    fireEvent.click(button3);
    fireEvent.click(multiplyButton);
    fireEvent.click(button5);
    fireEvent.click(equalButton);
    expect(runningTotal.textContent).toEqual('15');
  })

  it('should be able to divide', () => {
    fireEvent.click(button2);
    fireEvent.click(button1);
    fireEvent.click(divideButton);
    fireEvent.click(button7);
    fireEvent.click(equalButton);
    expect(runningTotal.textContent).toEqual('3');
  })

  it('should be able to concatenate multiple number button clicks', () => {
    fireEvent.click(button7);
    fireEvent.click(button2);
    fireEvent.click(button1);
    fireEvent.click(button3);
    fireEvent.click(button5);
    expect(runningTotal.textContent).toEqual('72135');
  })

  it('should be able to chain multiple operations together', () => {
    fireEvent.click(button2);
    fireEvent.click(button1);
    fireEvent.click(divideButton);
    fireEvent.click(button7);
    fireEvent.click(multiplyButton);
    fireEvent.click(button3);
    fireEvent.click(subtractButton);
    fireEvent.click(button2);    
    fireEvent.click(equalButton);
    expect(runningTotal.textContent).toEqual('7');
  })

  it('should be able to clear the running total without affecting the calculation', () => {
    fireEvent.click(button4);
    fireEvent.click(multiplyButton);
    fireEvent.click(button5);
    fireEvent.click(divideButton);
    fireEvent.click(button2);
    fireEvent.click(equalButton);
    fireEvent.click(clearButton);
    fireEvent.click(addButton);
    fireEvent.click(button3);
    fireEvent.click(equalButton);    
    expect(runningTotal.textContent).toEqual('13');
  })
})

