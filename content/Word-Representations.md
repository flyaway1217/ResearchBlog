Title: How to Represent Words in Computers
Date: 2020-05-09
Category: Representations
Keywords: word embeddings, word2vec
Tags: word embeddings, word2vec
Summary: 
Slug: word-representations
Comment_id: word-representations

As a semi-computer scientist, I always have a dream that we,
human, can make the computers understand what we say.
Instead of writing sophisticated code or using other input
devices (a mouse and a keyboard) to give instructions to
computers, we can directly talk to a computer and give
instructions. The first step to accomplish this science
fiction sence is to let the computer understand
we say -- natural languages, which is the ulitmate target of
**natural language processing(NLP)** research. And the first
step to let computers to understand natural languages is to
represent the basic element of natural language, words,  as
a form that computers can understand. This rasies a big
research direction in NLP: **word representations**. This is
the sub-area I am interested most in NLP. In this series
post, I am going to present some important research
achievements on this topic. 

In this very first post, I will first explain why do we need a
different representation for computers and how do we do it.
I want to present a "map" on this area so that we can
understand where are we on the path to our ulitmate
target: given instructions to computers by talking.

# Why Representing Words

Language is the most important characteristic of human that
can distinguish us from other animals. Although some animals
like dplphin can also communcate with each other, they can
not express complex objects or concepts. Language is the
unique ability of human. It enables us to communicate with
each other, exchange ideas and pass on knowledge. However,
when we sit down to think about what is language, we find
that language is just a sequence of words or symbols that
orgainized by some grammar or pattern. Humans can translate
their thoughts into a sequence of symbols and another one
can translate that sequence back to thoughts. This process
may happen without even us realizing it. However, with the
development of modern information technology, we start to
wonder, can we make the computers to understand what we say
without any sophisticated coding or device?

Although talking to a computer is a very appealing idea, in
reality, it is still a hard problem. Why? Because computers
"think" differently from human. Language is full of
ambiguity which is somehow a advantage because it enables us
to use a finite set of symbols to describe this infinite
world. However, this ambiguity does not work for computers.
Computers can not understand these ambiguity because it only
deals with numbers which is deterministic. For example,
computers can perform adding or multiplying operations, but
computers can not understand the difference between the
fruit "Apple" and the company "Apple". To computers, these
two words are the same symbol and represents the same
meanning.

In order to let computers understand the ambiguity of
natural language, we need to "translate" natural language
into some representations that computers enjoy. The basic
element of this translation is to "translate" the words
because words are the smallest element that contains
information. Over the years, researchers developed many
different representing methods. These representing methods
evolved through different stages. Following is a brief
summary of all these different representing methods.

# Representing Methods

I divided the whole representing history into three stages:

- Prehistory: dictionary lookup
- Middle ages: one-hot encoding, bag-of-words, TF-IDF
- The Enlightenment: vector space model and distributed
  representations
- Modern time: Type vector(word2vec, Fasttext) and Token
  vector(ELMo and BERT)

## Dictionary Lookup(prehistory)

## One-hot encoding and bag-of-words(middle ages)

## Distributed Representation(Modern Times)

- TF-IDF vector
- Word2vec: Static
- Fastttext: subwords
- Elmo: Contextual
- BERT: Contextual
- XLNET:
- RoBERTa:
- GPT


# References

- https://towardsdatascience.com/word-representation-in-natural-language-processing-part-i-e4cd54fed3d4
- https://towardsdatascience.com/word-representation-in-natural-language-processing-part-ii-1aee2094e08a
- https://towardsdatascience.com/representing-text-in-natural-language-processing-1eead30e57d8
- https://machinelearningmastery.com/what-are-word-embeddings/
- https://monkeylearn.com/blog/introduction-to-topic-modeling/
