%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:			os-cloud-config
Version:		XXX
Release:		XXX
Summary:		Configuration for OpenStack clouds

License:		ASL 2.0
URL:			http://pypi.python.org/pypi/%{name}
Source0:		https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:		noarch
BuildRequires:		python-setuptools
BuildRequires:		python2-devel
BuildRequires:		python-pbr
BuildRequires:		git

Requires:		python-setuptools
Requires:		python-oslo-config
Requires:		python-babel
Requires:		python-keystoneclient
Requires:		python-novaclient
Requires:		python-pbr
Requires:		python-ironicclient >= 1.9.0
Requires:		pyOpenSSL
Requires:               python-oslo-i18n >= 2.1.0
Requires:               python-glanceclient >= 2.5.0
Requires:               python-neutronclient >= 5.1.0
Requires:               python-six

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
# REMOVEME: error caused by commit http://git.openstack.org/cgit/openstack/os-cloud-config/commit/?id=8cbab5ceeeae52363ea8c5188b8a0604cc420e34
