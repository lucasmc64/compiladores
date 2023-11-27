import derivationTree
from lexicon import Lexer
#from productions import Productions
from firsts import Firsts

class Syntactical:
	def __init__(self, file_path, transition_table) -> None:
		self.lexer = Lexer(file_path, transition_table)
		self.first = Firsts.first

	def analysis(self):
		self.nextToken = self.lexer.get_next_token()
		self.procedure_funcoes()
		 
	def procedure_funcoes(self):
		if(self.nextToken.name in self.first["funcao"]):
			self.procedure_funcao()
			self.procedure_funcoes_prime()
	
	def procedure_funcoes_prime(self):
		if(self.nextToken.name in self.first["funcoes"]):
				self.procedure_funcoes()

	def procedure_funcao(self):
		if(self.nextToken.name == "program"):
			self.nextToken = self.lexer.get_next_token()
			if(self.nextToken.name == "id"):
				self.nextToken = self.lexer.get_next_token()
				if(self.nextToken.name == "("):
					self.nextToken = self.lexer.get_next_token()
					if(self.nextToken.name == ")"):
						self.nextToken = self.lexer.get_next_token()
						self.procedure_bloco()
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
			self.nextToken = self.lexer.get_next_token()
			self.procedure_variaveis()
			self.procedure_comandos()
			if(self.nextToken.name == "end"):
				self.nextToken = self.lexer.get_next_token()
			else:
				print("Error: 'end' expected")
		else:
			print("Error: 'begin' expected")
					

	def procedure_variaveis(self):
		if(self.nextToken.name in self.first["declaracao"]):
			self.procedure_declaracao()
			self.procedure_variaveis()
	
	def procedure_variaveis_prime(self):
		if(self.nextToken.name in self.first["variaveis"]):
			self.procedure_variaveis()

	def procedure_declaracao(self):
		if(self.nextToken.name == "tipo"):
			self.nextToken = self.lexer.get_next_token()
			if(self.nextToken.name == ":"):
				self.nextToken = self.lexer.get_next_token()
				self.procedure_ids()
				if(self.nextToken.name == ";"):
					self.nextToken = self.lexer.get_next_token()
				else:
					print("Error: ';' expected")
			else:
				print("Error: ':' expected")
		else:
			print("Error: type expected")

	def procedure_ids(self):
		if(self.nextToken.name == "id"):
			self.nextToken = self.lexer.get_next_token()
			self.procedure_ids_prime()
		else:
			print("Error: id expected")

	def procedure_ids_prime(self):

		if(self.nextToken.name == ","):
			self.nextToken = self.lexer.get_next_token()
			self.procedure_ids()

	def procedure_comando(self):
		if(self.nextToken.name in self.first["atribuicao"]):
			self.procedure_atribuicao()
		elif(self.nextToken.name in self.first["enquanto"]):
			self.procedure_enquanto()
		elif(self.nextToken.name in self.first["repeticao"]):
			self.procedure_repeticao()
		elif(self.nextToken.name in self.first["controle"]):
			self.procedure_controle()
		else:
			print("atribution, while, repetition or control block excpected")

	def procedure_comandos(self):
		if(self.nextToken.name in self.first["comando"]):
			self.procedure_comando()
			self.procedure_comandos()

	def procedure_atribuicao(self):
		if(self.nextToken.name == "id"):
			self.nextToken = self.lexer.get_next_token()
			if(self.nextToken.name == ":="):
				self.nextToken = self.lexer.get_next_token()
				self.procedure_expressao()
				if(self.nextToken.name == ";"):
					self.nextToken = self.lexer.get_next_token()
			else:
				print("error: ':=' expected")
		else:
			print("error: id expected")

	def procedure_comando_bloco(self):
		if(self.nextToken.name in self.first["comando"]):
			self.procedure_comando()
		elif(self.nextToken.name in self.first["bloco"]):
			self.procedure_bloco()
		else:
			print("Error: expected block or command")

	def procedure_condicao(self):
		if(self.nextToken.name in self.first["expressao"]):
			self.procedure_expressao()
			if(self.nextToken.name == "op_rel"):
				self.nextToken = self.lexer.get_next_token()
				self.procedure_expressao()
			else:
				print("error: relational operator expected")
		else:
			print("error: expression expected")

	def procedure_controle(self):
		if(self.nextToken.name == "if"):
			self.nextToken = self.lexer.get_next_token()
			self.procedure_condicao()
			if(self.nextToken.name == "then"):
				self.nextToken = self.lexer.get_next_token()
				self.procedure_comando_bloco()
				self.procedure_controle_prime()

	def procedure_controle_prime(self):
		if(self.nextToken.name == "else"):
			self.nextToken = self.lexer.get_next_token()
			self.procedure_comando_bloco()
		else:
			print("error: 'else' expected")

	def procedure_enquanto(self):
		if(self.nextToken.name == "while"):
			self.nextToken = self.lexer.get_next_token()
			self.procedure_condicao()
			self.procedure_comando_bloco()

	def procedure_repeticao(self):
		if(self.nextToken.name == "repeat"):
			self.nextToken = self.lexer.get_next_token()
			self.procedure_comando_bloco()
			if(self.nextToken.name == "until"):
				self.nextToken = self.lexer.get_next_token()
				self.procedure_condicao()
				if(self.nextToken.name == ";"):
					self.nextToken = self.lexer.get_next_token()
				else:
					print("; expected")
			else:
				print("until expected")
		else:
			print("repeat expected")
	def procedure_expressao(self):
		if(self.nextToken.name in self.first["expressao_p2"]):
			self.procedure_expressao_p2()
			self.procedure_expressao_prime()
		else:
			print('Error: expressao esperada')

	def procedure_expressao_prime(self):
		if(self.nextToken.name == "+"):
			self.nextToken = self.lexer.get_next_token()
			self.procedure_expressao_p2()
			self.procedure_expressao_prime()
		elif(self.nextToken.name == "-"):
			self.nextToken = self.lexer.get_next_token()
			self.procedure_expressao_p2()
			self.procedure_expressao_prime()


	def procedure_expressao_p2(self):
		if(self.nextToken.name in self.first["expressao_p3"]):
			self.procedure_expressao_p3()
			self.procedure_expressao_p2_prime()
		else:
			print('Error: expressao esperada')

	def procedure_expressao_p2_prime(self):
		if(self.nextToken.name == "*"):
			self.nextToken = self.lexer.get_next_token()
			self.procedure_expressao_p3()
			self.procedure_expressao_p2_prime()
		elif(self.nextToken.name == "/"):
			self.nextToken = self.lexer.get_next_token()
			self.procedure_expressao_p3()
			self.procedure_expressao_p2_prime()

	def procedure_expressao_p3(self):
		if(self.nextToken.name in self.first["expressao_p3"]):
			self.procedure_expressao_p4()
			self.procedure_expressao_p3_prime()
		else:
			print('Error: expressao esperada')

	def procedure_expressao_p3_prime(self):
		if(self.nextToken.name == "^"):
			self.nextToken = self.lexer.get_next_token()
			self.procedure_expressao_p4()
			self.procedure_expressao_p3_prime()

	def procedure_expressao_p4(self):
		if(self.nextToken.name == "id"):
			self.nextToken = self.lexer.get_next_token()
		elif(self.nextToken.name == "number"):
			self.nextToken = self.lexer.get_next_token()
		elif(self.nextToken.name == "char"):
			self.nextToken = self.lexer.get_next_token()
		elif(self.nextToken.name == "("):
			self.nextToken = self.lexer.get_next_token()
			self.procedure_expressao_p3()
			if(self.nextToken.name == ")"):
				self.nextToken = self.lexer.get_next_token()
			else:
				print("Error: ')' expected. Good luck")
		elif(self.nextToken.name == "-"):
			self.nextToken = self.lexer.get_next_token()
			self.procedure_expressao_p4()
		else:
			print("Error: 'id' or 'int' or 'float' or 'char' or '(' or '-' expected.")
