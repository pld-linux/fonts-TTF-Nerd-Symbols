Summary:	Just the Nerd Font Icons. I.e Symbol font only
Name:		fonts-TTF-Nerd-Symbols
Version:	3.4.0
Release:	1
License:	MIT
Group:		Fonts
Source0:	https://github.com/ryanoasis/nerd-fonts/releases/download/v%{version}/NerdFontsSymbolsOnly.zip
# Source0-md5:	a0caf173734e58937970550b8dcab9c8
URL:		https://www.nerdfonts.com/
BuildRequires:	unzip
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ttffontsdir	%{_fontsdir}/TTF

%description
This font contains (in the patched-fonts folder) all symbols and is
intended to be used as fallback or together with fontconfig - so that
you do not need to individually patch all the fonts. YMMV.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/fonts/conf.d,%{ttffontsdir}}

cp -p *.ttf $RPM_BUILD_ROOT%{ttffontsdir}
cp -p 10-nerd-font-symbols.conf $RPM_BUILD_ROOT/etc/fonts/conf.d/

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc README.md
/etc/fonts/conf.d/10-nerd-font-symbols.conf
%{ttffontsdir}/*.ttf
