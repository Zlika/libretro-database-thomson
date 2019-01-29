This repository includes cheat codes files and a content data for Thomson MO/TO games, to be used with RetroArch. It mimics the [libretro-database](https://github.com/libretro/libretro-database), but only includes content for Thomson MO/TO computers.

# RetroArch Database

RetroArch incoporates a ROM scanning system to automatically produce playlists. Each ROM that is scanned by the playlist generator is checked against a database of ROMs that are known to be good copies.

## Contents

- [`cht`](cht) Cheats to various games
- [`dat`](dat) The DAT file for Thomson games
- [`rdb`](rdb) The compiled RetroArch database file
- [`scripts`](scripts) Scripts to generate the DAT file and the thumbnails files from the https://www.screenscraper.fr website

## Sources

|System|Source|Repository|
|----|---|---|
|Thomson - MO/TO|[ScreenScraper](https://www.screenscraper.fr)|[libretro-database-thomson](https://github.com/Zlika/libretro-database-thomson)|

## Building

To build a complete set of RDB files for RetroArch or to generate a single RDB file, see [RetroArch/libretro-db/README.md](https://github.com/libretro/RetroArch/blob/master/libretro-db/README.md).
