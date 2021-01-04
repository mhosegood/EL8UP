Name:           kickstart
Version:        1.0
Release:        1%{?dist}
Summary:        Kickstart file collection
Group:          Kickstart
License:        First Alternative License conditions apply
URL:            http://www.firstalt.co.uk
Source0:        kickstart.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
%description
%global debug_package %{nil}
%prep
%setup -q
%build
%install
install -m 0755 -d $RPM_BUILD_ROOT/opt/kickstart
install -m 644 ks.cfg $RPM_BUILD_ROOT/opt/kickstart/ks.cfg
install -m 644 192.168.200.28-pike.kickstart $RPM_BUILD_ROOT/opt/kickstart/192.168.200.28-pike.kickstart
%clean
rm -rf $RPM_BUILD_ROOT
%files
%dir /opt
/opt/kickstart
%post
systemctl  enable  cockpit.socket  --now
echo  "Image version 7.6 June 2020" > /etc/FArelease

%changelog
