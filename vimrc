#autocmd BufNewFile *.py call append(0,'#!/bin/python')
autocmd BufNewFile *.py norm i#!/usr/bin/env python3
autocmd BufNewFile *.pl norm i#!/usr/bin/perl -w
