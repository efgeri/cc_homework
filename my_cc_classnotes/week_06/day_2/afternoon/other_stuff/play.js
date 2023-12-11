const assert = require('assert')

// assert.equal(1, '1')
// Not the best becasue it only checks for ==

// assert.strictEqual([1, 2, 3], [1, 2, 3])
// This will come back as false because these are two differet arrays

assert.deepEqual([1, 2, 3], ['1', '2', '3'])
// This passes because deepequal looks into the value, but it doesn't check the type. It's not strict enough
// Also passes with numbers changed to strings

assert.deepEqual([1, 2, 3], ['1', '2', '3'])
// this is the best