Summary:	xfree86-type1 font
Summary(pl):	Font xfree86-type1
Name:		xorg-font-font-xfree86-type1
Version:	0.99.1
Release:	0.1
License:	MIT
Group:		Fonts
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC3/font/font-xfree86-type1-%{version}.tar.bz2
# Source0-md5:	5b6688cea95067886574c191992c3bc5
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	fontconfig
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	t1utils
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-util-util-macros
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/Type1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfree86-type1 font.

%description -l pl
Font xfree86-type1.

%prep
%setup -q -n font-xfree86-type1-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-fontdir=%{_fontsdir}/Type1

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# convert *.pfa to .pfb
cd $RPM_BUILD_ROOT%{_fontsdir}/Type1
t1binary cursor.pfa cursor.pfb
rm -f cursor.pfa
sed -e '1d;s/\.pfa /.pfb /' fonts.scale > fonts.scale.xfree86
rm -f fonts.scale fonts.dir fonts.cache-1

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst Type1

%postun
fontpostinst Type1

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%{_fontsdir}/Type1/cursor.pfb
%{_fontsdir}/Type1/fonts.scale.xfree86
