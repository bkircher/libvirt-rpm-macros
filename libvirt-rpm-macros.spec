Name:           libvirt-rpm-macros
Version:        1
Release:        1%{?dist}
Summary:        RPM macro to disable netcf in libvirt

License:        GPLv2
URL:            https://github.com/bkircher/libvirt-rpm-macros

BuildArch:      noarch

%description
%{summary}.

This is to disable deprecated (and orphaned) netcf when building newer
libvirt on CentOS Stream 8.

%prep
%autosetup -c -D -T

%build
# Nothing to build

%install
mkdir -p %{buildroot}/%{_rpmconfigdir}/macros.d/
echo '%_without_netcf 1' > %{buildroot}/%{_rpmconfigdir}/macros.d/macros.libvirt

%files
%{_rpmconfigdir}/macros.d/macros.libvirt

%changelog
* Tue Feb 1 2022 Ben Kircher <bkircher@0xadd.de> - 1-1
- Initial package
