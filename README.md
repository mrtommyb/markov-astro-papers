# markov-astro-papers

One day in the shower I was considering how the language and style of academic papers have changed over time. I thought about a fun way to investigate this and came up with creating fake paper titles using a Markov chain trained on the titles of papers from a given year.

There are a couple of bits of code here: getPapers.py can be used to download the titles and first authors of papers from a given year, core.py does the Markov bit and tweets the results. [Markovify](https://github.com/jsvine/markovify) made making the Markov chain super-duper easy.

The result is that the code can be used to tweet a paper title, author and year. Here are a few good one.

```
Beauchamp et al., Can the existence of the heliospheric termination shock. (1995)
Maturi et al., Optical and Near Infrared Spectrograph Observations of the Universe. (2005)
Ursini et al., Echelle Spectroscopy of Star Formation Across Cosmic Time with MAVEN. (2015)
```

This code isn't really all that useable, both ADS and Twitter require you to have API keys. If anyone wants the code to be in better shape, make an issue.
