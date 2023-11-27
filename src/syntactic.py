import derivationTree as dt
from lexicon import Lexer
#from productions import Productions
from firsts import Firsts

class Syntactical:
	def __init__(self, file_path, transition_table) -> None:
		self.lexer = Lexer(file_path, transition_table)
		self.first = Firsts.first
		self.tree = dt.newNode("root", None)

	def analysis(self):
		self.nextToken = self.lexer.get_next_token()
		self.tree = dt.newNode("funcoes", self.tree)
		self.procedure_funcoes()
		return self.tree
		 
	def procedure_funcoes(self):
		if(self.nextToken.name in self.first["funcao"]):
			self.tree.child.append(dt.newNode("funcao", self.tree))
			self.tree = self.tree.child[-1]
			self.procedure_funcao()
			self.tree = self.tree.parent
			if(len(self.tree.child[-1].child) == 0):
				self.tree.child.pop()
			self.tree.child.append(dt.newNode("funcoes'", self.tree))
			self.tree = self.tree.child[-1]
			self.procedure_funcoes_prime()
			self.tree = self.tree.parent
			if(len(self.tree.child[-1].child) == 0):
				self.tree.child.pop()
	
	def procedure_funcoes_prime(self):
		if(self.nextToken == None):
			return
		if(self.nextToken.name in self.first["funcoes"]):
			self.tree.child.append(dt.newNode("funcoes", self.tree))
			self.tree = self.tree.child[-1]
			self.procedure_funcoes()
			self.tree = self.tree.parent
			if(len(self.tree.child[-1].child) == 0):
				self.tree.child.pop()

	def procedure_funcao(self):
		
		if(self.nextToken.name == "program"):
			self.tree.child.append(dt.newNode("program", self.tree))
			self.nextToken = self.lexer.get_next_token()
			if(self.nextToken.name == "id"):
				self.tree.child.append(dt.newNode("id", self.tree))
				self.nextToken = self.lexer.get_next_token()
				if(self.nextToken.name == "("):
					self.tree.child.append(dt.newNode("(", self.tree))
					self.nextToken = self.lexer.get_next_token()
					if(self.nextToken.name == ")"):
						self.tree.child.append(dt.newNode(")", self.tree))
						self.nextToken = self.lexer.get_next_token()
						self.tree.child.append(dt.newNode("bloco", self.tree))
						self.tree = self.tree.child[-1]
						self.procedure_bloco()
						self.tree = self.tree.parent
						if(len(self.tree.child[-1].child) == 0):
							self.tree.child.pop()
					else:
							print("Error: ')' expected")
				else:
						print("Error: '(' expected")
			else:
				print("Error: id expected")
		else:
				print("Error: 'program' expected")

	def procedure_bloco(self):
		if(self.nextToken.name == "begin"):
			self.tree.child.append(dt.newNode("begin", self.tree))
			self.nextToken = self.lexer.get_next_token()
			self.tree.child.append(dt.newNode("variaveis", self.tree))
			self.tree = self.tree.child[-1]
			self.procedure_variaveis()
			self.tree = self.tree.parent
			if(len(self.tree.child[-1].child) == 0):
				self.tree.child.pop()
			self.tree.child.append(dt.newNode("comandos", self.tree))
			self.tree = self.tree.child[-1]
			self.procedure_comandos()
			self.tree = self.tree.parent
			if(len(self.tree.child[-1].child) == 0):
				self.tree.child.pop()
			if(self.nextToken.name == "end"):
				self.tree.child.append(dt.newNode("end", self.tree))
				self.nextToken = self.lexer.get_next_token()
			else:
				print("Error: 'end' expected")
		else:
			print("Error: 'begin' expected")
					

	def procedure_variaveis(self):
		if(self.nextToken.name in self.first["declaracao"]):
			self.tree.child.append(dt.newNode("declaracao", self.tree))
			self.tree = self.tree.child[-1]
			self.procedure_declaracao()
			self.tree = self.tree.parent
			if(len(self.tree.child[-1].child) == 0):
				self.tree.child.pop()
			self.tree.child.append(dt.newNode("variaveis'", self.tree))
			self.tree = self.tree.child[-1]
			self.procedure_variaveis_prime()
			self.tree = self.tree.parent
			if(len(self.tree.child[-1].child) == 0):
				self.tree.child.pop()
	
	def procedure_variaveis_prime(self):
		if(self.nextToken.name in self.first["variaveis"]):
			self.tree.child.append(dt.newNode("variaveis", self.tree))
			self.tree = self.tree.child[-1]
			self.procedure_variaveis()
			self.tree = self.tree.parent
			if(len(self.tree.child[-1].child) == 0):
				self.tree.child.pop()

	def procedure_declaracao(self):
		if(self.nextToken.name == "tipo"):
			self.tree.child.append(dt.newNode("tipo", self.tree))
			self.nextToken = self.lexer.get_next_token()
			if(self.nextToken.name == ":"):
				self.tree.child.append(dt.newNode(":", self.tree))
				self.nextToken = self.lexer.get_next_token()
				self.tree.child.append(dt.newNode("ids", self.tree))
				self.tree = self.tree.child[-1]
				self.procedure_ids()
				self.tree = self.tree.parent
				if(len(self.tree.child[-1].child) == 0):
					self.tree.child.pop()
				if(self.nextToken.name == ";"):
					self.tree.child.append(dt.newNode(";", self.tree))
					self.nextToken = self.lexer.get_next_token()
				else:
					print("Error: ';' expected")
			else:
				print("Error: ':' expected")
		else:
			print("Error: type expected")

	def procedure_ids(self):
		if(self.nextToken.name == "id"):
			self.tree.child.append(dt.newNode("id", self.tree))
			self.nextToken = self.lexer.get_next_token()
			self.tree.child.append(dt.newNode("ids'", self.tree))
			self.tree = self.tree.child[-1]
			self.procedure_ids_prime()
			self.tree = self.tree.parent
			if(len(self.tree.child[-1].child) == 0):
				self.tree.child.pop()
		else:
			print("Error: id expected")

	def procedure_ids_prime(self):

		if(self.nextToken.name == ","):
			self.tree.child.append(dt.newNode(",", self.tree))
			self.nextToken = self.lexer.get_next_token()
			self.procedure_ids()

	def procedure_comando(self):
		if(self.nextToken.name in self.first["atribuicao"]):
			self.tree.child.append(dt.newNode("atribuicao", self.tree))
			self.tree = self.tree.child[-1]
			self.procedure_atribuicao()
			self.tree = self.tree.parent
			if(len(self.tree.child[-1].child) == 0):
				self.tree.child.pop()
		elif(self.nextToken.name in self.first["enquanto"]):
			self.tree.child.append(dt.newNode("enquanto", self.tree))
			self.tree = self.tree.child[-1]
			self.procedure_enquanto()
			self.tree = self.tree.parent
			if(len(self.tree.child[-1].child) == 0):
				self.tree.child.pop()
		elif(self.nextToken.name in self.first["repeticao"]):
			self.tree.child.append(dt.newNode("repeticao", self.tree))
			self.tree = self.tree.child[-1]
			self.procedure_repeticao()
			self.tree = self.tree.parent
			if(len(self.tree.child[-1].child) == 0):
				self.tree.child.pop()
		elif(self.nextToken.name in self.first["controle"]):
			self.tree.child.append(dt.newNode("controle", self.tree))
			self.tree = self.tree.child[-1]
			self.procedure_controle()
			self.tree = self.tree.parent
			if(len(self.tree.child[-1].child) == 0):
				self.tree.child.pop()
		else:
			print("atribution, while, repetition or control block excpected")

	def procedure_comandos(self):
		if(self.nextToken.name in self.first["comando"]):
			self.tree.child.append(dt.newNode("comando", self.tree))
			self.tree = self.tree.child[-1]
			self.procedure_comando()
			self.tree = self.tree.parent
			if(len(self.tree.child[-1].child) == 0):
				self.tree.child.pop()
			self.tree.child.append(dt.newNode("comandos", self.tree))
			self.tree = self.tree.child[-1]
			self.procedure_comandos()
			self.tree = self.tree.parent
			if(len(self.tree.child[-1].child) == 0):
				self.tree.child.pop()

	def procedure_atribuicao(self):
		if(self.nextToken.name == "id"):
			self.tree.child.append(dt.newNode("id", self.tree))
			self.nextToken = self.lexer.get_next_token()
			if(self.nextToken.name == ":="):
				self.tree.child.append(dt.newNode(":=", self.tree))
				self.nextToken = self.lexer.get_next_token()
				self.tree.child.append(dt.newNode("expressao", self.tree))
				self.tree = self.tree.child[-1]
				self.procedure_expressao()
				self.tree = self.tree.parent
				if(len(self.tree.child[-1].child) == 0):
					self.tree.child.pop()
				if(self.nextToken.name == ";"):
					self.tree.child.append(dt.newNode(";", self.tree))
					self.nextToken = self.lexer.get_next_token()
			else:
				print("error: ':=' expected")
		else:
			print("error: id expected")

	def procedure_comando_bloco(self):
		if(self.nextToken.name in self.first["comando"]):
			self.tree.child.append(dt.newNode("comando", self.tree))
			self.tree = self.tree.child[-1]
			self.procedure_comando()
			self.tree = self.tree.parent
			if(len(self.tree.child[-1].child) == 0):
				self.tree.child.pop()
		elif(self.nextToken.name in self.first["bloco"]):
			self.tree.child.append(dt.newNode("bloco", self.tree))
			self.tree = self.tree.child[-1]
			self.procedure_bloco()
			self.tree = self.tree.parent
			if(len(self.tree.child[-1].child) == 0):
				self.tree.child.pop()
		else:
			print("Error: expected block or command")

	def procedure_condicao(self):
		if(self.nextToken.name in self.first["expressao"]):
			self.tree.child.append(dt.newNode("expressao", self.tree))
			self.tree = self.tree.child[-1]
			self.procedure_expressao()
			self.tree = self.tree.parent
			if(len(self.tree.child[-1].child) == 0):
				self.tree.child.pop()
			if(self.nextToken.name == "op_rel"):
				self.tree.child.append(dt.newNode("op_rel", self.tree))
				self.nextToken = self.lexer.get_next_token()
				self.tree.child.append(dt.newNode("expressao", self.tree))
				self.tree = self.tree.child[-1]
				self.procedure_expressao()
				self.tree = self.tree.parent
				if(len(self.tree.child[-1].child) == 0):
					self.tree.child.pop()
			else:
				print("error: relational operator expected")
		else:
			print("error: expression expected")

	def procedure_controle(self):
		if(self.nextToken.name == "if"):
			self.tree.child.append(dt.newNode("if", self.tree))
			self.nextToken = self.lexer.get_next_token()
			self.tree.child.append(dt.newNode("condicao", self.tree))
			self.tree = self.tree.child[-1]
			self.procedure_condicao()
			self.tree = self.tree.parent
			if(len(self.tree.child[-1].child) == 0):
				self.tree.child.pop()
			if(self.nextToken.name == "then"):
				self.tree.child.append(dt.newNode("then", self.tree))
				self.nextToken = self.lexer.get_next_token()
				self.tree.child.append(dt.newNode("bloco", self.tree))
				self.tree = self.tree.child[-1]
				self.procedure_comando_bloco()
				self.tree = self.tree.parent
				if(len(self.tree.child[-1].child) == 0):
					self.tree.child.pop()
				self.tree.child.append(dt.newNode("controle'", self.tree))
				self.tree = self.tree.child[-1]
				self.procedure_controle_prime()
				self.tree = self.tree.parent
				if(len(self.tree.child[-1].child) == 0):
					self.tree.child.pop()

	def procedure_controle_prime(self):
		if(self.nextToken.name == "else"):
			self.tree.child.append(dt.newNode("else", self.tree))
			self.nextToken = self.lexer.get_next_token()
			self.tree.child.append(dt.newNode("comando_bloco", self.tree))
			self.tree = self.tree.child[-1]
			self.procedure_comando_bloco()
			self.tree = self.tree.parent
			if(len(self.tree.child[-1].child) == 0):
				self.tree.child.pop()

	def procedure_enquanto(self):
		if(self.nextToken.name == "while"):
			self.tree.child.append(dt.newNode("while", self.tree))
			self.nextToken = self.lexer.get_next_token()
			self.tree.child.append(dt.newNode("condicao", self.tree))
			self.tree = self.tree.child[-1]
			self.procedure_condicao()
			self.tree = self.tree.parent
			if(len(self.tree.child[-1].child) == 0):
				self.tree.child.pop()
			self.tree.child.append(dt.newNode("comando_bloco", self.tree))
			self.tree = self.tree.child[-1]
			self.procedure_comando_bloco()
			self.tree = self.tree.parent
			if(len(self.tree.child[-1].child) == 0):
				self.tree.child.pop()

	def procedure_repeticao(self):
		if(self.nextToken.name == "repeat"):
			self.tree.child.append(dt.newNode("repeat", self.tree))
			self.nextToken = self.lexer.get_next_token()
			self.tree.child.append(dt.newNode("comando_bloco", self.tree))
			self.tree = self.tree.child[-1]
			self.procedure_comando_bloco()
			self.tree = self.tree.parent
			if(len(self.tree.child[-1].child) == 0):
				self.tree.child.pop()
			if(self.nextToken.name == "until"):
				self.tree.child.append(dt.newNode("until", self.tree))
				self.nextToken = self.lexer.get_next_token()
				self.tree.child.append(dt.newNode("condicao", self.tree))
				self.tree = self.tree.child[-1]
				self.procedure_condicao()
				self.tree = self.tree.parent
				if(len(self.tree.child[-1].child) == 0):
					self.tree.child.pop()
				if(self.nextToken.name == ";"):
					self.tree.child.append(dt.newNode(";", self.tree))
					self.nextToken = self.lexer.get_next_token()
				else:
					print("; expected")
			else:
				print("until expected")
		else:
			print("repeat expected")
	def procedure_expressao(self):
		if(self.nextToken.name in self.first["expressao_p2"]):
			self.tree.child.append(dt.newNode("expressao_p2", self.tree))
			self.tree = self.tree.child[-1]
			self.procedure_expressao_p2()
			self.tree = self.tree.parent
			if(len(self.tree.child[-1].child) == 0):
				self.tree.child.pop()
			self.tree.child.append(dt.newNode("expressao'", self.tree))
			self.tree = self.tree.child[-1]
			self.procedure_expressao_prime()
			self.tree = self.tree.parent
			if(len(self.tree.child[-1].child) == 0):
				self.tree.child.pop()
		else:
			print('Error: expressao esperada')

	def procedure_expressao_prime(self):
		if(self.nextToken.name == "+"):
			self.tree.child.append(dt.newNode("+", self.tree))
			self.nextToken = self.lexer.get_next_token()
			self.tree.child.append(dt.newNode("expressao_p2", self.tree))
			self.tree = self.tree.child[-1]
			self.procedure_expressao_p2()
			self.tree = self.tree.parent
			if(len(self.tree.child[-1].child) == 0):
				self.tree.child.pop()
			self.tree.child.append(dt.newNode("expressao'", self.tree))
			self.tree = self.tree.child[-1]
			self.procedure_expressao_prime()
			self.tree = self.tree.parent
			if(len(self.tree.child[-1].child) == 0):
				self.tree.child.pop()
		elif(self.nextToken.name == "-"):
			self.tree.child.append(dt.newNode("-", self.tree))
			self.nextToken = self.lexer.get_next_token()
			self.tree.child.append(dt.newNode("expressao_p2", self.tree))
			self.tree = self.tree.child[-1]
			self.procedure_expressao_p2()
			self.tree = self.tree.parent
			if(len(self.tree.child[-1].child) == 0):
				self.tree.child.pop()
			self.tree.child.append(dt.newNode("expressao'", self.tree))
			self.tree = self.tree.child[-1]
			self.procedure_expressao_prime()
			self.tree = self.tree.parent
			if(len(self.tree.child[-1].child) == 0):
				self.tree.child.pop()

	def procedure_expressao_p2(self):
		if(self.nextToken.name in self.first["expressao_p3"]):
			self.tree.child.append(dt.newNode("expressao_p3", self.tree))
			self.tree = self.tree.child[-1]
			self.procedure_expressao_p3()
			self.tree = self.tree.parent
			if(len(self.tree.child[-1].child) == 0):
				self.tree.child.pop()
			self.tree.child.append(dt.newNode("expressao_p2'", self.tree))
			self.tree = self.tree.child[-1]
			self.procedure_expressao_p2_prime()
			self.tree = self.tree.parent
			if(len(self.tree.child[-1].child) == 0):
				self.tree.child.pop()
		else:
			print('Error: expressao esperada')

	def procedure_expressao_p2_prime(self):
		if(self.nextToken.name == "*"):
			self.tree.child.append(dt.newNode("*", self.tree))
			self.nextToken = self.lexer.get_next_token()
			self.tree.child.append(dt.newNode("expressao_p3", self.tree))
			self.tree = self.tree.child[-1]
			self.procedure_expressao_p3()
			self.tree = self.tree.parent
			if(len(self.tree.child[-1].child) == 0):
				self.tree.child.pop()
			self.tree.child.append(dt.newNode("expressao_p2'", self.tree))
			self.tree = self.tree.child[-1]
			self.procedure_expressao_p2_prime()
			self.tree = self.tree.parent
			if(len(self.tree.child[-1].child) == 0):
				self.tree.child.pop()
		elif(self.nextToken.name == "/"):
			self.tree.child.append(dt.newNode("/", self.tree))
			self.nextToken = self.lexer.get_next_token()
			self.tree.child.append(dt.newNode("expressao_p3", self.tree))
			self.tree = self.tree.child[-1]
			self.procedure_expressao_p3()
			self.tree = self.tree.parent
			if(len(self.tree.child[-1].child) == 0):
				self.tree.child.pop()
			self.tree.child.append(dt.newNode("expressao_p2'", self.tree))
			self.tree = self.tree.child[-1]
			self.procedure_expressao_p2_prime()
			self.tree = self.tree.parent
			if(len(self.tree.child[-1].child) == 0):
				self.tree.child.pop()

	def procedure_expressao_p3(self):
		if(self.nextToken.name in self.first["expressao_p3"]):
			self.tree.child.append(dt.newNode("expressao_p4", self.tree))
			self.tree = self.tree.child[-1]
			self.procedure_expressao_p4()
			self.tree = self.tree.parent
			if(len(self.tree.child[-1].child) == 0):
				self.tree.child.pop()
			self.tree.child.append(dt.newNode("expressao_p3'", self.tree))
			self.tree = self.tree.child[-1]
			self.procedure_expressao_p3_prime()
			self.tree = self.tree.parent
			if(len(self.tree.child[-1].child) == 0):
				self.tree.child.pop()
		else:
			print('Error: expressao esperada')

	def procedure_expressao_p3_prime(self):
		if(self.nextToken.name == "^"):
			self.tree.child.append(dt.newNode("^", self.tree))
			self.nextToken = self.lexer.get_next_token()
			self.tree.child.append(dt.newNode("expressao_p4", self.tree))
			self.tree = self.tree.child[-1]
			self.procedure_expressao_p4()
			self.tree = self.tree.parent
			if(len(self.tree.child[-1].child) == 0):
				self.tree.child.pop()
			self.tree.child.append(dt.newNode("expressao_p3'", self.tree))
			self.tree = self.tree.child[-1]
			self.procedure_expressao_p3_prime()
			self.tree = self.tree.parent
			if(len(self.tree.child[-1].child) == 0):
				self.tree.child.pop()

	def procedure_expressao_p4(self):
		if(self.nextToken.name == "id"):
			self.tree.child.append(dt.newNode("id", self.tree))
			self.nextToken = self.lexer.get_next_token()
		elif(self.nextToken.name == "number"):
			self.tree.child.append(dt.newNode("number", self.tree))
			self.nextToken = self.lexer.get_next_token()
		elif(self.nextToken.name == "char"):
			self.tree.child.append(dt.newNode("char", self.tree))
			self.nextToken = self.lexer.get_next_token()
		elif(self.nextToken.name == "("):
			self.tree.child.append(dt.newNode("(", self.tree))
			self.nextToken = self.lexer.get_next_token()
			self.tree.child.append(dt.newNode("expressao", self.tree))
			self.tree = self.tree.child[-1]
			self.procedure_expressao()
			self.tree = self.tree.parent
			if(len(self.tree.child[-1].child) == 0):
				self.tree.child.pop()
			if(self.nextToken.name == ")"):
				self.tree.child.append(dt.newNode(")", self.tree))
				self.nextToken = self.lexer.get_next_token()
			else:
				print("Error: ')' expected. Good luck")
		elif(self.nextToken.name == "-"):
			self.tree.child.append(dt.newNode("-", self.tree))
			self.nextToken = self.lexer.get_next_token()
			self.tree.child.append(dt.newNode("expressao_p4", self.tree))
			self.tree = self.tree.child[-1]
			self.procedure_expressao_p4()
			self.tree = self.tree.parent
			if(len(self.tree.child[-1].child) == 0):
				self.tree.child.pop()
		else:
			print("Error: 'id' or 'int' or 'float' or 'char' or '(' or '-' expected.")
