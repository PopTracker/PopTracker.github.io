PopTracker is a project to offer a universal, scriptable randomizer tracking solution that is
open source, runs everywhere and supports auto-tracking.


## Download

### Latest {{ site.data.releases.latest.version }}
{% if site.data.releases.latest %}
{% comment %}<!-- see .github/make_data.py -->{% endcomment %}
<a class="download" href="{{ site.data.releases.latest.windows_download }}">Windows</a>
<a class="download" href="{{ site.data.releases.latest.macos_download }}">macOS</a>
<a class="download" href="{{ site.data.releases.latest.appimage_download }}">Linux AppImage</a>
<a class="download" href="{{ site.data.releases.latest.linux_download }}">Linux tar.xz</a>
[Source]({{ site.data.releases.latest.source_download }}) •
[Changelog]({{ site.data.releases.latest.changelog }}) •
[All Downloads]({{ site.data.releases.latest.url }}){% if site.data.releases.next and site.data.releases.next.url %} •
[Preview {{ site.data.releases.next.version }}]({{ site.data.releases.next.url }}){% endif %}
{% else %}
[GitHub Release Page](https://github.com/black-sliver/popTracker/releases/latest)
{% endif %}

See [build instructions](https://github.com/black-sliver/PopTracker/blob/master/BUILD.md)
if you want to build it yourself.


## Color Picker

To customize map colors, follow the instructions on [the Color Picker page](color-picker.html)


## More Info

Head over to [the project readme](https://github.com/black-sliver/PopTracker#readme) for more information.


## JSON Schema

See [schema](schema).
