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
URL:		http://cire.sf.net/
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

