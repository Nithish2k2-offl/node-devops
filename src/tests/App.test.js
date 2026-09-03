import { describe, it, expect } from 'vitest';

// 1. The function we want to test (or import it from another file)
function add(a, b) {
  return a + b;
}

// 2. The Test Suite
describe('add() function', () => {
  
  it('should correctly add two positive numbers', () => {
    // Act
    const result = add(2, 3);
    
    // Assert
    expect(result).toBe(5);
  });

  it('should return a negative number when adding two negative numbers', () => {
    const result = add(-2, -3);
    expect(result).toBe(-5);
  });
  
});
