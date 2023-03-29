# QCrypt 2023 website


[![Netlify Status](https://api.netlify.com/api/v1/badges/3b2d4f11-42a3-42fc-bbfc-1debed945d5e/deploy-status)](https://app.netlify.com/sites/qcrypt2023/deploys)

Live site at https://2023.qcrypt.net

Using the Hugo template from https://github.com/GDGToulouse/devfest-theme-hugo
adapted from the fork by the cloudnative-amsterdam people: https://github.com/cloudnative-amsterdam/public-website

theme submodule now included directly in this git repository.

## Building this conference site from scratch

1. Install [Hugo](https://gohugo.io)
2. Clone this repo:

```bash
git clone git@github.com:QCrypt/website-2023.git
```

3. It's done. Just start Hugo server to see the site live!

```bash
cd ../..
hugo server
```

5. Edit the markdown source files with ending .md in the /content/ subdirectory to make changes to the site. You might also have to edit .json and .yml files in the /data/ subdirectory. As long as the hugo server is running, your changes should be visible immediately at http://localhost:1313/.

6. Using a suitable editor like [Visual Studio Code](https://code.visualstudio.com/) or [Atom](https://atom.io/) allows to easily search across all source files, and will help finding the correct file to edit if you want to make specific changes.

7. When you are happy with the result, commit the changes to the master branch. The site is then automatically deployed to https://qcrypt2023.netlify.com/ and accessible under https://2023.qcrypt.net . If you have the proper rights, you can see the deployment logs on [netlify](https://app.netlify.com/sites/qcrypt2023/deploys).

## Customizing the theme
The theme is located in the themes/devfest-theme-hugo subdirectory. 

First, install [yarn](https://yarnpkg.com/lang/en/docs/install/).

Then, use
```
cd themes/devfest-theme-hugo
yarn
```
to install the dependencies.

As you might not have the right version of npm, you might have to install the node version manager [nvm](https://github.com/nvm-sh/nvm). Then, use
```
nvm install 10.0
```

In the same directory, run `npm start` to watch [Sass](https://sass-lang.com/) changes.

When you are happy with the result run `npm run build` to build the minified versions of `theme.js` and `theme.css`. Then commit to these.

### Installing on a new ARM Mac
node-sass is not yet ported to ARM processors, but there is a work-around described here:
https://github.com/sass/node-sass/issues/3033#issuecomment-763180778
TODO: newer software exists now...

## Setting up the next year 2024 based on year 2023

### creating new repositories on GitHub
1. create new empty repository QCrypt/website-2024 from the web: https://github.com/organizations/QCrypt/repositories/new
2. clone the empty repository QCrypt/website-2024 onto local hard drive
3. clone QCrypt/website-2023 into a temporary directory, remove bulky data like slides and posters, copy the rest over to the empty local website-2024

13. ```git add *```
15. ```git commit -m 'initial commit'```

The old 2023 website should now be ready to be served by ```hugo server```. It is ready to be updated to the 2024 edition.

### create new team and add admins
1. on https://github.com/orgs/QCrypt/teams, create a new team ```QCrypt 2024```
2. add admins https://github.com/orgs/QCrypt/teams/qcrypt-2024/members
3. add repositories https://github.com/orgs/QCrypt/teams/qcrypt-2024/repositories

### setting up netfliy & domain name
1. create new site on https://app.netlify.com/teams/qcrypt/overview by "import from existing project"
2. connect to Git provider: GitHub
3. pick correct repository: QCrypt/website-2024
3. rename project to qcrypt2024
4. In [Gandi](https://admin.gandi.net/domain/c9de5b76-af33-11e7-8de2-00163ec31f40/qcrypt.net/records): add a new DNS entry, as suggested in netlify:  ```2024	CNAME	10800	qcrypt2024.netlify.app.```
5. In netlify https://app.netlify.com/teams/qcrypt/members: add new admin as collaborator to 2024 site

### slack integration
1. create a new private channel on QCrypt slack, named website-2024
1. on https://api.slack.com/apps/A01P06YNCCU/incoming-webhooks , create a new Webhook (on the bottom of the page)
1. paste the Webhook URL into netfliy:  https://app.netlify.com/sites/qcrypt2024/settings/deploys (for deploy succeesful and deploy failed)
1. add admins to Slack channel

### general
- connect new admins to admins from last year
- update hugo version? check what needs to be updated.
