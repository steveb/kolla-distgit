Name:       openstack-kolla
Version:    XXX
Release:    XXX
Summary:    Refresh system configuration

License:    ASL 2.0
URL:        http://pypi.python.org/pypi/kolla
Source0:    http://tarballs.openstack.org/kolla/kolla-%{version}.tar.gz

BuildArch:  noarch
BuildRequires:  python-setuptools
BuildRequires:  python2-devel
BuildRequires:  python-pbr

Requires:   python-setuptools
Requires:   python-gitdb
Requires:   GitPython
Requires:   python-jinja2
Requires:   python-docker-py
Requires:   python-six
Requires:   python2-oslo-config
Requires:   python-crypto
Requires:   python-netaddr

%description
Templates and tools from the Kolla project to build OpenStack container images.

%prep
%setup -q -n kolla-%{upstream_version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

mkdir -p %{buildroot}%{_datadir}/kolla/docker
cp -vr docker/ %{buildroot}%{_datadir}/kolla

# setup.cfg required for kolla-build to discover the version
install -p -D -m 644 setup.cfg %{buildroot}%{_datadir}/kolla/setup.cfg

# remove tests
rm -fr %{buildroot}%{python_sitelib}/kolla/tests

# remove tools
rm -fr %{buildroot}%{_datadir}/kolla/tools

%files
%doc README.rst
%doc LICENSE
%doc %{_datadir}/kolla/doc
%doc %{_datadir}/kolla/etc_examples
%doc %{_datadir}/kolla/openrc-example
%{_bindir}/kolla-build
%{_bindir}/kolla-genpwd
%{python_sitelib}/kolla*
%{_datadir}/kolla/docker
%{_datadir}/kolla/setup.cfg

%changelog