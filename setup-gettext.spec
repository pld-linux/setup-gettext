Summary:	Script intended to be used instead of either gettextize or autopoint
Summary(pl):	Skrypt do u¿ywania zamiast gettextize lub autopoint
Name:		setup-gettext
Version:	0.1.5
Release:	1
Epoch:		0
License:	GPL
Group:		Development/Tools
Source0:	http://www.chipx86.com/linuxstuff/gettext/%{name}
# NoSource0-md5: 73f1ea0228a1d71475b6881aadccf0fc
URL:		http://www.chipx86.com/linuxstuff/gettext/
Requires:	gettext-autopoint
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This script is intended to be used instead of either gettextize or
autopoint. It handles most of the magic of cross-version
compatibility.

%description -l pl
Ten skrypt mo¿e byæ u¿ywany zamiast gettextize lub autopoint.
Obs³uguje wiêksz± czê¶æ magii zwi±zanej z kompatybilno¶ci± z ró¿nymi
wersjami gettexta.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
