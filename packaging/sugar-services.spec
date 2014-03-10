Name:           sugar-services 
Version:        0.6.0
Release:        1
Summary:        Allow Sugar activities talk to Sugar shell

License:        GPLv2+
URL:            https://github.com/walterbender/sugarservices
Source0:        %{name}-%{version}.tar.gz

Requires:       python >= 2.7, sugar >= 0.100

BuildArch:      noarch

%description
Service for allowing Sugar activities talk to sugar shell, network manager, etc

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/sugar/extensions/webservice/
cp -r extensions/webservice/sugarservices $RPM_BUILD_ROOT/%{_datadir}/sugar/extensions/webservice/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/sugar/extensions/webservice/sugarservices

%changelog
* Mon Mar 10 2014 Martin Abente Lahaye <tch@sugarlabs.org>
- initial package release
