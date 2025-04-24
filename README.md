# ChemCard
a game of Chemistry Card

## class diagram
```mermaid

'''
title: ChemCard
'''
classDiagram
  card <|-- elecard
  card <|-- numcard
  card <|-- symcard
  card <|-- pnkcard
  
  equ --* subst
  subst --o card

 ```
