%define	name	cire
%define	version 0.14.0
%define rel	5
%define	release	%mkrel %rel

Name:		%{name} 
Summary:	An Open-Source Diary Program
Version:	%{version} 
Release:	%{release} 
Source0:	%{name}-%{version}.tar.bz2
# Courtesy of the open clipart library
# http://openclipart.org/clipart/unsorted/glossy_paper__gino_river_01.svg
Source1:	%{name}-48.png
URL:		https://cire.sf.net/
# Not sure where it actually fits
Group:		Office
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPL
BuildRequires: imagemagick

%description
Cire is a Free and Open-Source Program for keeping an Electronic
Journal or Diary. It is designed to run on Linux and other Unixes.

Some Possibilities include:
* Keep a Personal Diary
* Keep a Log of Progress on a Programming Project
* Encrypt Messages to Friends (Put the Message in a Diary File, encrypt it,
  send the diary file to your friend, have them decrypt it.)

You can use:

 'cire -g <diary filename>' to Start GTK Interface,
 'cire -n <diary filename>' to Start Ncurses Interface,
 'cire -t <diary filename>' to Start Text Interface,

%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_bindir}/%{name}                
Icon=%{name}                                
Categories=Office;                
Name=Cire                
Comment=A open-source diary program
EOF

mkdir -p %{buildroot}/%{_iconsdir}/ %{buildroot}/%{_miconsdir}/
install -m644 %{SOURCE1} -D %{buildroot}/%{_liconsdir}/%{name}.png
convert %{buildroot}/%{_liconsdir}/%{name}.png -resize 32x32 %{buildroot}/%{_iconsdir}/%{name}.png
convert %{buildroot}/%{_liconsdir}/%{name}.png -resize 16x16 %{buildroot}/%{_miconsdir}/%{name}.png
%makeinstall

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean 
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(-,root,root)
%doc README TODO HACKING CREDITS CHANGES
%{_bindir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/*



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.14.0-5mdv2011.0
+ Revision: 617038
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 0.14.0-4mdv2010.0
+ Revision: 424868
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 0.14.0-3mdv2009.0
+ Revision: 218435
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Thierry Vignaud <tv@mandriva.org> 0.14.0-3mdv2008.1
+ Revision: 132935
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- import cire


* Fri Oct 21 2005 Nicolas L�cureuil <neoclust@mandriva.org> 0.14.0-3mdk
- Fix BuildRequires

* Sun Sep 04 2005 Michael Scherer <misc@mandriva.org> 0.14.0-2mdk
- Rebuild to avoid libglitz deps

* Wed Aug 17 2005 Eskild Hustvedt <eskild@mandrake.org> 0.14.0-1mdk
- Initial Mandriva Linux package
