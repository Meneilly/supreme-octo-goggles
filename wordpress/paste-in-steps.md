# Putting the portal on your WordPress site (Twenty Twenty)

You need to be logged in as an **Administrator**. WordPress removes scripts pasted in by other roles, and the portal won't work without them.

1. Open the latest file, `cilni-portal-draft-9-wordpress.html`, in a plain text editor (Notepad, TextEdit in plain-text mode, or VS Code) and copy **everything**.
2. In WordPress go to **Pages → Add New**. Give the page a title, such as "Payroll onboarding". The title is hidden on the page itself but still shows in the browser tab and menus.
3. In the right-hand panel, under **Page → Template**, choose **Full Width Template**.
4. Click **+**, add a **Custom HTML** block, and paste the code into it. Don't add anything else to the page.
5. Click **Preview**, check it works, then **Publish**.

To swap in a later draft, open the page, select the Custom HTML block, delete its contents and paste the new code.

## Settings

Line 3 of the file holds the settings, all on one line:

- `theme` is `'light'` (the default), `'dark'`, or `'auto'` to follow each visitor's device. From Draft 9 this is only the starting colour scheme: visitors can change it in the portal's Display menu, and their choice is remembered.
- `waitBaseMs`, `waitPerWordMs`, `waitMinMs`, `waitMaxMs` set how long Next stays locked the first time a card is shown, in milliseconds.
- `guardMs` is the double-tap guard.
- `tidyPage: true` hides the page title and the gap above the portal. Set it to `false` to keep the title.
- Changing `storageKey` (for example to `'cilni-portal-wp-2'`) starts everyone from the beginning again.

## If something looks wrong

- **The code shows up as text, or nothing appears:** the block was pasted by a non-admin, or a security plugin is stripping scripts. Paste it again as an Administrator.
- **Caching plugins** (WP Rocket, Autoptimize and similar) can break inline scripts if "combine" or "delay JavaScript" is turned on. Exclude this page if that happens.
