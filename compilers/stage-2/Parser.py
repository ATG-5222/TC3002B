from Lexer import *

class Parser:
	def __init__(self, filepath):
		self.__lex = Lexer(filepath)
		self.__token: Token

		self.__firstPrimaryExpression = set((Tag.ID, Tag.NUMBER, Tag.TRUE, Tag.FALSE, ord('(')))

		self.__firstUnaryExpression = self.__firstPrimaryExpression.union(set((ord('-'), ord('!'))))

		self.__firstExtendedMultiplicativeExpression = set((ord('*'), ord('/'), Tag.MOD))

		self.__firstMultiplicativeExpression = self.__firstUnaryExpression

		self.__firstExtendedAdditiveExpression = set((ord('+'), ord('-')))

		self.__firstExtendedRelationalExpression = set((ord('<'), ord('<='), ord('>'), ord('>=')))

		self.__firstRelationalExpression = self.__firstMultiplicativeExpression

		self.__firstExtendedEqualityExpression = set((ord('='), ord('<>')))

		self.__firstEqualityExpression = self.__firstRelationalExpression

		self.__firstExtendedConditionalTerm = set((Tag.AND,))

		self.__firstConditionalTerm = self.__firstEqualityExpression

		self.__firstExtendedConditionalExpression = set((Tag.OR,))

		self.__firstConditionalExpression = self.__firstConditionalTerm

		self.__firstConditionalStatement = set((Tag.IF, Tag.IFELSE))

		self.__firstRepetitiveStatement = set((Tag.WHILE,))

		self.__firstStructuredStatement = self.__firstConditionalStatement.union(self.__firstRepetitiveStatement)

		self.__firstElement = set((Tag.STRING,)).union(self.__firstConditionalExpression)

		self.__firstExpression = self.__firstConditionalExpression

		self.__firstDrawingStatement = set((Tag.CLEAR, Tag.CIRCLE, Tag.ARC, Tag.PENUP, Tag.PENDOWN, Tag.COLOR, Tag.PENWIDTH))

		self.__firstMovementStatement = set((Tag.FORWARD, Tag.BACKWARD, Tag.LEFT, Tag.RIGHT, Tag.SETX, Tag.SETY, Tag.SETXY, Tag.HOME))

		self.__firstSimpleStatement = set((Tag.VAR, Tag.ID, Tag.PRINT)).union(self.__firstMovementStatement).union(self.__firstDrawingStatement)

		self.__firstStatement = self.__firstSimpleStatement.union(self.__firstStructuredStatement)

		self.__firstStatementSequence = self.__firstStatement

		self.__firstProgram = self.__firstStatementSequence

	def __error(self, extra = None):
		text = 'Line ' + str(self.__lex.getLine()) + " - " 
		if extra == None:
			text = text + "."
		else:
			text = text + extra
		raise Exception(text)

	def __check(self, tag):
		if self.__token.getTag() == tag:
			self.__token = self.__lex.scan()
		else:
			text = 'Line ' + str(self.__lex.getLine()) + " - expected "
			if tag != Tag.ID:
				text = text + str(Token(tag)) + " before " + str(self.__token) 
			else:
				text = text + "an identifier before " + str(self.__token) 
			self.__error(text)

	def analize(self):
		self.__token = self.__lex.scan()
		self.__program()

	def __primaryExpression(self):
		if self.__token.getTag() in self.__firstPrimaryExpression:
			if self.__token.getTag() == Tag.ID:
				self.__check(Tag.ID)
			elif self.__token.getTag() == Tag.NUMBER:
				self.__check(Tag.NUMBER)
			elif self.__token.getTag() == Tag.TRUE:
				self.__check(Tag.TRUE)
			elif self.__token.getTag() == Tag.FALSE:
				self.__check(Tag.FALSE)
			elif self.__token.getTag() == ord('('):
				self.__check(ord('('))
				self.__expression()
				self.__check(ord(')'))
		else:
			self.__error("expected a primary expression before " + str(self.__token))

	def __unaryExpression(self):
		if self.__token.getTag() in self.__firstPrimaryExpression:
			if self.__token.getTag() == ord('-'):
				self.__check(ord('-'))
				self.__unaryExpression()
			elif self.__token.getTag() == ord('!'):
				self.__check(ord('!'))
				self.__unaryExpression()
			else:
				self.__primaryExpression()
		else: 
			self.__error("expected an unary expression before " + str(self.__token))

	def __extendedMultiplicativeExpression(self):
		if self.__token.getTag() in self.__firstExtendedMultiplicativeExpression:
			if self.__token.getTag() == ord('*'):
				self.__check(ord('*'))
				self.__unaryExpression()
				self.__extendedMultiplicativeExpression()
			elif self.__token.getTag() == ord('/'):
				self.__check(ord('/'))
				self.__unaryExpression()
				self.__extendedMultiplicativeExpression()
			elif self.__token.getTag() == Tag.MOD:
				self.__check(Tag.MOD)
				self.__unaryExpression()
				self.__extendedMultiplicativeExpression()
		else:
			pass

	def __multiplicativeExpression(self):
		if self.__token.getTag() in self.__firstMultiplicativeExpression:
			self.__unaryExpression()
			self.__extendedMultiplicativeExpression()
		else:
			self.__error("expected an multiplicative expression before " + str(self.__token))

	def __extendedAdditiveExpression(self):
		if self.__token.getTag() in self.__firstExtendedAdditiveExpression:
			if self.__token.getTag() == ord('+'):
				self.__check(ord('+'))
				self.__multiplicativeExpression()
				self.__extendedAdditiveExpression()
			elif self.__token.getTag() == ord('-'):
				self.__check(ord('-'))
				self.__multiplicativeExpression()
				self.__extendedAdditiveExpression()
		else:
			pass

	def __additiveExpression(self):
		if self.__token.getTag() in self.__firstMultiplicativeExpression:
			self.__multiplicativeExpression()
			self.__extendedAdditiveExpression()
		else:
			self.__error("expected an additive expression before " + str(self.__token))

	def __extendedRelationalExpression(self):
		if self.__token.getTag() in self.__firstExtendedRelationalExpression:
			if self.__token.getTag() == ord('<'):
				self.__check(ord('<'))
				self.__additiveExpression()
				self.__extendedRelationalExpression()
			elif self.__token.getTag() == ord('<='):
				self.__check(ord('<='))
				self.__additiveExpression()
				self.__extendedRelationalExpression()
			elif self.__token.getTag() == ord('>'):
				self.__check(ord('>'))
				self.__additiveExpression()
				self.__extendedRelationalExpression()
			elif self.__token.getTag() == ord('>='):
				self.__check(ord('>='))
				self.__additiveExpression()
				self.__extendedRelationalExpression()
		else:
			pass

	def __relationalExpression(self):
		if self.__token.getTag() in self.__firstAdditiveExpression:
			self.__additiveExpression()
			self.__extendedRelationalExpression()
		else:
			self.__error("expected a relational expression before " + str(self.__token))

	def __extendedEqualityExpression(self):
		if self.__token.getTag() in self.__firstExtendedEqualityExpression:
			if self.__token.getTag() == ord('='):
				self.__check(ord('='))
				self.__relationalExpression()
				self.__extendedEqualityExpression()
			elif self.__token.getTag() == ord('<>'):
				self.__check(ord('<>'))
				self.__relationalExpression()
				self.__extendedEqualityExpression()
		else:
			pass

	def __equalityExpression(self):
		if self.__token.getTag() in self.__firstRelationalExpression:
			self.__relationalExpression()
			self.__extendedEqualityExpression()
		else:
			self.__error("expected an equality expression before " + str(self.__token))

	def __extendedConditionalTerm(self):
		if self.__token.getTag() in self.__firstExtendedConditionalTerm:
			if self.__token.getTag() == Tag.AND:
				self.__check(Tag.AND)
				self.__equalityExpression()
				self.__extendedConditionalTerm()
		else:
			pass

	def __conditionalTerm(self):
		if self.__token.getTag() in self.__firstEqualityExpression:
			self.__equalityExpression()
			self.__extendedConditionalTerm()
		else:
			self.__error("expected a conditional term before " + str(self.__token))

	def __extendedConditionalExpression(self):
		if self.__token.getTag() in self.__firstExtendedConditionalExpression:
			if self.__token.getTag() == Tag.OR:
				self.__check(Tag.OR)
				self.__conditionalTerm()
				self.__extendedConditionalExpression()
		else:
			pass

	def __conditionalExpression(self):
		if self.__token.getTag() in self.__firstConditionalTerm:
			self.__conditionalTerm()
			self.__extendedConditionalExpression()
		else:
			self.__error("expected a conditional expression before " + str(self.__token))

	def __expression(self):
		if self.__token.getTag() in self.__firstConditionalExpression:
			self.__conditionalExpression()
		else:
			self.__error("expected an expression before " + str(self.__token))

	def __ifElseStatement(self):
		if self.__token.getTag() == Tag.IFELSE:
			self.__check(Tag.IFELSE)
			self.__expression()
			self.__check(ord('['))
			self.__statementSequence()
			self.__check(ord(']'))
			self.__check(ord('['))
			self.__statementSequence()
			self.__check(ord(']'))
		else:
			self.__error("expected an IFELSE expression before " + str(self.__token))

	def __ifStatement(self):
		if self.__token.getTag() == Tag.IF:
			self.__check(Tag.IF)
			self.__expression()
			self.__check(ord('['))
			self.__statementSequence()
			self.__check(ord(']'))
		else:
			self.__error("expected an IF expression before " + str(self.__token))

	def __conditionalStatement(self):
		if self.__token.getTag() in self.__firstConditionalStatement:
			if self.__token.getTag() == Tag.IF:
				self.__ifStatement()
			elif self.__token.getTag() == Tag.IFELSE:
				self.__ifElseStatement()
		else:
			self.__error("expected an conditional expression before " + str(self.__token))

	#TODO: Implement __repetitiveStatement
	def __repetitiveStatement(self):
		pass

	def __structuredStatement(self):
		if self.__token.getTag() in self.__firstStructuredStatement:
			if self.__token.getTag() in self.__firstConditionalStatement:
				self.__conditionalStatement()
			elif self.__token.getTag() == Tag.WHILE:
				self.__repetitiveStatement()
		else:
			self.__error("expected an structured expression before " + str(self.__token))

	def __element(self):
		if self.__token.getTag() in self.__firstElement:
			if self.__token.getTag() == Tag.STRING:
				self.__check(Tag.STRING)
			elif self.__token.getTag() in self.__firstExpression:
				self.__expression()
		else:
			self.__error("expected an element expression before " + str(self.__token))

	def __elementList(self):
		if self.__token.getTag() == ord(','):
			self.__check(ord(','))
			self.__element()
			self.__elementList()
		else:
			pass

	def __textStatement(self):
		if self.__token.getTag() == Tag.PRINT:
			self.__check(Tag.PRINT)
			self.__check(ord('('))
			self.__element()
			self.__elementList()
			self.__check(ord(')'))
		else:
			self.__error("expected a PRINT statement before " + str(self.__token))

	def __penWidthStatement(self):
		if self.__token.getTag() == Tag.PENWIDTH:
			self.__check(Tag.PENWIDTH)
			self.__expression()
		else:
			self.__error("expected a PENWIDTH statement before " + str(self.__token))

	def __colorStatement(self):
		if self.__token.getTag() == Tag.COLOR:
			self.__check(Tag.COLOR)
			self.__check(ord('('))
			self.__expression()
			self.__check(ord(','))
			self.__expression()
			self.__check(ord(','))
			self.__expression()
			self.__check(ord(')'))
		else:
			self.__error("expected a COLOR statement before " + str(self.__token))

	def __penDownStatement(self):
		if self.__token.getTag() == Tag.PENDOWN:
			self.__check(Tag.PENDOWN)
			self.__check(ord('('))
			self.__check(ord(')'))
		else:
			self.__error("expected a PENDOWN statement before " + str(self.__token))

	def __penUpStatement(self):
		if self.__token.getTag() == Tag.PENUP:
			self.__check(Tag.PENUP)
			self.__check(ord('('))
			self.__check(ord(')'))
		else:
			self.__error("expected a PENUP statement before " + str(self.__token))

	def __arcStatement(self):
		if self.__token.getTag() == Tag.ARC:
			self.__check(Tag.ARC)
			self.__check(ord('('))
			self.__expression()
			self.__check(ord(','))
			self.__expression()
			self.__check(ord(')'))
		else:
			self.__error("expected a ARC statement before " + str(self.__token))

	def __circleStatement(self):
		if self.__token.getTag() == Tag.CIRCLE:
			self.__check(Tag.CIRCLE)
			self.__expression()
		else:
			self.__error("expected a CIRCLE statement before " + str(self.__token))

	def __clearStatement(self):
		if self.__token.getTag() == Tag.CLEAR:
			self.__check(Tag.CLEAR)
			self.__check(ord('('))
			self.__check(ord(')'))
		else:
			self.__error("expected a CLEAR statement before " + str(self.__token))

	def __drawingStatement(self):
		if self.__token.getTag() in self.__firstDrawingStatement:
			if self.__token.getTag() == Tag.CLEAR:
				self.__clearStatement()
			elif self.__token.getTag() == Tag.CIRCLE:
				self.__circleStatement()
			elif self.__token.getTag() == Tag.ARC:
				self.__arcStatement()
			elif self.__token.getTag() == Tag.PENUP:
				self.__penUpStatement()
			elif self.__token.getTag() == Tag.PENDOWN:
				self.__penDownStatement()
			elif self.__token.getTag() == Tag.COLOR:
				self.__colorStatement()
			elif self.__token.getTag() == Tag.PENWIDTH:
				self.__penWidthStatement()
		else:
			self.__error("expected a drawing statement before " + str(self.__token))

	def _home(self):
		if self.__token.getTag() == Tag.HOME:
			self.__check(Tag.HOME)
			self.__check(ord('('))
			self.__check(ord(')'))	

	def __setXYStatement(self):
		if self.__token.getTag() == Tag.SETXY:
			self.__check(Tag.SETXY)
			self.__check(ord('('))
			self.__expression()
			self.__check(ord(','))
			self.__expression()
			self.__check(ord(')'))
		else:
			self.__error("expected a SETXY statement before " + str(self.__token))

	#TODO: Implement __setXStatement
	def __setXStatement(self):
		pass

	#TODO: Implement __setYStatement
	def __setYStatement(self):
		pass

	#TODO: Implement __leftStatement
	def __leftStatement(self):
		pass

	#TODO: Implement __rightStatement
	def __rightStatement(self):
		pass

	#TODO: Implement __backwardStatement
	def __backwardStatement(self):
		pass

	#TODO: Implement __forwardStatement
	def __forwardStatement(self):
		pass

	#TODO: Implement __movementStatement
	def __movementStatement(self):
		pass

	def __assigmentStatement(self):
		if self.__token.getTag() == Tag.ID:
			self.__check(Tag.ID)
			self.__check(Tag.ASSIGN)
			self.__expression()
		else:
			self.__error("expected an ASSIGMENT statement before " + str(self.__token))

	def __identifierList(self):
		if self.__token.getTag() == ord(','):
			self.__check(ord(','))
			self.__check(Tag.ID)
			self.__identifierList()
		else:
			pass

	def __declarationStatement(self):
		if self.__token.getTag() == Tag.VAR:
			self.__check(Tag.VAR)
			self.__check(Tag.ID)
			self.__identifierList()
		else:
			self.__error("expected a DECLARATION statement before " + str(self.__token))

	def __simpleStatement(self):
		if self.__token.getTag() in self.__firstSimpleStatement:
			if self.__token.getTag() == Tag.VAR:
				self.__declarationStatement()
			elif self.__token.getTag() == Tag.ID:
				self.__assigmentStatement()
			elif self.__token.getTag() in self.__firstMovementStatement:
				self.__movementStatement()
			elif self.__token.getTag() in self.__firstDrawingStatement:
				self.__drawingStatement()
			elif self.__token.getTag() == Tag.PRINT:
				self.__textStatement()
			elif self.__token.getTag() == Tag.HOME:
				self._home()
		else:
			self.__error("expected a simple statement statement before " + str(self.__token))

	def __statement(self):
		if self.__token.getTag() in self.__firstStatement:
			if self.__token.getTag() in self.__firstSimpleStatement:
				self.__simpleStatement()
			elif self.__token.getTag() in self.__firstStructuredStatement:
				self.__structuredStatement()
		else:
			self.__error("expected a statement before " + str(self.__token))

	def __statementSequence(self):
		if self.__token.getTag() in self.__firstStatementSequence:
			self.__statement()
			self.__statementSequence()
		else:
			pass

	def __program(self):
		if self.__token.getTag() in self.__firstProgram:
			self.__declarationStatement()
			self.__statementSequence()
			if self.__token.getTag() != Tag.EOF:
				print(str(self.__token))
				self.__error("ilegal start of a statement")