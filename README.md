# mediascraper

## Scraper!!

## Example : 

```python
..

from discord.ext import commands

import mediascraper

hh = mediascraper.HentaiHaven()
ph = mediascraper.PornHub()
r34 = mediascraper.Rule34()
gb = mediascraper.Gelbooru()

class Media(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=['hh', 'hentai', 'hentaihaven'])
    async def hentai_haven(self, ctx, *args):
        video = await hh.category_search(str(" ").join(args))
        await ctx.send(video)

    @commands.command(aliases=['ph', 'porn', 'pornhub'])
    async def porn_hub(self, ctx, *args):
        video = await ph.video_search(str(" ").join(args))
        await ctx.send(video)

    @commands.command(alias=['r34', 'rule34'])
    async def rule34(self, ctx, *args):
        image = await r34.image_search(str(" ").join(args))
        await ctx.send(image)

    @commands.command(alias=['r34all', 'rule34all'])
    async def rule34all(self, ctx, *args):
        images = await r34.image_searchall(str(" ").join(args))
        for image in images:
            await ctx.send(image)

    @commands.command(aliases=['gbooru', 'gb'])
    async def gelbooru(self, ctx, *args):
        image = await gb.image_search(str(" ").join(args))
        await ctx.send(image)


def setup(bot):
    bot.add_cog(Media(bot))

..    
```
