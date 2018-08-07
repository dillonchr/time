# time
Service time parser really. I have been forever putting off writing my own app to manage my service time. But now I don't think it sounds like fun to write a bright and shiny GUI so I opted for something more shelly.

I started playing with bash, but I may have done written to some bad sectors in my brain while researching how to achieve my goal. I didn't want to use JS yet again because I'm just too quick to pull it out for action.

Python sounded good because I wanted to develop this app on a pi via ssh. So far, so good. Who knows what's next?

## report file
So this expects to have a file called `time.time` in the same directory as the script. The layout of that file is strict. Here's how to report time locally:

```
2018
08
04;2h;1p;1r;
```

That says 2018, in August, on the 4th, you got 2 hours, 1 placement, and 1 RV. :clap: by the way. 

## Usage
`./reporty.py {two_digit_month}`

This will parse your file, find the appropriate month and print your results for you to forward to your service group overseer.

```
$ ./report.py 08
('Hours', 4)
('Placements', 1)
('Returns', 1)
```
