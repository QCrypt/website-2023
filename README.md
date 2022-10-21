# QCrypt 2022 website

[![Netlify Status](https://api.netlify.com/api/v1/badges/3b2d4f11-42a3-42fc-bbfc-1debed945d5e/deploy-status)](https://app.netlify.com/sites/qcrypt2022/deploys)

Live site at https://2022.qcrypt.net

Using the Hugo template from https://github.com/GDGToulouse/devfest-theme-hugo
adapted from the fork by the cloudnative-amsterdam people: https://github.com/cloudnative-amsterdam/public-website

theme submodule at https://github.com/QCrypt/devfest-theme-hugo-2022

## Building this conference site from scratch

1. Install [Hugo](https://gohugo.io)
2. Clone this repo:

```bash
git clone git@github.com:QCrypt/website-2022.git
```

3. Update the theme submodule

```bash
cd website-2022/themes/devfest-theme-hugo
git submodule init
git submodule update
```

4. It's done. Just start Hugo server to see the site live!

```bash
cd ../..
hugo server
```

5. Edit the markdown source files with ending .md in the /content/ subdirectory to make changes to the site. You might also have to edit .json and .yml files in the /data/ subdirectory. As long as the hugo server is running, your changes should be visible immediately at http://localhost:1313/.

6. Using a suitable editor like [Atom](https://atom.io/) allows to easily search across all source files, and will help finding the correct file to edit if you want to make specific changes.

7. When you are happy with the result, commit the changes to the master branch. The site is then automatically deployed to https://qcrypt2022.netlify.com/ and accessible under https://2022.qcrypt.net . If you have the proper rights, you can see the deployment logs on [netlify](https://app.netlify.com/sites/qcrypt2022/deploys).

## Customizing the theme
The theme is located at https://github.com/QCrypt/devfest-theme-hugo-2022

First, install [yarn](https://yarnpkg.com/lang/en/docs/install/).

Then, use
```
cd themes/devfest-theme-hugo
yarn
```
to install the dependencies.

As you might have the right version of npm, you might have to install the node version manager [nvm](https://github.com/nvm-sh/nvm). Then, use
```
nvm install 10.0
```

In the same directory, run `npm start` to watch Sass changes.

When you are happy with the result run `npm run build` to build the minified version. Then commit the theme submodule.

### Installing on a new ARM Mac
node-sass is not yet ported to ARM processors, but there is a work-around described here:
https://github.com/sass/node-sass/issues/3033#issuecomment-763180778

## Setting up the next year 2022 based on year 2021
1. create new empty repository QCrypt/website-2022
2. clone QCrypt/website-2022 , remove bulky data like slides and posters, copy the rest over to the empty website-2022, except the themes subdirectory
3. in QCrypt/website-2022, change remote destination:
```git remote set-url origin https://github.com/QCrypt/website-2022.git```
4. ```git branch -M main```
5. ```git push -u origin main```

6. create new empty repository QCrypt/devfest-theme-hugo-2022
7. ```git clone QCrypt/devfest-theme-hugo-2021```
8. ```git remote set-url origin https://github.com/QCrypt/devfest-theme-hugo-2022.git```
9. ```git branch -M main```
10. ```git push -u origin main```

11. cd website-2022, mkdir themes
12. git submodule add https://github.com/QCrypt/devfest-theme-hugo-2022 devfest-theme-hugo
