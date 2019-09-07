---
layout: post
title:  "安装jekyll"
date:   2019-09-07 22:56:19 +0800
categories: jekyll update
---
## 缺失/usr/local/share/gems/gems/sassc-2.2.0/lib/sassc/libsass.so
[root@DESKTOP-LJ3J01Q yutian]# jekyll -v
Traceback (most recent call last):
        21: from /usr/local/bin/jekyll:23:in `<main>'
        20: from /usr/local/bin/jekyll:23:in `load'
        19: from /usr/local/share/gems/gems/jekyll-4.0.0/exe/jekyll:8:in `<top (required)>'
        18: from /usr/share/rubygems/rubygems/core_ext/kernel_require.rb:54:in `require'
        17: from /usr/share/rubygems/rubygems/core_ext/kernel_require.rb:54:in `require'
        16: from /usr/local/share/gems/gems/jekyll-4.0.0/lib/jekyll.rb:206:in `<top (required)>'
        15: from /usr/share/rubygems/rubygems/core_ext/kernel_require.rb:54:in `require'
        14: from /usr/share/rubygems/rubygems/core_ext/kernel_require.rb:54:in `require'
        13: from /usr/local/share/gems/gems/jekyll-sass-converter-2.0.0/lib/jekyll-sass-converter.rb:4:in `<top (required)>'
        12: from /usr/share/rubygems/rubygems/core_ext/kernel_require.rb:54:in `require'
        11: from /usr/share/rubygems/rubygems/core_ext/kernel_require.rb:54:in `require'
        10: from /usr/local/share/gems/gems/jekyll-sass-converter-2.0.0/lib/jekyll/converters/scss.rb:3:in `<top (required)>'
         9: from /usr/share/rubygems/rubygems/core_ext/kernel_require.rb:54:in `require'
         8: from /usr/share/rubygems/rubygems/core_ext/kernel_require.rb:54:in `require'
         7: from /usr/local/share/gems/gems/sassc-2.2.0/lib/sassc.rb:31:in `<top (required)>'
         6: from /usr/local/share/gems/gems/sassc-2.2.0/lib/sassc.rb:31:in `require_relative'
         5: from /usr/local/share/gems/gems/sassc-2.2.0/lib/sassc/native.rb:5:in `<top (required)>'
         4: from /usr/local/share/gems/gems/sassc-2.2.0/lib/sassc/native.rb:6:in `<module:SassC>'
         3: from /usr/local/share/gems/gems/sassc-2.2.0/lib/sassc/native.rb:10:in `<module:Native>'
         2: from /usr/local/share/gems/gems/ffi-1.11.1/lib/ffi/library.rb:99:in `ffi_lib'
         1: from /usr/local/share/gems/gems/ffi-1.11.1/lib/ffi/library.rb:99:in `map'
/usr/local/share/gems/gems/ffi-1.11.1/lib/ffi/library.rb:145:in `block in ffi_lib': Could not open library '/usr/local/share/gems/gems/sassc-2.2.0/lib/sassc/libsass.so': /usr/local/share/gems/gems/sassc-2.2.0/lib/sassc/libsass.so: cannot open shared object file: No such file or directory (LoadError)

在 https://apps.fedoraproject.org/packages/rubygem-sassc/ 下载rubygem-sassc-2.2.0-1.fc31.x86_64.rpm安装
