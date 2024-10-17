%define drakxtools_required_version  10.4.89-1mdv2007.0
%define drakxtools_conflicted_version  10.4.88

%define libname %mklibname %{name}

Summary:  Terminal server configurator
Name:     draktermserv
Version:  0.8.1
Release:  2
Source0:  %name-%version.tar.bz2
License:  GPL
Group:    System/Configuration/Printing
Url:      https://www.mandrivalinux.com/en/cvs.php3
BuildRequires: perl-MDK-Common-devel
Requires: drakxtools => %drakxtools_required_version
BuildRoot: %_tmppath/%name-%version-buildroot
Conflicts: drakxtools <= %drakxtools_conflicted_version
BuildArch: noarch

%description
Draktermserv is a terminal server configurator.

%prep
%setup -q

%build

%install
rm -fr $RPM_BUILD_ROOT
%makeinstall_std

#install lang
%find_lang %name

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc COPYING ChangeLog
%_sbindir/*




%changelog
* Wed Apr 15 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.8.1-1mdv2009.1
+ Revision: 367441
- translation updates

* Mon Sep 22 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.8-1mdv2009.0
+ Revision: 287078
- translation updates

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.7-3mdv2009.0
+ Revision: 244539
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Tue Mar 25 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.7-1mdv2008.1
+ Revision: 190157
- translation updates
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Oct 03 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.6-1mdv2008.0
+ Revision: 95064
- updated translation

* Thu Sep 27 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.5-1mdv2008.0
+ Revision: 93357
- updated translations
- updated translations

* Fri Jun 08 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.3-1mdv2008.0
+ Revision: 36959
- initial release after SVN crash in order to check everything is good


* Mon Mar 12 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.2-1mdv2007.1
+ Revision: 141959
- translation snapshot

* Fri Jan 19 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.1-2mdv2007.1
+ Revision: 110743
- do not require printerdrake

* Tue Jan 09 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.1-1mdv2007.1
+ Revision: 106619
- Import draktermserv

* Thu Nov 30 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.0-1mdv2007.1
- initial release (splited out of drakxtools)

