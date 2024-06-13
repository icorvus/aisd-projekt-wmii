def getLPS(text):
	lps = [0] * len(text)
	length = 0

	lps[0] = 0
	i = 1

	while i < len(text):
		if text[i] == text[length]:
			length += 1
			lps[i] = length
			i += 1
		else:
			if length == 0:
				lps[i] = 0
				i += 1
			else:
				length = lps[length - 1]
	return lps


def replacePattern(text, old_string, new_string):
	i = j = 0

	lps = getLPS(old_string)

	found = []
	while i < len(text):
		if text[i] == old_string[j]:
			i += 1
			j += 1
		if j == len(old_string):
			found.append(i - j)
			j = lps[j - 1]
		elif i < len(text) and old_string[j] != text[i]:
			if j == 0:
				i += 1
			else:
				j = lps[j - 1]

	ans = ""
	prev = 0

	for k in range(len(found)):
		if found[k] < prev:
			continue
		ans += text[prev:found[k]]
		ans += new_string
		prev = found[k] + len(old_string)

	ans += text[prev:]
	return (ans)
