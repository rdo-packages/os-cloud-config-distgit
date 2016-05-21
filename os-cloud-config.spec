Name:			os-cloud-config
Version:		XXX
Release:		XXX
Summary:		Configuration for OpenStack clouds

License:		ASL 2.0
URL:			http://pypi.python.org/pypi/%{name}
Source0:		http://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz

BuildArch:		noarch
BuildRequires:		python-setuptools
BuildRequires:		python2-devel
BuildRequires:		python-pbr
BuildRequires:		git

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
%autosetup -n %{name}-%{upstream_version} -S git

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

%files
%doc README.rst
%license LICENSE
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
