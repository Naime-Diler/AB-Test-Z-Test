########################################################################################################################
# A/B-Test: Unabhängiger Z-Test zur Analyse der Überlebensraten von Frauen und Männern – Vergleich der
# Überlebensanteile auf der Titanic
########################################################################################################################

import seaborn as sns
from statsmodels.stats.proportion import proportions_ztest

# Anwendung: Gibt es einen statistisch signifikanten Unterschied zwischen den Überlebensraten von Frauen und Männern?
############################

# H0: p1 = p2
# Es gibt keinen statistisch signifikanten Unterschied zwischen den Überlebensraten von Frauen und Männern.

# H1: p1 != p2
# Es gibt einen statistisch signifikanten Unterschied.

df = sns.load_dataset("titanic")
df.head()

# Durchschnittliche Überlebensrate für Frauen:
df.loc[df["sex"] == "female", "survived"].mean()  # --> 0.74

# Durchschnittliche Überlebensrate für Männer:
df.loc[df["sex"] == "male", "survived"].mean()  # --> 0.18

# Es gibt einen offensichtlichen Unterschied, aber wir führen den Test durch, um dies statistisch zu bestätigen.

# Anzahl der Überlebenden nach Geschlecht:
female_succ_count = df.loc[df["sex"] == "female", "survived"].sum()  # --> 233
male_succ_count = df.loc[df["sex"] == "male", "survived"].sum()  # --> 109

# Gesamtanzahl der Beobachtungen pro Gruppe:
female_total = df.loc[df["sex"] == "female", "survived"].shape[0]  # --> 314
male_total = df.loc[df["sex"] == "male", "survived"].shape[0]  # --> 577

# Durchführung des Z-Tests für zwei Anteile:
test_stat, pvalue = proportions_ztest(count=[female_succ_count, male_succ_count],
                                      nobs=[female_total, male_total])

print('Teststatistik = %.4f, p-Wert = %.4f' % (test_stat, pvalue))  # --> p-Wert: 0.0000

# Ergebnisinterpretation:
if pvalue < 0.05:
    print("H0 wird abgelehnt: Es gibt einen statistisch signifikanten Unterschied zwischen den Überlebensraten von Frauen und Männern.")
else:
    print("H0 kann nicht abgelehnt werden: Es gibt keinen signifikanten Unterschied zwischen den Überlebensraten.")


# Out: H0 wird abgelehnt: Es gibt einen statistisch signifikanten Unterschied zwischen den Überlebensraten von Frauen
# und Männern.