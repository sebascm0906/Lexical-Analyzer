def lexer(filepath):
  with open(filepath, 'r') as file:
    expressions = file.read()

  # Tipos de tokens
  TOKEN_TYPES = {
      '+': 'sum',
      '-': 'subtract',
      '*': 'multiply',
      '/': 'division',
      '=': 'assignment',
      '(': 'left parenthesis',
      ')': 'right parenthesis'
  }

  # Tabla de transiciones
  states = {
      0: {
          'letter': 8,
          'digit': 1,
          '=': 3,
          '+': 4,
          '-': 5,
          '*': 6,
          '/': 7,
          '(': 9,
          ')': 10,
          '.': 2
      },
      1: {
          'digit': 1,
          '.': 2
      },
      2: {
          'digit': 2
      },
      3: {},
      4: {},
      5: {},
      6: {},
      7: {},
      8: {
          'letter': 8
      },
      9: {},
      10: {}
  }

  # Initialize variables
  current_state = 0
  current_token = ''

  # Handle tokens
  def handle_token(token):
    if token:
      token_type = TOKEN_TYPES.get(
          token, 'variable'
          if token[0].isalpha() else 'float' if '.' in token else 'integer')
      print(f"{token}\t\t{token_type}")

  # Lexer
  for char in expressions:
    char_type = 'letter' if char.isalpha() else 'digit' if char.isdigit(
    ) else char

    if char_type in states[current_state]:
      current_state = states[current_state][char_type]
      current_token += char
    else:
      handle_token(current_token)
      current_token = ''
      current_state = 0
      if char_type in states[current_state]:
        current_state = states[current_state][char_type]
        current_token += char
        
  # Last token
  handle_token(current_token)


lexer("expressions.txt")