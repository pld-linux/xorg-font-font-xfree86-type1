Summary:	XFree86 Cursor font in Type1 format
Summary(pl.UTF-8):	Font XFree86 Cursor w formacie Type1
Name:		xorg-font-font-xfree86-type1
Version:	1.0.2
Release:	1
License:	MIT
Group:		Fonts
Source0:	http://xorg.freedesktop.org/releases/individual/font/font-xfree86-type1-%{version}.tar.bz2
# Source0-md5:	a966f5a8aade9e63af86d8a6bf3e8586
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	fontconfig
BuildRequires:	t1utils
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-util-util-macros
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/Type1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XFree86 Cursor font in Type1 format.

%description -l pl.UTF-8
Font XFree86 Cursor w formacie Type1.

%prep
%setup -q -n font-xfree86-type1-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--build=%{_host_platform} \
	--host=%{_host_platform} \
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

cat > Fontmap.xfree86 <<EOF
/Cursor                                  (cursor.pfb)   ;
EOF

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
%{_fontsdir}/Type1/Fontmap.xfree86
