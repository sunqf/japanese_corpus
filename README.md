

### Subtitle repositories

This list isn't exaustive, but it's a start

* http://www.d-addicts.com/forums/page/subtitles?sid=c00e06662e59c449c2b2814b22e7bc90#Japanese
  * ~600 dramas, ~5M sentance pairs
  * fansubs
  * japanese & english subs in different parts of same page
* http://opus.lingfil.uu.se/OpenSubtitles2016.php
  * 1.4M sentance pairs
  * professional translations, 1-1 en/jp matching (in same file)
* http://kitsunekko.net/dirlist.php?dir=subtitles%2F, http://kitsunekko.net/dirlist.php?dir=subtitles%2Fjapanese%2F
  * ~600 dramas/movies (largeley incomplete), ~3M pairs
  * fansubs
  * en/jp lists on different pages
* http://nihongo-jimaku.blogspot.jp/
  * ~225 movies (.25M sentances)
  * jp only, no en
* https://subscene.com/browse, http://v2.subscene.com/subtitles/a/japanese.aspx
  * seems like v2 of ^^
  * set filter to japanese, then get english for each item by changing url)
  * ~2000 movies/shows, ~5M sentance pairs
  * mix of fansubs & professional translations


### Roadblocks

* accessing paired translations
  * soln: crawl sub sites, pull down en and jp subs for matched films/tv shows
* Poor translations. I.e. I've seen subs that were generated by running another language's subs through google translate
  * soln: run language model over each movie/show's corpus. if average sentance quality is below some threshold, throw it out
* En/Jp subtitle mismatch. Sometimes the srt files don't have the same number of entries, and entries don't correspond to the same times. 
  * soln: sentance alignment model. run encoder over en/jp srt files. pair up nearby sentances with similar thought vectors
* romanji transliterations
  * soln: throw out

  

### file formats

* tmx
* ass
* srt
