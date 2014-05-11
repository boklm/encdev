Name:           [% project %]
Version:        [% c('version') %]
Release:        [% c('rpm_rel') %]%{?dist}
Source:         %{name}-%{version}.tar.[% c('compress_tar') %]
Summary:        [% c('summary') %]
URL:            [% c('url') %]
License:        CC0
BuildArch:      noarch
%description
[% c('description') -%]

%prep
%setup -q

%build

%install
make DESTDIR=%{buildroot} install

%files
%doc README.asc COPYING
%{_bindir}/%{name}
