Summary:	Light-weight cryptographic and SSL/TLS library
Name:		polarssl
Version:	0.14.3
Release:	1
License:	GPL v2+
Group:		Libraries
URL:		http://www.polarssl.org/
Source0:	http://polarssl.org/code/releases/%{name}-%{version}-gpl.tgz
# Source0-md5:	f1b2fe9087ab64d7ea40a276a3628583
Patch1:		cmake-with-install.patch
Patch2:		cmake-shared.patch
Patch3:		cmake-doxygen.patch
BuildRequires:	cmake
BuildRequires:	doxygen
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PolarSSL is a light-weight open source cryptographic and SSL/TLS
library written in C. PolarSSL makes it easy for developers to include
cryptographic and SSL/TLS capabilities in their (embedded)
applications with as little hassle as possible.

%package devel
Summary:	Development files for PolarSSL
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description    devel
This package contains libraries and header files for developing
applications that use PolarSSL

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%undos ChangeLog

%build
install -d build
cd build
%cmake .. \
	-DUSE_SHARED_POLARSSL_LIBRARY:BOOL=1
%{__make} VERBOSE=1
%{__make} VERBOSE=1 apidoc

%if %{with tests}
# Tests are not stable on 64-bit
ctest --output-on-failure
%endif

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	-C build \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}
mv $RPM_BUILD_ROOT%{_bindir} $RPM_BUILD_ROOT%{_libdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/libpolarssl.so.*.*.*
%ghost %{_libdir}/libpolarssl.so.1
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/aescrypt2
%attr(755,root,root) %{_libdir}/%{name}/benchmark
%attr(755,root,root) %{_libdir}/%{name}/cert_app
%attr(755,root,root) %{_libdir}/%{name}/dh_client
%attr(755,root,root) %{_libdir}/%{name}/dh_genprime
%attr(755,root,root) %{_libdir}/%{name}/dh_server
%attr(755,root,root) %{_libdir}/%{name}/hello
%attr(755,root,root) %{_libdir}/%{name}/md5sum
%attr(755,root,root) %{_libdir}/%{name}/mpi_demo
%attr(755,root,root) %{_libdir}/%{name}/rsa_genkey
%attr(755,root,root) %{_libdir}/%{name}/rsa_sign
%attr(755,root,root) %{_libdir}/%{name}/rsa_verify
%attr(755,root,root) %{_libdir}/%{name}/selftest
%attr(755,root,root) %{_libdir}/%{name}/sha1sum
%attr(755,root,root) %{_libdir}/%{name}/sha2sum
%attr(755,root,root) %{_libdir}/%{name}/ssl_cert_test
%attr(755,root,root) %{_libdir}/%{name}/ssl_client1
%attr(755,root,root) %{_libdir}/%{name}/ssl_client2
%attr(755,root,root) %{_libdir}/%{name}/ssl_server
%attr(755,root,root) %{_libdir}/%{name}/ssl_test

%files devel
%defattr(644,root,root,755)
%doc include/apidoc/*
%{_libdir}/libpolarssl.so
%{_includedir}/%{name}
