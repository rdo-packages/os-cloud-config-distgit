Name:			os-cloud-config
Version:		0.1.9
Release:		1%{?dist}
Summary:		Configuration for OpenStack clouds

License:		ASL 2.0
URL:			http://pypi.python.org/pypi/%{name}
Source0:		http://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz

BuildArch:		noarch
BuildRequires:		python-setuptools
BuildRequires:		python2-devel
BuildRequires:		python-pbr

Requires:		python-setuptools
Requires:		python-argparse
Requires:		python-oslo-config
Requires:		python-babel
Requires:		python-keystoneclient
Requires:		python-novaclient
Requires:		python-ironicclient
Requires:		pyOpenSSL

%description
os-cloud-config offers a suite of tools and libraries used to do the initial
configuration of OpenStack clouds.

%prep
%setup -q -n %{name}-%{version}

#
# patches_base: 0.1.9
#

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%files
%doc README.rst
%doc LICENSE
%{python_sitelib}/os_cloud_config*
%{_bindir}/generate-keystone-pki
%{_bindir}/init-keystone
%{_bindir}/register-nodes
%{_bindir}/setup-endpoints
%{_bindir}/setup-neutron

%changelog
* Fri Sep 12 2014 James Slagle <jslagle@redhat.com> - 0.1.9-1
- Setup for rdopkg
- Bump to 0.1.9

* Fri Sep 12 2014 James Slagle <jslagle@redhat.com> - 0.1.8-3
- Add python-pbr to BuildRequires

* Fri Sep 05 2014 James Slagle <jslagle@redhat.com> - 0.1.8-2
- Updating spec for Fedora review process

* Mon Aug 25 2014 Derek Higgins <derekh@redhat.com> - 0.1.8-1
- Add setup-endpoints and setup-neutron
- initial package
