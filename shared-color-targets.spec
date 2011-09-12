%define alphatag 20091218

Summary: Shared color targets for creating color profiles
Name: shared-color-targets
Version: 0.1.0
Release: %mkrel 1
URL: http://github.com/hughsie/shared-color-targets
Source0: http://people.freedesktop.org/~hughsient/releases/%{name}-%{version}.tar.xz
License: GPLv2+ and Public Domain and CC-BY-SA
Group: System/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

%description 
The shared-color-targets package contains various targets which are useful for
programs that create ICC profiles.
This package only contains the free targets that can be safely distributed
with Fedora.

%prep
%setup -q

%build
%configure2_5x

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%dir %{_datadir}/color/targets
%{_datadir}/color/targets/*.it8
%dir %{_datadir}/shared-color-targets

# Wolf Faust
%dir %{_datadir}/shared-color-targets/wolf_faust
%{_datadir}/shared-color-targets/wolf_faust/*
%dir %{_datadir}/color/targets/wolf_faust
%dir %{_datadir}/color/targets/wolf_faust/reflective
%{_datadir}/color/targets/wolf_faust/reflective/*.it8
%dir %{_datadir}/color/targets/wolf_faust/transmissive
%{_datadir}/color/targets/wolf_faust/transmissive/*.it8

