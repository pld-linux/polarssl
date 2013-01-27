Summary:	Light-weight cryptographic and SSL/TLS library
Summary(pl.UTF-8):	Lekka biblioteka kryptograficzna oraz SSL/TLS
Name:		polarssl
Version:	1.2.4
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://polarssl.org/code/releases/%{name}-%{version}-gpl.tgz
# Source0-md5:	f23fc73b0c5ef1c51294c20f3ea0dcb0
URL:		http://www.polarssl.org/
BuildRequires:	cmake >= 2.6
BuildRequires:	doxygen
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PolarSSL is a light-weight open source cryptographic and SSL/TLS
library written in C. PolarSSL makes it easy for developers to include
cryptographic and SSL/TLS capabilities in their (embedded)
applications with as little hassle as possible.

%description -l pl.UTF-8
PolarSSL to lekka, mająca otwarte źródła biblioteka kryptograficzna
oraz SSL/TLS napisana w C. PolarSSL ułatwia programistom dołączanie
funkcji kryptograficznych i SSL/TLS do swoich (wbudowanych) aplikacji
przy jak najmniejszym narzucie.

%package devel
Summary:	Development files for PolarSSL
Summary(pl.UTF-8):	Pliki programistyczne biblioteki PolarSSL
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header files for developing applications
that use PolarSSL.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do tworzenia aplikacji
wykorzystujących bibliotekę PolarSSL.

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	-DUSE_SHARED_POLARSSL_LIBRARY:BOOL=1

%{__make} 
%{__make} apidoc

%if %{with tests}
# Tests are not stable on 64-bit
ctest --output-on-failure
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
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
%attr(755,root,root) %ghost %{_libdir}/libpolarssl.so.2
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/aescrypt2
%attr(755,root,root) %{_libdir}/%{name}/benchmark
%attr(755,root,root) %{_libdir}/%{name}/cert_app
%attr(755,root,root) %{_libdir}/%{name}/crl_app
%attr(755,root,root) %{_libdir}/%{name}/crypt_and_hash
%attr(755,root,root) %{_libdir}/%{name}/dh_client
%attr(755,root,root) %{_libdir}/%{name}/dh_genprime
%attr(755,root,root) %{_libdir}/%{name}/dh_server
%attr(755,root,root) %{_libdir}/%{name}/gen_entropy
%attr(755,root,root) %{_libdir}/%{name}/gen_random_ctr_drbg
%attr(755,root,root) %{_libdir}/%{name}/gen_random_havege
%attr(755,root,root) %{_libdir}/%{name}/generic_sum
%attr(755,root,root) %{_libdir}/%{name}/hello
%attr(755,root,root) %{_libdir}/%{name}/key_app
%attr(755,root,root) %{_libdir}/%{name}/md5sum
%attr(755,root,root) %{_libdir}/%{name}/mpi_demo
%attr(755,root,root) %{_libdir}/%{name}/o_p_test
%attr(755,root,root) %{_libdir}/%{name}/rsa_decrypt
%attr(755,root,root) %{_libdir}/%{name}/rsa_encrypt
%attr(755,root,root) %{_libdir}/%{name}/rsa_genkey
%attr(755,root,root) %{_libdir}/%{name}/rsa_sign
%attr(755,root,root) %{_libdir}/%{name}/rsa_verify
%attr(755,root,root) %{_libdir}/%{name}/selftest
%attr(755,root,root) %{_libdir}/%{name}/sha1sum
%attr(755,root,root) %{_libdir}/%{name}/sha2sum
%attr(755,root,root) %{_libdir}/%{name}/ssl_cert_test
%attr(755,root,root) %{_libdir}/%{name}/ssl_client1
%attr(755,root,root) %{_libdir}/%{name}/ssl_client2
%attr(755,root,root) %{_libdir}/%{name}/ssl_fork_server
%attr(755,root,root) %{_libdir}/%{name}/ssl_mail_client
%attr(755,root,root) %{_libdir}/%{name}/ssl_server
%attr(755,root,root) %{_libdir}/%{name}/ssl_test
%attr(755,root,root) %{_libdir}/%{name}/strerror

%files devel
%defattr(644,root,root,755)
%doc apidoc/*
%attr(755,root,root) %{_libdir}/libpolarssl.so
%{_includedir}/%{name}
