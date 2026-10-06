# Mistvale Assessment AI Prompt Log

## Prompt 1
- Tool: Gemini 3.6 Flash
- Type: code
- Prompt:
  > Audit index.html line by line. Do not change anything. Give me a numbered table: bug | line | why it's wrong | which rule it breaks (R1-R8, constraint, a11y, SEO). Cover cart maths, quantity limits, coupon, shipping, rounding, sold-out sorting, search/filter/sort interaction, async search race conditions, pincode "Checking..." stuck state, localStorage on first
- Outcome: accepted
- Why: Detailed complete line-by-line audit identifying 38 distinct bugs and constraints across the legacy codebase.

## Prompt 2
- Tool: Gemini 3.6 Flash
- Type: code
- Prompt:
  > Implement the complete refactored index.html resolving all audit bugs, enforcing rules R1-R8, checkout contract form, brand design tokens, typography, and SEO schema without external libraries.
- Outcome: modified
- Why: Implemented complete clean vanilla JS/CSS solution and corrected AI search index lookup and cart string concatenation edge cases.
