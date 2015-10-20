Name:			os-cloud-config
Version:		0.2.10
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
Requires:		python-pbr
# Add Back Requires on python-ironicclient once it's actually available
# Requires:		python-ironicclient
Requires:		pyOpenSSL

%description
os-cloud-config offers a suite of tools and libraries used to do the initial
configuration of OpenStack clouds.

%prep
%setup -q -n %{name}-%{version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

%files
%doc README.rst
%doc LICENSE
%{python2_sitelib}/os_cloud_config*
%{_bindir}/generate-keystone-pki
%{_bindir}/init-keystone
%{_bindir}/init-keystone-heat-domain
%{_bindir}/register-nodes
%{_bindir}/setup-endpoints
%{_bindir}/setup-flavors
%{_bindir}/setup-neutron
%{_bindir}/upload-kernel-ramdisk

%changelog
* Tue Oct 20 2015 James Slagle <jslagle@redhat.com> 0.2.10-1
- Update to upstream 0.2.10

* Tue Oct 28 2014 James Slagle <jslagle@redhat.com> 0.1.13-1
- Update to upstream 0.1.13

* Wed Oct 01 2014 James Slagle <jslagle@redhat.com> 0.1.11-1
- Update to upstream 0.1.11

* Mon Sep 29 2014 James Slagle <jslagle@redhat.com> 0.1.10-2
- Remove Requires on python-ironicclient

* Mon Sep 29 2014 James Slagle <jslagle@redhat.com> 0.1.10-1
- Update to upstream 0.1.10

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
