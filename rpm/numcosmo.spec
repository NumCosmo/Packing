#
# spec file for package numcosmo
#
# Copyright (c) 2012 Sandro Dias Pinto Vitenti <sandro@isoftware.com.br>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

Name:           numcosmo
Version:        0.12.0
Release:        2%{?dist}
Summary:        Numerical Cosmology

Group:          Productivity/Scientific/Physics
License:        GPL-3.0
URL:            https://savannah.nongnu.org/projects/numcosmo/
Source0:        http://download.savannah.gnu.org/releases/numcosmo/numcosmo-0.12.0rc7.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  pkg-config gcc gcc-fortran gobject-introspection-devel glib2-devel gsl-devel gmp-devel mpfr-devel fftw3-devel nlopt-devel sundials-devel sqlite3-devel libcfitsio-devel openblas-devel lapack-devel cblas-devel
Requires:       gsl gmp mpfr fftw3 nlopt sundials sqlite3 cfitsio libopenblas0

%description

The NumCosmo is a free software C library whose main purposes 
are to test cosmological models using observational data and to 
provide a set of tools to perform cosmological calculations. 
Particularly, the current version has implemented three different 
probes: cosmic microwave background (CMB),supernovae type Ia 
(SNeIa) and large scale structure (LSS) information, such as 
baryonic acoustic oscillations (BAO) and galaxy cluster 
abundance. The code supports a joint analysis of these data and 
the parameter space can include cosmological and phenomenological 
parameters. It is worth emphasizing that NumCosmo matter power 
spectrum and CMB codes were written independently of other 
implementations such as CMBFAST, CAMB, etc.

The library is structured in such way to simplify the inclusion 
of non-standard cosmological models. Besides the functions 
related to cosmological quantities, this library also implements 
mathematical and statistical tools. The former was developed to 
enable the inclusion of other probes and/or theoretical models 
and to optimize the codes. The statistical framework comprises 
algorithms which define likelihood functions, minimization, Monte 
Carlo, Fisher Matrix and profile likelihood methods.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%configure --disable-static --enable-shared --with-thread-pool-max=4 --enable-introspection
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(0644,root,root,0755)
%doc %{_datadir}/doc/%{name}-%{version}/
%doc %{_datadir}/man/man1/*
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/
%attr(0755, root, root) %{_bindir}/*
%dir %{_datadir}/%{name}-%{version}
%{_datadir}/%{name}-%{version}/data/

%files devel
%defattr(0644,root,root,0755)
%doc %{_datadir}/gtk-doc/html/%{name}/
%{_includedir}/%{name}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/gir-1.0/*
%dir %{_datadir}/%{name}-%{version}/examples
%attr(0755, root, root) %{_datadir}/%{name}-%{version}/examples/*.py
%{_datadir}/%{name}-%{version}/examples/*.c
%{_datadir}/%{name}-%{version}/examples/README

%changelog
