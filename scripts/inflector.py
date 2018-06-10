import re

# Finds singular and plural forms of nouns (and adjectives?)
class Inflector:
    # List of rules in *increasing* order of priority
    PLURALIZE_RULES = [[r'$', r's'],
	               [r'(s)$', r'\1'],
	               [r'(z|r)$', r'\1es'],
	               [r'al$', r'ais'],
	               [r'el$', r'eis'],
	               [r'ol$', r'ois'],
	               [r'ul$', r'uis'],
	               [r'([^aeou])il$', r'\1is'],
	               [r'm$', r'ns'],
	               [r'^(japon|escoc|ingl|dinamarqu|fregu|portugu)ês$', r'\1eses'],
	               [r'^(|g)ás$', r'\1ases'],
	               [r'ão$', r'ões'],
	               [r'^(irm|m)ão$', r'\1ãos'],
		       [r'^(alem|c|p)ão$', r'\1ães']]
    
    SINGULARIZE_RULES = [[r'([^ê])s$', r'\1'],
	                 [r'^(á|gá)s$', r'\1s'],
	                 [r'(r|z)es$', r'\1'],
	                 [r'([^p])ais$', r'\1al'],
	                 [r'éis$', r'el'],
	                 [r'eis$', r'ei'],
	                 [r'ois$', r'ol'],
	                 [r'uis$', r'ul'],
                         [r'veis$', r'vel'],
	                 [r'(r|t|f|v)is$', r'\1il'],
	                 [r'ns$', r'm'],
	                 [r'sses$', r'sse'],
	                 [r'^(.*[^s]s)es$', r'\1'],
	                 [r'(ãe|ão|õe)s$', r'ão'],
	                 [r'(ae|ao|oe)s$', r'ao'],
	                 [r'(japon|escoc|ingl|dinamarqu|fregu|portugu)eses$', r'\1ês'],
		         [r'^(g|)ases$', r'\1ás']]

    EXCEPTIONS = [[r'abdômen', r'abdomens'],
		  [r'álcool', r'álcoois'],
	          [r"árvore", "árvores"],
		  [r'bênção', r'bênçãos'],
		  [r'campus', r'campi'],
		  [r"cadáver", "cadáveres"],
		  [r'capelão', r'capelães'],
		  [r'capitão', r'capitães'],
		  [r'chão', r'chãos'],
		  [r'charlatão', r'charlatães'],
		  [r'cidadão', r'cidadãos'],
		  [r'cônsul', r'cônsules'],
		  [r'cristão', r'cristãos'],
		  [r'difícil', r'difíceis'],
		  [r'email', r'emails'],
		  [r'escrivão', r'escrivães'],
		  [r'fóssil', r'fósseis'],
		  [r'gás', r'gases'],
		  [r'germens', r'germen'],
		  [r'grão', r'grãos'],
		  [r'hífen', r'hífens'],
		  [r'irmão', r'irmãos'],
		  [r'mal', r'males'],
		  [r'mão', r'mãos'],
		  [r'órfão', r'órfãos'],
		  [r'país', r'países'],
		  [r'pai', r'pais'],
		  [r'projétil', r'projéteis'],
		  [r'réptil', r'répteis'],
		  [r'sacristão', r'sacristães'],
		  [r'sotão', r'sotãos'],
		  [r'tabelião', r'tabeliães']]

    def apply_rules(word, rules):
        for rule in reversed(rules):
            word, count = re.subn(rule[0], rule[1], word)
            if count > 0: break;
        return word        

    def pluralize(word):
        for exception in Inflector.EXCEPTIONS:
            if word == exception[0]:
                return exception[1]
        return Inflector.apply_rules(word, Inflector.PLURALIZE_RULES)

    def singularize(word):
        for exception in Inflector.EXCEPTIONS:
            if word == exception[1]:
                return exception[0]
        return Inflector.apply_rules(word, Inflector.SINGULARIZE_RULES)
