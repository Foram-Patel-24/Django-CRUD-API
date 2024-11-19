import base64

# Your base64 encoded string
encoded_string = """
//5bAA0ACgAgACAAewANAAoAIAAgACAAIAAiAG0AbwBkAGUAbAAiADoAIAAiAFUAcwBlAHIALgB1AHMAZQByACIALAANAAoAIAAgACAAIAAiAHAAawAiADoAIAAxACwADQAKACAAIAAgACAAIgBmAGkAZQBsAGQAcwAiADoAIAB7AA0ACgAgACAAIAAgACAAIAAiAHAAYQBzAHMAdwBvAHIAZAAiADoAIAAiAHAAYgBrAGQAZgAyAF8AcwBoAGEAMgA1ADYAJAA4ADcAMAAwADAAMAAkAGsAMgBIAGgANABhAEIAZwBvAFUARwBWAGkAegAwAGcAOABoAGwAMwB6AHcAJABrAFoAdgAyADIAbABxAEIAVQBKAGQASgBjAEUAdwA2AFQAbwAwAE0AZwBnAGsARABpAFcASQBpAGsAcAAzADAAMgBjAHEAQwBoAFIAbgB2AEEAaQBJAD0AIgAsAA0ACgAgACAAIAAgACAAIAAiAGkAcwBfAHMAdQBwAGUAcgB1AHMAZQByACIAOgAgAA==ZgBhAGwAcwBlACwADQAKACAAIAAgACAAIAAgACIAdQBzAGUAcgBuAGEAbQBlACIAOgAgACIAYQB2AGQAZgBmAGQAZgBkACIALAANAAoAIAAgACAAIAAgACAAIgBmAGkAcgBzAHQAXwBuAGEAbQBlACIAOgAgACIAIgAsAA0ACgAgACAAIAAgACAAIAAiAGwAYQBzAHQAXwBuAGEAbQBlACIAOgAgACIAIgAsAA0ACgAgACAAIAAgACAAIAAiAGkAcwBfAHMAdABhAGYAZgAiADoAIABmAGEAbABzAGUALAANAAoAIAAgACAAIAAgACAAIgBkAGEAdABlAF8AagBvAGkAbgBlAGQAIgA6ACAAIgAyADAAMgA0AC0AMQAxAC0AMQAzAFQAMQAyADoAMQA1ADoANQA2AC4AMgA2ADYAWgAiACwADQAKACAAIAAgACAAIAAgACIAbABhAHMAdABfAA==ZgBhAGwAcwBlACwADQAKACAAIAAgACAAIAAgACIAdQBzAGUAcgBuAGEAbQBlACIAOgAgACIAYQB2AGQAZgBmAGQAZgBkACIALAANAAoAIAAgACAAIAAgACAAIgBmAGkAcgBzAHQAXwBuAGEAbQBlACIAOgAgACIAIgAsAA0ACgAgACAAIAAgACAAIAAiAGwAYQBzAHQAXwBuAGEAbQBlACIAOgAgACIAIgAsAA0ACgAgACAAIAAgACAAIAAiAGkAcwBfAHMAdABhAGYAZgAiADoAIABmAGEAbABzAGUALAANAAoAIAAgACAAIAAgACAAIgBkAGEAdABlAF8AagBvAGkAbgBlAGQAIgA6ACAAIgAyADAAMgA0AC0AMQAxAC0AMQAzAFQAMQAyADoAMQA1ADoANQA2AC4AMgA2ADYAWgAiACwADQAKACAAIAAgACAAIAAgACIAbABhAHMAdABfAA==IgAyADAAMgA0AC0AMQAxAC0AMQAzAFQAMQAyADoAMQA1ADoANQA3AC4AMQA2ADIAWgAiACwADQAKACAAIAAgACAAIAAgACIAZABlAGwAZQB0AGUAZAAiADoAIAAwACwADQAKACAAIAAgACAAIAAgACIAZwByAG8AdQBwAHMAIgA6ACAAWwBdACwADQAKACAAIAAgACAAIAAgACIAdQBzAGUAcgBfAHAAZQByAG0AaQBzAHMAaQBvAG4AcwAiADoAIABbAF0ADQAKACAAIAAgACAAfQANAAoAIAAgAH0ALAANAAoAIAAgAHsADQAKACAAIAAgACAAIgBtAG8AZABlAGwAIgA6ACAAIgBVAHMAZQByAC4AdQBzAGUAcgAiACwAIgAyADAAMgA0AC0AMQAxAC0AMQAzAFQAMQAyADoAMQA1ADoANQA3AC4AMQA2ADIAWgAiACwADQAKACAAIAAgACAAIAAgACIAZABlAGwAZQB0AGUAZAAiADoAIAAwACwADQAKACAAIAAgACAAIAAgACIAZwByAG8AdQBwAHMAIgA6ACAAWwBdACwADQAKACAAIAAgACAAIAAgACIAdQBzAGUAcgBfAHAAZQByAG0AaQBzAHMAaQBvAG4AcwAiADoAIABbAF0ADQAKACAAIAAgACAAfQANAAoAIAAgAH0ALAANAAoAIAAgAHsADQAKACAAIAAgACAAIgBtAG8AZABlAGwAIgA6ACAAIgBVAHMAZQByAC4AdQBzAGUAcgAiACwAbABzAGUALAANAAoAIAAgACAAIAAgACAAIgB1AHMAZQByAG4AYQBtAGUAIgA6ACAAIgBEAEYAIgAsAA0ACgAgACAAIAAgACAAIAAiAGYAaQByAHMAdABfAG4AYQBtAGUAIgA6ACAAIgAiACwADQAKACAAIAAgACAAIAAgACIAbABhAHMAdABfAG4AYQBtAGUAIgA6ACAAIgAiACwADQAKACAAIAAgACAAIAAgACIAaQBzAF8AcwB0AGEAZgBmACIAOgAgAGYAYQBsAHMAZQAsAA0ACgAgACAAIAAgACAAIAAiAGQAYQB0AGUAXwBqAG8AaQBuAGUAZAAiADoAIAAiADIAMAAyADQALQAxADEALQAxADMAVAAxADIAOgAxADYAOgAwADYALgAxADcANgBaACIALAANAAoAIAAgACAAIAAgACAAIgBsAGEAcwB0AF8AbABvAGcAaQBuACIAOgAgAG4AdQBsAGwALAANAAoAIAAgACAAIAAgACAAIgBlAG0AYQBpAGwAIgA6ACAAIgB0AGUAcwB0ADgAOABAAGcAbQBhAGkAbAAuAGMAbwBtACIALAANAAoAIAAgACAAIAAgACAAIgBpAHMAXwBhAGMAdABpAHYAZQAiADoAIABmAGEAbABzAGUALAANAAoAIAAgACAAIAAgACAAIgBzAHQAYQB0AHUAcwAiADoAIAAiAEkAbgBhAGMAdABpAHYAZQAiACwADQAKACAAIAAgACAAIAAgACIAYwByAGUAYQB0AGUAZABfAGEAdAAiADoAIAAiADIAMAAyADQALQAxADEALQAxADMAVAAxADIAOgAxADYAOgAwADYALgA5ADYAMQBaACIALAANAAoAIAAgACAAIAAgACAAIgB1AHAAZABhAHQAZQBkAF8AYQB0ACIAOgAgAA==IgAyADAAMgA0AC0AMQAxAC0AMQA1AFQAMQAwADoAMAAxADoANAA0AC4AMgAxADgAWgAiACwADQAKACAAIAAgACAAIAAgACIAZABlAGwAZQB0AGUAZAAiADoAIAAwACwADQAKACAAIAAgACAAIAAgACIAZwByAG8AdQBwAHMAIgA6ACAAWwBdACwADQAKACAAIAAgACAAIAAgACIAdQBzAGUAcgBfAHAAZQByAG0AaQBzAHMAaQBvAG4AcwAiADoAIABbAF0ADQAKACAAIAAgACAAfQANAAoAIAAgAH0ALAANAAoAIAAgAHsADQAKACAAIAAgACAAIgBtAG8AZABlAGwAIgA6ACAAIgBVAHMAZQByAC4AdQBzAGUAcgAiACwADQAKACAAIAAgACAAIgBwAGsAIgA6ACAAMwAsAA0ACgA=IAAgACAAIAAiAGYAaQBlAGwAZABzACIAOgAgAHsADQAKACAAIAAgACAAIAAgACIAcABhAHMAcwB3AG8AcgBkACIAOgAgACIAcABiAGsAZABmADIAXwBzAGgAYQAyADUANgAkADgANwAwADAAMAAwACQAYwAyAFoARQBHAEsAYwBVAHMAeQBXAHcAZwBUADAAVwBIAFoAeABEAFUATwAkAE8ALwBPADUARABZAHoAZgA2AEkAbQB1AFcATABFADAAZgBIADYAZAAyAFkALwBBAC8AUAB1AFEAWQBKADkASwBsAFIARwBRAFUAMgAyAGwAZQA5AEEAPQAiACwADQAKACAAIAAgACAAIAAgACIAaQBzAF8AcwB1AHAAZQByAHUAcwBlAHIAIgA6ACAAZgBhAA==bABzAGUALAANAAoAIAAgACAAIAAgACAAIgB1AHMAZQByAG4AYQBtAGUAIgA6ACAAIgBEAEYARABFAE8AUgBBADgAOAAiACwADQAKACAAIAAgACAAIAAgACIAZgBpAHIAcwB0AF8AbgBhAG0AZQAiADoAIAAiACIALAANAAoAIAAgACAAIAAgACAAIgBsAGEAcwB0AF8AbgBhAG0AZQAiADoAIAAiACIALAANAAoAIAAgACAAIAAgACAAIgBpAHMAXwBzAHQAYQBmAGYAIgA6ACAAZgBhAGwAcwBlACwADQAKACAAIAAgACAAIAAgACIAZABhAHQAZQBfAGoAbwBpAG4AZQBkACIAOgAgACIAMgAwADIANAAtADEAMQAtADEANABUADAANgA6ADEAOAA6ADAANgAuADAANgAwAFoAIgAsAA0ACgAgACAAIAAgACAAIAAiAGwAYQBzAHQAXwBsAG8=AGcAaQBuACIAOgAgACIAMgAwADIANAAtADEAMQAtADEANABUADAAOAA6ADAAOAA6ADAAMABaACIALAANAAoAIAAgACAAIAAgACAAIgBlAG0AYQBpAGwAIgA6ACAAIgBkAGUAbwByAGEAMAA4ADAAOABAAGcAbQBhAGkAbAAuAGMAbwBtACIALAANAAoAIAAgACAAIAAgACAAIgBpAHMAXwBhAGMAdABpAHYAZQAiADoAIAB0AHIAdQBlACwADQAKACAAIAAgACAAIAAgACIAcwB0AGEAdAB1AHMAIgA6ACAAIgBQAGUAbgBkAGkAbgBnACIALAANAAoAIAAgACAAIAAgACAAIgBjAHIAZQBhAHQAZQBkAF8AYQB0ACIAOgAgACIAMgAwADIANAAtADEAMQAtADEANABUADAANgA6ADEAOAA6ADAANgAuADUAOAA0AFoAIgAsAA0ACgAgACAAIAAgACAAIAAiAHUAcABkAA==YQB0AGUAZABfAGEAdAAiADoAIAAiADIAMAAyADQALQAxADEALQAxADQAVAAwADYAOgAxADgAOgAwADYALgA1ADgANABaACIALAANAAoAIAAgACAAIAAgACAAIgBkAGUAbABlAHQAZQBkACIAOgAgADAALAANAAoAIAAgACAAIAAgACAAIgBnAHIAbwB1AHAAcwAiADoAIABbAF0ALAANAAoAIAAgACAAIAAgACAAIgB1AHMAZQByAF8AcABlAHIAbQBpAHMAcwBpAG8AbgBzACIAOgAgAFsAXQANAAoAIAAgACAAIAB9AA0ACgAgACAAfQANAAoAXQANAAoA
"""

# Decode the base64 string
decoded_bytes = base64.b64decode(encoded_string)

# Convert to string if it's text-based
decoded_string = decoded_bytes.decode('utf-8', errors='ignore')

# Output the decoded string
print(decoded_string)