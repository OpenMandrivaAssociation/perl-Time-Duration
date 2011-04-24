%define upstream_name    Time-Duration
%define upstream_version 1.06

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:    Rounded or exact English expression of durations
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Time/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::Pod::Coverage)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides functions for expressing durations in rounded or exact
terms.

In the first example in the Synopsis, using duration($interval_seconds):

If the 'time() - $start_time' is 3 seconds, this prints "Runtime: *3
seconds*.". If it's 0 seconds, it's "Runtime: *0 seconds*.". If it's 1
second, it's "Runtime: *1 second*.". If it's 125 seconds, you get "Runtime:
*2 minutes and 5 seconds*.". If it's 3820 seconds (which is exactly 1h, 3m,
40s), you get it rounded to fit within two expressed units: "Runtime: *1
hour and 4 minutes*.". Using duration_exact instead would return "Runtime:
*1 hour, 3 minutes, and 40 seconds*".

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README ChangeLog META.yml
%{_mandir}/man3/*
%perl_vendorlib/*


