# Site Records

## Recording archaeological, heritage and rock art sites

## What is it?

A site record holds what a fieldworker writes down at a site: its number, when it was visited, where it is, what is there and what state it is in. Each site record hangs off an authority record, so the site keeps one identity in the catalogue and the holdings described against it stay linked to it.

Where a site is matters more than anything else in the record. A precise position is what makes looting and vandalism possible, so the plugin restricts it rather than hiding it from everyone. Staff who need the position see it. Everyone else sees, at most, a deliberately coarse area, and by default nothing at all beyond a note that the location is restricted.

## Who can do what

Nothing about site records is public.

| Action | Who |
| --- | --- |
| Browse and view site records | Contributors, editors and administrators |
| Add and edit site records | Editors and administrators |
| Delete a site record | Administrators only |
| See a sensitive site's exact position | Editors and administrators |

: Site record permissions

A researcher account is signed in, but it is not staff, and it does not see exact positions. That is deliberate. Contributors can open a site record, but they see its position the way the public would.

## Adding a site record

Open the authority record for the site and choose **Add site record** in the *Site record* panel. Only one thing is needed to save: the record has to belong to an authority record, which it does when you start from there.

The form has five parts.

**Identification.** Site number, date visited and the photograph numbers taken on the visit.

**Locality.** Latitude and longitude in decimal degrees, the coordinate datum, altitude in metres, the map sheet, and *Locality as originally recorded*. That last field keeps the source's wording verbatim (map sheet strings, site codes, the original notation), so nothing is lost when a position is converted.

**Setting.** Region, aspect and the site's dimensions (height, width, depth in metres).

**Attributes.** Ticked lists for tradition, site type, damage, surface contents, excavation potential, mineral and rock contents, deposit depth and deposit contents. Each list has a note field for anything the ticks do not capture.

**Field recorders.** Everyone who recorded the site, each with a role. Then a free-text site description, a contact name and email, and notes.

## The sensitivity tick

Under the locality fields is *Locality is sensitive - generalise it for readers without clearance*. It is ticked on every new record, and a record that has never had it set is treated as sensitive. Protection is the starting point; exposing a position is a decision someone has to make.

Clear the tick only for a site whose position is already public knowledge, such as a declared monument or a site whose excavation report has been published. An unticked site shows its exact position to anyone who can see the record.

## What other people see

For a sensitive site, readers without clearance see one of two things, depending on how the instance is configured:

- **No location** (the default): a note that the location of the site is restricted to protect it. The page still shows that the site has coordinates, so nobody mistakes a restricted record for an incomplete one.
- **An approximate area** of about 10, 25 or 50 km, with a note that the position is deliberately imprecise.

The coarse area is produced by rounding, not by shifting the point, so looking at the same site many times cannot be averaged back to where it really is. The raw text fields (the map sheet and the locality as originally recorded) are never shown to a reader without clearance, whichever option is set.

The same rule applies everywhere a position can appear: the site record page, the panel on the authority record, the site record browse list, maps, reports and exports. In lists, a restricted position carries a *restricted* badge and a coarsened one an *approximate* badge.

## Browsing site records

**Site records** (`/site-record`) lists every site record you are allowed to see, with the badges above. Open one to see the full record, or go to its authority record to see the holdings linked to the site.

## Administration

The public setting (`site_locality_public`: none, 10, 25 or 50) is set by an administrator. It defaults to none and should stay there until the institution has decided what, if anything, the public may know about where its sites are.

Bulk loading of a site catalogue, coordinates, map sheets and holding periods is done from the command line by an administrator; see the plugin's README.

## Tips and FAQ

**Two sites have the same name. Which is which?** Many site names repeat: a farm name can be shared by dozens of separate sites. Go by the site number and map sheet, which together identify a site, never by the name alone.

**I can see a site but not where it is.** You are probably signed in without editor rights, or as a contributor. Ask an administrator if your work needs exact positions.

**Can I put coordinates in the description instead?** Please do not. Only the locality fields are protected. Anything typed into the description, notes or a holding's scope and content is shown to everyone who can see that text.
