# lntree
A simple tool to symlink the leaves of a directory tree to a certain folder(s) or file(s)

# Install

Available on Ubuntu 18:04 and later:

```
snap install lntree
```

# Use

Simply execute:

```
lntree SRC DST
```

where 
 * SRC can be a file, a dir or a group of them (metacharacters) where dst will point to
 * DST is the path to a folder that is the root of the tree whose leaves will be linked to src