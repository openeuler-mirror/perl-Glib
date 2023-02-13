%global _empty_manifest_terminate_build 0
Name:           perl-Glib
Version:        1.3293
Release:        3
Summary:        Perl wrappers for the GLib utility and Object libraries
License:        LGPL-2.1
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Glib/
Source0:        http://www.cpan.org/authors/id/X/XA/XAOC/Glib-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  glib2-devel perl-devel
BuildRequires:  gcc
BuildRequires:  perl-generators
BuildRequires:  perl-ExtUtils-Depends >= 0.300
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl-ExtUtils-PkgConfig >= 1.000
Requires:       perl-ExtUtils-Depends >= 0.300
Requires:       perl-ExtUtils-PkgConfig >= 1.000
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
%description
This wrapper attempts to provide a perlish interface while remaining as
true as possible to the underlying C API, so that any reference materials
you can find on using GLib may still apply to using the libraries from
perl. This module also provides facilities for creating wrappers for other
GObject-based libraries. The "SEE ALSO" section contains pointers to all
sorts of good information.
%package help
Summary : Perl wrappers for the GLib utility and Object libraries
Provides: perl-Glib-doc
%description help
This wrapper attempts to provide a perlish interface while remaining as
true as possible to the underlying C API, so that any reference materials
you can find on using GLib may still apply to using the libraries from
perl. This module also provides facilities for creating wrappers for other
GObject-based libraries. The "SEE ALSO" section contains pointers to all
sorts of good information.
%prep
%setup -q -n Glib-%{version}
%build
export PERL_MM_OPT=""
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
export PERL_MM_OPT=""
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

pushd %{buildroot}
touch filelist.lst
if [ -d usr/bin ];then
    find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ];then
    find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ];then
    find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib ];then
    find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
popd
mv %{buildroot}/filelist.lst .
%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files -f filelist.lst
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog.pre-git doctypes Glib.exports LICENSE META.json NEWS  README TODO xsapi.pod.foot xsapi.pod.head
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Glib*
%files help
%{_mandir}/*

%changelog
* Fri Feb 10 2023 lichaoran <pkwarcraft@hotmail.com> 1.3293-3
- add buildRequires: add gcc as we using it to compile
- and perl-generators to auto-generate perl module provides

* Mon Jun 13 2022 peijiankang <peijiankang@kylinos.cn> 1.3293-2
- remove %{dist} from spec file

* Sat Jun 20 2020 Perl_Bot <Perl_Bot@openeuler.org> 1.3293-1
- Specfile autogenerated by Perl_Bot
