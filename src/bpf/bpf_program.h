#ifndef BPF_PROGRAM_H
#define BPF_PROGRAM_H

#define BKL_CTRL 0
#define BKL_SHIFT 1
#define BKL_ALT 2
#define BKL_META 3

struct bkl_key_event
{
    unsigned int code;
    u8 ctrl;
    u8 shift;
    u8 alt;
    u8 meta;
};

#endif
