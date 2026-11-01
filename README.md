# LeetCode Solutions in Python

I've been solving LC problems randomly over the past month but neglected to store them on a repo, so I've decided to start from scratch and put them on here to try and keep up practice.

Attempts are written by hand and AI help is only used if I'm completely stumped (I'll mark them in file so I know which ones got me).

No completion goals or anything, I just want to try to stay in practice after flubbing coding interviews more than once.


## Repository Architecture

~~Solutions will be separated by difficulty, but files are named after the LC problem including number, so hopefully it is simple enough to navigate.~~
EDIT: This dir structure felt more cumbersome than it was worth, so I changed it to a flat structure.

* The core algorithmic class (`Solution`) sits at the top of code, which can be copy-pasted in LC to use their test cases.
* I use Vim/NeoVim when I code, so I'll generally write in a test case or two to test in terminal instead of on LC's site. Written into __name__ so it won't get in the way of running on LC.

Problems are categorized by difficulty and prefixed by their official LeetCode index number to maintain alphabetical and numerical alignment:

##  Development Environment

* **Language:** Python 3.10+ (utilizing modern strict type hinting)
* **Editor:** Neovim with lightly customised NVChad
* **Testing:** Depends on the problem, but should always clear all LC test cases online before I push

##  Running Solutions Locally

For other learners, you can run solutions using python3 locally if you prefer:

```bash
python3 Medium/3619_count_islands_with_total_value_divisible_by_k.py
```
