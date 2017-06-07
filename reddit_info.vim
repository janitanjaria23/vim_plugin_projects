function! Reddit()
    pyfile reddit_info_fetcher.py
endfunction
command! -nargs=0 Reddit call Reddit()